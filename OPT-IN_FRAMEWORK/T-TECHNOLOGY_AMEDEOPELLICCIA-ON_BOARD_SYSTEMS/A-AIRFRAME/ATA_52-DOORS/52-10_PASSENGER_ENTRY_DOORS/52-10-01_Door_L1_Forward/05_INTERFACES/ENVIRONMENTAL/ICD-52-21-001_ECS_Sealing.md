# Interface Control Document
## Door L1 Forward ECS Sealing Interface

**ICD Number:** ICD-52-21-001  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 21 (Environmental Control System)

---

## 1. INTERFACE OVERVIEW

This ICD defines the interface between Door L1 Forward and the Environmental Control System (ECS) for cabin pressurization and sealing.

---

## 2. PRESSURE SEALING REQUIREMENTS

### 2.1 Operating Pressure Differential
- Maximum differential: 9.1 psi (typical cruise at 41,000 ft)
- Design differential: 8.5 psi (nominal)
- Proof pressure: 10.2 psi (1.2× max operating)
- Leak rate limit: 0.05 CFM @ 8.5 psi

### 2.2 Seal System Interface
- Primary seal: Inflatable silicone (see ICD-52-53-005)
- Seal inflation: 15 psi pneumatic from bleed air
- Seal monitoring: Pressure switch feedback
- Emergency deflation: Automatic on emergency opening

---

## 3. CABIN PRESSURE INTERFACE

### 3.1 Pressure Load Distribution
- Total pressure load: 115 kN @ 8.5 psi
- Distributed load: 15 kN per square meter
- Load path: Door → Latches → Fuselage frame
- Pressure relief: Safety valve if door jammed

### 3.2 Depressurization Effects
- Emergency descent: Door structure withstands rapid depressurization
- Seal integrity: Maintained during normal depressurization
- Leak detection: ECS monitors cabin pressure rate
- Door indication: Pressure differential interlock

---

## 4. TEMPERATURE INTERFACE

### 4.1 Operating Temperature Range
- Exterior surface: -70°C to +85°C
- Interior surface: +10°C to +35°C (cabin temperature)
- Temperature gradient: Managed by door insulation
- Thermal expansion: Accounted for in seal design

### 4.2 Insulation Requirements
- Door panel insulation: R-value 3.5 (SI units)
- Thermal conductivity: <0.04 W/(m·K)
- Condensation prevention: Vapor barrier included
- Thermal bridges: Minimized at fasteners

---

## 5. HUMIDITY AND MOISTURE

### 5.1 Moisture Control
- Cabin humidity: 10-20% RH typical
- Condensation prevention: Interior surface above dew point
- Drainage: Integral drain paths in seal groove
- Moisture barrier: Seal groove sealed to interior

### 5.2 Water Ingress Prevention
- Rain seal: Secondary blade seal (ICD-52-53-005)
- Drain system: 4 drain tubes, 12mm diameter
- Freeze protection: Drain tubes heated (optional)
- Standing water: Design prevents pooling

---

## 6. VENTILATION

### 6.1 Door Cavity Ventilation
- Ventilation: Small vent holes to equalize pressure
- Airflow: <1 CFM through cavity
- Purpose: Prevent moisture buildup
- Filter: Optional to prevent debris entry

### 6.2 Vent Hole Locations
- Upper door frame: 2× vent holes, 6mm diameter
- Lower door frame: 2× vent holes with drain
- Placement: Non-structural areas only

---

## 7. ECS INTEGRATION

### 7.1 Pneumatic Supply for Seal
- Source: Bleed air system (ATA 36)
- Regulation: 15 psi ±2 psi
- Isolation: Solenoid valve, electrically controlled
- Emergency: Manual deflation override

### 7.2 Seal Inflation Control
- Control signal: From door controller
- Inflation sequence: Automatic on door close and lock
- Deflation: Automatic on door unlock
- Monitoring: Pressure switch in inflation line

---

## 8. PRESSURE RELIEF

### 8.1 Overpressure Protection
- Relief valve: Set at 12 psi (cabin pressure)
- Location: Cabin pressure control system
- Door protection: Designed for 1.33× max pressure
- Safety factor: 2.0 ultimate

### 8.2 Differential Interlock
- Pressure differential sensor: Monitors door area
- Interlock function: Prevents door opening if pressure >0.5 psi
- Override: Emergency only, with warning
- Indication: Flight deck caution if attempted

---

## 9. VERIFICATION

- [x] Pressure leak test completed
- [x] Seal inflation system tested
- [ ] Thermal cycling test - scheduled
- [ ] Humidity exposure test - scheduled
- [ ] Ice/freeze test - scheduled

---

## 10. ENVIRONMENTAL TEST REQUIREMENTS

### 10.1 Pressure Testing
- Proof test: 10.2 psi, 2 minutes hold
- Leak test: 8.5 psi, measure leak rate
- Fatigue test: 60,000 cycles, 0 to 8.5 psi
- Ultimate: 17.0 psi (burst test on test article)

### 10.2 Temperature Testing
- Cold soak: -70°C, 4 hours
- Hot soak: +85°C, 4 hours
- Thermal shock: Rapid transition -70°C to +85°C
- Operational: Full functional test at temperature extremes

---

## 11. RESPONSIBILITIES

| Item | ATA 52 (Door) | ATA 21 (ECS) |
|------|---------------|--------------|
| Door pressure load | Design & provide | Load definition |
| Seal system | Provide & install | Pneumatic supply |
| Insulation | Provide & install | Requirements |
| Drain system | Provide | Integration |
| Pressure monitoring | Interface signals | System monitoring |

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | TBD | Initial draft |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
