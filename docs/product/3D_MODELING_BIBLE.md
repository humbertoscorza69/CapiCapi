# 3D MODELING BIBLE v1.0

Status: DRAFT - PHASE 1A
Date: 2026-09-04
Truth level: PROVISIONAL unless explicitly marked `TBD — REQUIRES PHYSICAL TEST`.

## Purpose

This bible defines how an approved 2D/reference Capi design becomes a 3D production candidate. It integrates `docs/product/FDM_DESIGN_STANDARD.md` and `docs/product/COLOR_DFM_STANDARD.md`.

No final 3D geometry is created in Phase 1A.

## 1. Source / Reference Hierarchy

Use sources in this order:

1. approved human decision record
2. `docs/brand/CAPI_VISUAL_DNA.md`
3. approved character reference package from `docs/brand/CHARACTER_REFERENCE_STANDARD.md`
4. `docs/brand/VISUAL_LANGUAGE.md`
5. `docs/brand/CAPI_MASTER_SPEC.md`
6. `docs/product/FDM_DESIGN_STANDARD.md`
7. `docs/product/COLOR_DFM_STANDARD.md`
8. model-specific brief
9. slicer findings
10. physical print test results

If sources conflict, stop and escalate.

## 2. Base-Character Geometry Preservation

The base Capi geometry is the asset being protected.

Do not change without explicit approval:

- head silhouette
- muzzle identity
- eye family
- ear family
- body mass relationship
- paw/leg language
- default stance
- accessory zone map

Variants may add role-specific forms, but cannot redesign the base character.

## 3. Manifold / Watertight Requirements

Every production candidate must be:

- manifold
- watertight
- free of non-manifold edges
- free of accidental internal shells unless intentionally used and slicer-safe
- free of intersecting geometry that produces unreliable slicing
- consistently scaled
- oriented intentionally

Validation toolchain: TBD.

## 4. Allowed Body / Variant Modifications

Allowed with approval:

- integrated clothing panels
- fused hats/helmets
- fused glasses/visors
- relief badges
- thickened straps
- simplified bags/tools
- texture planes above tested printable limits

Not allowed by default:

- separate parts
- unsupported props
- thin dangling details
- hidden base identity
- pose changes that break the master silhouette

## 5. Intended Build Orientation

Build orientation is defined at the beginning of modeling.

The modeler must document:

- intended build face
- expected visible layer direction
- support-risk zones
- color-Z implications
- plate contact and stability

Do not rely on auto-orient as the engineering solution.

## 6. Zero-Support Design Philosophy

Target:

- zero supports
- zero manual assembly
- zero sanding
- zero painting
- zero post-processing

Any support requirement normally fails DFM unless a written exception is approved.

## 7. Overhang-Aware Construction

Use:

- chamfers
- self-supporting slopes
- gradual transitions
- fused geometry
- arches where useful

Numeric overhang limits remain `TBD — REQUIRES PHYSICAL TEST`.

## 8. Bridge-Aware Construction

Avoid open spans where possible. Where bridges are intentional, document:

- bridge location
- expected span
- visual consequence if sagging occurs
- slicer setting dependency

Bridge limits remain `TBD — REQUIRES PHYSICAL TEST`.

## 9. Fused-Accessory Rules

Accessories must:

- be fused to the body or a robust contact zone
- preserve base Capi recognition
- use thickened geometry
- avoid thin stems
- avoid support dependency
- be visible in the intended views

## 10. Fragile-Feature Avoidance

Reject:

- thin ears
- thin glasses arms
- hairline chains
- narrow antennae
- separate fingers/toes
- sharp protruding props
- micro buckles/buttons that snap or vanish

Minimum thickness remains `TBD — REQUIRES PHYSICAL TEST`.

## 11. Color-Region Architecture

Color regions must be planned as geometry.

Document:

- color count
- color role
- region boundaries
- whether boundaries follow natural geometry seams
- whether the region creates many Z-layer swaps

Maximum automatic colors: 4.

Target standard colors: 3 where possible.

## 12. Color-Z-Aware Modeling

The modeler must consider vertical color overlap while creating geometry.

Required later:

- vertical range of each color
- layer overlap risks
- estimated filament swaps
- purge risks
- prime tower expectation
- flush-to-infill opportunity

Unknown values are `TBD — REQUIRES SLICER DATA`.

## 13. Geometry-Vs-Color Decision Rules

Prefer relief geometry over extra filament color when:

- the detail is small
- color would add many swaps
- the feature can read as embossed/recessed detail
- the feature is accessory texture, stitching, buttons, zipper, badge, or seam

Use color when:

- it defines primary character readability
- it defines eyes/face at approved scale
- it materially improves collectible appeal
- it does not create unacceptable Color-Z cost

## 14. Detail Classes

### Structural Detail

Structural detail affects silhouette or physical volume.

Examples:

- helmet
- backpack
- large coat collar
- body pose
- ears
- paws

Structural detail must be DFM-reviewed early because it changes printability and recognition.

### Relief Detail

Relief detail communicates accessories/material without requiring extra filament color where possible.

Examples:

- stitching
- badge outline
- zipper line
- chain relief
- pocket seam

Relief detail must remain above tested printable dimensions.

### Micro Detail

Micro detail is below or near the reliable printable limit at approved nozzle/scale.

Examples:

- tiny text
- eyelashes
- miniature buttons
- hairline whiskers
- fine fabric grain

Micro detail is forbidden unless proven printable at the approved nozzle, scale, material, and layer height.

## 15. Minimum Feature Values

All minimum feature values are `TBD — REQUIRES PHYSICAL TEST`.

Required tests:

- raised line width
- recessed line width
- relief depth
- eye size
- muzzle detail
- ear root thickness
- accessory root thickness
- bridge span
- overhang behavior

## 16. Source File Requirements

Future source files must include:

- editable model source
- exported mesh
- units documented in millimeters
- version/revision ID
- source references
- intended build orientation
- color-region notes
- changelog/revision notes

Heavy source files belong in Drive, not Git.

## 17. STL / 3MF / Export Requirements

Required exports later:

- STL for geometry review where useful
- 3MF for Bambu Studio/project settings
- preview renders
- slicer screenshots/exports
- Color-Z audit input

Export requirements remain provisional until the first modeling toolchain is selected.

## 18. Naming / Versioning

Use stable IDs from `docs/operations/ID_STANDARD.md`.

Model revisions:

```text
CAPI-S01-001-M001
CAPI-S01-001-M002
```

Filenames are not identity. Metadata records are identity.

## 19. Visual QA

Visual QA checks:

- matches approved reference package
- passes costume-removed recognition test
- preserves head/body/muzzle/eye/ear/paw language
- avoids forbidden drift
- works in front, 3/4, side, and back views
- expression remains within allowed limits

## 20. DFM QA

DFM QA checks:

- intended orientation documented
- support-free target met
- no fragile features
- manifold/watertight
- color count <= 4
- Color-Z audit prepared
- no post-processing dependency
- no untested micro detail

## 21. Handoff To Print Agent

Required handoff package:

- model revision ID
- source reference package
- editable source file location
- export file locations
- intended build orientation
- color count and regions
- DFM notes
- unresolved risks
- slicer-ready package
- requested print test matrix

## 22. Rejection / Escalation Criteria

Reject or escalate if:

- visual DNA is not preserved
- more than 4 automatic colors are required
- supports are required
- manual assembly is required
- model is not manifold/watertight
- detail is below tested printable limit
- geometry depends on painting/sanding
- slicer data contradicts assumptions
- physical tests invalidate visual or DFM rules

## Phase 1A Boundary

This document prepares future modeling work. It does not authorize Capi v0 modeling or final consumer character design.
