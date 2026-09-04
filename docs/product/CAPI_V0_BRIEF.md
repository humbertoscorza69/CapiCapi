# CAPI V0 BRIEF v1.0

Status: DRAFT
Date: 2026-09-04
Truth level: PROVISIONAL

## Purpose

Capi v0 is an engineering test character, not a sellable launch character. Its purpose is to reveal physical constraints before CAPICAPI commits to a master character, palette, rarity system, or Series 01.

## Required Test Loads

Capi v0 must intentionally exercise:

- four colors
- eyes and face
- clothing
- one accessory
- embossed detail
- recessed detail
- moderate geometry complexity
- support-free printing
- AMS Lite multicolor behavior
- realistic collectible proportions

## Constraints

- Maximum automatic colors: 4.
- Target colors where possible: 3.
- Supports: target zero.
- Assembly: zero.
- Sanding: zero.
- Painting: zero.
- Post-processing: zero.

## Initial Character Concept

Working concept: `CAPI_ENGINEER_V0_TEST`

Reason: an engineer/test-lab theme can naturally include clothing, one fused tool/accessory, embossed details, and contrast zones without implying a final consumer character.

PROVISIONAL visual elements:

- base Capi body
- simple work vest or lab apron integrated into torso
- fused small wrench, caliper, or test badge accessory
- face with standard Capi eyes and muzzle
- relief markings to test line readability

## Palette

Do not buy filament until this palette is frozen.

| Role | Color | Status |
|---|---|---|
| Body | warm capybara brown/tan family | PROVISIONAL |
| Face/muzzle | lighter neutral | PROVISIONAL |
| Clothing | one saturated brand/test color | PROVISIONAL |
| Detail/accent | dark eye/detail color | PROVISIONAL |

Exact filament brands, SKUs, costs, and material behavior: TBD — REQUIRES PHYSICAL TEST.

## Digital DFM Requirements

Before physical printing:

- intended build orientation documented
- no auto-orient dependency
- no unsupported fragile protrusions
- accessory fused to main body
- color regions reviewed by Z-height
- slicer estimates captured
- Color-Z audit completed
- print plate layout drafted for 1 unit

## Physical Test Matrix

Only after digital DFM pass:

- sizes: 40 mm, 50 mm, 60 mm
- layer heights: 0.08 mm, 0.12 mm, 0.16 mm
- batching: 1 unit, 5 units, 10 units, maximum practical plate

All results must use real measurements.

## Success Criteria

Capi v0 succeeds if it produces useful manufacturing knowledge. It does not need to become a sellable character.

Pass conditions:

- at least one size/layer combination is physically acceptable
- support-free print is feasible or failure reasons are documented
- color-Z behavior is measured
- purge and print-time data are captured
- design standard can be updated from evidence

Fail conditions:

- face or detail language cannot be printed clearly
- accessory breaks or requires assembly
- supports become necessary without a compelling documented reason
- color strategy creates unacceptable purge/time behavior

## Open Questions

- Which exact accessory best tests print constraints without becoming fragile?
- Should clothing occupy a continuous Z band to reduce color swaps?
- Which body color family becomes the core brand identity?
- What is the target product size after blind quality comparison?
