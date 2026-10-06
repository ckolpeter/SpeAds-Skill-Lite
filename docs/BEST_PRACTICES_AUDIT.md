# Best-practices retrofit audit — 2026-10-06

Scope: SpeAds Skill Lite only. This is an implementation audit, not platform certification, account eligibility verification, or a claim of cross-model quality.

| Check | Result | Evidence |
|---|---|---|
| SKILL.md below 500 lines | PASS | Enforced by `scripts/release_gate.py`. |
| All runtime references directly linked from SKILL.md | PASS | Both reference files are in the Reference map; nested reference directories are rejected. |
| Long references have a content list | PASS (guarded) | `data-contract.md` has an explicit Contents section; any future reference over 100 lines without one fails release. |
| Degrees of freedom are explicit | PASS | Strategy prose is high freedom, plan shape medium freedom, financial/validation operations low freedom. |
| Ordered checklist | PASS | The Skill includes a concise order-sensitive checklist and failure-return rule. |
| Self-correction loop | PASS | Draft → validate → repair → revalidate is explicit and validators cannot be weakened. |
| Dependencies explicit | PASS | Python 3.10+ standard library only; no third-party runtime package or network dependency. |
| Cross-model evaluation | NOT_RUN | Required lanes are defined in `evals/MODEL_EVAL_MATRIX.md`; real host/model runs remain pending. |

## Release interpretation

A release-gate PASS proves repository structure and deterministic invariants only. It does not prove Shopee feature availability, seller eligibility, attribution quality, model quality, or advertising performance.
