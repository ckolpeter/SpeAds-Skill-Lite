# Codex / Claude Code development handoff

## First review

Recommended execution: Codex Desktop/CLI with your already-verified coding model, high reasoning for contract/statistical changes. Independent review: a fresh Claude Code session. No model/provider names are hardcoded in this repository.

```text
先讀 README.md、SKILL.md、AGENTS.md、references/data-contract.md、profile.json、docs/TEST_REPORT.md。
只處理目前 Repo，不修改 ShopeeAds、Runmo 或其他 Skill，不串接廣告平台。
先跑 python3 -m unittest discover -s tests -v 與 python3 scripts/release_gate.py。
在新的 output 子目錄跑 JSON 規劃與 canonical CSV 分析，再 validate 兩份 JSON。
確認 five-language README 連結、已知限制、資料缺漏／歸因／CPS-CPC 邊界。
先回報 PASS / FAIL / NOT_RUN 與證據，不要為了測試變綠而重算未審查的 manifest。
若要新增功能，先提一個最小範圍並加入 regression tests；保留 Lite 的 no-network 邊界。
```

## Architecture

`profile.json` is the platform-specific workflow/mode/source/budget-scope policy. `scripts/toolkit.py` is a deliberately vendored offline engine. Each repository is independently runnable with no sibling dependency. Platform branches isolate eBay fee basis, GMV Max attribution and Walmart Buy Box. Schema mode sets and distinct workflow/scope records isolate Shopee, Lazada and Etsy. Do not turn this into a shared network SDK without a new scope decision.

## Extension priorities

1. Collect anonymized real seller exports plus field dictionaries, site, currency and attribution notes. Add one explicitly named exporter/version adapter with golden fixtures; never silently accept arbitrary CSV.
2. Add more native-language worked examples and model output evaluations. Five-language documentation is not a full multilingual generation engine.
3. Add confidence/uncertainty analysis with declared statistical assumptions. No blanket 7-day or 20-click auto-stop rule.
4. Verify actual desktop skill discovery, correct selection among all Skills, relative paths and constrained tool behavior.
5. Add platform-specific planning features only after checking current official sources and the target account UI.

No OAuth, credentials, ad publishing, budget mutations, pixels or live reporting belong to this Lite release. Separate Pro work needs a new threat model and explicit authority checks.

## Editing and release

Inspect `git status` and baseline tests first. Update schema, engine, examples, tests, source records and docs together. Do not change canonical artifacts by hand. Update output fixtures by rerunning the engine after reviewing diffs. Regenerate MANIFEST only after intentional changes, then rerun tests and gate. Preserve LICENSE/NOTICE. Use a new version for behavioral changes; do not silently replace a published immutable asset.

This v1 has not been reviewed against real seller data, live account eligibility, conversion performance, or the user's desktop app. Test reports distinguish local/CI checks from those NOT_RUN items.
