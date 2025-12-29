# 56-10-01-002 — Heating System Check

| Field | Value |
|-------|-------|
| **Document ID** | 56-10-01-002 |
| **Version** | 1.0 |
| **Date** | 2025-12-02 |
| **Status** | DRAFT |
| **Classification** | OPERATIONAL |

---

## 1. Purpose

This procedure defines the pre-flight functional check sequence for the windshield and window heating systems, ensuring anti-ice and anti-fog capabilities are serviceable before flight.

## 2. Scope

Applicable to all AMPEL360 Q100 aircraft equipped with:

- Windshield heating system (ATA 56-25)
- Side window heating elements
- Heating controller (LRU 56-25-01)

## 3. Prerequisites

- Aircraft on ground power or APU running
- Exterior temperature noted (affects heating response time)
- No active window heating faults displayed
- Heating system circuit breakers verified IN

## 4. Procedure

### 4.1 System Power-Up

| Step | Action | Expected Result | Notes |
|------|--------|-----------------|-------|
| 1 | Verify WINDOW HEAT CB — IN | CB engaged | OVHD panel |
| 2 | Select WINDOW HEAT → ON | System powers | Controller active |
| 3 | Monitor system self-test | PASS within 30 s | Automatic sequence |
| 4 | Verify no heating faults | No amber/red indications | EICAS/ECAM |

### 4.2 Heating Element Test

| Step | Action | Expected Result | Notes |
|------|--------|-----------------|-------|
| 5 | Select HEAT TEST mode | Test sequence initiates | If equipped |
| 6 | Monitor L/R windshield temp rise | Both panels respond | Temperature display |
| 7 | Verify side window heating | Indicators normal | If heated side windows |
| 8 | Check ammeter readings | Within limits per AMM | Power draw normal |
| 9 | Select HEAT TEST → OFF | Normal operation resumes | End test mode |

### 4.3 Controller Status

| Step | Action | Expected Result | Notes |
|------|--------|-----------------|-------|
| 10 | Review heating system page | All channels GREEN | MFD/ECAM |
| 11 | Verify AUTO mode available | AUTO selectable | Normal dispatch |
| 12 | Check overheat protection status | ARMED | Safety circuit |

## 5. Operating Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| OFF | Heating disabled | Ground ops, warm conditions |
| LOW | Anti-fog / light icing | Taxi, light moisture |
| NORMAL | Standard operation | In-flight, normal icing |
| HIGH | Heavy icing conditions | Severe weather |
| AUTO | Temperature-controlled | Default in-flight |

## 6. Fault Response

| Indication | Meaning | Action |
|------------|---------|--------|
| WINDOW HEAT FAIL | Controller failure | Check CB, refer MEL |
| OVHT L/R WSHLD | Overheat detected | System auto-shuts, maintenance required |
| TEMP SENSOR FAIL | Sensor malfunction | Manual mode available, MEL dispatch |

## 7. Completion Criteria

- All heating elements respond to test
- No active faults or warnings
- AUTO mode available for dispatch
- Overheat protection armed

## 8. Related Documents

- [README.md](./README.md) — Preflight bucket overview
- [56-10-01_001_Window-Preflight-Inspection.md](./56-10-01_001_Window-Preflight-Inspection.md) — Visual inspection
- [56-10-01_003_Rain-Repellent-Servicing.md](./56-10-01_003_Rain-Repellent-Servicing.md) — Rain repellent servicing

## 9. Traceability

| Requirement ID | Description |
|----------------|-------------|
| REQ-56-10-002 | Pre-flight heating system verification |
| REQ-56-25-001 | Windshield heating controller functionality |
| REQ-56-25-002 | Overheat protection requirements |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-02.

---

*END OF DOCUMENT*
