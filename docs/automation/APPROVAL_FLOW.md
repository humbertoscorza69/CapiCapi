# APPROVAL FLOW v1.0

Status: RESERVED, NOT IMPLEMENTED
Date: 2026-09-04

## Purpose

Define future human approval before scheduling or publishing content.

## Flow

```text
Agent generates candidate
-> REVIEW
-> Telegram approval packet
-> Human decision
-> APPROVED / REJECTED / CHANGE_REQUESTED
```

Approved:

```text
APPROVED -> SCHEDULED -> PUBLISHED -> ANALYZED
```

Rejected:

```text
REJECTED -> archive or revise
```

Change requested:

```text
CHANGE_REQUESTED -> generation/editing
```

## Telegram Packet

Future packet fields:

- preview
- content ID
- Capi ID
- platform
- caption
- hook
- audio
- scheduled time
- experiment/hypothesis

## Rule

Human approval remains mandatory for publishing during MVP.
