# Install or develop SpeAds Skill Lite

## Use without installation

Open this repository in your desktop coding tool. Explicitly ask it to read SKILL.md and follow the offline workflow. This is not proof of automatic discovery.
Run Python commands from this root directory. Python 3.10+ is required. Windows may use `py -3` instead of `python3`.

## Local personal Skill installation (opt-in)

The complete folder is required, not SKILL.md alone. Verify the package first. The installer is dry-run by default and refuses to replace an existing destination.

Codex local user directory, per the official guide:

```bash
python3 scripts/install_skill.py --destination "$HOME/.agents/skills/speads-skill-lite"
python3 scripts/install_skill.py --destination "$HOME/.agents/skills/speads-skill-lite" --apply
```

Claude Code local user directory:

```bash
python3 scripts/install_skill.py --destination "$HOME/.claude/skills/speads-skill-lite"
python3 scripts/install_skill.py --destination "$HOME/.claude/skills/speads-skill-lite" --apply
```

Project locations may use `.agents/skills/<skill-id>` or `.claude/skills/<skill-id>` in a separate target project. Do not install a package inside its own source tree. Do not copy `.git`, credentials or outputs. Avoid duplicate same-named installations. Re-open/reload your host as its current documentation requires, then verify explicit selection and implicit routing with evals/manual-cases.md.

These local folders do not automatically install a Skill into every cloud/Cowork session. Consult the host documentation for that product. No automatic host settings edits, plugin publishing or account connection is performed.

This release's installer copying is tested separately from actual host activation. Host application/model usage can involve network access and charges; that is not part of these offline scripts.

Sources: https://developers.openai.com/codex/skills/ and https://code.claude.com/docs/en/skills (checked 2026-10-05).
