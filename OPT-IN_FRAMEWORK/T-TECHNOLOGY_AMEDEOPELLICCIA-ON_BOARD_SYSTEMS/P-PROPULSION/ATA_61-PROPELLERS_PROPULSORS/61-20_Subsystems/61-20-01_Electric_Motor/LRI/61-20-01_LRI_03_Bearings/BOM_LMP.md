# BOM + LMP — Bearing System (LRI-61-20-01-03)

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-01_03_BOM_LMP                    |
| **LRI ID**         | LRI-61-20-01-03                        |
| **Part Number**    | PN-EM-BRG-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Last Updated**   | 2025-12-01                             |

---

## 1. Bill of Materials (BOM)

### 1.1 Major Components

| Item | Part Number     | Description                  | Specification         | Qty | Unit Mass (kg) | Illustrated |
|------|-----------------|------------------------------|-----------------------|-----|----------------|-------------|
| 1    | PN-EM-BRG-001   | Bearing System (Complete)    | —                     | 1   | 18.5           | Y           |
| 1.1  | PN-EM-BDE-001   | DE Angular Contact Bearing   | 7220-BECBP            | 1   | 4.8            | Y           |
| 1.2  | PN-EM-BND-001   | NDE Cylindrical Roller Bearing| NU 220 ECM           | 1   | 4.2            | Y           |
| 1.3  | PN-EM-BHS-001   | Bearing Housing (DE)         | Al-7075-T6            | 1   | 3.5            | Y           |
| 1.4  | PN-EM-BHS-002   | Bearing Housing (NDE)        | Al-7075-T6            | 1   | 3.2            | Y           |
| 1.5  | PN-EM-SEL-001   | Labyrinth Seal Set           | Stainless Steel       | 4   | 0.18           | Y           |
| 1.6  | PN-EM-SEL-002   | Lip Seal Set                 | Viton                 | 4   | 0.08           | Y           |

### 1.2 Lubrication Components

| Item | Part Number     | Description                  | Specification         | Qty | Illustrated |
|------|-----------------|------------------------------|-----------------------|-----|-------------|
| 2.1  | PN-EM-OIL-001   | Turbine Oil                  | MIL-PRF-23699         | 2 L | N           |
| 2.2  | PN-EM-FLT-001   | Oil Filter Element           | 10 μm, Beta 1000      | 2   | Y           |
| 2.3  | PN-EM-ORF-001   | Oil Orifice (flow control)   | 0.8 mm                | 2   | N           |
| 2.4  | PN-EM-TTG-001   | Oil Supply Tubing            | SS 316, 6 mm OD       | 2 m | N           |

### 1.3 Sensors

| Item | Part Number     | Description                  | Specification         | Qty | Illustrated |
|------|-----------------|------------------------------|-----------------------|-----|-------------|
| 3.1  | PN-EM-VIB-001   | Vibration Accelerometer      | 100 mV/g, IEPE        | 3   | Y           |
| 3.2  | PN-EM-TMP-001   | RTD Temperature Sensor       | PT100 Class A         | 2   | Y           |
| 3.3  | PN-EM-FLW-001   | Oil Flow Sensor              | 0.1-1.0 L/min         | 2   | Y           |

### 1.4 Hardware

| Item | Part Number     | Description                  | Specification         | Qty | Illustrated |
|------|-----------------|------------------------------|-----------------------|-----|-------------|
| 4.1  | PN-EM-BLK-001   | Bearing Lock Nut             | KMT 20                | 2   | Y           |
| 4.2  | PN-EM-WSH-003   | Lock Washer                  | MB 20                 | 2   | N           |
| 4.3  | PN-EM-SPC-001   | Bearing Spacer Ring          | Al-6061-T6            | 2   | Y           |

---

## 2. Lubrication and Maintenance Plan (LMP)

### 2.1 Lubrication Schedule

| Task ID       | Description                          | Lubricant           | Interval    | Marking Required |
|---------------|--------------------------------------|---------------------|-------------|------------------|
| LMP-BRG-001   | Oil Level Check                      | MIL-PRF-23699       | 100 FH      | N                |
| LMP-BRG-002   | Oil Sample Analysis                  | MIL-PRF-23699       | 500 FH      | Y                |
| LMP-BRG-003   | Oil Change                           | MIL-PRF-23699       | 2,500 FH    | Y                |
| LMP-BRG-004   | Oil Filter Replacement               | —                   | 2,500 FH    | Y                |

### 2.2 Inspection Schedule

| Task ID       | Description                          | Method              | Interval    | Acceptance Criteria           |
|---------------|--------------------------------------|---------------------|-------------|-------------------------------|
| INS-BRG-001   | Vibration Trend Analysis             | Accelerometer       | 100 FH      | < 4.0 mm/s RMS                |
| INS-BRG-002   | Temperature Trend Analysis           | RTD                 | Continuous  | < 95°C                        |
| INS-BRG-003   | Oil Spectrometry (Wear Metals)       | Lab analysis        | 500 FH      | Fe < 20 ppm, Cu < 10 ppm      |
| INS-BRG-004   | Visual Inspection (External)         | Visual              | 500 FH      | No leaks, damage              |
| INS-BRG-005   | Bearing Clearance Check              | Feeler gauge        | 5,000 FH    | Per manufacturer spec         |

### 2.3 Replacement Criteria

| Component            | Life Limit (FH) | Life Limit (Cycles) | Condition-Based Trigger            |
|----------------------|-----------------|---------------------|------------------------------------|
| DE Bearing           | 30,000          | 36,000              | Vibration > 7 mm/s, temp > 110°C   |
| NDE Bearing          | 30,000          | 36,000              | Vibration > 7 mm/s, temp > 105°C   |
| Labyrinth Seals      | 15,000          | —                   | Oil leakage detected               |
| Lip Seals            | 10,000          | —                   | Oil leakage detected               |
| Oil Filter           | 2,500           | —                   | Differential pressure > 1.5 bar    |

---

## 3. Maintenance Procedures Reference

| Procedure ID   | Description                          | AMM Reference         |
|----------------|--------------------------------------|-----------------------|
| MP-61-20-01-20 | Bearing Inspection (In-Situ)         | AMM 61-20-01-20       |
| MP-61-20-01-21 | DE Bearing Replacement               | AMM 61-20-01-21       |
| MP-61-20-01-22 | NDE Bearing Replacement              | AMM 61-20-01-22       |
| MP-61-20-01-23 | Seal Replacement                     | AMM 61-20-01-23       |
| MP-61-20-01-24 | Oil System Service                   | AMM 61-20-01-24       |
| MP-61-20-01-25 | Vibration Sensor Calibration         | AMM 61-20-01-25       |

---

## 4. Illustrated Parts Breakdown

See Central Illustration Repository:
- `61-90-20_01-03-FIG_001` — Bearing System Exploded View
- `61-90-20_01-03-FIG_002` — DE Bearing Assembly
- `61-90-20_01-03-FIG_003` — NDE Bearing Assembly
- `61-90-20_01-03-FIG_004` — Oil System Schematic

---

## 5. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending human review
- **Last AI Update:** 2025-12-01
