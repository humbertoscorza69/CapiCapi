# LIFECYCLE AND STATUS STANDARD v1.0

Status: ACTIVE
Date: 2026-09-04

## Asset Lifecycle

Canonical content/product asset lifecycle:

```text
RAW
-> INGESTED
-> PROCESSED
-> GENERATED
-> REVIEW
-> APPROVED
-> SCHEDULED
-> PUBLISHED
-> ANALYZED
```

Not every asset uses every state. For example, a raw printing timelapse may move from `RAW` to `INGESTED` to `PROCESSED` without being scheduled.

## Status Values

Use these values unless a schema narrows them:

- `RAW`
- `INGESTED`
- `CLASSIFIED`
- `IDEA`
- `PROCESSED`
- `GENERATED`
- `REVIEW`
- `APPROVED`
- `SCHEDULED`
- `PUBLISHED`
- `ANALYZED`
- `REJECTED`
- `ARCHIVED`
- `BLOCKED`

## Product Status

Product/Capi status values:

- `NOT_STARTED`
- `CONCEPT`
- `DESIGN_REVIEW`
- `DFM_REVIEW`
- `PRINT_TEST`
- `REVISION_REQUIRED`
- `APPROVED_FOR_PRODUCTION`
- `RETIRED`
- `BLOCKED`

## Experiment Status

Experiment status values:

- `DRAFT`
- `RUNNING`
- `MEASURED`
- `ADOPTED`
- `REJECTED`
- `RETEST`
- `BLOCKED`

## Approval Status

Approval status values:

- `NOT_REQUESTED`
- `PENDING`
- `APPROVED`
- `REJECTED`
- `CHANGE_REQUESTED`

## Rule

Status is stored in metadata records. Folder location may reflect status for human workflow, but folder location is not the database.
