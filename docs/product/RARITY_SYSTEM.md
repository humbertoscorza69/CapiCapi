# RARITY SYSTEM v1.0

Status: DRAFT
Date: 2026-09-04
Truth level: PROVISIONAL

## Purpose

The rarity system creates collectible structure while keeping scarcity claims truthful and operationally manageable.

## Initial Rarity Tiers

Working tiers:

- COMMON
- UNCOMMON
- RARE
- EPIC
- LEGENDARY
- SECRET
- SHINY

Probabilities: TBD. Do not publish odds until production, inventory, and fulfillment controls are ready.

## Truthful Scarcity Rules

- If an edition says 200 units, never silently produce 500.
- If odds are published, they must match actual pull mechanics.
- If a variant is retired, reprints must be explicitly labeled.
- Defects, test prints, and prototypes must not be mixed into consumer rarity counts unless disclosed.

## Manufacturing Cost Is Not Rarity

Rare does not need to mean harder or more expensive to manufacture.

Examples:

- a one-color gold/silk/glow Capi may be visually rare while cheaper to print than a 4-color common
- a common role may require more color changes than a shiny single-material role

The rarity system should use this intelligently, but never deceptively.

## Mystery Pull Control

Before mystery/random pulls are offered, the project needs:

- SKU definitions
- production batch records
- inventory tracking
- edition count controls
- fulfillment records
- returned/defective unit handling
- published consumer claim review

Status: BLOCKED until production validation.

## Metadata Fields

Each collectible should eventually define:

- `character_id`
- `series_id`
- `variant_id`
- `rarity_tier`
- `edition_type`
- `edition_limit`
- `manufacturing_batch_id`
- `material_profile`
- `release_status`

## Open Risks

- Probability design without real demand data may create bad inventory.
- Complex rarity mechanics may outpace manufacturing controls.
- Scarcity claims create legal and brand risk if not tracked rigorously.
