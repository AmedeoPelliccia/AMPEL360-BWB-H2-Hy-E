# 61-20-01_05_001 — Reliability Data

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-01_05_001_Reliability_Data       |
| **Subsystem**      | 61-20-01_Electric_Motor                |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Version**        | 1.0                                    |
| **Last Updated**   | 2025-12-01                             |
| **Owner**          | AMPEL360 Propulsion Team               |
| **Standard**       | OPT-IN Framework v1.2                  |

---

## 1. Reliability Requirements

### 1.1 Design Life

| Parameter | Value | Unit |
|-----------|-------|------|
| Design Service Life | 60,000 | FH |
| Design Cycles | 30,000 | Cycles |
| Calendar Life | 25 | Years |

### 1.2 Reliability Targets

| Parameter | Target | Notes |
|-----------|--------|-------|
| MTBF | 50,000 FH | Mean Time Between Failures |
| MTBUR | 15,000 FH | Mean Time Between Unscheduled Removals |
| Dispatch Reliability | 99.8% | Per departure |
| Mission Reliability | 99.95% | Per flight |

---

## 2. Failure Modes and Effects Analysis (FMEA) Summary

### 2.1 Critical Failure Modes

| FM ID | Failure Mode | Effect | Severity | Detection | RPN |
|-------|--------------|--------|----------|-----------|-----|
| FM-001 | Winding short circuit | Loss of motor power | 9 | Temperature, current | 144 |
| FM-002 | Bearing seizure | Motor lockup | 10 | Vibration, temperature | 120 |
| FM-003 | Magnet demagnetization | Reduced power output | 7 | Torque feedback | 98 |
| FM-004 | Resolver failure | Loss of position feedback | 8 | PCU diagnostics | 96 |
| FM-005 | Coolant leak | Thermal runaway | 8 | Flow sensor, level | 112 |
| FM-006 | Insulation breakdown | Ground fault, fire | 10 | Insulation monitoring | 100 |

### 2.2 Failure Rate Predictions

| Component | Failure Rate (per 10⁶ FH) | Source |
|-----------|---------------------------|--------|
| Stator Winding | 8.5 | NPRD-2016 |
| Rotor Assembly | 2.1 | NPRD-2016 |
| DE Bearing | 15.0 | Manufacturer data |
| NDE Bearing | 12.0 | Manufacturer data |
| Resolver | 5.0 | Manufacturer data |
| Temperature Sensors | 3.0 | Generic |
| Connectors | 2.5 | MIL-HDBK-217F |
| **Total Motor** | **48.1** | Sum |

---

## 3. Component Life Limits

### 3.1 Life-Limited Parts (LLPs)

| Part | Life Limit | Basis | Part Number |
|------|------------|-------|-------------|
| Drive-End Bearing | 30,000 FH | Fatigue | 61-20-01-100 |
| Non-Drive-End Bearing | 30,000 FH | Fatigue | 61-20-01-101 |
| Rotor Retaining Sleeve | 60,000 FH | Fatigue | 61-20-01-102 |
| Shaft Coupling | 60,000 FH | Fatigue | 61-20-01-103 |

### 3.2 Condition-Monitored Parts

| Part | Monitoring Method | Threshold |
|------|-------------------|-----------|
| Stator Windings | Insulation resistance | < 100 MΩ |
| Permanent Magnets | Back-EMF test | < 95% nominal |
| Bearings | Vibration signature | ISO 10816 Zone C |
| Resolver | Accuracy check | > ±5 arcmin error |

---

## 4. Maintenance Concept

### 4.1 Maintenance Levels

| Level | Tasks | Location |
|-------|-------|----------|
| Line | Visual inspection, connector check | Aircraft |
| Base | Sensor replacement, bearing change | Hangar |
| Shop | Overhaul, rewind | OEM/MRO |

### 4.2 Maintenance Intervals

| Task | Interval | Duration | Personnel |
|------|----------|----------|-----------|
| Visual Inspection | 500 FH | 15 min | 1 tech |
| Functional Test | 2,500 FH | 1 hr | 1 tech |
| Bearing Inspection | 10,000 FH | 4 hr | 2 techs |
| Bearing Replacement | 30,000 FH | 8 hr | 2 techs |
| Overhaul | 60,000 FH | 40 hr | Shop |

---

## 5. Reliability Growth

### 5.1 Test Program

| Phase | Hours | Failures | MTBF |
|-------|-------|----------|------|
| Development | 5,000 | 12 | 417 |
| Qualification | 3,000 | 2 | 1,500 |
| Production (target) | 50,000 | 1 | 50,000 |

### 5.2 Reliability Improvement Actions

| Issue | Root Cause | Corrective Action | Status |
|-------|------------|-------------------|--------|
| Early bearing failures | Misalignment | Improved assembly tooling | Closed |
| Winding hotspots | Cooling blockage | Revised jacket design | Closed |
| Resolver drift | Thermal expansion | Material change | In work |

---

## 6. Safety Analysis Reference

| Document | Reference |
|----------|-----------|
| FHA | ATA61-FHA-001 |
| PSSA | ATA61-PSSA-001 |
| SSA | ATA61-SSA-001 (pending) |
| CCA | ATA61-CCA-001 (pending) |

---

## Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending engineering review
