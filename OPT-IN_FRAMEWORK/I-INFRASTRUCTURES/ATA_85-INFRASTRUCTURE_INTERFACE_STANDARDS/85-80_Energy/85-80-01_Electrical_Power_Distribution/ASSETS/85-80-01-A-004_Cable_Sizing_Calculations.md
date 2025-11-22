# 85-80-01-A-004 Cable Sizing Calculations

## Document Information

- **Asset ID**: 85-80-01-A-004
- **Title**: Cable Sizing Methodology and Calculations
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

## Purpose

This document provides the methodology and example calculations for sizing power cables in airport electrical infrastructure for AMPEL360 aircraft operations.

## Applicable Standards

- [IEC 60364-5-52](https://www.iec.ch/) - Selection and erection of electrical equipment - Wiring systems
- [IEC 60502](https://www.iec.ch/) - Power cables with extruded insulation
- [BS 7671](https://electrical.theiet.org/) - UK Wiring Regulations
- [IEEE 835](https://standards.ieee.org/) - IEEE Standard Power Cable Ampacity Tables

## Cable Sizing Methodology

Cable sizing must satisfy the following criteria:

1. **Current-Carrying Capacity (Ampacity)**
2. **Voltage Drop**
3. **Short-Circuit Withstand**
4. **Earth Fault Loop Impedance** (for automatic disconnection)

### 1. Current-Carrying Capacity

The cable must be sized to carry the design current continuously without exceeding temperature limits.

#### Design Current (Ib)

- **Single Load**: Ib = Load current
- **Motor Circuit**: Ib = 1.25 × Motor full load current
- **Feeder**: Ib = Sum of connected loads × Diversity factor

#### Cable Rating (Iz)

The tabulated current-carrying capacity (It) from IEC 60364-5-52 or cable manufacturer's data must be derated for installation conditions:

```
Iz = It × Ca × Cg × Ci × Cc
```

Where:
- **Ca** = Ambient temperature correction factor
- **Cg** = Grouping (bunching) correction factor
- **Ci** = Thermal insulation correction factor
- **Cc** = Cable installation method correction factor

#### Selection Criterion

```
In ≥ Ib
Iz ≥ In
```

Where:
- **In** = Nominal rating of protective device
- **Ib** = Design current
- **Iz** = Current-carrying capacity of cable

### 2. Voltage Drop

Maximum voltage drop limits per [IEC 60364-5-52](https://www.iec.ch/):

- **Lighting circuits**: 3%
- **Other uses**: 5%
- **Combined (from origin to final circuit)**: 4% lighting, 8% other

#### Voltage Drop Calculation

For three-phase circuits:

```
ΔV = √3 × Ib × (R × cosφ + X × sinφ) × L
```

For single-phase circuits:

```
ΔV = 2 × Ib × (R × cosφ + X × sinφ) × L
```

Where:
- **ΔV** = Voltage drop (V)
- **Ib** = Design current (A)
- **R** = Cable resistance per unit length (Ω/km)
- **X** = Cable reactance per unit length (Ω/km)
- **cosφ** = Power factor
- **sinφ** = √(1 - cosφ²)
- **L** = Cable length (km)

#### Percentage Voltage Drop

```
Vd% = (ΔV / Un) × 100
```

Where **Un** = Nominal voltage (V)

### 3. Short-Circuit Withstand

The cable must withstand the thermal effects of short-circuit current without damage.

#### Minimum Cross-Sectional Area

```
S = √(I²t) / k
```

Where:
- **S** = Minimum cross-sectional area (mm²)
- **I** = Prospective short-circuit current (A)
- **t** = Disconnection time of protective device (s)
- **k** = Factor depending on conductor and insulation material (A/mm²)

**k-values** (from IEC 60364-5-54):
- Copper conductor, PVC insulation (70°C): k = 115
- Copper conductor, XLPE insulation (90°C): k = 143
- Aluminum conductor, PVC insulation: k = 76
- Aluminum conductor, XLPE insulation: k = 94

### 4. Earth Fault Loop Impedance

For automatic disconnection of supply (ADS), the earth fault loop impedance must be low enough to ensure the protective device operates within the required time.

#### Criterion

```
Zs ≤ (Uo × Cmin) / Ia
```

Where:
- **Zs** = Earth fault loop impedance (Ω)
- **Uo** = Nominal voltage to earth (230V for 400V system)
- **Cmin** = Minimum voltage factor (typically 0.95)
- **Ia** = Current causing automatic operation within required time

## Example Calculations

### Example 1: 11kV Feeder Cable

**Given:**
- Design current (Ib) = 400A
- Cable length (L) = 250m
- Installation: Three single-core cables in trefoil, direct buried
- Ambient temperature: 30°C
- Load power factor: 0.95 lagging
- Prospective short-circuit current: 25 kA
- Fault clearing time: 1 second

**Step 1: Select Cable Size Based on Current Capacity**

From IEC 60502 tables for 11kV XLPE cables:
- 240 mm² copper, It = 480A (at 20°C, single circuit)

**Correction Factors:**
- Ca (30°C): 1.0 (base temperature 20°C for buried cables)
- Cg (single circuit): 1.0
- Ci (no additional insulation): 1.0
- Cc (direct buried): 1.0

```
Iz = 480 × 1.0 × 1.0 × 1.0 × 1.0 = 480A
```

**Check:** Iz (480A) > Ib (400A) ✓

**Step 2: Voltage Drop**

For 240 mm² copper at 11kV:
- R = 0.0754 Ω/km (90°C)
- X = 0.11 Ω/km

```
ΔV = √3 × 400 × (0.0754 × 0.95 + 0.11 × 0.312) × 0.25
    = √3 × 400 × (0.0716 + 0.0343) × 0.25
    = √3 × 400 × 0.1059 × 0.25
    = 18.4 V

Vd% = (18.4 / 11000) × 100 = 0.167%
```

**Check:** 0.167% < 2% (acceptable) ✓

**Step 3: Short-Circuit Withstand**

For copper XLPE (k = 143):

```
S_min = √(25000² × 1) / 143
      = √(625,000,000) / 143
      = 25000 / 143
      = 175 mm²
```

**Check:** 240 mm² > 175 mm² ✓

**Result:** 240 mm² copper XLPE cable is suitable.

---

### Example 2: 400V Sub-Main Cable

**Given:**
- Design current (Ib) = 200A
- Cable length (L) = 50m
- Installation: Multicore cable on cable tray
- Ambient temperature: 40°C
- Two other circuits on same tray (grouped)
- Load power factor: 0.9 lagging
- Prospective short-circuit current: 15 kA
- Fault clearing time: 0.2 seconds

**Step 1: Select Cable Size**

From IEC 60364-5-52 tables:
- 95 mm² copper, PVC insulated, It = 246A (at 30°C, Reference Method E)

**Correction Factors:**
- Ca (40°C): 0.87
- Cg (3 circuits touching): 0.75
- Ci: 1.0
- Cc: 1.0

```
Iz = 246 × 0.87 × 0.75 × 1.0 × 1.0 = 160A
```

**Check:** Iz (160A) < Ib (200A) ✗

**Try 120 mm² copper:**
- It = 286A

```
Iz = 286 × 0.87 × 0.75 = 186A
```

Still insufficient. **Try 150 mm²:**
- It = 328A

```
Iz = 328 × 0.87 × 0.75 = 214A
```

**Check:** Iz (214A) > Ib (200A) ✓

**Step 2: Voltage Drop**

For 150 mm² copper at 400V:
- R = 0.124 Ω/km (70°C)
- X = 0.08 Ω/km

```
ΔV = 2 × 200 × (0.124 × 0.9 + 0.08 × 0.436) × 0.05
    = 2 × 200 × (0.1116 + 0.0349) × 0.05
    = 2 × 200 × 0.1465 × 0.05
    = 2.93 V

Vd% = (2.93 / 400) × 100 = 0.73%
```

**Check:** 0.73% < 5% ✓

**Step 3: Short-Circuit Withstand**

For copper PVC (k = 115):

```
S_min = √(15000² × 0.2) / 115
      = √(45,000,000) / 115
      = 6708 / 115
      = 58 mm²
```

**Check:** 150 mm² > 58 mm² ✓

**Result:** 150 mm² 4-core copper PVC cable is suitable.

---

### Example 3: Low Voltage Final Circuit

**Given:**
- Design current (Ib) = 32A (ring final circuit)
- Cable length (L) = 40m (longest point)
- Installation: In conduit in insulated wall
- Ambient temperature: 30°C
- Protective device: 32A MCB (Type B)
- Prospective short-circuit current: 6 kA
- Maximum disconnection time: 0.4s (per IEC 60364-4-41)

**Step 1: Select Cable Size**

Standard ring final circuit uses 2.5 mm² or 4 mm² copper cables.

From IEC 60364-5-52:
- 2.5 mm² copper, PVC, It = 24A (Reference Method C, clipped direct)

**Correction Factors:**
- Ca (30°C): 1.0 (base)
- Cg: 1.0 (single circuit)
- Ci (in insulated wall): 0.5

```
Iz = 24 × 1.0 × 1.0 × 0.5 = 12A
```

This is insufficient. **Try 4 mm²:**
- It = 32A

```
Iz = 32 × 1.0 × 1.0 × 0.5 = 16A
```

Still low for a radial circuit. For a **ring circuit**, the effective current capacity is doubled at the origin, so:

```
Iz_ring = 16A × 2 = 32A
```

**Check:** Iz (32A) ≥ Ib (32A) ✓ (ring circuit configuration)

**Step 2: Voltage Drop**

For 2.5 mm² copper in ring:
- Effective length = 40m / 2 = 20m (ring circuit)
- R = 7.41 mΩ/m
- X ≈ 0 (negligible for short LV circuits)

```
ΔV = 2 × 32 × 7.41 × 10^-3 × 20 = 9.5 V

Vd% = (9.5 / 230) × 100 = 4.1%
```

**Check:** 4.1% > 3% for lighting but acceptable if not all lighting.

**Step 3: Earth Fault Loop Impedance**

For 32A MCB Type B, maximum Zs for 0.4s disconnection:
- From IEC 60898, Ia = 5 × In = 160A
- Uo = 230V, Cmin = 0.95

```
Zs_max = (230 × 0.95) / 160 = 1.37 Ω
```

**Check circuit impedance:**
- Phase conductor: (R1 × L) = 7.41 × 40 = 296 mΩ = 0.296 Ω
- CPC (2.5 mm²): (R2 × L) = 7.41 × 40 = 0.296 Ω (assuming same size)
- R1 + R2 = 0.592 Ω

Assuming Ze (external impedance) = 0.35 Ω (typical TN-S supply):

```
Zs = Ze + R1 + R2 = 0.35 + 0.592 = 0.942 Ω
```

**Check:** Zs (0.942 Ω) < Zs_max (1.37 Ω) ✓

**Result:** 2.5 mm² twin & earth (or 2.5 mm² ring circuit) is suitable for this application.

---

## Software Tools

For complex installations, use specialized software:

- **ETAP** - Electrical Transient Analyzer Program
- **DIgSILENT PowerFactory** - Power system analysis
- **AMTECH ProDesign** - Electrical design and calculation
- **Trimble AutoCAD Electrical** - With cable calculation modules

## Summary Table: Typical Cable Sizes

| Application                  | Voltage    | Typical Current | Typical Size (Cu)  | Installation Method      |
|------------------------------|------------|-----------------|--------------------|-----------------------   |
| 33kV Primary Feeder          | 33kV       | 300-800A        | 185-300 mm² SC     | Direct buried / Ducts    |
| 11kV Secondary Feeder        | 11kV       | 200-500A        | 120-240 mm² SC     | Direct buried / Ducts    |
| 11kV/400V Transformer Feed   | 11kV       | 100-300A        | 70-150 mm² SC      | Cable tray / Ducts       |
| LV Main Distribution         | 400V       | 400-1000A       | 185-400 mm² MC     | Cable tray               |
| LV Sub-Main                  | 400V       | 100-300A        | 70-150 mm² MC      | Cable tray / Trunking    |
| Final Circuit (Power)        | 230/400V   | 16-63A          | 2.5-16 mm² MC      | Conduit / Clipped        |
| Lighting Circuit             | 230V       | 6-16A           | 1.5-2.5 mm²        | Conduit / Clipped        |

**SC** = Single-Core, **MC** = Multi-Core

## References

- [IEC 60364-5-52](https://www.iec.ch/) - Low-voltage electrical installations - Part 5-52: Selection and erection of electrical equipment - Wiring systems
- [IEC 60502](https://www.iec.ch/) - Power cables with extruded insulation and their accessories for rated voltages
- [BS 7671](https://electrical.theiet.org/) - Requirements for Electrical Installations (UK)
- [IEEE 835](https://standards.ieee.org/) - IEEE Standard Power Cable Ampacity Tables

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval by electrical engineer.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.

---
