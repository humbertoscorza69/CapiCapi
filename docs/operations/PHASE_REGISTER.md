# PHASE REGISTER v1.3

Status: ACTIVE
Date: 2026-09-05

Each phase must carry objectives, required artifacts, acceptance criteria, unresolved risks, and explicit state.

## Phase 0 - Project Operating System

State: PASS

Objectives:

- establish source-of-truth policy
- create repository structure
- draft foundational standards
- define agent specifications
- prepare schemas and Google Drive integration
- implement local/GitHub and Drive filesystem architecture

Required artifacts:

- `README.md`
- `PROJECT_STATUS.md`
- `ROADMAP.md`
- `DECISIONS.md`
- foundational docs
- agent specs
- schemas
- Drive manifest and setup docs
- `PHASE_0_REPORT.md`
- `PHASE_0_ARCHITECTURE_AUDIT.md`

Acceptance criteria:

- artifacts exist in the local repo
- Drive integration is prepared without credentials
- phase gates and decisions are documented
- Drive operational hierarchy is created idempotently
- owner approves Phase 0

Unresolved risks:

- no physical manufacturing data
- no approved visual master

## Phase 1A - CAPICAPI Visual DNA Definition

State: BLOCKED pending explicit approval of the Round 1 morphological experiment and prompts. Round 0 reviewed without selection; no downstream development authorized.

Objectives:

- define the required CAPICAPI visual identity attributes before final geometry
- define the final character reference package standard
- retain four Round 0 art directions as evidence and propose materially different Round 1 morphological construction rules
- define a future 3D modeling bible without beginning final 3D modeling
- reclassify `docs/product/CAPI_V0_BRIEF.md` as a future engineering prototype brief

Required artifacts:

- `docs/brand/CAPI_VISUAL_DNA.md`
- `docs/brand/CHARACTER_REFERENCE_STANDARD.md`
- `docs/brand/VISUAL_DIRECTION_EXPLORATION.md`
- `docs/product/3D_MODELING_BIBLE.md`
- `docs/product/MASTER_CHARACTER_PIPELINE.md`
- updated `docs/product/CAPI_V0_BRIEF.md`

Acceptance criteria:

- visual DNA requirements cover head/body proportions, silhouettes, muzzle, eyes, ears, paws, stance, curvature, expressions, accessory zones, immutable/flexible traits, and forbidden drift
- exploration process preserves Round 0 evidence, adds an explicitly approved Round 1 morphological hero screen, and requires separate authorization for later full base-character views, expressions, and role tests
- no final numeric proportions, filament colors, consumer characters, Capi v0 models, or Series 01 assets are frozen
- owner approves or amends Round 1 scope and exact prompts before generation; proposed scope is ten families with two independent samples each
- owner evaluates capybara recognition, distinctive morphology, and accessory compatibility together, including conceptual envelopes, repeatable dressing architecture, and identity survival under substantial coverage; no automatic ranking or premature body-architecture selection
- severe systematic accessory/FDM conflicts prevent a recommendation to advance until resolved; custom accessory geometry alone is not a failure, and Round 1 contains no costume generation
- owner separately authorizes hero survivors for Base Character Round development or requests more exploration; later tests and a Phase 1B decision remain required

Unresolved risks:

- no approved visual master exists yet
- no approved reference images exist yet
- final numeric ratios remain `TBD — REQUIRES APPROVED VISUAL MASTER`
- printable minimums remain `TBD — REQUIRES PHYSICAL TEST`

## Phase 1B - Provisional Visual Master / Reference Pack

State: BLOCKED

Objectives:

- create the approved base Capi 2D visual master
- assemble the full reference package required by `docs/brand/CHARACTER_REFERENCE_STANDARD.md`
- define provisional visual DNA values from approved reference images
- record approved and rejected examples

Required artifacts:

- approved orthographic and 3/4 reference sheets
- silhouette sheet
- proportion grid
- expression sheet
- color and material reference
- accessory-zone map
- immutable-feature map
- approved/rejected example set
- updated `docs/brand/CAPI_VISUAL_DNA.md`

Acceptance criteria:

- owner approves the provisional visual master
- reference package is complete enough for future Design and 3D Modeling Agents
- visual identity survives costume tests

Unresolved risks:

- selected direction may fail costume/series stress tests
- visual master may require simplification for FDM later

## Phase 1C - Provisional 3D Master Adapted for DFM

State: BLOCKED

Objectives:

- translate approved 2D/reference geometry into a provisional 3D master candidate
- preserve base-character visual DNA while adapting for FDM
- prepare slicer-ready geometry for engineering validation

Required artifacts:

- source modeling file
- STL/3MF export package
- visual QA report
- DFM QA report
- Color-Z audit
- handoff package to the Print Agent

Acceptance criteria:

- candidate follows `docs/product/3D_MODELING_BIBLE.md`
- geometry is manifold, watertight, intentionally oriented, and zero-support by design or escalated
- base-character geometry changes are documented and approved

Unresolved risks:

- 2D visual features may not survive printable scale
- color-region boundaries may create unacceptable purge or print risk

## Phase 2 - Engineering / Physical Capi v0 Validation

State: BLOCKED

Objectives:

- use `docs/product/CAPI_V0_BRIEF.md` as an engineering prototype brief
- print and measure the provisional master under realistic constraints
- validate detail, scale, strength, color changes, purge waste, print time, failure rate, and operator effort

Required artifacts:

- Capi v0 engineering model package
- slicer profile/package
- print experiment records
- photos/videos of test prints
- measured material/time/waste data
- issue and revision log

Acceptance criteria:

- physical test matrix is complete enough to revise standards
- minimum feature values are evidence-backed
- the visual master is revised if FDM evidence requires it

Unresolved risks:

- filament palette not selected
- measurement tools not confirmed
- printer utilization unknown
- accessory fragility unknown

## Phase 3 - Capi Master v1.0 Production Lock

State: BLOCKED

Objectives:

- lock Capi Master v1.0 only after physical validation
- reconcile visual DNA, 3D model, DFM rules, and manufacturing evidence
- define the production-safe invariant base for future variants

Required artifacts:

- Capi Master v1.0 approved spec
- production-locked source model
- production export package
- physical validation report
- updated manufacturing standards
- recorded production-lock decision

Acceptance criteria:

- visual identity and FDM survivability are both proven
- all remaining TBD values are either measured, approved provisional, or explicitly deferred
- owner approves production lock

Unresolved risks:

- physical test data may require visual redesign
- unit economics may be unacceptable at desired quality

## Phase 4 - First Sellable Character Set

State: BLOCKED

Objectives:

- design first sellable characters from Capi Master v1.0
- validate roles, costumes, accessories, and expressions against locked visual DNA
- avoid beginning Series 01 before sellable character readiness

Required artifacts:

- first sellable character briefs
- reference sheets
- DFM reports
- Color-Z audits
- QA reports

Acceptance criteria:

- characters read as one IP family
- each character passes product, visual, DFM, and QA review
- production constraints are evidence-backed

Unresolved risks:

- no sellable character roster approved
- packaging and pricing may change scope

## Phase 5 - Series 01

State: BLOCKED

Objectives:

- define first launch series
- assign rarity tiers only after production feasibility is known
- plan truthful mystery/edition mechanics

Required artifacts:

- Series 01 plan
- character roster
- SKU/variant table
- rarity control plan
- batch and inventory control method

Acceptance criteria:

- rarity claims are truthful and trackable
- production plan matches measured printer capacity
- launch scope is operationally feasible

Unresolved risks:

- demand unknown
- packaging not validated
- fulfillment controls not defined

## Phase 6 - Content / Growth Engine v0

State: BLOCKED

Objectives:

- create manual content experiment loop
- define approval packets
- measure viral and commercial outcomes separately

Required artifacts:

- content experiment records
- approval workflow notes
- creative templates
- analytics export process

Acceptance criteria:

- every creative has a hypothesis
- human approval occurs before publishing
- results are recorded with structured variables

Unresolved risks:

- product assets may not exist
- platform access unavailable
- sales attribution unknown

## Phase 7 - Automated Experimentation Engine

State: BLOCKED

Objectives:

- connect trend, strategy, creative, QA, approval, scheduling, posting, analytics, and learning loop
- keep publishing controlled by approval

Required artifacts:

- automation architecture
- n8n workflows or equivalent
- approval integration
- QA gates
- monitoring and rollback plan

Acceptance criteria:

- automation consumes approved source documents
- no auto-publish without approval
- failures are visible and recoverable

Unresolved risks:

- platform APIs and rules may change
- automation may amplify bad claims
- approval latency may affect cadence

## Phase 8 - Production Scaling

State: BLOCKED

Objectives:

- decide when to add printers or staff/process changes
- scale from measured demand and utilization

Required artifacts:

- utilization report
- demand report
- yield/failure analysis
- labor model
- expansion decision proposal

Acceptance criteria:

- capacity bottleneck is proven
- added hardware is financially justified
- quality and fulfillment can scale

Unresolved risks:

- demand may be temporary
- operator labor may become bottleneck before printer count
- quality control may degrade with volume
