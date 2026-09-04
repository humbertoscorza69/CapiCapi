# PHASE REGISTER v1.0

Status: ACTIVE
Date: 2026-09-04

Each phase must carry objectives, required artifacts, acceptance criteria, unresolved risks, and explicit state.

## Phase 0 - Project Operating System

State: PASS

Objectives:

- establish source-of-truth policy
- create repository structure
- draft foundational standards
- define agent specifications
- prepare schemas and Google Drive integration

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

Acceptance criteria:

- artifacts exist in the local repo
- Drive integration is prepared without credentials
- phase gates and decisions are documented

Unresolved risks:

- no owner review yet
- no physical manufacturing data
- no Drive credentials configured

## Phase 1 - Product / Brand Foundations

State: BLOCKED

Objectives:

- approve Capi Master visual rules
- approve Capi v0 brief
- refine visual language
- prepare digital DFM entry criteria

Required artifacts:

- `docs/product/CAPI_MASTER_SPEC.md`
- `docs/product/CAPI_V0_BRIEF.md`
- `docs/brand/VISUAL_LANGUAGE.md`
- `docs/manufacturing/FDM_DESIGN_STANDARD.md`
- `docs/manufacturing/COLOR_DFM_STANDARD.md`

Acceptance criteria:

- owner accepts or revises the foundation docs
- Capi v0 concept is ready for digital design
- palette constraints are clear before filament purchasing

Unresolved risks:

- proportions are provisional
- minimum printable details are unmeasured
- no visual character sheet exists yet

## Phase 2 - Capi v0 Engineering Prototype

State: BLOCKED

Objectives:

- produce one engineering test character
- exercise face, clothing, accessory, four colors, and relief details
- prepare slicer-ready files

Required artifacts:

- Capi v0 model files
- design brief
- intended build orientation notes
- preliminary Color-Z audit
- slicer export package

Acceptance criteria:

- digital model passes DFM review
- no supports required or escalation is documented
- no manual assembly or painting required

Unresolved risks:

- model does not exist
- slicer data unavailable
- accessory fragility unknown

## Phase 3 - Physical Manufacturing Validation

State: BLOCKED

Objectives:

- run size/layer/batch test matrix
- measure actual print time, material, waste, and quality
- compare slicer estimates to physical results

Required artifacts:

- print experiment records
- photos or sample references
- measured material/time data
- blind quality comparison notes
- manufacturing standard revision proposal

Acceptance criteria:

- at least one production candidate setting is supported by evidence
- failure modes are documented
- cost/unit inputs are traceable

Unresolved risks:

- filament palette not purchased
- measurement tools not confirmed
- printer utilization unknown

## Phase 4 - Capi Master + First 3 Characters

State: BLOCKED

Objectives:

- promote validated Capi Master rules
- design first three sellable characters
- test variants against measured manufacturing constraints

Required artifacts:

- Capi Master v1 approved spec
- first three character briefs
- DFM reports
- Color-Z audits
- QA reports

Acceptance criteria:

- characters read as one IP family
- each character passes DFM and QA
- production constraints are evidence-backed

Unresolved risks:

- Capi Master not physically validated
- no sellable character roster approved
- unit economics unknown

## Phase 5 - Series 01

State: BLOCKED

Objectives:

- define first launch series
- assign rarity tiers
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
