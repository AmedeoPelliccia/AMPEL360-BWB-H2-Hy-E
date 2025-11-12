# ATA 28-10-10: Primary H₂ Storage Tank (6-digit Level)

**Parent Subsystem:** 28-10-00 - H₂ Storage Tanks  
**ATA Code:** 28-10-10  
**Level:** Functional Assembly (6-digit)  
**Classification:** Safety Critical - DAL A

---

## Assembly Description

The Primary H₂ Storage Tank is the main liquid hydrogen containment vessel for the AMPEL360 aircraft. It is a Type IV composite overwrapped pressure vessel (COPV) with multi-layer vacuum insulation (MLVI), designed to store [TBD] kg of liquid hydrogen at -253°C and operating pressures up to [TBD] bar.

### Key Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Capacity** | [TBD] kg LH₂ | Nominal usable capacity |
| **Internal Volume** | [TBD] liters | At 20K, density ≈ 71 kg/m³ |
| **Operating Pressure** | [TBD] bar | Maximum Expected Operating Pressure (MEOP) |
| **Design Pressure** | [TBD] bar | 1.5 × MEOP minimum per standards |
| **Burst Pressure** | [TBD] bar | > 2.25 × MEOP (certification test) |
| **Empty Weight** | [TBD] kg | Tank + insulation + instrumentation |
| **Full Weight** | [TBD] kg | With maximum LH₂ load |
| **Length** | [TBD] mm | Overall tank length |
| **Diameter** | [TBD] mm | Maximum outer diameter |
| **Design Life** | 20 years / 10,000 cycles | Minimum required service life |

---

## 8-Digit Component Breakdown

### 28-10-10-01: Tank Shell (Composite Overwrap)
- **Function:** Primary pressure containment structure
- **Inner Liner:** High-density polyethylene (HDPE) or aluminum
- **Overwrap:** Carbon fiber (T700 or T1000) with epoxy resin
- **Winding Pattern:** Hoop + helical layers optimized for pressure
- **Thickness:** [TBD] mm composite + [TBD] mm liner

### 28-10-10-02: End Domes (Forward and Aft)
- **Function:** Tank closures with penetrations for fittings
- **Material:** Same composite construction as shell
- **Boss Penetrations:** Liquid outlet, gas inlet/outlet, instrumentation
- **Geometry:** Geodesic or isotensoid shape (optimized stress)

### 28-10-10-03: Internal Baffles
- **Function:** Anti-slosh, thermal stratification prevention
- **Material:** Aluminum alloy (cryogenic compatible)
- **Design:** Perforated plates with controlled flow area
- **Quantity:** [TBD] baffles distributed along tank length

### 28-10-10-04: Liquid Level Sensor Assembly
- **Function:** Measure LH₂ quantity (0-100% range)
- **Type:** Capacitive probe (dielectric constant of LH₂)
- **Probe Length:** [TBD] mm (full tank height)
- **Accuracy:** ±2% of full scale
- **Output:** 4-20mA + ARINC 429 digital
- **Part Numbers:** See 9-digit breakdown (28-10-10-041, 042, 043)

### 28-10-10-05: Temperature Sensor Array
- **Function:** Multi-zone temperature monitoring
- **Sensor Type:** Type T thermocouples (Cu-CuNi, cryogenic rated)
- **Quantity:** 8 sensors per tank (top, mid, bottom, wall zones)
- **Temperature Range:** -270°C to +85°C
- **Accuracy:** ±1°C or ±0.75% (whichever is greater)
- **Output:** Thermocouple voltage + cold junction compensation

### 28-10-10-06: Pressure Transducer
- **Function:** Real-time tank pressure measurement
- **Type:** Strain gauge or capacitive (cryogenic rated)
- **Range:** 0 to [TBD] bar absolute
- **Accuracy:** ±0.25% full scale
- **Response Time:** < 10 ms
- **Output:** 4-20mA + digital (ARINC 429 or RS-485)

### 28-10-10-07: Safety Valve (Primary)
- **Function:** Overpressure protection (primary relief)
- **Type:** Spring-loaded safety relief valve
- **Set Pressure:** [TBD] bar (typically 110% of MEOP)
- **Flow Capacity:** [TBD] kg/min gaseous H₂ at set pressure
- **Re-seat Pressure:** ≥ 90% of set pressure
- **Certification:** ASME Section VIII Division 1

### 28-10-10-08: Safety Valve (Secondary/Redundant)
- **Function:** Backup overpressure protection
- **Type:** Spring-loaded safety relief valve (independent)
- **Set Pressure:** [TBD] bar (typically 115% of MEOP)
- **Redundancy:** Completely independent from primary
- **Same specifications as 28-10-10-07**

### 28-10-10-09: Burst Disk Assembly
- **Function:** Ultimate overpressure protection (last resort)
- **Type:** Rupture disk (one-time use)
- **Rupture Pressure:** [TBD] bar (typically 150% of MEOP)
- **Material:** Inconel or stainless steel
- **Replacement:** Required after activation
- **Telltale Indicator:** Visual indication of rupture

### 28-10-10-10: Liquid Outlet Valve
- **Function:** Control LH₂ flow from tank to feed line (28-20-10)
- **Type:** Solenoid-actuated ball valve (fail-closed)
- **Size:** [TBD] mm diameter
- **Actuation:** 28 VDC + pneumatic backup
- **Response Time:** < 100 ms (close), < 500 ms (open)

### 28-10-10-11: Multi-Layer Insulation (MLI) Assembly
- **Function:** Minimize radiative heat transfer to LH₂
- **Material:** 20-40 layers of aluminized mylar (crinkled)
- **Effective k:** < [TBD] W/m·K
- **Attachment:** Wrapped around tank, secured with tapes
- **Maintenance:** Visual inspection for damage, no routine replacement

### 28-10-10-12: Vacuum Jacket
- **Function:** Outer shell maintaining vacuum for insulation
- **Material:** Stainless steel or aluminum alloy
- **Vacuum Level:** < 10⁻⁵ mbar (high vacuum)
- **Leak Rate:** < [TBD] mbar·L/s helium equivalent
- **Penetrations:** Minimized, sealed with vacuum-tight fittings

### 28-10-10-13: Vacuum Port and Getter System
- **Function:** Evacuate and maintain vacuum, absorb residual H₂
- **Vacuum Port:** Valve for initial pumpdown and monitoring
- **Getter Material:** Activated charcoal or zeolite
- **Getter Capacity:** [TBD] g of H₂ absorption
- **Monitoring:** Vacuum gauge (ionization or cold cathode)

### 28-10-10-14: Mounting Attachment Points
- **Function:** Interface to tank mounting structure (28-10-30)
- **Type:** Lugs or brackets (load-distributing)
- **Material:** Titanium alloy (Ti-6Al-4V)
- **Thermal Isolation:** G-10 or similar low-k insulating pads
- **Load Capacity:** [TBD] kN axial, [TBD] kN lateral

---

## Example: 9-Digit Part Variants

### 28-10-10-04: Liquid Level Sensor - Part Variants

#### 28-10-10-041: Level Sensor (Standard Production)
- **Probe Length:** [TBD] mm (nominal for primary tank)
- **P/N:** AMPEL-28-LLS-041-A
- **Manufacturer:** [Sensor Manufacturer Name]
- **Unit Cost:** $[TBD]
- **Lead Time:** [TBD] weeks

#### 28-10-10-042: Level Sensor (Extended Range)
- **Probe Length:** [TBD] mm +10% (for tolerance variation)
- **P/N:** AMPEL-28-LLS-042-A
- **Use:** Backup or replacement with dimensional tolerance
- **Interchangeable:** Yes, with calibration update

#### 28-10-10-043: Level Sensor (Service/Spare)
- **Probe Length:** Universal/field-trimmable design
- **P/N:** AMPEL-28-LLS-043-A
- **Use:** Spare parts inventory (reduces SKU count)
- **Calibration:** Includes calibration certificate

---

## Interfaces

### Fluid Interfaces
- **Liquid Outlet (28-10-10-10):** Connects to 28-20-10 (Main Feed Line)
- **Gas Inlet/Vent:** Connects to 28-50-00 (Boil-Off Recovery)
- **Fill Connection:** Connects to 28-10-60 (Tank Filling Interface)
- **Relief Discharge:** Vents to atmosphere via safe discharge path

### Mechanical Interfaces
- **Mounting Points (28-10-10-14):** Attaches to 28-10-30 (Mounting Structure)
- **Structural Loads:** Transfers pressure, weight, inertial loads to airframe

### Electrical/Data Interfaces
- **Level Sensor (28-10-10-04):** 4-20mA + ARINC 429 to ATA 31 (Instrumentation)
- **Temperature Array (28-10-10-05):** 8 × thermocouple signals to data acquisition
- **Pressure Transducer (28-10-10-06):** 4-20mA + digital to flight deck + CAOS
- **Outlet Valve (28-10-10-10):** 28 VDC control from fuel system controller

---

## Safety Analysis (Component Level)

### Critical Failure Modes
1. **Tank rupture:** Catastrophic → Prevented by design margins (2.25× burst), inspections
2. **Insulation failure:** Major → Detectable via boil-off rate increase, vacuum monitoring
3. **Relief valve failure (closed):** Hazardous → Mitigated by redundant valve + burst disk
4. **Sensor failures:** Minor → Multiple sensors, cross-checking, CAOS validation

### Safety Design Features
- **Redundant pressure relief:** Primary + secondary valves + burst disk
- **Fail-safe outlet valve:** Closes on power loss (spring return)
- **Multiple sensors:** Cross-validation detects single sensor failure
- **Leak detection:** Hydrogen sensors around tank, vacuum monitoring

---

## CAOS Integration (Component Level)

### Real-Time Monitoring
- **Pressure trends:** Detect slow leaks or regulator drift
- **Temperature distribution:** Identify thermal stratification issues
- **Level vs. pressure correlation:** Validate sensor accuracy
- **Vacuum degradation:** Predict insulation performance loss

### Predictive Maintenance
- **Sensor calibration drift:** ML models detect when re-calibration needed
- **Valve cycling wear:** Track actuation count, predict maintenance
- **Insulation performance:** Boil-off rate trending vs. ambient conditions
- **Composite fatigue:** Cycle counting toward design life limit

### Digital Twin
- **Thermal model:** Simulates tank temperature and boil-off
- **Structural model:** FEA-based stress analysis updated with real loads
- **Fluid dynamics:** CFD model of internal flow and stratification
- **Synchronization:** Real sensor data calibrates and validates models

---

## Certification Test Requirements

### Pressure Tests
- **Proof Pressure Test:** 1.5 × MEOP for [TBD] duration
- **Leak Test:** Helium leak detection < [TBD] mbar·L/s
- **Cycle Test:** 1.5 × design life (15,000 cycles) to validate fatigue life
- **Burst Test:** Destructive test on qualification unit, > 2.25 × MEOP

### Thermal Tests
- **Boil-off Test:** Validate insulation performance over 24-48 hours
- **Thermal Cycle:** -253°C to ambient, [TBD] cycles
- **Rapid Fill/Drain:** Thermal shock resistance

### Environmental Tests
- **Vibration:** Per DO-160 or equivalent aircraft specification
- **Shock:** Crash pulse simulation
- **Humidity/Salt Fog:** External surface corrosion resistance

### Safety Tests
- **Relief Valve Flow:** Verify capacity at set pressure
- **Burst Disk Rupture:** Verify rupture pressure and fragment containment
- **Fire Test:** External fire resistance (if required by location)

---

## Manufacturing and Quality Control

### Composite Tank Shell (28-10-10-01)
- **Process:** Automated filament winding
- **Cure Cycle:** Autoclave or oven cure per material specification
- **Inspection:** Ultrasonic C-scan for voids, delaminations
- **Quality:** First article inspection, production sampling plan

### Sensor Installation (28-10-10-04, -05, -06)
- **Calibration:** Factory calibration with certificate
- **Installation:** Torque specifications for fittings
- **Verification:** Post-installation functional test

### Vacuum System (28-10-10-12, -13)
- **Evacuation:** Pump to < 10⁻⁵ mbar, seal vacuum port
- **Leak Check:** Helium leak detection on all vacuum penetrations
- **Getter Activation:** Heat cycle to activate getter material

---

## Maintenance Procedures (Component Level)

### Periodic Inspections
- **Visual (Daily):** Check for frost, leaks, damage to external insulation
- **Vacuum Check (500 FH):** Verify vacuum level within specification
- **Sensor Calibration (500 FH):** Compare sensors, check against ground reference
- **Relief Valve Test (500 FH):** Manual actuation test (without gas flow)

### Replacement Intervals
- **Relief Valves:** Overhaul every [TBD] hours or [TBD] years
- **Sensors:** Replace on condition (calibration drift or failure)
- **Getter:** Replace if vacuum degrades beyond specification
- **Tank Assembly:** Service life 10,000 cycles or 20 years, then inspect for life extension

---

## Digital Product Passport (Component Level)

Each component has serialized tracking:

```json
{
  "ata_code": "28-10-10-04",
  "part_number": "AMPEL-28-LLS-041-A",
  "serial_number": "LLS-25110101234",
  "installation": {
    "parent_assembly": "28-10-10 (S/N AMPEL-PT-001-00042)",
    "aircraft_msn": "AMPEL-BWB-001",
    "position": "Primary Tank - Level Sensor",
    "installed_date": "2025-10-01"
  },
  "calibration": {
    "factory_calibration": "2025-09-15",
    "last_in_situ_check": "2025-11-10",
    "next_calibration_due": "2026-05-10",
    "calibration_drift": "+0.3% (within spec)"
  },
  "lifecycle": {
    "power_on_hours": 456.3,
    "failure_count": 0,
    "replacement_history": []
  }
}
```

---

## Weight Budget (Component Level)

| Component | Quantity | Unit Weight (kg) | Total (kg) |
|-----------|----------|------------------|------------|
| 28-10-10-01: Tank Shell | 1 | [TBD] | [TBD] |
| 28-10-10-02: End Domes | 2 | [TBD] | [TBD] |
| 28-10-10-03: Baffles | [TBD] | [TBD] | [TBD] |
| 28-10-10-04: Level Sensor | 1 | 0.5 | 0.5 |
| 28-10-10-05: Temp Sensors | 8 | 0.05 | 0.4 |
| 28-10-10-06: Pressure Trans | 1 | 0.2 | 0.2 |
| 28-10-10-07: Relief Valve (P) | 1 | 1.5 | 1.5 |
| 28-10-10-08: Relief Valve (S) | 1 | 1.5 | 1.5 |
| 28-10-10-09: Burst Disk | 1 | 0.3 | 0.3 |
| 28-10-10-10: Outlet Valve | 1 | 2.0 | 2.0 |
| 28-10-10-11: MLI | - | [TBD] | [TBD] |
| 28-10-10-12: Vacuum Jacket | 1 | [TBD] | [TBD] |
| 28-10-10-13: Getter System | 1 | 0.5 | 0.5 |
| 28-10-10-14: Mounting Points | [TBD] | [TBD] | [TBD] |
| **Total (Empty Tank)** | | | **[TBD]** |

---

## Next Level: 8-Digit Component Documentation

For detailed part-level specifications, see:
- `28-10-10-01_TANK_SHELL/` (composite structure details)
- `28-10-10-04_LEVEL_SENSOR/` (sensor specifications and variants)
- `28-10-10-07_PRIMARY_RELIEF_VALVE/` (valve certification)

Each 8-digit component can have its own 14-folder documentation for complex parts.

---

**Assembly Owner:** Tank Design Team  
**Safety Classification:** DAL A  
**Last Update:** 2025-11-12  
**Generated by:** AMPEL360 Documentation Expert Agent
