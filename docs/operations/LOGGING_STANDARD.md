# LOGGING STANDARD v1.0

Status: ACTIVE
Date: 2026-09-04

## Purpose

Define logging requirements for future agents, n8n workflows, sync jobs, and error/dead-letter handling.

## Local Log Homes

- `logs/agents`
- `logs/n8n`
- `logs/sync`
- `logs/errors`

## Minimum Agent Run Fields

- `run_id`
- `agent`
- `workflow`
- `started_at`
- `finished_at`
- `status`
- `inputs`
- `outputs`
- `artifacts`
- `model_provider`
- `model_name`
- `prompt_version`
- `token_cost`
- `api_cost`
- `error_details`
- `retry_count`
- `human_decision`

## Error / Dead Letter Handling

Failures should create records with:

- source workflow
- failing input
- error class
- retry count
- next owner
- recovery recommendation
- whether human action is required

## Security

Logs must never contain plaintext secrets, access tokens, OAuth refresh tokens, API keys, passwords, or full credential JSON.
