# 61-20-01_01_001 — Stator Electromagnetic Design

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-01_01_001                        |
| **LRI ID**         | LRI-61-20-01-01                        |
| **Part Number**    | PN-EM-STA-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Version**        | 1.0                                    |
| **Last Updated**   | 2025-12-01                             |

---

## 1. Purpose

This document defines the electromagnetic and mechanical design of the **Stator Assembly** for the 4 MW PMSM Electric Motor used in the AMPEL360 Q100 EDF propulsors.

---

## 2. Stator Configuration

### 2.1 Core Design

| Parameter                  | Value                     | Unit    |
|----------------------------|---------------------------|---------|
| **Outer Diameter**         | 640                       | mm      |
| **Inner Diameter (Bore)**  | 420                       | mm      |
| **Stack Length**           | 380                       | mm      |
| **Number of Slots**        | 72                        | —       |
| **Slot Type**              | Semi-closed               | —       |
| **Lamination Material**    | M19 Silicon Steel (0.35mm)| —       |
| **Stacking Factor**        | 0.97                      | —       |
| **Core Mass**              | 145                       | kg      |

### 2.2 Winding Design

| Parameter                  | Value                     | Unit    |
|----------------------------|---------------------------|---------|
| **Winding Type**           | Distributed, double-layer | —       |
| **Coil Span**              | 6 slots                   | —       |
| **Turns per Coil**         | 4                         | —       |
| **Parallel Paths**         | 2                         | —       |
| **Conductor Type**         | Litz wire (rectangular)   | —       |
| **Conductor Material**     | Copper (Class H insulation)| —      |
| **Fill Factor**            | 0.65                      | —       |
| **Phase Resistance (25°C)**| 2.8                       | mΩ      |
| **Phase Inductance (Ld)**  | 0.42                      | mH      |
| **Phase Inductance (Lq)**  | 0.85                      | mH      |

### 2.3 Electrical Ratings

| Parameter                  | Continuous    | Peak (30s)  | Unit    |
|----------------------------|---------------|-------------|---------|
| **Phase Current (RMS)**    | 1,800         | 2,200       | A       |
| **Current Density**        | 8.5           | 10.5        | A/mm²   |
| **Back-EMF Constant**      | 1.45          | —           | V/(rad/s)|
| **Power Factor**           | 0.92          | 0.88        | —       |

---

## 3. Thermal Design

### 3.1 Cooling Architecture

| Feature                    | Description                                          |
|----------------------------|------------------------------------------------------|
| **Cooling Method**         | Direct stator jacket (liquid cooled)                 |
| **Coolant**                | 50/50 Glycol-Water mixture                           |
| **Jacket Configuration**   | Spiral channel machined into housing                 |
| **Flow Rate (nominal)**    | 25 L/min                                             |
| **Inlet Temperature**      | 40°C (max)                                           |
| **Outlet Temperature**     | 65°C (max)                                           |

### 3.2 Temperature Limits

| Component                  | Max Operating | Max Transient | Class   |
|----------------------------|---------------|---------------|---------|
| **Winding Hotspot**        | 155           | 180           | °C (H)  |
| **Slot Liner**             | 180           | 200           | °C      |
| **Core (Laminations)**     | 120           | 140           | °C      |
| **End Windings**           | 150           | 175           | °C      |

### 3.3 Thermal Sensors

| Sensor ID      | Location                  | Type    | Range           |
|----------------|---------------------------|---------|-----------------|
| RTD-STA-01     | Slot 6 (Phase A)          | PT100   | -40 to +200°C   |
| RTD-STA-02     | Slot 30 (Phase B)         | PT100   | -40 to +200°C   |
| RTD-STA-03     | Slot 54 (Phase C)         | PT100   | -40 to +200°C   |
| RTD-STA-04     | End Winding (DE)          | PT100   | -40 to +200°C   |
| RTD-STA-05     | End Winding (NDE)         | PT100   | -40 to +200°C   |
| RTD-STA-06     | Stator Core (yoke)        | PT100   | -40 to +200°C   |

---

## 4. Materials and Processes

### 4.1 Core Manufacturing

| Process Step               | Method                                | Specification   |
|----------------------------|---------------------------------------|-----------------|
| **Lamination Stamping**    | Progressive die stamping              | ±0.05 mm        |
| **Lamination Coating**     | C5 organic coating                    | 5 μm thickness  |
| **Core Stacking**          | Interlock / bonded stack              | 0.97 factor     |
| **Core Annealing**         | Stress relief (750°C, 2h, N₂)         | Post-stack      |

### 4.2 Winding Manufacturing

| Process Step               | Method                                | Specification   |
|----------------------------|---------------------------------------|-----------------|
| **Coil Winding**           | Automated precision winding           | ±0.5 turn       |
| **Slot Insertion**         | Manual insertion with tooling         | —               |
| **Lacing**                 | Polyester cord lacing                 | Every 25 mm     |
| **VPI Impregnation**       | Vacuum Pressure Impregnation          | Class H resin   |
| **Curing**                 | Oven cure (165°C, 6h)                 | —               |

---

## 5. Quality and Testing

### 5.1 In-Process Tests

| Test                       | Method                                | Acceptance      |
|----------------------------|---------------------------------------|-----------------|
| **Winding Resistance**     | 4-wire measurement                    | ±2% of nominal  |
| **Insulation Resistance**  | Megger (500 VDC)                      | > 100 MΩ        |
| **HiPot (Ground)**         | 2 × Vrated + 1000 V, 1 min            | No breakdown    |
| **Surge Test**             | Surge comparison                      | < 5% deviation  |

### 5.2 Acceptance Tests

| Test                       | Method                                | Acceptance      |
|----------------------------|---------------------------------------|-----------------|
| **Partial Discharge**      | Per IEC 60034-27                      | < 200 pC        |
| **Inductance**             | LCR meter (1 kHz)                     | ±5% of nominal  |
| **Back-EMF Waveform**      | Spin test (motor mode)                | THD < 3%        |

---

## 6. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending human review
- **Last AI Update:** 2025-12-01
