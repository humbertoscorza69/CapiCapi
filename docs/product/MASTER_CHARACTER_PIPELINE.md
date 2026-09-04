# MASTER CHARACTER PIPELINE v1.1

Status: ACTIVE - PHASE 1A
Date: 2026-09-05

## Purpose

Define the correct progression from visual exploration to production-locked Capi Master. The visual master must not be permanently frozen before physical manufacturing tests reveal what survives FDM production.

## Progression

```text
Phase 1A - Visual direction exploration
-> Phase 1B - Provisional visual master / reference pack
-> Phase 1C - Provisional 3D master adapted for DFM
-> Phase 2 - Engineering/physical Capi v0 validation
-> Phase 3 - Capi Master v1.0 production lock
```

## Phase 1A - Visual Direction Exploration

Objective:

- retain four Round 0 visual directions and their twelve hero concepts as exploratory evidence
- propose Round 1 morphological hypotheses to test capybara recognition together with distinctive structural identity; generation requires explicit experiment approval
- keep quadruped/loaf and upright/mascot architecture open
- use specifically approved hero concepts as mandatory image references only after separate authorization for base views and later tests
- choose no final direction without human approval

Artifacts:

- `docs/brand/CAPI_VISUAL_DNA.md`
- `docs/brand/VISUAL_DIRECTION_EXPLORATION.md`
- `docs/brand/CHARACTER_REFERENCE_STANDARD.md`
- exploration scorecard or report later

Gate state: BLOCKED pending human approval of the Round 1 experiment and exact prompts. Round 0 was reviewed without selection. Proposed scope is ten morphological families with two independent single-view samples each; no generation or downstream development is authorized yet. See `docs/brand/VISUAL_DIRECTION_EXPLORATION.md` and D-0011.

## Phase 1B - Provisional Visual Master / Reference Pack

Objective:

- develop one approved visual direction into a provisional reference package

Required:

- orthographic view sheet
- silhouette sheet
- expression sheet
- proportion grid
- accessory-zone map
- immutable-feature map
- approved/rejected examples

Output remains provisional because FDM tests may force visual changes.

## Phase 1C - Provisional 3D Master Adapted For DFM

Objective:

- translate the approved visual reference package into a DFM-aware 3D candidate

Required:

- source model
- intended build orientation
- color-region architecture
- DFM review
- preliminary Color-Z audit
- handoff package to Print Agent

Output remains provisional until physical tests.

## Phase 2 - Engineering / Physical Capi v0 Validation

Objective:

- use Capi v0 as an engineering prototype to test printability, size, layer height, purge, waste, quality, and throughput

`docs/product/CAPI_V0_BRIEF.md` belongs here as the engineering prototype brief. It does not define CAPICAPI visual identity.

## Phase 3 - Capi Master v1.0 Production Lock

Objective:

- update the visual and 3D master from measured physical evidence
- approve production rules
- lock Capi Master v1.0 only after validation

## Gate Rule

Do not move from one step to the next without a documented gate decision. Human approval is mandatory between Phase 1A and Phase 1B.
