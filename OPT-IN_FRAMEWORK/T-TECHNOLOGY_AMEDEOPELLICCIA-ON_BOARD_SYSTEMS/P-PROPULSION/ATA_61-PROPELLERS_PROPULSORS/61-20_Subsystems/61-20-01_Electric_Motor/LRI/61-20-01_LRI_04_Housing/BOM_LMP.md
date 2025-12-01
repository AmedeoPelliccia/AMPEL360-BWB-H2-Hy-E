# BOM + LMP — Housing/Frame Assembly (LRI-61-20-01-04)

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-01_04_BOM_LMP                    |
| **LRI ID**         | LRI-61-20-01-04                        |
| **Part Number**    | PN-EM-HSG-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Last Updated**   | 2025-12-01                             |

---

## 1. Bill of Materials (BOM)

### 1.1 Major Components

| Item | Part Number     | Description                  | Material              | Qty | Unit Mass (kg) | Illustrated |
|------|-----------------|------------------------------|-----------------------|-----|----------------|-------------|
| 1    | PN-EM-HSG-001   | Housing Assembly (Complete)  | —                     | 1   | 62.0           | Y           |
| 1.1  | PN-EM-HBY-001   | Housing Body (Main Barrel)   | Al-7075-T6            | 1   | 48.0           | Y           |
| 1.2  | PN-EM-ECP-001   | End Cap (Drive End)          | Al-7075-T6            | 1   | 5.5            | Y           |
| 1.3  | PN-EM-ECP-002   | End Cap (Non-Drive End)      | Al-7075-T6            | 1   | 4.8            | Y           |
| 1.4  | PN-EM-FLG-001   | Mounting Flange              | 4340 Steel            | 1   | 3.2            | Y           |
| 1.5  | PN-EM-LFT-001   | Lifting Lug Set              | 4340 Steel            | 2   | 0.25           | Y           |

### 1.2 Cooling System Components

| Item | Part Number     | Description                  | Specification         | Qty | Illustrated |
|------|-----------------|------------------------------|-----------------------|-----|-------------|
| 2.1  | PN-EM-PRT-001   | Coolant Inlet Port           | G 3/4" BSP, SS 316    | 1   | Y           |
| 2.2  | PN-EM-PRT-002   | Coolant Outlet Port          | G 3/4" BSP, SS 316    | 1   | Y           |
| 2.3  | PN-EM-ORN-001   | O-Ring (End Cap DE)          | Viton, AS 568-265     | 1   | N           |
| 2.4  | PN-EM-ORN-002   | O-Ring (End Cap NDE)         | Viton, AS 568-258     | 1   | N           |
| 2.5  | PN-EM-PLG-001   | Drain Plug                   | G 1/4" BSP, magnetic  | 1   | N           |

### 1.3 Hardware

| Item | Part Number     | Description                  | Specification         | Qty | Illustrated |
|------|-----------------|------------------------------|-----------------------|-----|-------------|
| 3.1  | PN-EM-MBT-001   | Mounting Bolt                | NAS 6612-16           | 12  | Y           |
| 3.2  | PN-EM-ECB-001   | End Cap Bolt (DE)            | NAS 6604-12           | 16  | N           |
| 3.3  | PN-EM-ECB-002   | End Cap Bolt (NDE)           | NAS 6604-10           | 12  | N           |
| 3.4  | PN-EM-WSH-004   | Flat Washer Set              | AN 960                | 40  | N           |
| 3.5  | PN-EM-GRD-001   | Grounding Stud               | Cu, M8                | 2   | Y           |

### 1.4 Consumables

| Item | Part Number     | Description                  | Specification         | Qty      | Maintenance Marking |
|------|-----------------|------------------------------|-----------------------|----------|---------------------|
| 4.1  | PN-EM-SEA-002   | Thread Sealant (Coolant)     | Loctite 565           | 0.05 L   | N                   |
| 4.2  | PN-EM-GRS-001   | Anti-Seize Compound          | MIL-PRF-907           | 0.1 kg   | N                   |
| 4.3  | PN-EM-COR-002   | Corrosion Preventive         | MIL-PRF-16173         | 0.25 L   | N                   |

---

## 2. Lubrication and Maintenance Plan (LMP)

### 2.1 Maintenance Schedule

| Task ID       | Description                          | Method                    | Interval    | Marking Required |
|---------------|--------------------------------------|---------------------------|-------------|------------------|
| LMP-HSG-001   | Visual Inspection (External)         | Visual                    | 500 FH      | N                |
| LMP-HSG-002   | Mounting Bolt Torque Check           | Torque wrench             | 2,500 FH    | Y                |
| LMP-HSG-003   | Cooling System Pressure Test         | Hydrostatic               | 5,000 FH    | Y                |
| LMP-HSG-004   | Grounding Continuity Check           | Multimeter                | 1,000 FH    | Y                |
| LMP-HSG-005   | Corrosion Inspection                 | Visual + dye penetrant    | 5,000 FH    | Y                |

### 2.2 Inspection Criteria

| Feature                    | Normal Condition        | Warning                   | Critical            |
|----------------------------|-------------------------|---------------------------|---------------------|
| **Mounting Bolts**         | Torque 85 ±5 Nm         | < 75 Nm                   | < 65 Nm             |
| **Cooling Jacket**         | No leakage              | Weeping                   | Active leak         |
| **End Cap O-Rings**        | No deformation          | Visible wear              | Breach / extrusion  |
| **Surface Corrosion**      | None visible            | Light surface             | Pitting > 0.5 mm    |
| **Grounding**              | < 10 mΩ                 | > 50 mΩ                   | > 100 mΩ            |

### 2.3 Replacement Criteria

| Component            | Life Limit (FH) | Life Limit (Cycles) | Condition-Based Trigger            |
|----------------------|-----------------|---------------------|------------------------------------|
| Housing Body         | 75,000          | 90,000              | Fatigue crack indication           |
| End Cap O-Rings      | 10,000          | —                   | Leak detected, visible damage      |
| Mounting Bolts       | 25,000          | 30,000              | Elongation, thread damage          |
| Coolant Ports        | 50,000          | —                   | Thread damage, corrosion           |
| Lifting Lugs         | On-condition    | —                   | Crack indication, deformation      |

---

## 3. Maintenance Procedures Reference

| Procedure ID   | Description                          | AMM Reference         |
|----------------|--------------------------------------|-----------------------|
| MP-61-20-01-30 | Housing External Inspection          | AMM 61-20-01-30       |
| MP-61-20-01-31 | End Cap Removal / Installation       | AMM 61-20-01-31       |
| MP-61-20-01-32 | Cooling System Leak Test             | AMM 61-20-01-32       |
| MP-61-20-01-33 | Mounting Bolt Replacement            | AMM 61-20-01-33       |
| MP-61-20-01-34 | NDT Inspection (Dye Penetrant)       | AMM 61-20-01-34       |
| MP-61-20-01-35 | Grounding Continuity Test            | AMM 61-20-01-35       |

---

## 4. Illustrated Parts Breakdown

See Central Illustration Repository:
- `61-90-20_01-04-FIG_001` — Housing Assembly Exploded View
- `61-90-20_01-04-FIG_002` — Cooling Channel Layout
- `61-90-20_01-04-FIG_003` — Mounting Flange Detail
- `61-90-20_01-04-FIG_004` — End Cap Assembly

---

## 5. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending human review
- **Last AI Update:** 2025-12-01
