# ATA 02 - Operations Information
## Definitions and Terminology

**Document ID:** AMPEL360-02-00-00-OVR-DT  
**Version:** 1.0.0  
**Date:** 2025-11-04  
**Classification:** Operations Critical

---

## 1. PURPOSE

This document provides standard definitions and terminology used throughout AMPEL360 operational documentation, ensuring consistent understanding across all operational personnel.

---

## 2. AIRCRAFT-SPECIFIC TERMS

### 2.1 Blended Wing Body (BWB)

**Blended Wing Body (BWB):** Aircraft configuration where the fuselage and wings are smoothly integrated into a single lifting surface, as opposed to conventional tube-and-wing design.

**Center Body:** The central portion of the BWB containing the main passenger cabin and cargo holds.

**Outer Wings:** The outboard sections of the BWB providing additional lift and containing fuel tanks and propulsion systems.

**Mean Aerodynamic Chord (MAC):** The average chord of the BWB planform, used as reference for center of gravity calculations. For AMPEL360: 15.5m.

**Wetted Area:** Total external surface area exposed to airflow. BWB has 25% less than equivalent conventional aircraft.

### 2.2 Hydrogen Fuel System

**Liquid Hydrogen (LH2):** Hydrogen cooled to -253°C (20K) for dense storage. Primary fuel for AMPEL360.

**Cryogenic:** Temperatures below -150°C. LH2 storage requires cryogenic systems.

**Boil-Off:** Natural evaporation of LH2 due to heat ingress. AMPEL360: 0.3% per hour on ground.

**Usable Fuel:** Fuel that can be reliably consumed by fuel cells. AMPEL360: 7,850 kg of 8,000 kg total.

**Unusable Fuel:** Fuel that cannot be reliably delivered to fuel cells (heel, trapped). AMPEL360: 150 kg.

**Single-Point Refueling:** Refueling through one connection point. H2 refueling time: 45 minutes for full tank.

**Emergency Defueling:** Rapid removal of H2 fuel for safety. Maximum time: 60 minutes.

### 2.3 Fuel Cell Propulsion

**Proton Exchange Membrane (PEM) Fuel Cell:** Type of fuel cell using polymer electrolyte membrane. AMPEL360 uses 4 × 2.5 MW PEM stacks.

**Stack:** Complete fuel cell assembly generating electrical power. AMPEL360: 4 stacks total, 3 minimum for dispatch.

**Efficiency:** Ratio of electrical energy output to fuel energy input. AMPEL360 fuel cells: 55-60%.

**Time Between Overhaul (TBO):** Operational hours before major maintenance required. Fuel cell TBO: 20,000 hours.

**Thermal Management:** System for maintaining fuel cell operating temperature (60-80°C).

**Response Time:** Time to reach requested power output. AMPEL360 fuel cells: 3 seconds.

### 2.4 CAOS System

**CAOS:** Cosmic Advanced Optimization System. AI-powered operations support system.

**Digital Twin:** Real-time virtual model of the aircraft reflecting current state.

**Neural Network:** Machine learning model trained on operational data.

**Fleet Learning:** Continuous improvement from aggregated fleet operational data.

**Confidence Level:** Percentage (0-100%) indicating CAOS certainty in recommendation.

**Advisory Mode:** CAOS provides recommendations; crew retains full authority.

---

## 3. OPERATIONAL TERMS

### 3.1 Weight and Balance

**Maximum Takeoff Weight (MTOW):** Maximum weight authorized for takeoff. AMPEL360: 80,000 kg.

**Maximum Landing Weight (MLW):** Maximum weight authorized for landing. AMPEL360: 70,000 kg.

**Maximum Zero Fuel Weight (MZFW):** Maximum weight excluding fuel. AMPEL360: 65,000 kg.

**Operational Empty Weight (OEW):** Weight of aircraft ready for operations (crew, catering, unusable fuel) but no payload or usable fuel.

**Center of Gravity (CG):** Point where aircraft weight is balanced. Expressed as % MAC. AMPEL360 range: 15-42% MAC.

**Zero Fuel Center of Gravity (ZFCG):** CG position with no usable fuel aboard.

**Loading Envelope:** Allowable combinations of weight and CG position.

### 3.2 Performance Terms

**V1:** Decision speed for takeoff. Above V1, takeoff must continue.

**VR:** Rotation speed. Speed at which pilot initiates rotation for liftoff.

**V2:** Takeoff safety speed. Minimum speed with one engine (fuel cell) inoperative.

**VMCA:** Minimum control speed in air. Minimum speed for directional control.

**Vmo:** Maximum operating speed (indicated airspeed). AMPEL360: 350 KIAS.

**Mmo:** Maximum operating Mach number. AMPEL360: M0.87.

**Service Ceiling:** Maximum altitude for sustained flight. AMPEL360: FL450.

**Range:** Maximum distance aircraft can fly. AMPEL360: 3,500 NM.

**Endurance:** Maximum time aircraft can remain airborne. AMPEL360: 12 hours.

### 3.3 Limitations

**Operating Limitation:** Maximum or minimum value for safe operation.

**Structural Limitation:** Limit imposed by airframe strength.

**System Limitation:** Limit imposed by system capability.

**Environmental Limitation:** Limit imposed by weather/conditions.

**Regulatory Limitation:** Limit imposed by aviation authorities.

---

## 4. FLIGHT PLANNING TERMS

### 4.1 Fuel Planning

**Trip Fuel:** Fuel required from departure to destination.

**Contingency Fuel:** Additional fuel for unforeseen circumstances. Minimum: 5% of trip fuel.

**Alternate Fuel:** Fuel to reach alternate airport plus approach.

**Final Reserve Fuel:** Fuel to hold at 1,500 ft for specified time. AMPEL360: 45 minutes (675 kg H2).

**Extra Fuel:** Additional fuel at captain's discretion.

**Taxi Fuel:** Fuel for ground operations. Typical: 10 kg H2.

**Total Fuel Required:** Sum of all fuel components above.

### 4.2 ETOPS

**ETOPS:** Extended Range Twin-engine Operational Performance Standards. For AMPEL360, extended range operations with fuel cell redundancy.

**ETOPS Entry Point:** Point where aircraft enters ETOPS segment.

**ETOPS Exit Point:** Point where aircraft exits ETOPS segment.

**ETOPS Alternate:** Airport meeting ETOPS alternate requirements.

**Threshold Distance:** Distance requiring ETOPS approval. AMPEL360: 180 minutes.

---

## 5. EMERGENCY TERMS

### 5.1 Alerting

**Warning:** Condition requiring immediate crew action.

**Caution:** Condition requiring crew awareness and possible action.

**Advisory:** Information for crew awareness.

**Master Warning:** Red annunciator for warnings.

**Master Caution:** Amber annunciator for cautions.

### 5.2 Response

**Immediate Action:** Memory item requiring instant response.

**QRH:** Quick Reference Handbook. Cockpit emergency checklist.

**Diversion:** Unplanned landing at alternate airport.

**Emergency Descent:** Rapid descent due to pressurization loss or other emergency.

**Ditching:** Emergency landing on water.

**Evacuation:** Emergency egress of all occupants.

---

## 6. REGULATORY TERMS

### 6.1 Certification

**Type Certificate (TC):** Approval for aircraft design.

**Type Certificate Data Sheet (TCDS):** Official specification of approved design.

**Airworthiness Directive (AD):** Mandatory modification or inspection.

**Service Bulletin (SB):** Recommended modification or inspection.

**Special Condition:** Certification requirement for novel design features.

### 6.2 Operations

**Air Operator Certificate (AOC):** Authorization to conduct commercial operations.

**Operations Specifications (OpSpecs):** Specific authorizations and limitations for operator.

**Minimum Equipment List (MEL):** List of equipment that may be inoperative for dispatch.

**Configuration Deviation List (CDL):** List of missing external parts allowed for dispatch.

---

## 7. AMPEL360-SPECIFIC ACRONYMS

**AMPEL360:** Advanced Multi-Purpose Efficient Low-emission 360° platform  
**BWB:** Blended Wing Body  
**H2:** Hydrogen (chemical symbol for hydrogen)  
**Hy-E:** Hydrogen-Electric (fuel cell propulsion)  
**Q100:** Platform designation (Quantum 100 series)  
**INTEGRA:** Integrated Green Aviation  
**CAOS:** Cosmic Advanced Optimization System  
**LH2:** Liquid Hydrogen  
**PEM:** Proton Exchange Membrane (fuel cell type)  
**FC:** Fuel Cell  
**DAC:** Direct Air Capture (CO₂ capture system)  

---

## 8. UNITS AND CONVERSIONS

*See Units_Measurement.md for detailed conversion tables*

**Mass:**
- kg (kilogram) - Primary unit
- lb (pound) = 0.4536 kg

**Distance:**
- m (meter), km (kilometer) - Primary units
- ft (foot) = 0.3048 m
- NM (nautical mile) = 1.852 km

**Speed:**
- kt (knot) = 1 NM/hr - Primary unit
- km/h = 0.5400 kt
- Mach number - Ratio to speed of sound

**Temperature:**
- °C (Celsius) - Primary unit
- K (Kelvin) = °C + 273.15
- °F (Fahrenheit) = (°C × 9/5) + 32

---

## 9. CONTACT INFORMATION

**Terminology Questions:**
- Email: terminology@ampel360.aero
- Phone: +34 91 XXX XXXX

**Technical Publications:**
- Email: tech-pubs@ampel360.aero
- Phone: +34 91 XXX XXXX (24/7)

---

**Document Status:** ✅ RELEASED  
**Effective Date:** 2029-01-01 (Entry Into Service)  
**Next Review:** 2026-11-04 (Annual)  
**Configuration Control:** Git SHA-256: [hash]
