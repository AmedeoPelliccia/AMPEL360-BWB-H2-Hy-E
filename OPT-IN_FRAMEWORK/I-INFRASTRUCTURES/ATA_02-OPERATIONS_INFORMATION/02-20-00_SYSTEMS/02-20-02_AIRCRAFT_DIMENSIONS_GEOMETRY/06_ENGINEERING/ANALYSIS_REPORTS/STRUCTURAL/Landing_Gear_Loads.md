# Landing Gear Loads Analysis

**Analysis ID:** 02-11-00-STR-004  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Structural - Landing Gear Loads  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Calculate landing gear reaction loads for all critical landing and ground handling conditions per CS-25.471 through CS-25.511:
- Level landing vertical loads
- Tail-down landing loads
- One-gear landing loads
- Side load conditions (drift landings)
- Taxi, turning, and braking loads

---

## 2. Landing Gear Configuration

### 2.1 Main Landing Gear
- **Type:** Twin-wheel bogies, 2 main gear legs
- **Track:** 12.5 m
- **Wheelbase (MLG to NLG):** 18.0 m
- **Static load (each MLG):** TBD kN
- **Tire pressure:** 1,450 kPa (210 psi)

### 2.2 Nose Landing Gear
- **Type:** Twin-wheel
- **Static load:** TBD kN
- **Steering angle:** ±70°

---

## 3. Load Cases

### 3.1 Landing Conditions (CS-25.473 to CS-25.485)

| Load Case | Description | Vertical Load Factor | Forward Load | Lateral Load |
|-----------|-------------|----------------------|--------------|--------------|
| LC-LDG-01 | Level landing, symmetric | 1.0 × MTOW × n | 0.25 × V | 0 |
| LC-LDG-02 | Tail-down landing | TBD | TBD | 0 |
| LC-LDG-03 | One-gear landing | 1.0 × MTOW × n × 1.0 | TBD | 0 |
| LC-LDG-04 | Side load (drift) | 1.0 × MTOW × n | TBD | 0.5 × V |
| LC-LDG-05 | Rebound | 1.0 × MTOW × n × 0.6 | 0 | 0 |

Where:
- MTOW = Maximum Take-Off Weight (TBD kg)
- n = limit load factor (per CS-25.473)
- V = vertical reaction load

### 3.2 Ground Handling (CS-25.491 to CS-25.511)

| Load Case | Description | Applied Load |
|-----------|-------------|--------------|
| LC-GRD-01 | Taxi bump | TBD |
| LC-GRD-02 | Max braking | TBD |
| LC-GRD-03 | Turning (max steering) | TBD |
| LC-GRD-04 | Towing loads | TBD |

---

## 4. Analysis Results

### 4.1 Critical Landing Loads

**Level Landing (CS-25.479):**
- Vertical load factor: n = 3.0 (limit)
- Vertical reaction per MLG: TBD kN
- Forward reaction per MLG: TBD kN

**One-Gear Landing (CS-25.483):**
- Single MLG vertical load: TBD kN
- Lateral load on gear attachment: TBD kN

### 4.2 Gear Attachment Loads
- **Wing attachment shear:** TBD kN
- **Wing attachment moment:** TBD kN·m
- **Margin of safety:** TBD

---

## 5. Energy Absorption

### 5.1 Landing Impact Energy
E = 0.5 × m × V²

Where:
- m = landing mass (TBD kg)
- V = vertical descent velocity (CS-25.473: 10 ft/s = 3.05 m/s)

Energy per gear: TBD kJ

### 5.2 Shock Absorber Stroke
Required stroke to absorb energy: TBD mm

---

## 6. References

- `04_DESIGN/STRUCTURAL_DESIGN/Landing_Gear_Design.md`
- `CALCULATIONS/STRUCTURAL/Gear_Loads_Spreadsheet.csv`
- CS-25.471 through CS-25.511
- `TRADE_STUDIES/Gear_Height_Trade_Study.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
