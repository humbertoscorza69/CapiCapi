# CONTENT EXPERIMENT STANDARD v1.0

Status: DRAFT
Date: 2026-09-04

## Purpose

Define the standard for content experiments across raw media, generated assets, review, approval, publishing, and analysis.

## Lifecycle

```text
RAW
-> INGESTED
-> PROCESSED/GENERATED
-> REVIEW
-> APPROVED
-> SCHEDULED
-> PUBLISHED
-> ANALYZED
```

## Required Record

Use `schemas/content_item.schema.json` for content assets and `schemas/experiment.schema.json` for marketing experiments.

## Approval

No content moves from `REVIEW` to `SCHEDULED` without human approval.
