# COLOR DFM STANDARD v1.0

Status: DRAFT
Date: 2026-09-04
Truth level: PROVISIONAL

## Purpose

Color is a manufacturing variable, not only a visual choice. CAPICAPI must track color count, color placement through Z, filament swaps, purge, prime tower use, and printer-hours per unit.

## Color Limits

Rules:

- maximum 4 automatic colors per standard Capi
- target 3 colors when possible
- 4 colors only when visually justified or needed for Capi v0 testing
- no fifth color for realism alone

## Geometry Before Color

Use geometry to communicate:

- chains
- stitching
- buttons
- watches
- zippers
- badges
- seams
- texture

If a detail can be communicated by relief without harming printability, prefer geometry over another filament color.

## Color-Z Audit

Every production candidate requires a Color-Z audit.

Required fields:

- colors
- vertical range of each color
- number of filament swaps
- purge volume
- purge ratio
- prime tower usage
- flush-to-infill opportunity
- units per plate
- printer-hours per unit
- color-related failure risks

Unknown values must be marked `TBD — REQUIRES SLICER DATA` or `TBD — REQUIRES PHYSICAL TEST`.

## Pass / Fail Guidance

PASS requires:

- 4 or fewer automatic colors
- no unplanned manual filament changes
- acceptable support-free geometry
- documented color-Z audit
- no color detail below tested printable size

FAIL normally applies when:

- more than 4 automatic colors are needed
- color regions cause excessive swaps with no visual justification
- a color is used for a detail that relief could handle better
- the design depends on painting

BLOCKED applies when:

- slicer data is unavailable
- palette is not frozen
- physical behavior of the material/color combination is unknown

## Flush Strategy

Hierarchy:

1. No support.
2. Flush into internal geometry where legitimate.
3. Flush into a useful secondary object if practical.
4. Unavoidable purge.

Do not design unnecessary supports just to consume purge.

## Open Risks

- A 4-color visual design may be uneconomical if colors overlap through many Z layers.
- Shiny/special materials may print differently from standard materials.
- Flush-to-infill benefit is unknown until slicer and physical tests are recorded.
