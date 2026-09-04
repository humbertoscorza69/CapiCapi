# FDM DESIGN STANDARD v1.0

Status: DRAFT
Date: 2026-09-04
Truth level: PROVISIONAL unless marked `KNOWN` or `TBD — REQUIRES PHYSICAL TEST`.

## Purpose

CAPICAPI figures are designed for FDM production from the beginning. Product design, visual design, slicing, and unit economics are one workflow.

## Known Hardware Context

Initial production hardware:

- Bambu Lab A1
- 0.4 mm nozzle
- AMS Lite
- one printer

Official current reference facts verified on 2026-09-04:

- Bambu lists A1 build volume as 256 mm x 256 mm x 256 mm.
- Bambu lists the included A1 nozzle diameter as 0.4 mm.
- Bambu states A1 supports one AMS Lite, which means a maximum of 4 colors.

Sources are recorded in `docs/research/SOURCES.md`.

## Manufacturing Philosophy

Targets:

- zero supports
- zero manual assembly
- zero sanding
- zero painting
- zero post-processing

Ideal process:

```text
PRINT
-> REMOVE FROM BUILD PLATE
-> QC
-> PACKAGE
```

Every minute of manual labor per unit is a scaling defect.

## Intended Build Orientation

Every model must define its intended build orientation before slicing.

Rules:

- Do not rely on auto-orient as the engineering solution.
- Model around the intended orientation.
- Accessories must be fused and self-supporting in that orientation.
- Failure in intended orientation returns to design unless escalated.

## Support-Free Geometry

Use:

- self-supporting angles
- chamfers instead of hard unsupported ledges
- arches where appropriate
- controlled bridges
- fused accessories
- contact geometry
- robust ears/accessories
- integrated clothing
- embossed/recessed details

Avoid:

- thin chains
- dangling parts
- unsupported hats or tools
- narrow separated limbs
- high-relief details that snap
- details that require sanding or painting

## Overhangs And Bridges

Approved numeric limits: TBD — REQUIRES PHYSICAL TEST.

Until tested, the DFM agent must classify overhang and bridge assumptions as PROVISIONAL and require slicer/print validation.

## Minimum Detail Rules

No minimum printable numeric values are approved yet.

Test categories:

- raised line width
- recessed line width
- relief depth
- eye diameter
- nose geometry
- accessory root thickness
- leg separation
- bridge span
- text/icon readability

Status: TBD — REQUIRES PHYSICAL TEST.

## Failure Conditions

A design normally fails DFM if it requires:

- support material
- manual assembly
- painting
- sanding
- brittle independent accessory geometry
- more than 4 automatic colors
- unmeasured claims about production speed, cost, or quality

Escalations require a documented reason and decision log entry.

## DFM Review Output

Every candidate must produce:

- model ID
- intended orientation
- color count
- support status
- fragile-feature notes
- Color-Z audit
- slicer estimate
- unit economics placeholder
- DFM status: `PASS`, `FAIL`, or `BLOCKED`

## Open Risks

- Physical printer calibration may alter acceptable overhang/detail rules.
- Filament choice may affect small details and color bleed.
- Support-free targets may conflict with some attractive accessory concepts.
