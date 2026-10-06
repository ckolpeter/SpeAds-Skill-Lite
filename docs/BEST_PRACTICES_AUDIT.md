# Best-practices retrofit audit — 2026-10-07

Scope: SpeAds Skill Lite only. This is an implementation and scoped behavior audit, not platform certification, account eligibility verification, or a claim of live advertising performance.

| Check | Result | Evidence |
|---|---|---|
| SKILL.md below 500 lines | PASS | Enforced by `scripts/release_gate.py`. |
| All runtime references directly linked from SKILL.md | PASS | Both Markdown reference files are in the Reference map; nested reference directories are rejected. |
| Long references have a content list | PASS (guarded) | `data-contract.md` has an explicit Contents section; any future reference over 100 lines without one fails release. |
| Degrees of freedom are explicit | PASS | Strategy prose is high freedom, plan shape medium freedom, financial/validation operations low freedom. |
| Ordered checklist | PASS | The Skill includes a concise order-sensitive checklist and failure-return rule. |
| Self-correction loop design | PASS | Draft → validate → repair → revalidate is explicit and validators may not be weakened. |
| Self-correction loop behavior | PASS (scoped) | Observed in Claude Code with Haiku 4.5, Sonnet 5, and Opus 5 using a `publish_authorized` tamper; all three rejected the fault, repaired the artifact, and revalidated successfully. |
| Dependencies explicit | PASS | Python 3.10+ standard library only; no third-party runtime package or network dependency. |
| Cross-model baseline behavior | PASS (scoped) | Haiku 4.5, Sonnet 5, and Opus 5 each completed the same synthetic planning/validation baseline while preserving unknowns and Lite boundaries. |
| Full host/model matrix | PARTIAL | Natural multi-Skill discovery, source-routing questions, report ambiguity cases, and Codex compatibility remain NOT_RUN. |

## Observed warnings

- Haiku completed correctly but took extra no-overwrite directory-management steps during the self-correction setup.
- Sonnet produced one evaluation report with an unreliable date; report metadata accuracy is therefore a warning, not a Skill safety failure.
- Opus inspected more project files than Sonnet during self-correction; no unsafe change or unnecessary platform-source read was demonstrated.

## Release interpretation

A release-gate PASS plus the scoped model-evaluation PASS establishes stronger confidence in local routing, deterministic delegation, safety-boundary handling, and repair/revalidation behavior for the tested fixtures. It still does not prove Shopee feature availability, seller eligibility, attribution quality, policy compliance, automatic Skill discovery, Codex behavior, or advertising performance.

Detailed observed and remaining lanes are recorded in `evals/MODEL_EVAL_MATRIX.md`.
