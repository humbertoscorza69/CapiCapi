# Roadmap

This roadmap is gate-driven. Later phases do not begin until the current phase has explicit `PASS`, `FAIL`, or `BLOCKED` status and the next phase has a documented entry condition.

## Phase 0 - Project Operating System

Objectives:

- Establish repository and Drive operating structure.
- Create canonical status, roadmap, changelog, and decision log.
- Draft foundation standards, schemas, agents, and integration scaffolds.
- Prepare Google Drive mirroring without credentials in Git.

Acceptance criteria:

- Required files exist and are understandable without this conversation.
- Source-of-truth policy is documented.
- Secrets policy is documented and enforced through `.gitignore`.
- Drive hierarchy exists for operational assets.

Status: PASS

## Phase 1A - CAPICAPI Visual DNA Definition

Objectives:

- Define what makes a CAPICAPI character recognizable before final 3D modeling.
- Create the standard for future approved reference images.
- Retain the four Round 0 art directions as evidence and explore distinct Round 1 morphological hypotheses after explicit experiment approval; no Round 0 winner is selected.
- Define how visual identity survives costume, role, and series changes.
- Create the modeling bible without modeling Capi v0.

Acceptance criteria:

- `docs/brand/CAPI_VISUAL_DNA.md` exists and is accepted or revised.
- `docs/brand/CHARACTER_REFERENCE_STANDARD.md` exists and is accepted or revised.
- `docs/brand/VISUAL_DIRECTION_EXPLORATION.md` preserves Round 0 and proposes the Round 1 morphological hook experiment, exact prompts, and review gates before later base views, expressions, or role tests.
- `docs/product/3D_MODELING_BIBLE.md` and `docs/product/MASTER_CHARACTER_PIPELINE.md` define future 3D handoff rules.
- Human owner explicitly approves the next visual direction step.

Status: BLOCKED pending human visual approval.

## Phase 1B - Provisional Visual Master / Reference Pack

Objectives:

- Produce the approved 2D visual master and reference package.
- Define provisional proportions, silhouette rules, expression limits, accessory zones, and immutable features from approved reference images.
- Record approved and rejected examples.

Acceptance criteria:

- Required reference package passes `docs/brand/CHARACTER_REFERENCE_STANDARD.md`.
- Visual DNA values move from TBD to provisional only where supported by approved images.
- Owner approves the provisional visual master.

Status: BLOCKED

## Phase 1C - Provisional 3D Master Adapted for DFM

Objectives:

- Translate the approved 2D/reference package into provisional 3D master geometry.
- Adapt the design for support-free FDM production on the Bambu Lab A1.
- Preserve base-character geometry while preparing for slicer and physical testing.

Acceptance criteria:

- 3D candidate follows `docs/product/3D_MODELING_BIBLE.md`.
- DFM and Color-Z checks are completed.
- Handoff to the Print Agent is ready.

Status: BLOCKED

## Phase 2 - Engineering / Physical Capi v0 Validation

Objectives:

- Use `docs/product/CAPI_V0_BRIEF.md` as an engineering prototype brief.
- Print and measure what survives real FDM production.
- Validate scale, strength, detail, color-region behavior, purge waste, print time, and operator effort.

Acceptance criteria:

- Physical tests are recorded with real measurements.
- Minimum feature values are updated from evidence.
- Provisional master changes are proposed where physical production requires them.

Status: BLOCKED

## Phase 3 - Capi Master v1.0 Production Lock

Objectives:

- Lock Capi Master v1.0 only after physical validation.
- Convert provisional visual/DFM findings into production rules.
- Define what may and may not change across sellable variants.

Acceptance criteria:

- Production-lock decision is recorded.
- Visual DNA, modeling bible, and manufacturing standards agree.
- Capi Master v1.0 is ready for sellable character development.

Status: BLOCKED

## Phase 4 - First Sellable Character Set

Objectives:

- Design first sellable CAPICAPI characters from the locked master.
- Validate role, costume, expression, and accessory variation against production rules.

Acceptance criteria:

- Characters read as one IP family.
- Each character passes visual, product, DFM, and QA review.

Status: BLOCKED

## Phase 5 - Series 01

Objectives:

- Define a coherent launch series after sellable character validation.
- Control rarity, SKU, packaging, inventory, and truthful scarcity mechanics.

Acceptance criteria:

- Series plan, SKUs, production constraints, and scarcity controls are approved.

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
