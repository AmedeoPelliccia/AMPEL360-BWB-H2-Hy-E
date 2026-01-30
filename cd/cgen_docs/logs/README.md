# CGen Docs Logs

This directory contains execution logs for CGen Docs Waves.

## Log Format

Logs are stored in JSONL (JSON Lines) format, one entry per processed document:

```json
{
  "timestamp": "2025-12-04T12:00:00Z",
  "batch_id": "BATCH_ONBOARD_A",
  "document": "path/to/document.md",
  "model": "gpt-5.1-codex",
  "tokens_used": 1500,
  "changed": true,
  "summary": "Added cross-references to ATA 21"
}
```

## Log Files

Each batch creates its own log file:
- `BATCH_ONBOARD_A.jsonl`
- `BATCH_ONBOARD_B.jsonl`
- `BATCH_INFRA_A.jsonl`

Wave reports are generated as Markdown:
- `BATCH_XXX_report.md`

---
