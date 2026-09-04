# PHASE GATES v1.0

Status: ACTIVE
Date: 2026-09-04

## Gate State Values

Every phase must be one of:

- PASS
- FAIL
- BLOCKED

## Required Gate Fields

Every phase gate record must include:

- phase ID
- phase name
- objectives
- required artifacts
- acceptance criteria
- unresolved risks
- evidence
- decision or status date
- gate state

## Current Gates

Phase 0: PASS

Phase 1: BLOCKED until owner review and Capi v0 design brief approval.

Phases 2-8: BLOCKED until prior gates pass.

## Gate Discipline

- Do not skip gates.
- Do not start Series 01 before Capi v0 physical validation.
- Do not treat drafted docs as measured evidence.
- Do not proceed from BLOCKED without resolving the stated blocker.
- Record meaningful gate changes in `DECISIONS.md` or `PROJECT_STATUS.md`.
