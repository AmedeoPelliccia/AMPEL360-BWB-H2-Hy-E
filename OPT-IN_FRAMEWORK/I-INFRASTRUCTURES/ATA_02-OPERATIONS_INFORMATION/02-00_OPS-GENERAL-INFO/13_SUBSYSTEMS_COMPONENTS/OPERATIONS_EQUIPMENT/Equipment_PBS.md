# Equipment Product Breakdown Structure (PBS)

**Document ID:** EQ-PBS-001  
**Version:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

## 1. Overview

This document defines the Product Breakdown Structure (PBS) for all Operations Equipment under ATA 02-00-00 GENERAL, including H₂ refueling equipment, ground support equipment (GSE), and emergency equipment.

## 2. Equipment PBS Hierarchy

### Level 1: Operations Equipment System (02-00-00)

#### Level 2: H₂ Refueling Equipment (02-32-00)

##### PNR-02-32-001: Refueling Panel Assembly
- **Function:** External access panel for H₂ refueling connection
- **Location:** Fuselage aft section, starboard side
- **Components:**
  - PNR-02-32-001-01: Panel Door (composite, UV resistant)
  - PNR-02-32-001-02: Locking Mechanism (electromagnetic lock)
  - PNR-02-32-001-03: Seal Kit (cryogenic rated)
  - PNR-02-32-001-04: Connector Assembly (H₂ rated)

##### PNR-02-32-002: Refueling Receptacle
- **Function:** Connects ground H₂ supply to aircraft system
- **Location:** Internal fuselage, behind refueling panel
- **Specifications:**
  - Pressure Rating: 700 bar (10,000 psi)
  - Flow Rate: 5 kg H₂/min
  - Temperature Range: -40°C to +85°C
- **Components:**
  - PNR-02-32-002-01: Receptacle Body (stainless steel)
  - PNR-02-32-002-02: Coupling Interface (quick disconnect)
  - PNR-02-32-002-03: Check Valve (redundant sealing)

##### PNR-02-32-003: Safety Equipment Set
- **Function:** Monitor and protect H₂ refueling operations
- **Components:**
  - PNR-02-32-003-01: H₂ Leak Detector (electrochemical sensor)
  - PNR-02-32-003-02: Emergency Shutoff Valve (fail-safe closed)
  - PNR-02-32-003-03: Fire Suppression Kit (water mist system)
  - PNR-02-32-003-04: Warning Placard Set (multilingual)

---

#### Level 2: Ground Support Equipment (02-GSE-XX)

##### PNR-02-GSE-001: Towing Equipment
- **Function:** Aircraft ground movement
- **Specifications:**
  - Tow Capacity: 250,000 kg (550,000 lb)
  - Speed: 0-5 km/h (0-3 mph)
- **Components:**
  - PNR-02-GSE-001-01: Towbar Assembly (telescoping, 6m-12m)
  - PNR-02-GSE-001-02: Tow Head (nose gear attachment)
  - PNR-02-GSE-001-03: Safety Chains (redundant safety)

##### PNR-02-GSE-002: Power Supply Unit
- **Function:** Ground electrical power for systems testing
- **Specifications:**
  - Power Output: 90 kVA, 115/200 VAC, 400 Hz
  - Voltage Regulation: ±2%
- **Components:**
  - PNR-02-GSE-002-01: Power Generator (diesel, 150 kVA)
  - PNR-02-GSE-002-02: Cable Reel (50m aircraft cable)
  - PNR-02-GSE-002-03: Connector Set (MIL-STD connectors)

##### PNR-02-GSE-003: Air Start Unit
- **Function:** Pneumatic power for APU/system start
- **Specifications:**
  - Air Flow: 2.0 kg/s (4.4 lb/s)
  - Pressure: 35 psi
- **Components:**
  - PNR-02-GSE-003-01: Compressor (rotary screw, diesel)
  - PNR-02-GSE-003-02: Hose Assembly (25m, pressure rated)
  - PNR-02-GSE-003-03: Control Panel (remote operation)

---

#### Level 2: Emergency Equipment (02-EMG-XX)

##### PNR-02-EMG-001: Emergency Response Kit
- **Function:** First response for operational incidents
- **Contents:**
  - PNR-02-EMG-001-01: First Aid Kit (ANSI Z308.1 compliant)
  - PNR-02-EMG-001-02: Emergency Tools (cutting, prying)
  - PNR-02-EMG-001-03: Communication Equipment (radio, satellite phone)
  - PNR-02-EMG-001-04: PPE Set (protective suits, gloves, goggles)
  - PNR-02-EMG-001-05: Emergency Lighting (portable, battery)

##### PNR-02-EMG-002: Fire Suppression Equipment
- **Function:** Fire detection and suppression for operations
- **Components:**
  - PNR-02-EMG-002-01: Fire Extinguisher (Halon 1211, 5 lb) [Being phased out]
  - PNR-02-EMG-002-01A: Fire Extinguisher (Clean Agent, 6 lb) [Replacement]
  - PNR-02-EMG-002-02: Fire Blanket (2m x 2m, flame retardant)
  - PNR-02-EMG-002-03: Fire Detection Sensors (thermal, smoke)
  - PNR-02-EMG-002-04: Fire Suppression System (water mist, H₂ compatible)

---

## 3. Equipment Specifications Summary

| Equipment | Part Number | Weight (kg) | Dimensions (L×W×H cm) | Power Requirements |
|-----------|-------------|-------------|----------------------|-------------------|
| Refueling Panel Assy | PNR-02-32-001 | 85 | 120×80×15 | 28V DC, 5A |
| Refueling Receptacle | PNR-02-32-002 | 45 | 50×40×30 | Passive |
| Safety Equipment Set | PNR-02-32-003 | 25 | Distributed | 28V DC, 2A |
| Towing Equipment | PNR-02-GSE-001 | 450 | 1200×60×40 | Tow vehicle powered |
| Power Supply Unit | PNR-02-GSE-002 | 2800 | 300×180×200 | Self-contained |
| Air Start Unit | PNR-02-GSE-003 | 3200 | 350×200×220 | Self-contained |
| Emergency Response Kit | PNR-02-EMG-001 | 35 | 80×50×30 | Battery (120h) |
| Fire Suppression Equip | PNR-02-EMG-002 | 95 | Distributed | 28V DC, 3A |

## 4. Interface Requirements

### 4.1 H₂ Refueling Equipment Interfaces

**To Aircraft Systems:**
- ATA 28-10: H₂ Storage Tanks (pressure, flow, temperature data)
- ATA 28-30: Fuel Management System (refuel control commands)
- ATA 31: Indicating System (refuel status display)
- ATA 26: Fire Protection (H₂ leak detection integration)

**To Ground Systems:**
- H₂ Supply Truck/Station (SAE J2601 compatible)
- Ground Power (for monitoring systems)
- Communications (radio link to ramp control)

### 4.2 GSE Equipment Interfaces

**Towing Equipment:**
- Aircraft nose landing gear (standard tow fitting)
- Tow vehicle (standard tow hitch)

**Power Supply Unit:**
- Aircraft external power receptacle (MIL-DTL-38999)
- Ground electrical grid (440V, 3-phase)

**Air Start Unit:**
- Aircraft pneumatic port (standard MS connector)
- Ground power (optional battery start)

### 4.3 Emergency Equipment Interfaces

**Fire Suppression:**
- Fire detection sensors to CAOS (real-time monitoring)
- Manual activation controls (push buttons, pull stations)

## 5. Maintenance Requirements

| Equipment | Inspection Interval | Overhaul Interval | MTBF (hours) | Certifications |
|-----------|---------------------|-------------------|--------------|----------------|
| Refueling Panel | 500 flight hours | 5000 flight hours | 10,000 | EASA Part-21 |
| Refueling Receptacle | 250 flight hours | 2500 flight hours | 8,000 | ISO 19881 |
| Safety Equipment | 100 flight hours | 1000 flight hours | 5,000 | ATEX, IECEx |
| Towing Equipment | 250 tow operations | 2500 operations | N/A | Local authority |
| Power Supply Unit | 500 hours | 5000 hours | 3,000 | ISO 9001 |
| Air Start Unit | 500 hours | 5000 hours | 3,500 | ISO 9001 |
| Emergency Kits | 90 days | Annual | N/A | ANSI, EN standards |
| Fire Suppression | 180 days | Annual | N/A | NFPA, EN3 |

## 6. Safety and Compliance

### 6.1 H₂ Equipment Safety

**Standards Compliance:**
- ISO 19881: Hydrogen refueling connectors
- SAE J2601: Fueling protocols for hydrogen vehicles
- ISO 19880-5: Dispensing systems and components
- NFPA 2: Hydrogen Technologies Code

**Safety Features:**
- Automatic leak detection with shutoff
- Redundant sealing and pressure relief
- Grounding and bonding protection
- Emergency disconnect capability

### 6.2 GSE Safety

**Standards Compliance:**
- SAE AS8046: Aircraft towing equipment
- MIL-STD-1366: Aircraft ground support equipment
- ISO 6966: Aircraft ground support equipment standards

**Safety Features:**
- Overload protection on towing equipment
- Voltage regulation and surge protection on power unit
- Pressure regulation and relief on air start unit

### 6.3 Emergency Equipment Certification

- ANSI Z308.1: First aid kits
- NFPA 10: Portable fire extinguishers
- EN 3: Portable fire extinguishers (European)
- ATEX: Equipment in explosive atmospheres

## 7. Training Requirements

| Equipment | Operator Training | Maintenance Training | Recertification |
|-----------|------------------|---------------------|-----------------|
| H₂ Refueling | 16 hours + practical | 40 hours + assessment | Annual |
| GSE (Towing) | 8 hours + practical | 24 hours | Annual |
| GSE (Power/Air) | 4 hours | 16 hours | Biennial |
| Emergency Equipment | 4 hours | 8 hours | Annual |
| Fire Suppression | 8 hours + practical | 16 hours | Annual |

## 8. Related Documents

- Master_Part_Number_Registry.csv
- Component_Breakdown_Structure.md
- OPERATIONS_EQUIPMENT/Equipment_Part_Numbers.csv
- SUPPLIER_MANAGEMENT/Approved_Suppliers_List.csv
- SPARES_MANAGEMENT/Recommended_Spares_List.csv

---

**Document Control:**
- **Version:** 1.0
- **Status:** Active
- **Approved By:** Operations Manager
- **Next Review Date:** 2026-05-05
- **Owner:** Operations Engineering
