# SECURITY STANDARD v1.0

Status: ACTIVE
Date: 2026-09-04

## Purpose

Protect credentials, tokens, private operational data, and public-claim integrity.

## Forbidden In Git

- `.env`
- OAuth credentials
- OAuth tokens
- API keys
- access tokens
- private keys
- generated heavy media
- raw photos/videos
- STL/3MF production assets

## Forbidden In Drive Documentation

- plaintext secrets
- OAuth client secrets
- refresh tokens
- API keys
- passwords

## Required Checks

Before commits:

- run `git status`
- confirm secrets are ignored
- avoid staging generated logs unless explicitly intended

Before publishing:

- verify human approval
- verify product claims
- verify rarity/scarcity claims

## Current Secret Paths

These local files may exist and must remain ignored:

- `integrations/google_drive/credentials.json`
- `integrations/google_drive/token.json`
- `integrations/google_drive/sync_log.jsonl`
