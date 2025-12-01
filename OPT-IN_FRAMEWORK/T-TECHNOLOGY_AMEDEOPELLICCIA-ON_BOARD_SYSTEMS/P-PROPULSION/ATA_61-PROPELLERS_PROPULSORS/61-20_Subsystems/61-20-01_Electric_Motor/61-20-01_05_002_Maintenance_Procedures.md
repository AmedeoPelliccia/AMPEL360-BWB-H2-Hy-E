# 61-20-01_05_002 — Maintenance Procedures

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-01_05_002_Maintenance_Procedures |
| **Subsystem**      | 61-20-01_Electric_Motor                |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Version**        | 1.0                                    |
| **Last Updated**   | 2025-12-01                             |
| **Owner**          | AMPEL360 Propulsion Team               |
| **Standard**       | OPT-IN Framework v1.2                  |

---

## 1. General

### 1.1 Purpose

This document provides maintenance procedures for the Electric Motor (61-20-01) subsystem of the AMPEL360 Q100 EDF propulsion system.

### 1.2 Safety Warnings

⚠️ **HIGH VOLTAGE** — DC link voltage up to 900 V. Follow lockout/tagout procedures.

⚠️ **ROTATING MACHINERY** — Ensure motor is at standstill before maintenance.

⚠️ **HOT SURFACES** — Motor surfaces may exceed 80°C. Allow cooling before work.

⚠️ **STRONG MAGNETS** — Rotor contains permanent magnets. Keep magnetic-sensitive items away.

### 1.3 Required Tools

| Tool | Part Number | Purpose |
|------|-------------|---------|
| Torque wrench (10-50 Nm) | GEN-TW-001 | Connector tightening |
| Megohmmeter (1000V) | GEN-MEG-001 | Insulation testing |
| Vibration analyzer | 61-VIB-001 | Bearing inspection |
| Resolver test set | 61-RES-001 | Position feedback test |
| Coolant pressure tester | 61-CPT-001 | Leak testing |

---

## 2. Line Maintenance Tasks

### 2.1 Task 61-20-01-200 — Pre-Flight Inspection

**Interval:** Before each flight

**Time:** 5 minutes

**Procedure:**

1. Visually inspect motor housing for damage, fluid leaks, or foreign objects
2. Check coolant hose connections for security and leaks
3. Verify electrical connector locking mechanisms engaged
4. Check for unusual odors (burnt insulation)
5. Review BITE status for motor health warnings

**Pass Criteria:**
- No visible damage or leaks
- All connectors secure
- No BITE warnings

---

### 2.2 Task 61-20-01-210 — Post-Flight Inspection

**Interval:** After each flight

**Time:** 5 minutes

**Procedure:**

1. Allow motor to cool (surface temp < 50°C)
2. Visually inspect for new damage or leaks
3. Check coolant level in reservoir (via sight glass)
4. Record any abnormal flight notes from crew

---

### 2.3 Task 61-20-01-300 — 500 FH Inspection

**Interval:** 500 FH ± 50 FH

**Time:** 30 minutes

**Procedure:**

1. Perform pre-flight inspection (Task 61-20-01-200)
2. Download and review motor health data:
   - Temperature trends
   - Vibration trends
   - Power/efficiency trends
3. Inspect coolant condition (color, clarity)
4. Check resolver cable for chafing
5. Measure insulation resistance (> 500 MΩ at 500V DC)
6. Document findings

**Pass Criteria:**
- Insulation resistance > 500 MΩ
- No adverse trends in health data
- Coolant clear, correct color

---

## 3. Base Maintenance Tasks

### 3.1 Task 61-20-01-400 — 2,500 FH Inspection

**Interval:** 2,500 FH ± 100 FH

**Time:** 2 hours

**Procedure:**

1. Perform 500 FH inspection tasks
2. Perform functional test:
   - Ground power applied
   - PCU self-test
   - Motor rotation test (idle speed)
   - Resolver accuracy check
3. Vibration signature analysis:
   - Baseline comparison
   - Bearing frequency analysis
4. Thermal imaging of motor housing
5. Coolant pressure test (5 bar, 10 min hold)
6. Torque check on all accessible fasteners

---

### 3.2 Task 61-20-01-500 — 10,000 FH Inspection

**Interval:** 10,000 FH ± 200 FH

**Time:** 8 hours

**Procedure:**

1. Perform 2,500 FH inspection tasks
2. Detailed bearing inspection:
   - High-frequency vibration analysis
   - Oil analysis (if oil-lubricated)
3. Stator winding tests:
   - Surge test
   - Hi-pot test (2× rated + 1000V)
   - DC resistance (phase balance)
4. Resolver calibration verification
5. Coolant flush and refill
6. Internal borescope inspection (if access ports available)

---

### 3.3 Task 61-20-01-600 — Bearing Replacement

**Interval:** 30,000 FH (hard limit)

**Time:** 16 hours

**Location:** Base maintenance (hangar)

**Procedure:**

1. Remove motor from nacelle (see AMM 61-20-01)
2. Transfer to bench
3. Disassemble drive end:
   - Remove coupling
   - Remove end bell
   - Extract bearing
4. Inspect bearing seat for wear
5. Install new bearing (61-20-01-100)
6. Reassemble with new seals
7. Repeat for non-drive end
8. Run-in test on bench
9. Reinstall motor

---

## 4. Troubleshooting Guide

### 4.1 Motor Will Not Start

| Symptom | Possible Cause | Action |
|---------|---------------|--------|
| No rotation, no fault | Power supply issue | Check DC link voltage |
| Fault code P-001 | Resolver fault | Check resolver cable |
| Fault code T-001 | Over-temperature | Allow cooling, check coolant |
| Fault code I-001 | Overcurrent | Check for mechanical binding |

### 4.2 Abnormal Vibration

| Frequency | Possible Cause | Action |
|-----------|---------------|--------|
| 1× RPM | Rotor imbalance | Bearing inspection |
| 2× RPM | Misalignment | Coupling alignment check |
| High frequency | Bearing defect | Replace bearing |
| Random | Loose component | Fastener inspection |

### 4.3 Over-Temperature

| Condition | Possible Cause | Action |
|-----------|---------------|--------|
| All phases high | Coolant issue | Check flow, coolant level |
| Single phase high | Winding damage | Winding test, borescope |
| Bearing high | Lubrication issue | Bearing inspection |

---

## 5. Component Replacement

### 5.1 Replaceable Items

| Item | Part Number | Replacement Task |
|------|-------------|------------------|
| Temperature Sensor | 61-20-01-200 | Task 61-20-01-R01 |
| Resolver | 61-20-01-201 | Task 61-20-01-R02 |
| DE Bearing | 61-20-01-100 | Task 61-20-01-600 |
| NDE Bearing | 61-20-01-101 | Task 61-20-01-600 |
| Coolant Seal Kit | 61-20-01-300 | Task 61-20-01-R03 |

---

## 6. Records

All maintenance actions shall be recorded in:
- Aircraft Technical Log
- Component History Record
- Digital Product Passport (ATA 95)

---

## Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending engineering review
