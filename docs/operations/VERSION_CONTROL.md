# VERSION CONTROL v1.0

Status: ACTIVE
Date: 2026-09-04

## Branches

Default branch naming for Codex-created branches:

```text
codex/<short-purpose>
```

Examples:

- `codex/phase-1-capi-v0-brief`
- `codex/drive-sync`
- `codex/schema-updates`

## Document Versions

Specifications use explicit versions:

- `v1.0` for first approved baseline
- `v1.1` for compatible updates
- `v2.0` for rule changes that alter previous assumptions materially

Do not erase history when physical tests disprove a rule. Create a new version and document why.

## Schema Versions

Schema files use filenames like:

```text
schemas/agent_handoff.v1.schema.json
```

Breaking changes require a new major schema file.

## Commit Discipline

Every meaningful change should identify:

- what changed
- why it changed
- evidence or test status
- affected phase or decision ID when applicable

Before committing:

- inspect `git status`
- confirm no secrets are staged
- confirm generated local logs are not staged unless intentionally versioned

## Change Control

Major changes require a decision log entry when they affect:

- manufacturing philosophy
- Capi Master identity
- rarity/scarcity claims
- source-of-truth policy
- automation/publishing permissions
- hardware scaling
