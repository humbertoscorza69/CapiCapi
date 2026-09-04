# Roadmap

This roadmap is gate-driven. Later phases do not begin until the current phase has explicit `PASS`, `FAIL`, or `BLOCKED` status and the next phase has a documented entry condition.

## Phase 0 - Project Operating System

Objectives:

- Establish repository structure.
- Create canonical status, roadmap, changelog, and decision log.
- Draft foundation standards.
- Define initial agent specifications.
- Create versioned schemas.
- Prepare Google Drive mirroring without credentials in Git.

Acceptance criteria:

- Required files exist and are understandable without this conversation.
- Source-of-truth policy is documented.
- Secrets policy is documented and enforced through `.gitignore`.
- Phase gate status is recorded.

Status: PASS

## Phase 1 - Product / Brand Foundations

Objectives:

- Stabilize Capi Master visual rules.
- Freeze Capi v0 design intent.
- Define initial palette constraints before buying filament.
- Confirm rarity and series architecture principles without fake probabilities.

Acceptance criteria:

- `docs/product/CAPI_MASTER_SPEC.md` accepted.
- `docs/brand/VISUAL_LANGUAGE.md` accepted.
- `docs/product/CAPI_V0_BRIEF.md` accepted.
- Manufacturing standards are ready for digital DFM review.

Status: BLOCKED pending review and Capi v0 design brief completion.

## Phase 2 - Capi v0 Engineering Prototype

Objectives:

- Produce one engineering test character model.
- Exercise 4 colors, face, clothing, one accessory, embossed/recessed details, and support-free geometry.
- Prepare slicer-ready files for DFM review.

Acceptance criteria:

- Digital model passes DFM review.
- Color-Z audit is completed from slicer data.
- No Series 01 work begins.

Status: BLOCKED

## Phase 3 - Physical Manufacturing Validation

Objectives:

- Run size, quality, and batching tests.
- Compare slicer estimates against measured physical results.
- Identify production size, layer height, batching approach, and unit economics.

Acceptance criteria:

- Test matrix recorded with real measurements.
- Blind perceived-quality comparison completed.
- Manufacturing standard updated from measured data.

Status: BLOCKED

## Phase 4 - Capi Master + First 3 Characters

Objectives:

- Promote tested Capi Master rules.
- Design first three sellable characters from one coherent IP language.
- Validate variants against manufacturing data.

Acceptance criteria:

- First three characters pass product, visual, DFM, and QA review.
- Edition and rarity claims are truthful and trackable.

Status: BLOCKED

## Phase 5 - Series 01

Objectives:

- Define a coherent launch series.
- Control common, uncommon, rare, epic, legendary, and secret/shiny mechanics.
- Prepare packaging and fulfillment assumptions for validation.

Acceptance criteria:

- Series plan, SKUs, production constraints, and truth-in-scarcity controls are approved.

Status: BLOCKED

## Phase 6 - Content / Growth Engine v0

Objectives:

- Run human-approved creative experiments.
- Track viral and commercial scores separately.
- Build repeatable content briefs and QA checks.

Acceptance criteria:

- Manual approval loop exists.
- Experiment data model is populated with real content results.

Status: BLOCKED

## Phase 7 - Automated Experimentation Engine

Objectives:

- Connect trend, strategy, creative, QA, approval, scheduling, analytics, and learning loops.
- Keep owner approval mandatory before publishing.

Acceptance criteria:

- Automation only operates on validated schemas and source documents.
- No auto-publishing without explicit approval.

Status: BLOCKED

## Phase 8 - Production Scaling

Objectives:

- Decide when to add printers or improve workflow based on measured utilization and demand.

Acceptance criteria:

- Expansion decision is supported by measured printer-hours, demand, yield, labor, and margin data.

Status: BLOCKED
