# INVENTORY STANDARD v1.0

Status: DRAFT
Date: 2026-09-04

## Purpose

Inventory records prevent false scarcity claims and connect production batches to sellable units.

## Required Concepts

- SKU
- Capi ID
- series ID
- variant ID
- production batch ID
- unit count produced
- unit count failed
- unit count approved
- unit count sold
- unit count held back
- edition limit when applicable

## Source Of Truth

Phase 0/MVP inventory metadata belongs in Git as structured records. Heavy exports, labels, photos, and fulfillment artifacts belong in Drive under `09_INVENTORY` and `10_ORDERS`.

## Rules

- Do not claim edition limits until units are trackable.
- Do not silently exceed published edition limits.
- Keep prototypes and failed tests separate from sellable units.
