# 57-10-80-03 — MMIP Context Links

## Purpose

Define how wing operations events become MMIP (Multi-Modal Integration
Platform) capsules and threads for context management and long-term memory.

## MMIP Capsule Types

### Wing Operations Capsules

| Capsule Type | Content | Scope | Retention |
|--------------|---------|-------|-----------|
| SHM Event | Sensor data, alert, context | task | 90 days |
| Exceedance | Flight data, severity | task | Permanent |
| Usage Summary | Per-flight indices | user_long_term | Permanent |
| Inspection Finding | Finding details, photos | task | Permanent |
| Repair Record | Repair details, substantiation | user_long_term | Permanent |

### Capsule Schema

```json
{
  "capsule_id": "MMIP-57-yyyymmdd-nnnnnn",
  "capsule_type": "shm_event | exceedance | usage_summary | ...",
  "scope": "task | user_long_term",
  "created": "ISO 8601",
  "aircraft_id": "Q100-xxx",
  "content": {
    // Type-specific content
  },
  "metadata": {
    "ata_chapter": "57-10",
    "component": "string",
    "severity": "info | warning | critical"
  },
  "retention_policy": {
    "min_retention": "90d | permanent",
    "export_allowed": true,
    "anonymization": "none | partial | full"
  }
}
```

## Thread Organization

### Per-Aircraft Threads

| Thread | Content | Purpose |
|--------|---------|---------|
| Wing Health History | All SHM events | Long-term health tracking |
| Usage Chronicle | All usage summaries | Lifecycle management |
| Maintenance Log | All maintenance events | Audit trail |

### Fleet Threads

| Thread | Content | Purpose |
|--------|---------|---------|
| Fleet Wing Trends | Aggregated trends | Fleet management |
| Safety Events | All safety-related events | Safety analysis |
| Best Practices | Lessons learned | Knowledge base |

## Scope Definitions

### Task Scope

Short-term operational context:
- Single flight or inspection
- Active until closed
- Automatically archived after resolution
- Accessible for 90 days post-close

### User Long-Term Scope

Persistent knowledge:
- Aircraft lifecycle data
- Permanent retention
- Accessible by authorized users
- Contributes to fleet knowledge base

## Export/Retention Policies

### Regulatory Requirements

| Data Type | Retention | Export |
|-----------|-----------|--------|
| Safety events | 10 years | Required |
| Maintenance records | Aircraft life | Required |
| Flight data | 60 days (raw) | As required |
| Usage indices | Aircraft life | As required |

### Privacy Considerations

| Data Type | Anonymization | Sharing |
|-----------|---------------|---------|
| Flight crew data | Full | Aggregated only |
| Passenger data | N/A | Not captured |
| Aircraft data | None | Per agreement |
| Fleet data | Partial | Benchmarking only |

## Integration Points

### MMIP → CAOS

| Flow | Content | Trigger |
|------|---------|---------|
| Context retrieval | Historical capsules | Agent query |
| Pattern matching | Similar past events | Event processing |
| Knowledge lookup | Best practices | Decision support |

### CAOS → MMIP

| Flow | Content | Trigger |
|------|---------|---------|
| Capsule creation | New events | Event occurrence |
| Thread update | Status changes | State transitions |
| Knowledge deposit | Lessons learned | Analysis completion |

## References

- [57-10-80-01_CAOS_Events_Mapping](./57-10-80-01_CAOS_Events_Mapping.md)
- [57-10-80-02_Agent_Roles](./57-10-80-02_Agent_Roles.md)
- MMIP Standard documentation

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.

---
