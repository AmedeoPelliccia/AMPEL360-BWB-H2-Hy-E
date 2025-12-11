# 10-00-04-003 — Design Constraints

**ATA Chapter:** 10 — Parking, Mooring, Storage & RTS  
**Document ID:** 10-00-04-003  
**Version:** 1.0  
**Status:** DRAFT  

---

## 1. Purpose

This document defines constraints, limitations, and boundary conditions that govern the design of parking, mooring, storage, and RTS provisions for the Q100 aircraft.

---

## 2. Geometric Constraints

### 2.1 BWB Airframe Geometry

- **Wing Span:** 80.4 m (264 ft) — limits mooring point accessibility
- **Overall Length:** 71.0 m (233 ft) — affects towing lug placement
- **Height at Tail:** 16.5 m (54 ft) — requires elevated access for tail mooring
- **Landing Gear Track:** Wide stance — influences jacking point distribution

### 2.2 Ground Clearance

- **Minimum Ground Clearance:** TBD mm (design target)
- **Landing Gear Height:** Affects placement of protective covers and ground locks
- **Underbelly Access:** Limited due to BWB configuration

---

## 3. Load Constraints

### 3.1 Aircraft Weight

- **Maximum Ramp Weight (MRW):** 650,000 kg (1,433,000 lb)
- **Maximum Takeoff Weight (MTOW):** 640,000 kg (1,410,000 lb)
- **Operating Empty Weight (OEW):** ~350,000 kg (est.)

### 3.2 Load Distribution

- **Jacking Points:** Must support 110% of MRW distributed per zone
- **Towing Fittings:** Must support 2× maximum towing load
- **Mooring Points:** Must withstand 90 kt wind loads per [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)

### 3.3 Dynamic Loads

- **Wind-induced oscillations** during mooring
- **Thermal expansion/contraction** in H₂ systems
- **Ground vibration** during towing operations

---

## 4. Environmental Constraints

### 4.1 Operating Environment

- **Temperature Range:** -55°C to +70°C (ambient)
- **Humidity:** 0% to 100% RH
- **Salt Spray:** Coastal airport operations
- **UV Exposure:** Long-term outdoor storage

### 4.2 Cryogenic Environment (H₂ Systems)

- **LH₂ Temperature:** -253°C (-423°F)
- **Thermal Cycling:** Repeated fill/empty cycles
- **Boil-off Rate:** Max XX kg/hr during storage (TBD)

### 4.3 Electrical Environment

- **HV System Voltage:** 800V DC (nominal), up to 1000V transients
- **Arc Flash Energy:** TBD kJ/m² at HV isolation points
- **Ground Fault Detection Sensitivity:** TBD mA

---

## 5. Operational Constraints

### 5.1 Ground Crew Access

- **Maximum Reach Height:** 2.5 m without elevated platform
- **Confined Spaces:** Limited access under BWB wing sections
- **Tool Requirements:** Standard GSE tools preferred

### 5.2 Turnaround Time Targets

- **Quick Turnaround (domestic):** 45 minutes
- **Standard Turnaround (international):** 90 minutes
- **Overnight Storage Setup:** 30 minutes

### 5.3 Airport Compatibility

- **Standard GSE Interfaces:** Must work with existing tow tractors, jacks, ground power units
- **ICAO Annex 14 Compliance:** Aircraft characteristics for aerodrome design
- **Clearance from Terminal Buildings:** Minimum 7.5 m wingtip clearance

---

## 6. Safety Constraints

### 6.1 Hydrogen Safety

- **Minimum Vent Distance:** 10 m from ignition sources (H₂ vent outlets)
- **Leak Detection Threshold:** 25% LEL (Lower Explosive Limit) for H₂
- **Exclusion Zones:** Personnel-free zones during H₂ venting

### 6.2 Electrical Safety

- **HV Isolation Verification:** Must achieve verified zero-energy state
- **LOTO Requirements:** Lockout capability for all HV isolation points
- **Arc Flash Boundaries:** Minimum approach distances per NFPA 70E

### 6.3 Mechanical Safety

- **Locking Mechanisms:** Fail-safe positive locks for ground locks
- **Visual Indicators:** Red/green status indicators required
- **Load Limiters:** Overload protection on critical fittings

---

## 7. Certification Constraints

### 7.1 Type Certificate Limitations

- Design must support **Type Certification (TC)** under [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) / Part 25
- Novel features (H₂, HV) may require **Special Conditions**

### 7.2 Maintainability Requirements

- **Maintenance Interval:** Provisions must support 12,000 flight hour / 10-year service life
- **Inspection Access:** All safety-critical items must be inspectable without special equipment
- **Replacement:** Critical components must be field-replaceable

---

## 8. Interface Constraints

### 8.1 Structural Interfaces

- Mounting points must not interfere with:
  - Wing-fuselage integration structure
  - LH₂ tank supports (ATA 28/73)
  - Landing gear attachments (ATA 32)
  - Cargo floor beams (ATA 25/53)

### 8.2 Systems Interfaces

- Must coordinate with:
  - Flight control surfaces (control surface locks)
  - Propulsion system (propeller/fan locks)
  - Environmental control system (cabin pressurization isolation)
  - Avionics cooling (thermal management during storage)

---

## 9. Manufacturing and Cost Constraints

### 9.1 Manufacturing Feasibility

- Use standard aerospace manufacturing processes
- Minimize custom tooling requirements
- Support serial production targets (50 aircraft/year)

### 9.2 Weight and Cost Targets

- **Weight Allocation (ATA 10 total):** TBD kg
- **Recurring Cost Target:** TBD USD per ship set
- **Non-recurring Cost Target:** TBD USD (NRE)

---

## 10. Traceability

- **Requirements:** Constraints flow to `10-00-03_Requirements/`
- **Design Decisions:** See `10-00-04-004_Design_Decisions.md`
- **Trade Studies:** See `10-00-06_Engineering/` for constraint-driven trades

---

## Document Control

- **Generated with assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT – Subject to human review and approval
- **Human approver:** _[to be completed]_
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-09

---
