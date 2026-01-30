# 57-00-02-50 — Zone Definitions

**ATA Chapter**: 57 — Wings  
**Folder**: 57-00-02_Safety / 57-00-02-50_ZSA  
**Status**: DRAFT  
**Owner**: Airframe & Structures Domain (ATA 57)

---

## 1. Purpose

This document defines the **wing zone structure** for Zonal Safety Analysis (ZSA) purposes.

---

## 2. Zone Definition Methodology

Wing zones are defined according to:

- Structural boundaries (spars, ribs, bulkheads)  
- Access panel locations  
- Environmental segregation needs  
- Functional groupings  
- ATA chapter responsibilities  

---

## 3. Zone Definitions

### 3.1 Z-57-100 — Wing Root

| Parameter | Value |
| :-- | :-- |
| Zone ID | Z-57-100 |
| Location | Wing-fuselage junction |
| Boundaries | Fuselage side to first inboard rib |
| Primary Function | Load transfer to fuselage |
| Access | Via fuselage and wing access panels |

**Equipment Installed:**
- Wing attachment fittings  
- Center wing box tie-in structure  
- Cross-feed fuel lines  
- Hydraulic connections  
- Electrical distribution  

**Environmental Factors:**
- Fuel vapor (adjacent to center tank)  
- High stress concentration area  
- Limited access  

---

### 3.2 Z-57-200 — Inner Wing Box

| Parameter | Value |
| :-- | :-- |
| Zone ID | Z-57-200 |
| Location | Inboard wing section |
| Boundaries | Wing root to mid-span structural break |
| Primary Function | Primary load-carrying, fuel storage |
| Access | Lower wing access panels |

**Equipment Installed:**
- Integral fuel tanks  
- Fuel quantity sensors  
- Structural health monitoring sensors  
- Pylon attachment provisions  

**Environmental Factors:**
- Fuel immersion  
- High bending loads  
- Temperature variation  

---

### 3.3 Z-57-300 — Mid Wing Box

| Parameter | Value |
| :-- | :-- |
| Zone ID | Z-57-300 |
| Location | Mid-span wing section |
| Boundaries | Mid-span to outer structural break |
| Primary Function | Primary load-carrying, fuel storage |
| Access | Lower wing access panels |

**Equipment Installed:**
- Integral fuel tanks  
- Fuel quantity sensors  
- SHM sensors  

**Environmental Factors:**
- Fuel immersion  
- Moderate bending loads  
- Temperature variation  

---

### 3.4 Z-57-400 — Outer Wing Box

| Parameter | Value |
| :-- | :-- |
| Zone ID | Z-57-400 |
| Location | Outboard wing section |
| Boundaries | Outer structural break to wing tip |
| Primary Function | Primary structure |
| Access | Lower wing access panels |

**Equipment Installed:**
- Navigation lights  
- Position lights  
- SHM sensors  

**Environmental Factors:**
- High deflection  
- Lightning strike exposure  

---

### 3.5 Z-57-500 — Leading Edge

| Parameter | Value |
| :-- | :-- |
| Zone ID | Z-57-500 |
| Location | Full span leading edge |
| Boundaries | Front spar to leading edge |
| Primary Function | Aerodynamics, slats, ice protection |
| Access | Leading edge access panels |

**Equipment Installed:**
- Slat tracks and mechanisms  
- Ice protection system (thermal or boots)  
- Slat position sensors  

**Environmental Factors:**
- Ice accretion  
- Bird strike exposure  
- Heat (ice protection)  
- Hydraulic fluid  

---

### 3.6 Z-57-600 — Trailing Edge

| Parameter | Value |
| :-- | :-- |
| Zone ID | Z-57-600 |
| Location | Full span trailing edge |
| Boundaries | Rear spar to trailing edge |
| Primary Function | Flaps, ailerons, spoilers |
| Access | Trailing edge access panels |

**Equipment Installed:**
- Flap tracks and mechanisms  
- Aileron actuation  
- Spoiler actuation  
- Position sensors  

**Environmental Factors:**
- Hydraulic fluid  
- Mechanical wear  
- Contamination  

---

### 3.7 Z-57-700 — Wing Tip

| Parameter | Value |
| :-- | :-- |
| Zone ID | Z-57-700 |
| Location | Wing extremity |
| Boundaries | Outer wing to tip |
| Primary Function | Aerodynamics, lighting |
| Access | Wing tip fairing |

**Equipment Installed:**
- Wing tip structure/winglet  
- Navigation lights  
- Strobe lights  

**Environmental Factors:**
- Lightning strike  
- Bird strike  
- High deflection  

---

## 4. Zone Mapping to ATA Chapters

| Zone | Primary ATA | Interface ATAs |
| :-- | :-- | :-- |
| Z-57-100 | 57 | 53 (Fuselage), 28 (Fuel) |
| Z-57-200 | 57 | 28 (Fuel), 71 (Powerplant) |
| Z-57-300 | 57 | 28 (Fuel) |
| Z-57-400 | 57 | 33 (Lights) |
| Z-57-500 | 57 | 27 (Controls), 30 (Ice Protection) |
| Z-57-600 | 57 | 27 (Controls) |
| Z-57-700 | 57 | 33 (Lights) |

---

## 5. References

- [57-00-02-50_ZSA_Overview.md](./57-00-02-50_ZSA_Overview.md)  
- [ZONE_ANALYSIS/57-00-02-50_ZSA_Results_Index.md](./ZONE_ANALYSIS/57-00-02-50_ZSA_Results_Index.md)  

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.  
- Status: **DRAFT** — Subject to human review and approval.  
- Human approver: _[to be completed]_.  
- Repository: `AMPEL360-BWB-H2-Hy-E`  
- Last AI update: 2025-11-29
