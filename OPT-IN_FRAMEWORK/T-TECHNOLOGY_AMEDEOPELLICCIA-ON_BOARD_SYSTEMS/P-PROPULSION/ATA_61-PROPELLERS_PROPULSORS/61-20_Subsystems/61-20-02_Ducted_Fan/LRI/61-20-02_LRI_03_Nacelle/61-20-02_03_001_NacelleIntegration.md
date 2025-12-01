# 61-20-02_03_001 — Nacelle Integration

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-02_03_001                        |
| **LRI ID**         | LRI-61-20-02-03                        |
| **Part Number**    | PN-DF-NAC-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Status**         | Active                                 |
| **Version**        | 1.0                                    |
| **Last Updated**   | 2025-12-01                             |
| **Owner**          | AMPEL360 Propulsion Team               |
| **Standard**       | OPT-IN Framework v1.2                  |

---

## 1. Overview

The **Nacelle Duct Assembly** is a Line Replaceable Item (LRI) within the Ducted Fan LRU. It comprises the internal annular duct that shapes inlet/outlet flow and houses the rotor/stator assemblies.

---

## 2. Design Parameters

### 2.1 Geometric Parameters

| Parameter                | Value       | Unit    | Notes                              |
|--------------------------|-------------|---------|-------------------------------------|
| **Outer Diameter (Max)** | 1,350       | mm      | Maximum cowl diameter              |
| **Inner Diameter (Min)** | 350         | mm      | Spinner fairing                    |
| **Axial Length (Total)** | 1,200       | mm      | Inlet to exhaust                   |
| **Inlet Length**         | 350         | mm      | Lip to fan face                    |
| **Fan Section Length**   | 250         | mm      | Rotor + stator                     |
| **Exhaust Length**       | 600         | mm      | Stator to nozzle exit              |
| **Contraction Ratio**    | 1.25        | —       | Inlet/fan face area ratio          |
| **Nozzle Area Ratio**    | 0.95        | —       | Exit/fan face area ratio           |

### 2.2 Aerodynamic Parameters

| Parameter                | Design Value | Off-Design Range | Unit    |
|--------------------------|--------------|------------------|---------|
| **Inlet Recovery**       | 0.995        | 0.990 – 0.998    | —       |
| **Duct Pressure Loss**   | 1.5          | 1.0 – 2.5        | %       |
| **Spillage Drag (Cruise)**| 0.8         | 0.5 – 1.5        | % thrust|
| **Nozzle Coefficient**   | 0.985        | 0.980 – 0.990    | —       |

---

## 3. Structural Design

### 3.1 Major Components

| Component              | Description                              |
|------------------------|------------------------------------------|
| **Inlet Cowl**         | Forward aerodynamic fairing              |
| **Fan Case**           | Containment structure around rotor       |
| **Intermediate Case**  | Structural ring between rotor and stator |
| **Exhaust Duct**       | Aft flow path and nozzle                 |
| **Acoustic Liner**     | Sound-absorbing panels                   |

### 3.2 Material Specification

| Component              | Material                  | Spec Reference      |
|------------------------|---------------------------|---------------------|
| **Inlet Cowl**         | CFRP (T800/3900)          | AMS 5774            |
| **Fan Case**           | CFRP + Kevlar hybrid      | Per programme spec  |
| **Intermediate Case**  | Ti-6Al-4V                 | AMS 4928            |
| **Exhaust Duct**       | CFRP (AS4/8552)           | AMS 5774            |
| **Acoustic Liner**     | Al honeycomb + perforate  | Per acoustic spec   |

### 3.3 Structural Loads

| Load Case              | Axial (kN) | Radial (kN) | Moment (kNm) |
|------------------------|------------|-------------|--------------|
| **Normal Operation**   | 45         | 5           | 15           |
| **Bird Strike**        | 120        | 85          | 55           |
| **Blade-Off**          | 180        | 220         | 120          |
| **Ground Handling**    | 25         | 35          | 40           |

---

## 4. Containment Design

### 4.1 Blade-Off Containment

| Parameter                | Design Value | Unit    |
|--------------------------|--------------|---------|
| **Fan Case Thickness**   | 12           | mm      |
| **Liner Thickness**      | 6            | mm      |
| **Energy Absorption**    | 850          | kJ      |
| **Fragment Velocity**    | 350          | m/s     |

### 4.2 Containment Verification

| Test                     | Standard             | Status              |
|--------------------------|----------------------|---------------------|
| **Blade Release**        | CS-E 810             | TBD                 |
| **Small Bird**           | CS-25.631            | TBD                 |
| **Large Bird**           | CS-25.631            | TBD                 |

---

## 5. Acoustic Treatment

### 5.1 Liner Configuration

| Zone                    | Type                  | Frequency Target (Hz) |
|-------------------------|-----------------------|-----------------------|
| **Inlet**               | SDOF honeycomb        | 2,000 – 4,000         |
| **Fan Case**            | DDOF honeycomb        | 1,000 – 3,000         |
| **Exhaust**             | SDOF honeycomb        | 1,500 – 3,500         |

### 5.2 Noise Attenuation

| Metric                  | Target                | Unit                  |
|-------------------------|-----------------------|-----------------------|
| **Inlet Attenuation**   | -8                    | dB (EPNL)             |
| **Exhaust Attenuation** | -6                    | dB (EPNL)             |
| **Overall Margin**      | -5                    | EPNdB (vs. Chapter 14)|

---

## 6. Interfaces

### 6.1 Internal Interfaces

| Interface ID    | Connected To                    | Type           | Description                          |
|-----------------|---------------------------------|----------------|--------------------------------------|
| IF-NAC-01       | LRI-61-20-02-01 (Rotor)         | Mechanical     | Fan case / rotor clearance           |
| IF-NAC-02       | LRI-61-20-02-02 (Stator)        | Mechanical     | Intermediate case / stator mount     |
| IF-NAC-03       | 61-20-01_Electric_Motor         | Mechanical     | Forward mount frame                  |

### 6.2 External Interfaces

| Interface ID    | Connected To                    | Type           | Description                          |
|-----------------|---------------------------------|----------------|--------------------------------------|
| IF-NAC-E01      | 61-50_Structures                | Structural     | Nacelle mount / pylon interface      |
| IF-NAC-E02      | ATA 57 – Wings                  | Structural     | Wing station attachment (if appl.)   |
| IF-NAC-E03      | ATA 21 – ECS                    | Thermal        | Bleed air / cooling (if applicable)  |

---

## 7. Manufacturing Requirements

### 7.1 Process Specification

| Process                | Specification              | Tolerance          |
|------------------------|----------------------------|--------------------|
| **CFRP Layup**         | Autoclave cure             | ±0.2 mm profile    |
| **Machining**          | 5-axis CNC                 | ±0.1 mm            |
| **Assembly**           | Precision jig assembly     | ±0.15 mm position  |
| **Bonding**            | FM-300 adhesive            | Per AMS 3686       |

---

## 8. References

- [CIR_LINKS.md](./CIR_LINKS.md) — Central Illustration Repository references
- [BOM_LMP.md](./BOM_LMP.md) — Bill of Materials and Lubrication/Maintenance Plan
- [../../LRU_61-20-02_DuctedFan.md](../../LRU_61-20-02_DuctedFan.md) — Parent LRU

---

## 9. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending human review
- **Last AI Update:** 2025-12-01
