# CAPICAPI

CAPICAPI is a collectible character/IP business built around stylized physical capybara figures, scalable Bambu Lab FDM manufacturing, controlled visual language, and a later AI-assisted growth/content operating system.

This repository is the canonical technical source of truth. Google Drive may mirror selected documents for human collaboration, but important documents originate here as Markdown, JSON, or YAML and are synchronized deliberately.

## Current Scope

Active work is limited to:

- Phase 1A - CAPICAPI Visual DNA Definition
- visual direction exploration architecture
- reference package and 3D modeling standards
- Drive sync of canonical Phase 1A documents

Out of scope until explicit approval:

- Series 01 character design
- final Capi v0 modeling
- consumer character freeze
- filament color selection
- n8n workflow implementation
- cloud infrastructure
- content publishing automation
- fake manufacturing, sales, or content performance data

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
- `docs/product` - physical product, print, packaging, rarity, and series architecture
- `docs/automation` - n8n, approval flow, and integration architecture
- `docs/experiments` - physical print and content experiment protocols
- `docs/marketing` - content bible and creative taxonomy
- `docs/operations` - source-of-truth, phase gates, version control
- `docs/research` - verified external references and research notes
- `agents` - approved agent contracts, prompts, tools, and preserved detailed specs
- `n8n` - reserved version-controlled n8n workflow structure
- `schemas` - versioned JSON Schemas for structured handoffs
- `integrations` - prepared integrations, starting with Google Drive
- `config` - non-secret manifests and configuration
- `data/metadata` - lightweight MVP metadata records
- `logs` - non-secret local log contracts and generated-log homes
- `models`, `production`, `data`, `scripts`, `archive` - controlled work areas for later phases

## Immediate Next Action

Review and approve or revise the Phase 1A visual direction workflow in `docs/brand/VISUAL_DIRECTION_EXPLORATION.md`.

Do not begin Capi v0 modeling, filament color selection, Series 01, or consumer character production until the Phase 1A visual direction receives explicit human approval.
