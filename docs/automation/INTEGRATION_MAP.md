# INTEGRATION MAP v1.0

Status: DRAFT
Date: 2026-09-04

## Purpose

Map integrations to responsibilities and source-of-truth boundaries.

## Integrations

| Integration | Local Home | Status | Purpose |
|---|---|---|---|
| Google Drive | `integrations/google_drive` | ACTIVE | Mirror docs and create Drive workspace folders. |
| Telegram | `integrations/telegram` | RESERVED | Future approval interface. |
| Instagram | `integrations/instagram` | RESERVED | Future platform asset/scheduling integration. |
| TikTok | `integrations/tiktok` | RESERVED | Future platform asset/scheduling integration. |
| AI Providers | `integrations/ai_providers` | RESERVED | Logical provider abstraction for reasoning, vision, image, video, voice. |

## Provider Roles

- `REASONING_PROVIDER`
- `VISION_PROVIDER`
- `IMAGE_PROVIDER`
- `VIDEO_PROVIDER`
- `VOICE_PROVIDER`

Provider implementations may change. CAPICAPI should not be tightly coupled to a single AI provider.
