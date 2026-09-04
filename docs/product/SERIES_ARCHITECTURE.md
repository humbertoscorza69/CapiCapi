# SERIES ARCHITECTURE v1.0

Status: DRAFT
Date: 2026-09-04
Truth level: PROVISIONAL

## Purpose

Series architecture defines how CAPICAPI groups characters, variants, rarity tiers, and releases without losing visual or manufacturing control.

## Required Sequence

The order is mandatory:

1. Phase 1A visual direction approval
2. Phase 1B provisional visual master / reference pack
3. Phase 1C provisional 3D master adapted for DFM
4. Phase 2 engineering / physical Capi v0 validation
5. Phase 3 Capi Master v1.0 production lock
6. first sellable character set
7. Series 01

Series 01 must not begin before Capi Master v1.0 production lock and sellable character validation.

## Series Anatomy

A series should eventually include:

- series ID
- theme
- character roster
- variant list
- rarity tier mapping
- manufacturing constraints
- packaging rules
- release window
- inventory plan
- content hooks
- retirement/reprint policy

## Candidate Series ID Format

```text
S01_CORE
S02_SEASONAL
S03_ADVENTURE
```

The exact public naming system is not finalized.

## Character Entry Template

```yaml
character_id: CAPI_ROLE_S01_COMMON
series_id: S01_CORE
role: TBD
rarity_tier: TBD
color_count: TBD
support_required: TBD
accessory: TBD
dfm_status: BLOCKED
release_status: NOT_STARTED
```

## Launch Discipline

Series 01 requires:

- coherent visual language
- physically validated detail limits
- known production speed and cost ranges
- documented packaging assumptions
- truthful rarity mechanics
- content plan tied to actual characters

## Open Risks

- Designing too many characters before measured constraints can create wasted modeling effort.
- Theme-first planning may push characters outside the Capi Master language.
- Manufacturing bottlenecks may require fewer launch SKUs than desired.
