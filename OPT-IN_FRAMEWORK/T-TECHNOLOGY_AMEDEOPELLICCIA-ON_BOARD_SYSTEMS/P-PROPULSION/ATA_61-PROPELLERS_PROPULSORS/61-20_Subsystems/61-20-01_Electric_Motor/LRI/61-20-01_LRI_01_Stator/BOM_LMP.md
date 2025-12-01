# BOM + LMP — Stator Assembly (LRI-61-20-01-01)

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-01_01_BOM_LMP                    |
| **LRI ID**         | LRI-61-20-01-01                        |
| **Part Number**    | PN-EM-STA-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Last Updated**   | 2025-12-01                             |

---

## 1. Bill of Materials (BOM)

### 1.1 Major Components

| Item | Part Number     | Description                  | Material              | Qty | Unit Mass (kg) | Illustrated |
|------|-----------------|------------------------------|-----------------------|-----|----------------|-------------|
| 1    | PN-EM-STA-001   | Stator Assembly (Complete)   | —                     | 1   | 175.0          | Y           |
| 1.1  | PN-EM-COR-001   | Stator Core Stack            | M19 Silicon Steel     | 1   | 145.0          | Y           |
| 1.2  | PN-EM-WDG-001   | Phase Winding Set (3-phase)  | Cu Litz / Class H     | 1   | 22.0           | Y           |
| 1.3  | PN-EM-SLT-001   | Slot Liner Set               | Nomex 410             | 72  | 0.015          | N           |
| 1.4  | PN-EM-WDG-002   | Slot Wedge Set               | G10 Fiberglass        | 72  | 0.008          | N           |
| 1.5  | PN-EM-END-001   | End Winding Support Bracket  | Al-6061-T6            | 2   | 0.85           | Y           |
| 1.6  | PN-EM-RTD-001   | RTD Temperature Sensor       | PT100 Class A         | 6   | 0.02           | Y           |

### 1.2 Electrical Terminations

| Item | Part Number     | Description                  | Specification         | Qty | Illustrated |
|------|-----------------|------------------------------|-----------------------|-----|-------------|
| 2.1  | PN-EM-TRM-001   | Phase Terminal Lug           | 500 A, M12            | 6   | Y           |
| 2.2  | PN-EM-BUS-001   | Neutral Bus Bar              | Cu, Sn-plated         | 1   | Y           |
| 2.3  | PN-EM-CON-001   | RTD Connector (6-pin)        | MIL-DTL-38999         | 2   | Y           |

### 1.3 Consumables and Insulation

| Item | Part Number     | Description                  | Specification         | Qty      | Maintenance Marking |
|------|-----------------|------------------------------|-----------------------|----------|---------------------|
| 3.1  | PN-EM-VPI-001   | VPI Resin (Class H)          | MIL-I-24092           | 15 L     | N                   |
| 3.2  | PN-EM-LAC-001   | Lacing Cord                  | MIL-T-713             | 50 m     | N                   |
| 3.3  | PN-EM-TAP-001   | Insulation Tape (Mica)       | NEMA Class H          | 5 rolls  | N                   |
| 3.4  | PN-EM-SLV-001   | Insulating Sleeve            | Silicone rubber       | 20 pcs   | N                   |

---

## 2. Lubrication and Maintenance Plan (LMP)

### 2.1 Maintenance Schedule (Stator-Specific)

| Task ID       | Description                          | Method                    | Interval    | Marking Required |
|---------------|--------------------------------------|---------------------------|-------------|------------------|
| LMP-STA-001   | Insulation Resistance Check          | Megger (500 VDC)          | 1,000 FH    | Y                |
| LMP-STA-002   | Winding Resistance Measurement       | 4-wire Kelvin bridge      | 2,500 FH    | Y                |
| LMP-STA-003   | Partial Discharge Test               | PD detector               | 5,000 FH    | Y                |
| LMP-STA-004   | Thermal Sensor Calibration Check     | Reference RTD comparison  | 5,000 FH    | Y                |
| LMP-STA-005   | End Winding Visual Inspection        | Borescope                 | 2,500 FH    | N                |

### 2.2 Condition Monitoring Parameters

| Parameter                  | Normal Range      | Warning Threshold | Critical Threshold |
|----------------------------|-------------------|-------------------|---------------------|
| **Winding Temperature**    | < 140°C           | > 150°C           | > 160°C             |
| **Insulation Resistance**  | > 100 MΩ          | < 50 MΩ           | < 10 MΩ             |
| **Phase Imbalance**        | < 2%              | > 5%              | > 10%               |
| **PD Level**               | < 200 pC          | > 500 pC          | > 1000 pC           |

### 2.3 Replacement Criteria

| Component            | Life Limit (FH) | Life Limit (Cycles) | Condition-Based Trigger           |
|----------------------|-----------------|---------------------|-----------------------------------|
| Stator Assembly      | 50,000          | 60,000              | Insulation failure, PD > 1000 pC  |
| RTD Sensors          | 25,000          | —                   | Drift > 5°C                       |
| Slot Wedges          | On-condition    | —                   | Looseness, cracking               |
| End Winding Supports | 50,000          | —                   | Cracking, deformation             |

---

## 3. Maintenance Procedures Reference

| Procedure ID   | Description                          | AMM Reference         |
|----------------|--------------------------------------|-----------------------|
| MP-61-20-01-01 | Stator Insulation Test               | AMM 61-20-01-01       |
| MP-61-20-01-02 | RTD Sensor Replacement               | AMM 61-20-01-02       |
| MP-61-20-01-03 | End Winding Inspection               | AMM 61-20-01-03       |
| MP-61-20-01-04 | Winding Repair (Minor)               | AMM 61-20-01-04       |
| MP-61-20-01-05 | Complete Stator Rewinding            | AMM 61-20-01-05       |

---

## 4. Illustrated Parts Breakdown

See Central Illustration Repository:
- `61-90-20_01-01-FIG_001` — Stator Assembly Exploded View
- `61-90-20_01-01-FIG_002` — Stator Core Detail
- `61-90-20_01-01-FIG_003` — Winding Configuration
- `61-90-20_01-01-FIG_004` — End Winding Support Detail

---

## 5. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending human review
- **Last AI Update:** 2025-12-01
