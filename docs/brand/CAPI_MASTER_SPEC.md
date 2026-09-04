# CAPI MASTER SPEC v1.0

Status: DRAFT - PROVISIONAL MASTER RULES
Date: 2026-09-04
Truth level: PROVISIONAL except where explicitly marked `KNOWN` or `TBD — REQUIRES PHYSICAL TEST`.

## Purpose

The Capi Master defines the visual and manufacturing rules that make every CAPICAPI character recognizable as part of one IP family. Variants such as Doctor, Biker, Wizard, or Astronaut must read as the same core character in different roles, not as unrelated capybara models.

Phase 1A note: this document is structurally useful but not specific enough to define final proprietary visual IP by itself. `docs/brand/CAPI_VISUAL_DNA.md` now owns Phase 1A visual identity definition, and this master spec remains provisional until visual reference and physical manufacturing validation are complete.

## Immutable Features

These features define the core Capi identity:

- compact capybara silhouette with calm, grounded posture
- rounded head and body language with no sharp realism
- broad, simple muzzle area
- small rounded ears integrated into the head mass
- low, sturdy legs/paws
- simple eye language that remains readable at small physical sizes
- accessory and clothing details integrated into the body where possible
- support-free intended build orientation

## Flexible Features

These may change by character variant:

- clothing theme
- accessory type
- expression within approved emotional range
- surface texture if printable and not fragile
- color palette within AMS Lite constraints
- embossed/recessed detail patterns
- pose variation within printability rules

## Body Proportions

All values are provisional until Capi v0 physical testing is complete.

| Attribute | Rule |
|---|---|
| Overall height | TBD — REQUIRES PHYSICAL TEST. Initial matrix: 40 mm, 50 mm, 60 mm. |
| Head/body ratio | PROVISIONAL: head and body should feel like one compact collectible mass, not a realistic animal sculpture. |
| Body mass | PROVISIONAL: rounded, loaf-like, stable on the build plate. |
| Legs/paws | PROVISIONAL: short, thick, and structurally robust. |
| Ear size | PROVISIONAL: readable but not fragile. Minimum thickness TBD. |
| Muzzle size | PROVISIONAL: broad enough to carry nose/mouth geometry without paint. |

## Eye Language

Allowed:

- calm dot or capsule eyes
- subtle eyelid geometry
- small expression changes through brow/eye angle if printable

Disallowed:

- tiny eyelashes or hairline details
- paint-dependent eyes
- realistic wet-eye detail
- eye geometry below tested printable size

Minimum printable eye and relief dimensions: TBD — REQUIRES PHYSICAL TEST.

## Muzzle Language

Allowed:

- broad snout plane or raised muzzle zone
- simple nose geometry
- recessed or embossed mouth marks if physically readable

Disallowed:

- thin whiskers
- paint-only facial detail
- undercuts or overhangs that require supports

## Ear Language

Ears should be rounded, fused into the head, and robust enough to survive handling. They should not be thin independent tabs.

Minimum ear root thickness: TBD — REQUIRES PHYSICAL TEST.

## Paw And Leg Language

Legs and paws should communicate capybara anatomy in simplified collectible form. They must also act as stable print and display geometry.

Allowed:

- subtle paw separations
- low relief toe indications
- integrated stance aids

Disallowed:

- thin protruding toes
- separate paw parts
- support-dependent leg gaps

## Silhouette

Every Capi variant must pass the silhouette test:

- recognizable as CAPICAPI with accessories removed or ignored
- recognizable from front, 3/4, and side
- stable visual mass with no fragile perimeter details
- accessory does not overpower the base character

## Allowed Expressions

Initial expression set:

- calm
- curious
- mildly serious
- sleepy
- proud
- surprised

Disallowed initial expressions:

- aggressive
- horror/gore
- hyper-realistic animal emotion
- expression dependent on paint or microscopic detail

## Accessory Zones

Preferred zones:

- head top/front: hats, helmets, small fused crowns
- face: fused glasses, masks, visors
- torso/front: badges, coats, armor relief
- side body: simplified bags, tools, shields
- back: cape, backpack, shell-like forms if support-free

Accessories must be fused, thickened, chamfered, and designed around build orientation.

## Naming Convention

Working format:

```text
CAPI_[ROLE]_[SERIES]_[VARIANT]
```

Examples:

- `CAPI_ENGINEER_V0_TEST`
- `CAPI_WIZARD_S01_COMMON`
- `CAPI_ASTRONAUT_S01_RARE`

Final consumer names may be more playful, but internal IDs must remain stable and machine-readable.

## Reference Poses

Initial allowed pose families:

- neutral standing loaf
- seated loaf
- walking hint with connected legs
- upright mini mascot stance

Every pose must pass DFM before visual approval.

## Minimum Printable Feature Sizes

No numeric minimums are approved yet.

Required tests:

- embossed line width
- recessed line width
- raised dot diameter
- eye insert diameter
- ear root thickness
- accessory stem thickness
- readable relief depth
- bridge length
- acceptable overhang angle by actual printer/material profile

Status: TBD — REQUIRES PHYSICAL TEST.

## Master Approval Checklist

- Core silhouette is recognizable.
- Variant reads as a CAPICAPI character.
- No more than 4 automatic colors.
- 3 colors used where visually sufficient.
- Color-Z audit completed.
- No supports required unless escalated with documented reason.
- No manual assembly.
- No sanding, painting, or post-processing.
- Minimum details are above tested printable limits.
- Naming and metadata are complete.

## Open Risks

- Visual proportions are not validated against physical prints.
- No character sheet exists yet.
- Minimum feature sizes are unknown.
- Accessory rules may change after Capi v0 failure analysis.
