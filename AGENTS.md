# CAPICAPI Agent Operating Contract v1.0

Status: ACTIVE
Date: 2026-09-04

## Purpose

This file is the root contract for future CAPICAPI agents. Agent runtimes are not activated in Phase 0; this repository establishes their homes, responsibilities, permissions, prompts, and data contracts.

## Logical Agents

| Agent | Local Home | Drive Output Home | Mission |
|---|---|---|---|
| ORCHESTRATOR | `agents/orchestrator` | `CAPICAPI/11_AGENT_OUTPUTS/ORCHESTRATOR` | Coordinates phases, handoffs, decisions, and gate discipline. |
| DESIGN AGENT | `agents/design` | `CAPICAPI/11_AGENT_OUTPUTS/DESIGN_AGENT` | Owns Capi visual rules, variants, colors, and DFM-aware design briefs. |
| PRODUCTION AGENT | `agents/production` | `CAPICAPI/11_AGENT_OUTPUTS/PRODUCTION_AGENT` | Owns production planning, batch records, inventory requirements, and fulfillment readiness. |
| PRINT AGENT | `agents/print` | `CAPICAPI/11_AGENT_OUTPUTS/PRINT_AGENT` | Owns Bambu/FDM profiles, print tests, waste, material/time benchmarks, and test evidence. |
| CONTENT AGENT | `agents/content` | `CAPICAPI/11_AGENT_OUTPUTS/CONTENT_AGENT` | Owns content concepts, hooks, scripts, captions, creative variants, and approval packets. |
| SOCIAL AGENT | `agents/social` | `CAPICAPI/11_AGENT_OUTPUTS/SOCIAL_AGENT` | Later owns scheduling/publishing coordination and platform-specific packaging after human approval. |
| ANALYTICS AGENT | `agents/analytics` | `CAPICAPI/11_AGENT_OUTPUTS/ANALYTICS_AGENT` | Owns performance ingestion, experiments, KPI analysis, winner/loser detection, and recommendations. |

## Permissions

Agents may read canonical local documentation, schemas, prompts, and non-secret configuration. Agents may write structured metadata and reports only to their assigned repository or Drive output areas.

Agents must not:

- bypass phase gates
- fabricate measured data
- commit secrets
- print credentials or tokens
- publish content without human approval
- buy materials or services
- treat filenames as database identifiers
- silently rewrite decision history

## Structured Outputs

Every future agent run should emit:

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
- `cost`
- `error`
- `retry_count`
- `human_decision`

Use `schemas/agent_event.schema.json` for run records and `schemas/agent_handoff.v1.schema.json` for cross-agent handoffs.

## Source Of Truth

Git owns agent definitions, prompts, schemas, workflow definitions, tests, and configuration templates. Drive owns heavy outputs, generated media, renders, working files, raw assets, and operational exports.

Structured metadata must be recorded in version-controlled JSON/CSV files for Phase 0/MVP. A database may be introduced later only if actual workflow volume justifies it.

## Phase 0 Stop Rule

Phase 0 establishes the operating structure. It does not begin Capi v0 modeling, filament selection, social publishing automation, or live n8n workflows.
