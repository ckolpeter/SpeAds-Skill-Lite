"""One-time, hash-pinned source import for six explicitly authorized public repos."""
from pathlib import Path, PurePosixPath
import base64, hashlib, json, lzma, os, shutil, subprocess, sys, tempfile, time
from urllib.request import urlopen

PIN = '93a54820870a0269e9d27fcb7c5a0c343a92f4d9'
SHA256 = '4154a37c5956ff57d4ff426375317a8f18a3d6e60ce17277d65f7a87bf07e73c'
TARGETS = {
 'ckolpeter/SpeAds-Skill-Lite': ('speads-skill-lite', '917b343d6912adb0d174480fd771e8166a02c700'),
 'ckolpeter/LazAds-Skill-Lite': ('lazads-skill-lite', '3e520638509a52cd54577bb88387534ff72b5522'),
 'ckolpeter/TikShopAds-Skill-Lite': ('tikshopads-skill-lite', '98101671e190871b564764baa8ee4af71e5ea7dd'),
 'ckolpeter/EbyAds-Skill-Lite': ('ebyads-skill-lite', '30f5af57a9f01d28c63e6ad67f6bfd2ef56ec96b'),
 'ckolpeter/EtsyAds-Skill-Lite': ('etsyads-skill-lite', 'a726dd920cccd5e8e017522b8955487f036adb7f'),
 'ckolpeter/WmtAds-Skill-Lite': ('wmtads-skill-lite', '222a07ed2fc1dd9753a939c0139d282de388ea99'),
}
STAGED = {
 '.import/part01.b64': '3e4aa487c563d17a9d3cb4f91a58bbecf5602690',
 '.import/part02.b64': '1baaf6c9626730ccaa1406e53d780c8126b7291d',
 '.import/part03.b64': 'f7fb4117f1d165fd2d8e77571524fcb64b0ad352',
 '.import/part04.b64': '4fe47ab321100ab5007f33d4f648883bc69b40b3',
 '.import/part05.b64': '3107596c8f7376c92e7584fa3a5dca034753e521',
 '.bootstrap/part01.txt': '23da5b3aa12550e1683169f3b9bf33ce3f905b41',
 '.bootstrap/part02.txt': '2717b75dab18c9332f471b87deb03b3e15b70c27',
 '.bootstrap/part03.txt': 'f33baf1f51159f37cf36c2ff452f87baa4133c0d',
 '.bootstrap/part04.txt': '29276fc419ac289b2d6d1903831a383ded445e49',
}

def git(*args, cwd=None):
    return subprocess.check_output(['git', *args], cwd=cwd, text=True).strip()

def fetch_piece(n):
    url = f'https://raw.githubusercontent.com/ckolpeter/SpeAds-Skill-Lite/{PIN}/.import/part{n:02}.b64'
    for attempt in range(3):
        try:
            with urlopen(url, timeout=30) as response:
                data = response.read(13000)
            if len(data) > 12000:
                raise ValueError('Oversized transport part')
            return data.strip()
        except Exception:
            if attempt == 2:
                raise
            time.sleep(3)

repo = os.environ['GITHUB_REPOSITORY']
skill_id, expected_tree = TARGETS[repo]
workspace = Path(os.environ['GITHUB_WORKSPACE']).resolve()
head = git('rev-parse', 'HEAD', cwd=workspace)
tracked = set(git('ls-files', cwd=workspace).splitlines())
allowed = {'.github/workflows/import.yml'}
if repo == 'ckolpeter/SpeAds-Skill-Lite':
    allowed |= set(STAGED) | {'.import/restore.py'}
if tracked - allowed:
    raise RuntimeError('Refusing to overwrite existing work: '+repr(sorted(tracked - allowed)))
for name in tracked & set(STAGED):
    if git('rev-parse', 'HEAD:'+name, cwd=workspace) != STAGED[name]:
        raise RuntimeError('Transport changed: '+name)
if git('status', '--porcelain', cwd=workspace):
    raise RuntimeError('Checkout must be clean')
encoded = b''.join(fetch_piece(n) for n in range(1, 6))
if len(encoded) != 54940:
    raise RuntimeError('Transport length mismatch')
compressed = base64.b64decode(encoded, validate=True)
if hashlib.sha256(compressed).hexdigest() != SHA256:
    raise RuntimeError('Transport checksum mismatch')
payload = lzma.decompress(compressed, memlimit=256*1024*1024)
if len(payload) > 5_000_000:
    raise RuntimeError('Oversized source payload')
data = json.loads(payload)
if data['format'] != 'aiads.compact-source.v1':
    raise RuntimeError('Wrong source format')
files = data['packages'][skill_id]
if not 1 <= len(files) <= 100:
    raise RuntimeError('Wrong file count')
with tempfile.TemporaryDirectory(prefix='retail-release-') as temp:
    root = Path(temp)
    for name, index in files.items():
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or '.git' in path.parts or str(path) != name:
            raise RuntimeError('Unsafe source path')
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(data['texts'][index], encoding='utf-8')
        target.chmod(0o644)
    profile = json.loads((root/'profile.json').read_text(encoding='utf-8'))
    if profile['repo'] != repo or profile['skill_id'] != skill_id:
        raise RuntimeError('Wrong platform source')
    (root/'examples/expected').mkdir(parents=True)
    code = "import sys,json;sys.path.insert(0,'scripts');import toolkit as t;from pathlib import Path;\nfor kind,file in [('brief','brief.synthetic.json'),('report','report.synthetic.json')]:\n a=t.build(t.read_json(Path('examples')/file),kind);name=a['kind'];(Path('examples/expected')/(name+'.json')).write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\\n',encoding='utf-8');(Path('examples/expected')/(name+'.md')).write_text(t.render(a),encoding='utf-8')"
    subprocess.run([sys.executable, '-c', code], cwd=root, check=True)
    subprocess.run([sys.executable, 'scripts/release_gate.py', '--write-manifest'], cwd=root, check=True)
    git('init', '-q', cwd=root)
    git('add', '.', cwd=root)
    actual_tree = git('write-tree', cwd=root)
    if actual_tree != expected_tree:
        raise RuntimeError('Reconstructed source tree mismatch: '+actual_tree)
    release_files = git('ls-files', cwd=root).splitlines()
    if len(release_files) != 41:
        raise RuntimeError('Expected 41 release files')
    subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'], cwd=root, check=True)
    subprocess.run([sys.executable, 'scripts/release_gate.py'], cwd=root, check=True)
    if git('rev-parse', 'HEAD', cwd=workspace) != head:
        raise RuntimeError('Checkout changed during validation')
    # GITHUB_TOKEN may not write workflows. Native connector finalizes test.yml later.
    for name in release_files:
        if name.startswith('.github/workflows/'):
            continue
        target = workspace / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root/name, target)
        target.chmod(0o644)
    for name in tracked - {'.github/workflows/import.yml'}:
        (workspace/name).unlink()
    git('config', 'user.name', 'github-actions[bot]', cwd=workspace)
    git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com', cwd=workspace)
    git('add', '-A', cwd=workspace)
    git('commit', '-m', 'feat: publish verified v1.0.0 offline marketplace source', cwd=workspace)
    git('push', 'origin', 'HEAD:main', cwd=workspace)
    print('SOURCE_IMPORTED; native workflow finalization still required; expected final tree '+expected_tree)
