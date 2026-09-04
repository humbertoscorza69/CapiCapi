# PRODUCTION WORKFLOW v1.0

Status: DRAFT
Date: 2026-09-04

## Purpose

Define the production operating flow from concept through approved batch without starting Capi v0 modeling.

## Workflow

```text
concept
-> product brief
-> visual design
-> DFM review
-> Color-Z audit
-> slicer package
-> print test
-> measured analysis
-> revision
-> production approval
-> batch record
-> inventory update
```

## Records

Required record types:

- Capi/product record
- model revision record
- print test record
- production batch record
- inventory record

## Drive Evidence

Heavy evidence belongs in Drive:

- model files
- 3MF/STL files
- slicer screenshots/exports
- photos/videos
- timelapses
- test print media

Metadata belongs in Git under `data/metadata` until a database is justified.
