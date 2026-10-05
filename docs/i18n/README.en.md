# SpeAds Skill Lite v1.0.0 — English

[← Back to main README](../../README.md)

AI Ads Academy · https://www.ai-ads.academy · Apache-2.0

## Overview

An offline, open-source marketplace advertising planning Skill. Platform-specific modes, requirements and dated official sources are in profile.json.

Offline Shopee Taiwan retail-ad planning, SKU economics and supplied-report analysis.

Modes: `full_site, comprehensive_search`

## What is included

Provides representative-order contribution, break-even CPA/net-revenue ROAS, readiness checks, equal-split pilot budget scenarios, and supplied-report analysis. eBay CPS fee bases, GMV Max blended attribution and Walmart Buy Box are kept separate.

## Quick start

Python 3.10+ standard library only. Run commands from the package root. Unknown values must remain null. Use a new output directory for each run. CSV input must match the supplied six-column template and have metadata; arbitrary native exports are not supported.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/release_gate.py
python3 scripts/toolkit.py plan examples/brief.synthetic.json --out-dir output/demo-plan
python3 scripts/toolkit.py validate output/demo-plan/plan.json
python3 scripts/toolkit.py analyze examples/report.csv --meta examples/report.meta.json --out-dir output/demo-analysis
python3 scripts/toolkit.py validate output/demo-analysis/analysis.json
```

## Limits and safety

No account connection, credentials, live data, ad publishing or budget changes. Financial numbers are scenarios, not recommendations or accounting advice. Gross-attributed GMV is not net profit, and paid-plus-organic ROI is not incremental paid-ad return. Human review is mandatory.

This release provides five-language introductory documentation, not a fully localized CLI or automatic translation engine. Deterministic fields are kept stable; a host model may write a separate explanation in your language. The host application may use cloud services and incur charges. Desktop discovery and output quality must still be tested.

Read the data contract, installation guide and development handoff. Keep personal data and credentials out of inputs and public repositories. Not an official product of the advertising platform.

[Data contract](../../references/data-contract.md) · [Install](../INSTALLATION.md) · [Development](../HANDOFF.md) · [Sources](../../references/official-sources.md)
