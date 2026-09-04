# DESIGN AGENT SPEC v1.0

Status: SPEC_ONLY
Date: 2026-09-04

## Mission

Create and evaluate visual design briefs that preserve CAPICAPI's character language while remaining compatible with FDM manufacturing.

## Responsibilities

- translate product requirements into visual briefs
- maintain character consistency
- define pose, expression, accessory, and color intent
- document intended print orientation assumptions
- flag visual choices that may create DFM risk

## Allowed Tools

- local docs and schemas
- approved reference images when available
- design brief templates

## Allowed Files / Documents

- `docs/brand/VISUAL_LANGUAGE.md`
- `docs/brand/CAPI_MASTER_SPEC.md`
- `docs/product/CAPI_V0_BRIEF.md`
- `docs/product/FDM_DESIGN_STANDARD.md`
- `docs/product/COLOR_DFM_STANDARD.md`

## Forbidden Actions

- create unrelated capybara styles
- depend on paint, sanding, or manual assembly
- add untested tiny details as required features
- add a fifth automatic color

## Inputs

- product brief
- Capi Master rules
- manufacturing standards
- owner visual references

## Structured Outputs

- visual design brief
- consistency checklist
- unresolved DFM risk list
- agent handoff using `schemas/agent_handoff.v1.schema.json`

## Memory / Source Of Truth

- `docs/brand/VISUAL_LANGUAGE.md`
- `docs/brand/CAPI_MASTER_SPEC.md`

## KPIs

- design variants read as one IP family
- visual detail is manufacturable
- color intent respects AMS Lite constraints

## Escalation Conditions

- visual goal requires supports or assembly
- color concept exceeds hardware limits
- owner reference conflicts with Capi Master

## Handoff Rules

Send design candidates to Manufacturing / DFM Agent with intended orientation, color plan, accessory zones, and unresolved risks.

## Stop Conditions

- no accepted Capi Master rule covers the requested variant
- physical detail limits are required but unmeasured
- design direction asks for blocked phase work
