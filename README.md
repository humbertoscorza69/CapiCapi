# CAPICAPI

CAPICAPI is a collectible character/IP business built around stylized physical capybara figures, scalable Bambu Lab FDM manufacturing, controlled visual language, and a later AI-assisted growth/content operating system.

This repository is the canonical technical source of truth. Google Drive may mirror selected documents for human collaboration, but important documents originate here as Markdown, JSON, or YAML and are synchronized deliberately.

## Current Scope

Active work is limited to:

- Phase 0 - Project Operating System
- Phase 1 - Product / Brand Foundations documentation foundation only

Out of scope for this first run:

- Series 01 character design
- n8n workflow implementation
- cloud infrastructure
- content publishing automation
- fake manufacturing, sales, or content performance data
- filament purchasing decisions

## Manufacturing Starting Point

Known starting hardware:

- Bambu Lab A1
- 0.4 mm nozzle
- AMS Lite
- maximum 4 automatic filament colors
- one printer only until real demand and utilization justify expansion

Measured manufacturing performance is currently unavailable. All cost, quality, yield, time, purge, and labor assumptions remain `TBD — REQUIRES PHYSICAL TEST`.

## Operating Principle

Product design and manufacturing engineering are one process:

```text
concept
-> visual design
-> FDM design-for-manufacturing
-> color-Z analysis
-> slicing
-> unit economics
-> physical test
-> revision
-> production approval
```

The slicer is part of product design.

## Repository Map

- `docs/brand` - visual language and brand/IP rules
- `docs/product` - master character spec, rarity, series architecture
- `docs/manufacturing` - FDM and AMS Lite color design standards
- `docs/experiments` - physical print and content experiment protocols
- `docs/marketing` - content bible and creative taxonomy
- `docs/operations` - source-of-truth, phase gates, version control
- `docs/research` - verified external references and research notes
- `agents` - agent specifications and templates
- `schemas` - versioned JSON Schemas for structured handoffs
- `integrations` - prepared integrations, starting with Google Drive
- `config` - non-secret manifests and configuration
- `models`, `production`, `data`, `scripts`, `archive` - controlled work areas for later phases

## Immediate Next Action

Review `PHASE_0_REPORT.md`, confirm the Phase 0 gate, then begin Phase 1 by turning `docs/product/CAPI_MASTER_SPEC.md` and `docs/product/CAPI_V0_BRIEF.md` into a digital Capi v0 design brief ready for DFM review.
