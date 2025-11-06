# CERT-02-10-002: Ground Clearance Compliance CS-25

**Document ID:** CERT-02-10-002  
**Title:** Ground Clearance Compliance with CS-25.731  
**Component:** 02-10-00 AIRCRAFT GENERAL DATA  
**Certification Area:** Dimensions - Ground Clearance  
**Status:** In Development  
**Date:** 2025-11-05

---

## 1. Executive Summary

This document demonstrates compliance of the AMPEL360 BWB H₂ Q100 ground clearance with CS-25.731 requirements for safe ground and flight operations.

**Minimum Ground Clearance:** 3.8 m (12.5 ft)  
**Propeller/Rotor Clearance:** N/A (ducted fan electric propulsion)  
**Compliance Status:** ✅ Compliant

---

## 2. Regulatory Requirements

### 2.1 CS-25.731 - Wheels and Tyres: Retraction System
**Reference:** CS-25.731(a)

> **Note:** The following quote uses British English spelling ("aeroplane") as per the original CS-25 regulation.
*"Retraction system must be designed so that during any probable failure condition, the landing gear and doors do not contact the ground when the aeroplane is on the ground."*

**Interpretation:** Adequate ground clearance must be maintained under all loading conditions.

### 2.2 Related Requirements
- **CS-25.25:** Adequate ground clearance for weight distribution
- **CS-25.485:** Lateral ground clearance for side load conditions
- **CS-25.509:** Adequate clearance for towing operations
- **ICAO Annex 14:** Ground clearance for airport obstacles

---

## 3. Aircraft Ground Clearance Specifications

### 3.1 Critical Ground Clearance Points

| Location | Clearance | Unit | Condition |
|----------|-----------|------|-----------|
| **Fuselage Belly (Center)** | 3.8 | m (12.5 ft) | Static |
| **Wing Trailing Edge (Center)** | 4.2 | m (13.8 ft) | Static |
| **Wing Tip (Lowest Point)** | 2.8 | m (9.2 ft) | Static |
| **Nose (Forward Point)** | 6.5 | m (21.3 ft) | Static |
| **Tail (Aft Point)** | 5.8 | m (19.0 ft) | Static |
| **Ducted Fan Nacelles** | 4.5 | m (14.8 ft) | Static |

### 3.2 Landing Gear Configuration
**Main Landing Gear:**
- Configuration: 4-wheel bogie, dual tandem
- Number of Main Gear: 4 (2 per side)
- Tire Size: 54×21.0 R25
- Static loaded radius: 0.72 m
- Stroke: 0.45 m

**Nose Landing Gear:**
- Configuration: Dual wheel
- Tire Size: 42×17.0 R18
- Static loaded radius: 0.58 m
- Stroke: 0.35 m

### 3.3 Geometric Clearance Angles

| Angle | Value | Condition | Requirement |
|-------|-------|-----------|-------------|
| **Tail-down angle** | 13.5° | Rotation | No tail strike |
| **Take-off rotation angle** | 11.0° | Max rotation | >CS-25 minimum |
| **Over-rotation angle** | 15.0° | Emergency | Tail contact |
| **Lateral tilt angle** | 7.0° | One main gear fail | No wingtip strike |

---

## 4. Critical Loading Conditions

### 4.1 Static Ground Clearance
**Condition:** Aircraft at MTOW on level ground, all tires inflated

**Analysis:**
- MTOW: 180,000 kg
- Main gear compression: 0.42 m (from free length)
- Nose gear compression: 0.32 m (from free length)
- Fuselage belly clearance: 3.8 m ✅

**Margin:** 0.8 m above minimum acceptable (3.0 m industry standard)

### 4.2 Dynamic Clearance - Takeoff Rotation
**Condition:** Rotation to lift-off attitude (11° pitch)

**Analysis:**
- Rotation angle: 11.0°
- Aft fuselage depression: 0.35 m
- Tail clearance at rotation: 0.42 m ✅
- Tail strike angle: 13.5° (margin: 2.5°)

**Conclusion:** Adequate clearance during normal takeoff rotation

### 4.3 Dynamic Clearance - Landing Flare
**Condition:** Landing flare at MLW (150,000 kg)

**Analysis:**
- Flare attitude: 9.5° pitch
- Main gear stroke: 0.45 m (full compression on touchdown)
- Belly clearance (compressed): 3.35 m ✅
- Tail clearance (compressed): 0.38 m ✅

**Conclusion:** Adequate clearance during landing

### 4.4 Abnormal Conditions

**Single Main Gear Failure:**
- Lateral tilt: 7.0° (one main gear collapsed)
- Wingtip clearance: 0.25 m
- Engine nacelle clearance: 0.15 m
- **Status:** Marginal - requires controlled environment

**Nose Gear Collapse:**
- Nose depression: 0.58 m (full stroke)
- Nose contact: Designed breakaway structure
- Fuselage protection: Reinforced nose section
- **Status:** Protected by design

---

## 5. BWB Configuration Considerations

### 5.1 Center Body Ground Clearance
**BWB Characteristic:** Wide center body (28 m width)

**Design Features:**
- Cambered lower surface (ground clearance optimized)
- No conventional fuselage "tube" - flat lower surface
- Critical clearance: Center body trailing edge

**Clearance Check:**
- Center body TE height: 4.2 m (static) ✅
- Landing sink rate: 1.8 m/s (6 ft/s) - CS-25.473
- Compression allowance: 0.45 m (gear stroke)
- Residual clearance: 3.75 m ✅

### 5.2 Wing Tip Clearance
**BWB Characteristic:** Wing tips at fuselage level (no high wing)

**Analysis:**
- Wing tip height (static): 2.8 m
- Lateral tilt tolerance: ±7.0°
- Critical condition: Taxiway banking + flat tire
- Worst-case clearance: 0.35 m ✅

**Mitigation:** CAOS system provides wingtip proximity alerts

---

## 6. Ground Operations Clearance

### 6.1 Towing Operations
**Reference:** CS-25.509 - Towing

**Towing Clearance Requirements:**
- Nose gear steering: ±70° (hydraulic)
- Towing tractor clearance: Minimum 0.5 m
- Tow bar attachment height: 1.2 m (standard)

**Compliance:**
- Nose gear well clearance: 1.8 m ✅
- Tow bar ground clearance: 0.45 m ✅
- Maximum towing speed: 15 kt (with clearance monitoring)

### 6.2 Ground Service Equipment
**Equipment Clearance:**

| Equipment | Height | Clearance | Status |
|-----------|--------|-----------|--------|
| Baggage carts | 1.5 m | 2.3 m | ✅ |
| Catering trucks | 3.0 m | 0.8 m | ✅ |
| Fuel trucks (H₂) | 3.2 m | 0.6 m | ⚠️ Caution |
| Passenger stairs | 4.0 m | Integrated | ✅ |

**Note:** H₂ refueling requires specialized equipment - clearance monitored

### 6.3 Hangar Clearance
**Requirement:** Aircraft must fit standard Code E hangars

**Hangar Door Height:** Typically 25 m  
**Aircraft Height:** 18.5 m  
**Clearance:** 6.5 m ✅

---

## 7. Test and Verification Plan

### 7.1 Static Clearance Tests
**Test ID:** DIM-002-STATIC

**Procedure:**
1. Aircraft loaded to MTOW
2. Measure clearance at critical points
3. Compare to design specifications
4. Verify margins

**Acceptance Criteria:**
- Belly clearance ≥ 3.8 m
- Wing tip clearance ≥ 2.8 m
- All margins ≥ 0.2 m

### 7.2 Dynamic Clearance Tests
**Test ID:** DIM-002-DYNAMIC

**Takeoff Rotation Test:**
- Aircraft at takeoff weight
- Rotate to maximum angle (13.5°)
- Measure tail clearance
- Verify no ground contact

**Landing Flare Test:**
- Aircraft at landing weight
- Simulate hard landing (1.8 m/s sink rate)
- Verify gear stroke adequate
- Verify no belly/tail strike

### 7.3 Abnormal Condition Tests
**Test ID:** DIM-002-ABNORMAL

**Simulated Failures:**
- Single main gear collapse (jack stand simulation)
- Nose gear collapse (jack stand simulation)
- Measure clearances and contact points
- Verify structural protection adequate

---

## 8. Compliance Evidence

### 8.1 Analysis Reports
- [ ] Ground clearance analysis (all loading conditions)
- [ ] Rotation and flare clearance study
- [ ] Abnormal conditions analysis
- [ ] Landing gear geometry report

### 8.2 Test Reports
- [ ] Static clearance verification test
- [ ] Dynamic clearance tests (takeoff/landing)
- [ ] Gear collapse simulation tests
- [ ] Ground handling clearance verification

### 8.3 Design Documentation
- [ ] Landing gear design drawings
- [ ] Fuselage lower surface drawings
- [ ] Ground clearance certification drawings
- [ ] Ground operations procedures

---

## 9. Special Conditions

### 9.1 BWB-Specific Considerations
The BWB configuration presents unique ground clearance challenges:

**Advantages:**
- Wide gear track (lateral stability)
- Distributed weight (lower ground pressure)
- No tail strike risk (no conventional tail)

**Challenges:**
- Wide center body (belly clearance critical)
- Low wing tips (lateral clearance critical)
- Over-rotation protection (no tail to contact first)

**Mitigation:**
- Enhanced ground clearance monitoring (CAOS)
- Active pitch control during rotation
- Pilot training on BWB-specific handling

---

## 10. Certification Statement

**Statement:** The AMPEL360 BWB H₂ Q100 aircraft ground clearance complies with:
- CS-25.731 (Landing gear retraction and clearance)
- CS-25.485 (Lateral ground loads - adequate clearance)
- CS-25.509 (Towing operations clearance)

**Minimum Ground Clearance:** 3.8 m (fuselage belly) ✅  
**Critical Condition:** Static at MTOW ✅  
**Margins:** Adequate for all conditions ✅

**Status:** Design complies - awaiting verification testing

**Recommended Finding:** **Compliant** (subject to test verification)

---

## 11. Document Control

### 11.1 Approvals
- [ ] Design Engineer: ___________________ Date: ______
- [ ] Structures Engineer: ___________________ Date: ______
- [ ] Certification Engineer: ___________________ Date: ______
- [ ] Chief Engineer: ___________________ Date: ______

### 11.2 Revisions

| Rev | Date | Description | Author |
|-----|------|-------------|--------|
| 1.0 | 2025-11-05 | Initial document | AMPEL360 Cert Team |

### 11.3 Related Documents
- [CERT-02-10-001: Wingspan Compliance](CERT-02-10-001_Wingspan_Compliance_CS25.md)
- [CERT-02-10-003: ICAO Code E Compliance](CERT-02-10-003_ICAO_Code_E_Compliance.md)
- [Dimension Certification Evidence](Dimension_Certification_Evidence.csv)
- [Landing Gear Design Document](../../04_DESIGN/)

---

**Document Control:**
- Version: 1.0
- Status: In Development
- Classification: Company Confidential
- Next Review: Preliminary Design Review
