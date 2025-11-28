# 57-10-60-03 — SHM Alarm Policies

## Purpose

Define the alarm policies for Structural Health Monitoring (SHM) alerts,
including thresholds, severity levels, and required actions.

## Alarm Levels

### Level 1 – Advisory

| Characteristic | Description |
|----------------|-------------|
| Display | Maintenance page |
| Crew action | None required in flight |
| Dispatch impact | None |
| Maintenance action | Review at next scheduled check |

### Level 2 – Caution

| Characteristic | Description |
|----------------|-------------|
| Display | EICAS caution |
| Crew action | Awareness, monitor |
| Dispatch impact | MEL consideration |
| Maintenance action | Inspect before next flight |

### Level 3 – Warning

| Characteristic | Description |
|----------------|-------------|
| Display | EICAS warning |
| Crew action | Reduce loads, consider divert |
| Dispatch impact | No dispatch |
| Maintenance action | Ground until resolved |

## Alarm Thresholds

### Strain-Based Alerts

| Parameter | Advisory | Caution | Warning |
|-----------|----------|---------|---------|
| Root bending strain | > 70% limit | > 85% limit | > 95% limit |
| Skin panel strain | > 70% limit | > 85% limit | > 95% limit |
| Spar cap strain | > 65% limit | > 80% limit | > 90% limit |

### Damage Detection Alerts

| Detection Type | Advisory | Caution | Warning |
|----------------|----------|---------|---------|
| Acoustic emission | Pattern A | Pattern B | Pattern C |
| Disbond area | > TBD cm² | > TBD cm² | > TBD cm² |
| Crack indication | Initial detect | Growth detected | Critical size |

### Sensor Health Alerts

| Condition | Advisory | Caution | Warning |
|-----------|----------|---------|---------|
| Sensor drift | > 5% | > 10% | > 20% |
| Sensor failure | Single | Multiple in zone | Critical coverage loss |
| Data quality | Intermittent | Degraded | Failed |

## Alert Actions

### In-Flight Actions

| Alert Level | Pilot Action | Dispatch Action |
|-------------|--------------|-----------------|
| Advisory | None | Continue ops |
| Caution | Monitor, note | MEL check |
| Warning | Reduce loads, consider divert | Ground |

### Ground Actions

| Alert Level | Maintenance Action | Engineering Action |
|-------------|-------------------|-------------------|
| Advisory | Review at next check | None |
| Caution | Inspect before next flight | Evaluate if required |
| Warning | Ground, detailed inspection | Full evaluation required |

## Alert Reset Criteria

| Condition | Reset Method |
|-----------|--------------|
| Transient exceeded | Automatic after 60 s normal |
| Sustained exceeded | Engineering evaluation |
| Damage detected | Inspection + engineering signoff |
| Sensor failure | Sensor replacement |

## References

- [57-10-60-01_SHM_Sensor_Layout](./57-10-60-01_SHM_Sensor_Layout.md)
- [57-10-60-02_SHM_Data_Paths](./57-10-60-02_SHM_Data_Paths.md)
- [57-10-80_CAOS_INTEGRATION](../57-10-80_CAOS_INTEGRATION/) (alert routing)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.

---
