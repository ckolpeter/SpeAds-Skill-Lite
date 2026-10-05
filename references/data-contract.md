# Data contract v1.0

All inputs must match the JSON schemas in `schemas/` plus the semantic checks in `scripts/toolkit.py`.
No platform API enums or upload payloads are represented. Command output is a local artifact only.

## Brief input

Copy `templates/brief.json`. Required keys are present in the template. Keep unknowns as `null`, never as guessed zero.
`platform` is fixed by this package. `market` is a two-letter marketplace-site label, not user nationality or document language; `currency` is one uppercase three-letter currency code. The program does not validate site availability or currency legal tender. No FX conversion.
`source.kind` is `synthetic` or `user_provided`; `source.note` describes the de-identified source.
`money_decimals` specifies accounting precision for budget splits, from 0 through 4; select the precision appropriate to your billing context.

`campaign.mode` must appear in `profile.json`. `days` is 1–366. `budget` is a total cap, not a daily budget. `account_ready` and `feature_confirmed` are user-supplied `true`/`false`/`null` assertions, not verified eligibility. `target_return` is recorded as context only and never validated as a supported platform target. `ad_rate` is a fraction such as `0.10` for 10%, used only for eBay General. Other modes leave it null.

Each product has a local `sku` alias, title, stock, listing_ready, advertising_eligible, buy_box, order_revenue, order_costs, target_profit, expected_cvr, fee_base_per_order and terms. The three readiness booleans remain tri-state; Buy Box gates only Walmart. `terms` are supplied research candidates, not verified keyword volume or live bids. No official item, account or campaign IDs are needed.

## Economics: one representative fulfilled order

All monetary inputs refer to **the same representative order** for that SKU, not a mixture of per-item and per-order costs. For multi-unit baskets, supply aggregate revenue and costs for the basket. Do not apply clicked-SKU margins to unrelated halo purchases.

`order_revenue` means seller revenue after discounts/refund allowance and remitted sales tax, **before the non-ad costs listed below**. Include shipping collected only consistently with the cost basis. Do not use settlement revenue that already deducts those same costs.
`order_costs.cogs` is merchandise cost; `platform_fees` contains non-ad marketplace/payment fees; `fulfilment` contains seller-funded shipping/packaging/fulfilment; `other` contains non-overlapping other variable costs (e.g. creator commission and an appropriate returns-cost allowance). Enter known zero explicitly. No default platform fee schedule is supplied. Avoid double counting creator or fulfilment fees.
`target_profit` is the desired contribution remaining per representative order after advertising, not company net profit. Fixed overhead/income tax are not automatically modeled. This is planning math, not accounting or tax advice.

C = order_revenue − sum(order_costs)

break_even_cpa = C, only when C > 0

break_even_roas_on_net_revenue = order_revenue / C

target_ad_allowance = C − target_profit

target_roas_on_net_revenue = order_revenue / target_ad_allowance, only when allowance > 0

economic_cpc_ceiling = target_ad_allowance × expected_cvr, only when both are known and mode is not eBay General

`expected_cvr` is a user scenario fraction [0,1], not observed or predicted performance. No bid multipliers or auction minimums are modeled. These economic limits are approximate scenarios, never executable bid recommendations.
For eBay General, provide `fee_base_per_order` from the applicable fee basis, including any applicable shipping/taxes/other amounts. It is not assumed equal to net seller revenue. The scenario fee is `ad_rate × fee_base_per_order`; economic rate ceilings divide contribution/allowance by that base and are capped at 1. This does **not** validate the platform's accepted ad-rate range.

Numeric inputs are finite nonnegative decimal strings or JSON numbers, at most 1e12 and six fractional digits. Rates are fractions, not percent numbers. Negative contribution may appear as an output. Decimal output is displayed to six decimal places and may round; do not copy a rounded ceiling directly into a live setting. Zero-denominator ratios are null, not infinity or zero.

## Readiness and budgets

`PILOT_CANDIDATE` requires positive economics, explicit target profit/headroom, positive known stock, supplied eligibility/listing/account/feature confirmations and any mode-specific checks. It is NOT a platform approval or recommendation to spend. Missing facts produce `NEEDS_INPUT`; known blockers produce `BLOCKED`.
Budget is split equally among candidates as an illustrative pilot accounting allocation. Rounding remainder stays in reserve. With no eligible candidates, the whole cap is reserved. It is not an optimization algorithm, demand forecast or a UI budget field. Etsy/Store/LIVE and eBay General have different budget scopes stated in the output. Per-SKU splits do not imply per-SKU platform controls.

## Report input: JSON or canonical CSV + metadata

Use `examples/report.synthetic.json`, or an exact CSV header:

```csv
sku,impressions,clicks,orders,spend,revenue
```

CSV accepts UTF-8/BOM, blanks as unknown and dot-decimal amounts (no currency symbols or thousands separators). It is **not** a universal importer for native exports. Map and review the source report manually first. `examples/report.meta.json` supplies every non-row field. Headers, unknown columns and duplicate SKU aliases are rejected. Max 500 products/rows, 2 MB input files. Validation/rendering allow up to 16 MB for an artifact containing the input snapshot and computed result. Internal totals may exceed the 1e12 per-input-field cap. Validation/rendering allow up to 16 MB for an artifact containing the input snapshot and computed result. Internal totals may exceed the 1e12 per-input-field cap.

All rows share one platform, site, currency, campaign mode, date interval, revenue basis and attribution definition. `start_date` <= `end_date`. `attribution_window` records the supplied definition, not one invented by the tool. `window_complete` is tri-state and must reflect conversion lag/refunds as appropriate. `rows_disjoint=true` is required before totals are calculated; otherwise they are withheld. Do not mix campaign totals, product totals, overlapping dates or duplicate halo revenue. Distinct SKU labels do not prove revenue is disjoint.

`sales_scope` is `paid_click`, `paid_mixed`, `paid_and_organic` or `unknown`. `paid_click` is needed for a click-order ratio; eBay General suppresses it regardless. GMV Max accepts only `paid_and_organic` or `unknown` in v1; it never labels mixed return as paid-only ROAS. `revenue_basis` is `gross_reported`, `net_settled` or `unknown`.

CTR = clicks/impressions; effective_spend_per_click = spend/clicks; CPM = spend×1000/impressions. The cpc field is populated only for CPC modes; eBay General keeps cpc null and records billing_model=CPS. Effective spend/click on CPS billing is only an accounting ratio, never a CPC bid. Return = supplied revenue/spend and is labeled paid, blended or unclassified according to scope. Cost per reported order = spend/reported orders; it does not prove acquisition cost or incrementality. The tool never compares gross-attributed returns directly to net-revenue economic break-even thresholds and never infers total profit from attribution.
Incomplete attribution, missing facts or quality warnings prevent decisive interpretations. `REVIEW_ZERO_ORDERS_NOT_AUTOMATIC_PAUSE` requests manual investigation only; it is not an automated stop instruction. No universal sample-size or performance benchmark is invented.

## Output and replay

Plan contract: `<slug>.plan@1.0`; analysis: `<slug>.analysis@1.0`. Envelopes contain input snapshot, deterministic result, local hash ID, producer_version, kind, status, review, generation_mode and fixed false publishing/external flags. Status is `PLAN_READY` or `ANALYSIS_READY`, always `HUMAN_REVIEW_REQUIRED`.
`validate` recomputes from the input snapshot and compares the entire canonical artifact; changed outputs or authorization flags are rejected. This is consistency checking, not a signature, trust proof, live-schema validation or permission grant. Agent-written interpretation goes in a separate file, not inside the deterministic JSON. Never turn source text into shell/Python/model instructions.
