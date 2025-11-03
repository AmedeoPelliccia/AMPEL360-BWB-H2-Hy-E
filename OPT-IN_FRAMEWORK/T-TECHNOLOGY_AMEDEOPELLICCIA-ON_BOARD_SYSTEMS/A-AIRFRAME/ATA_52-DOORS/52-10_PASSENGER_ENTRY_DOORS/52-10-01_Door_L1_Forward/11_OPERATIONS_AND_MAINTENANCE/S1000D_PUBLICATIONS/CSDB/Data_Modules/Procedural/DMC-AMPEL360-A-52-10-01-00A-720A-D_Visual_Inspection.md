# Visual Inspection Procedure
## DMC-AMPEL360-A-52-10-01-00A-720A-D

**Issue:** 001  
**Issue Date:** 2025-11-03  
**Information Code:** 720 (Inspection)  
**Classification:** Unclassified  
**Applicable to:** AMPEL360 BWB H2 Hy-E Q100 INTEGRA

---

## 1. GENERAL

This procedural data module provides visual inspection procedures for Door L1 Forward.

---

## 2. APPLICABILITY

**Task:** Visual inspection of door assembly  
**Frequency:** Every 500 flight hours or 180 days (whichever occurs first)  
**Task Card:** MT-52-10-01-001  
**Zone:** 200 (Forward fuselage, left side)

---

## 3. REQUIREMENTS

### 3.1 Prerequisites
- Aircraft on jacks or level ground
- Aircraft power OFF (unless required for testing)
- Adequate lighting (minimum 50 footcandles)
- Access equipment positioned safely

### 3.2 Personnel
- **Required:** 1 qualified technician
- **Qualifications:** Licensed A&P, Door systems familiarization
- **Training:** Visual inspection techniques (AC 43-204)

### 3.3 Tools and Equipment
- Inspection mirror with LED light
- Flashlight (bright, white LED)
- Feeler gauge set (0.001" - 0.050")
- CAOS diagnostic tablet (optional but recommended)
- Digital camera for discrepancy documentation

### 3.4 References
- DMC-AMPEL360-A-52-10-01-00A-000A-D (Door Description)
- DMC-AMPEL360-A-00-00-00-00A-018C-D (Warnings)
- DMC-AMPEL360-A-00-00-00-00A-018D-D (Cautions)

---

## 4. SAFETY

### 4.1 Warnings

**⚠️ WARNING:** DO NOT operate door with aircraft power ON unless specifically required for operational check.

**⚠️ WARNING:** Ensure door is properly secured before entering inspection area beneath door.

### 4.2 Cautions

**CAUTION:** Use only approved cleaning materials on door surfaces. Avoid harsh chemicals that may damage seals or coatings.

**CAUTION:** If CAOS system is used during inspection, ensure system is in maintenance mode to prevent false alerts.

---

## 5. INSPECTION PROCEDURE

### 5.1 External Inspection

#### 5.1.1 Door Exterior Surface
1. Inspect outer door panel for:
   - Cracks, dents, or deformation
   - Paint or coating damage
   - Corrosion or discoloration
   - Fluid leakage or staining
   - Impact damage

2. Inspect door window:
   - Cracks, crazing, or delamination
   - Optical distortion
   - Seal integrity
   - Mounting security

**Acceptable:** No cracks, minor paint chips acceptable if no corrosion present

**Unacceptable:** Any crack in structure or window, corrosion, fluid leakage

#### 5.1.2 Door Seals (External View)
1. Inspect door perimeter seal:
   - Compression uniformity
   - Surface condition (no cuts, tears, hardening)
   - Attachment security
   - Foreign object debris (FOD) in seal area

2. Check seal contact with door frame:
   - No gaps >0.010" when door closed
   - Uniform compression around perimeter
   - No seal extrusion or rolling

**Acceptable:** Uniform seal contact, minor surface wear acceptable

**Unacceptable:** Cuts, tears, gaps >0.010", hardening, loose attachment

**CAOS Enhancement:** If CAOS tablet connected, review seal pressure data to correlate with visual findings.

#### 5.1.3 Door Frame Interface
1. Inspect door frame contact area:
   - Surface condition (no damage, wear, corrosion)
   - Alignment marks visible and aligned
   - Frame structure integrity

**Acceptable:** Clean contact surface, alignment within marks

**Unacceptable:** Frame damage, misalignment, corrosion

---

### 5.2 Internal Inspection

#### 5.2.1 Door Interior Panel
1. Inspect inner door panel:
   - Surface condition
   - Trim attachment security
   - Access panel security
   - No evidence of moisture intrusion

2. Check emergency release handle:
   - Handle condition and marking
   - Attachment security
   - Clearance for operation
   - Instruction placard legible

**Acceptable:** All items secure, handle functional, placard legible

**Unacceptable:** Loose components, handle obstruction, illegible placard

#### 5.2.2 Latch Mechanisms
1. Inspect all 8 latch assemblies:
   - Visual condition (no wear, cracks, corrosion)
   - Latch pins: no scoring, wear, or deformation
   - Latch engagement indication: proper operation
   - Mounting hardware: secure, torque seal intact

2. Check latch operation:
   - Smooth operation (no binding or sticking)
   - Positive engagement (audible/visual confirmation)
   - Return spring function

**Acceptable:** Smooth operation, positive engagement, no visible wear

**Unacceptable:** Binding, excessive wear, cracks, loose mounting

**CAOS Enhancement:** Compare visual findings with CAOS latch force data.

```
CAOS> SENSOR_DATA latch --all
Latch 1: 285 lbf - NORMAL
Latch 2: 280 lbf - NORMAL
Latch 3: 290 lbf - NORMAL
Latch 4: 275 lbf - NORMAL
Latch 5: 288 lbf - NORMAL
Latch 6: 282 lbf - NORMAL
Latch 7: 286 lbf - NORMAL
Latch 8: 279 lbf - NORMAL
```

#### 5.2.3 Hinge Assemblies
1. Inspect upper and lower hinges:
   - Hinge pins: secure, no wear or corrosion
   - Hinge bushings: no excessive play
   - Lubrication: adequate (light film visible)
   - Mounting hardware: secure, torque seal intact
   - Structure around hinges: no cracks, deformation

2. Check hinge operation:
   - Open and close door slowly
   - Listen for unusual noises
   - Feel for binding or resistance

**Acceptable:** Smooth operation, no play, adequate lubrication

**Unacceptable:** Excessive play, binding, dry hinges, loose hardware

#### 5.2.4 Actuator Assembly
1. Inspect actuator:
   - Visual condition (no damage, leaks, corrosion)
   - Mounting security
   - Electrical connections: secure, no chafing
   - Actuator rod: no bending, scoring

**Acceptable:** Good condition, secure mounting, no leaks

**Unacceptable:** Leakage, damage, loose mounting, electrical issues

#### 5.2.5 Wiring and Sensors
1. Inspect wiring harnesses:
   - Routing: per design, no chafing
   - Support: all tie-wraps secure
   - Condition: no cuts, abrasion, or damage
   - Connectors: secure, no corrosion

2. Check CAOS sensors (visual only):
   - Mounting security
   - Physical condition
   - No visible damage to sensor heads
   - Wiring connections secure

**Acceptable:** All wiring secured, connectors tight, no damage

**Unacceptable:** Chafing, cuts, loose connections, damaged sensors

**CAOS Enhancement:** Perform CAOS self-test to verify all sensors functional.

```
CAOS> SELF_TEST sensors
Testing sensors...
Strain gauges (4): OK
Pressure sensors (6): OK
Temperature sensors (4): OK
Accelerometers (2): OK
Proximity sensors (8): OK
All sensors operational
```

---

### 5.3 Seal Detailed Inspection

#### 5.3.1 Forward Seal
1. Remove door interior access panel at forward seal
2. Inspect seal from interior:
   - Compression: measure with feeler gauge
   - Surface condition: no cuts, hardening
   - Bonding: secure to door
   - Age: check date code (replace if >5 years)

3. Measure seal compression:
   - Nominal: 0.080" - 0.095" compressed
   - Minimum acceptable: 0.075"

**CAOS Correlation:** Review seal pressure data:
```
CAOS> SEAL_DATA forward
Forward seal pressure: 8.9 psi
Effectiveness: 92%
Trend: Stable
Status: NORMAL
```

#### 5.3.2 Aft Seal
1. Inspect aft seal (same procedure as forward seal)
2. **Note:** Aft seal has shown fleet-wide tendency for accelerated degradation
3. Pay special attention to compression and pressure data

**CAOS Correlation:**
```
CAOS> SEAL_DATA aft
Aft seal pressure: 7.8 psi
Effectiveness: 81% ⚠️
Trend: Declining
Status: CAUTION - Schedule detailed inspection
Recommendation: Replace within 100 FH
```

**Action:** If CAOS indicates <85% effectiveness, perform detailed seal measurement and document findings. Consider seal replacement per DMC-*-540A-D.

---

### 5.4 Gap Measurements

1. With door closed and latched, measure gaps:
   - Forward edge: 0.125" ± 0.030"
   - Aft edge: 0.125" ± 0.030"
   - Upper edge: 0.125" ± 0.030"
   - Lower edge: 0.125" ± 0.030"

2. Check step between door and fuselage:
   - Maximum: 0.030" (door proud of fuselage)
   - Acceptable flush to 0.020" recessed

**Acceptable:** Gaps within tolerance, step within limits

**Unacceptable:** Gaps out of tolerance (indicates misrigging)

**Action:** If gaps out of tolerance, refer to DMC-*-540A-D (Adjustment/Rigging)

---

## 6. DISCREPANCY DOCUMENTATION

### 6.1 Recording Findings
For any discrepancies found:
1. Photograph the discrepancy
2. Record in aircraft maintenance log
3. Document in CAOS system (if available)
4. Tag door if unserviceable
5. Notify maintenance control

### 6.2 CAOS Documentation
If CAOS tablet is used:
```
CAOS> LOG_DISCREPANCY
Type: Visual inspection finding
Component: [select from list]
Description: [enter description]
Severity: [INFO/CAUTION/WARNING/CRITICAL]
Action: [required action]
Photo: [attach photo]
Submit to: Maintenance log + Digital twin
```

### 6.3 Corrective Action
- **Minor:** Can be corrected during current inspection
- **Major:** Requires separate work order
- **Critical:** Aircraft unserviceable until corrected

---

## 7. INSPECTION COMPLETION

### 7.1 Final Steps
1. Ensure all access panels reinstalled
2. Remove all tools and equipment
3. Perform operational check if any work performed
4. Update maintenance records
5. Clear any maintenance tags

### 7.2 CAOS Update
If CAOS was used during inspection:
```
CAOS> INSPECTION_COMPLETE 720A
Task: Visual Inspection
Completion date: [auto-filled]
Findings: [summary]
Next due: [calculated]
Digital twin: Updated
Status: Complete
```

### 7.3 Sign-Off
Make the following entry in aircraft maintenance records:

"Accomplished visual inspection of Door L1 Forward per DMC-AMPEL360-A-52-10-01-00A-720A-D. [Discrepancies found and corrected / No discrepancies found / Discrepancies noted in separate work order]. Next due: [date/hours]. Digital twin synchronized."

**Technician Signature:** ________________  
**License Number:** ________________  
**Date:** ________________

---

## 8. REVISION HISTORY

| Issue | Date | Changes | Approved By |
|-------|------|---------|-------------|
| 001 | 2025-11-03 | Initial release | Chief Engineer |

---

**Prepared by:** AMPEL360 Technical Publications  
**Approved by:** Chief Engineer, Airframe Systems  
**Next Review:** 2026-11-03

---

*This data module is part of the S1000D-compliant CAOS-enabled documentation system for AMPEL360 aircraft.*
