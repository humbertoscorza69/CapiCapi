# CHARACTER REFERENCE STANDARD v1.0

Status: DRAFT - PHASE 1A
Date: 2026-09-04
Truth level: PROVISIONAL

## Purpose

This standard defines the final reference package required after a visual direction is approved. The reference package becomes mandatory context for future Design and 3D Modeling Agents.

No final reference package exists yet.

## Required Reference Package

An approved Capi visual master must include:

- orthographic front view
- front 3/4 view
- side view
- back view
- top view where useful
- silhouette sheet
- proportion grid
- expression sheet
- color reference
- material reference
- accessory-zone map
- immutable-feature map
- `DO NOT CHANGE` examples
- approved examples
- rejected examples

## View Requirements

All views must describe the same character geometry.

Front:

- head/body relationship
- eye placement
- muzzle width
- ear placement
- paw/leg stance

Front 3/4:

- muzzle projection
- cheek/head curvature
- eye wrap or placement behavior
- accessory zone readability

Side:

- head profile
- muzzle projection
- back/body curve
- leg/body integration
- intended build-orientation implications

Back:

- body silhouette
- ear/back relationship
- back accessory zone
- tail/no-tail rule if relevant

Top where useful:

- head depth
- body footprint
- ear placement
- stance footprint

## Silhouette Sheet

The silhouette sheet must show:

- front silhouette
- 3/4 silhouette
- side silhouette
- back silhouette
- costume-removed silhouette
- quick costume silhouettes

Purpose: prove recognition without color, surface details, or captions.

## Proportion Grid

The grid must capture visual proportions without prematurely converting them into production dimensions.

Required:

- total height units
- head height/mass units
- body height/mass units
- muzzle block position
- eye centerline
- ear placement zone
- foot/base footprint

Status: TBD — REQUIRES APPROVED VISUAL MASTER.

## Expression Sheet

The expression sheet must show:

- neutral
- calm
- curious
- sleepy
- proud
- surprised
- mildly serious

Each expression must preserve the same eye/muzzle family.

## Color Reference

Color references should define roles, not final filament SKUs:

- body color role
- muzzle color role
- eye/detail role
- costume/accent role

Exact filament selections remain blocked until DFM and physical testing.

## Material Reference

Material reference may include:

- matte body finish
- shiny/silk variant behavior
- glow/special material candidates
- texture intent

All material behavior remains `TBD — REQUIRES PHYSICAL TEST`.

## Accessory-Zone Map

Must show where accessories may attach without destroying base recognition:

- head
- face
- torso/front
- side body
- back
- base/feet where applicable

Each zone must include visual and future DFM notes.

## Immutable-Feature Map

Must label features that cannot change between variants:

- head silhouette
- muzzle identity
- eye family
- ear family
- body mass
- stance/paw language

Final list remains provisional until a direction is approved.

## DO NOT CHANGE Examples

The package must include negative examples showing unacceptable drift:

- generic bear head
- hamster-like body
- realistic capybara
- over-accessorized costume hiding the base form
- fragile thin detail
- micro-detail expression

## Approved And Rejected Examples

Every future direction decision should store:

- approved images
- rejected images
- rejection reason
- decision date
- approver
- linked decision ID

## Storage

Canonical reference-package requirements live in Git. Heavy reference images and sheets belong in Drive under:

```text
CAPICAPI/01_PRODUCT/BASE_CAPI/REFERENCES
```

When approved, metadata must store Drive file IDs and stable visual master IDs. Do not rely only on filenames.
