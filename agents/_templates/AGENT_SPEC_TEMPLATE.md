# AGENT SPEC TEMPLATE v1.0

Status: TEMPLATE
Date: 2026-09-04

## Mission

State the agent's purpose in one or two sentences.

## Responsibilities

- TBD

## Allowed Tools

- local repository files relevant to the mission
- approved schemas
- approved integrations when configured

## Allowed Files / Documents

- TBD

## Forbidden Actions

- bypass phase gates
- fabricate measured data
- commit secrets
- publish content without approval
- purchase materials or services without explicit owner approval

## Inputs

- TBD

## Structured Outputs

Use versioned schemas where possible. If no schema exists, produce Markdown with explicit truth labels.

## Memory / Source Of Truth

List canonical documents that define the agent's memory.

## KPIs

- TBD

## Escalation Conditions

- missing data
- conflict between documents
- rule violation
- required human approval

## Handoff Rules

Define the next agent, required evidence, and schema.

## Stop Conditions

Define when the agent must stop instead of continuing.
