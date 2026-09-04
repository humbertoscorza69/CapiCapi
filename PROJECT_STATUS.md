# Project Status

Date: 2026-09-05

## Gate Summary

| Phase | Name | State | Notes |
|---|---|---:|---|
| Phase 0 | Project Operating System | PASS | Owner approved Phase 0; repository and Drive operating structure are active. |
| Phase 1A | CAPICAPI Visual DNA Definition | BLOCKED | Owner reviewed Round 0 without selection; Round 1 morphological experiment is proposed and awaits explicit generation approval. |
| Phase 1B | Provisional Visual Master / Reference Pack | BLOCKED | Requires owner selection or revision of a Phase 1A visual direction. |
| Phase 1C | Provisional 3D Master Adapted for DFM | BLOCKED | Requires approved 2D/reference package from Phase 1B. |
| Phase 2 | Engineering / Physical Capi v0 Validation | BLOCKED | Requires provisional DFM-adapted 3D master; `CAPI_V0_BRIEF.md` is an engineering prototype brief only. |
| Phase 3 | Capi Master v1.0 Production Lock | BLOCKED | Requires measured physical validation showing what survives FDM production. |
| Phase 4 | First Sellable Character Set | BLOCKED | Requires Capi Master v1.0 production lock. |
| Phase 5 | Series 01 | BLOCKED | Requires approved sellable character set and production constraints. |
| Phase 6 | Content / Growth Engine v0 | BLOCKED | Requires approved product assets and human approval process. |
| Phase 7 | Automated Experimentation Engine | BLOCKED | Requires validated manual experiment loop and data model. |
| Phase 8 | Production Scaling | BLOCKED | Requires measured demand, utilization, yield, and unit economics. |

## Current Truth Classification

- `KNOWN`: project intent, initial hardware constraint, local repo as source of truth, phase model.
- `MEASURED`: none yet.
- `ESTIMATED`: none approved yet.
- `ASSUMED`: that initial manufacturing will target Bambu Lab A1 + AMS Lite only.
- `PROVISIONAL`: visual language, product rules, agent responsibilities, schemas.
- `TBD — REQUIRES PHYSICAL TEST`: print time, quality level, purge waste, failure rate, labor per unit, cost per unit, preferred physical size.

## Active Risks

- No physical Capi v0 has been modeled, sliced, or printed.
- No filament palette is frozen.
- Google Drive credentials and token are configured locally and ignored by Git.
- Google Drive folder/file IDs are recorded in `config/drive_manifest.json`.
- Approved local/GitHub and Drive filesystem architecture is implemented.
- Phase 0 architecture audit is recorded in `PHASE_0_ARCHITECTURE_AUDIT.md`.
- Phase 1A architecture and Round 0 framework were owner-approved; no character design is approved.
- Round 0 was reviewed without selection and remains exploratory evidence in Drive.
- Round 1 proposes ten morphological families with two independent hero samples each (20 images); this scope and its exact prompts are not yet approved. No Round 1 images exist.
- Quadruped/loaf versus upright/mascot remains open; neither architecture is selected.
- No consumer character has been frozen.
- No content, sales, or production analytics data exists.
- Visual IP rules are not yet validated against approved reference images or physical model tests.

## Required Before Phase 1A PASS

- Owner approves or amends the Round 1 experiment and prompts in `docs/brand/VISUAL_DIRECTION_EXPLORATION.md` before generation.
- After approved exploration, owner reviews the evidence and separately authorizes any Base Character Round development using specifically approved hero references.
- Later base, expression, and role validation and an explicit Phase 1B decision are still required; experiment approval is not Phase 1A completion.
- No final numeric ratios are frozen unless they come from an approved visual master.
- No Capi v0 engineering prototype work begins.

Canonical phase details are maintained in `docs/operations/PHASE_REGISTER.md`.
