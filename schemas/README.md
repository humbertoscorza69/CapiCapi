# Schemas

Status: ACTIVE
Date: 2026-09-04

CAPICAPI schemas define machine-readable handoffs, gates, audits, experiments, and integration manifests.

Versioning:

- schema filenames include a major version, for example `agent_handoff.v1.schema.json`
- breaking changes require a new major schema file
- compatible additions can be documented in the same major version if consumers tolerate optional fields

Current schemas:

- `capi.schema.json`
- `series.schema.json`
- `model_revision.schema.json`
- `print_test.schema.json`
- `production_batch.schema.json`
- `content_item.schema.json`
- `experiment.schema.json`
- `publication.schema.json`
- `agent_event.schema.json`
- `agent_handoff.v1.schema.json`
- `phase_gate.v1.schema.json`
- `color_z_audit.v1.schema.json`
- `print_experiment_result.v1.schema.json`
- `content_experiment.v1.schema.json`
- `drive_manifest.v1.schema.json`
