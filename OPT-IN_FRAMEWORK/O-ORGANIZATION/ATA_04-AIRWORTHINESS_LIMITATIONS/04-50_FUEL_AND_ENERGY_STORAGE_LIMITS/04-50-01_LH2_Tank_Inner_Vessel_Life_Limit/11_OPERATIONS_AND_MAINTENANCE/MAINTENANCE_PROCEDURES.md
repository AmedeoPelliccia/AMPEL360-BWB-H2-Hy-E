# Operations and Maintenance: 04-50-01 - LH₂ Tank Inner Vessel Life Limit

## 1.0 Operator Responsibilities

### 1.1 Life Limit Tracking
**Mandatory Requirements:**

**Flight Cycle Tracking:**
- Primary system: Aircraft Condition Monitoring System (ACMS)
- Secondary system: Manual logbook entry
- Recording frequency: Each flight
- Verification: Monthly cross-check ACMS vs. logbook

**Thermal Cycle Tracking:**
- Primary system: Fuel Management System (FMS) automatic counter
- Secondary system: Ground crew manual log
- Trigger event: LH₂ level change > 10% tank capacity
- Recording: Each fill/drain operation

**Calendar Time Tracking:**
- Start date: Tank installation date (from serial number plate)
- Recording: Aircraft permanent records
- Verification: Annual maintenance check

### 1.2 Cycle Count Alert System
**ACMS Alert Thresholds:**
- **47,500 FC (95% of limit):** MAINTENANCE ADVISORY
  - Action: Initiate replacement tank procurement
  - Lead time: Typical 6-month delivery for new tank
  
- **49,500 FC (99% of limit):** MAINTENANCE CAUTION
  - Action: Confirm replacement tank delivery schedule
  - Action: Plan aircraft downtime for tank swap
  
- **50,000 FC (limit reached):** MAINTENANCE WARNING + ENGINE START INHIBIT
  - Action: Ground aircraft immediately
  - Action: Schedule tank replacement within 30 days

**Thermal Cycle Alert:**
- **71,250 TC (95% of limit):** MAINTENANCE ADVISORY
- **75,000 TC (limit reached):** MAINTENANCE WARNING
  - Note: Also inhibits engine start

**Calendar Alert:**
- **19 years (95% of limit):** Annual inspection flag
- **20 years (limit reached):** Certificate of Airworthiness suspended

### 1.3 Pre-Flight Checks
**Daily Inspection (by Flight Crew):**
- Verify ACMS cycle count display functional
- Check for H₂ leak indication (LED indicator on cockpit panel)
- Confirm vacuum pressure within limits (< 1×10⁻³ torr)
- Review maintenance logbook for deferred items related to fuel system

**Pre-Flight Procedure:**
```
1. Power on ACMS
2. Select FUEL SYSTEM page on MFD
3. Verify:
   - Flight cycles: [Current count] / 50,000
   - Thermal cycles: [Current count] / 75,000
   - Calendar time: [Years.Months] / 20.0
   - Tank S/N: [Verify matches logbook]
4. Check status:
   - Green: Normal operation authorized
   - Amber: Approaching limit, advisory message
   - Red: Limit exceeded, NO-GO for flight
```

## 2.0 Maintenance Procedures

### 2.1 Routine Inspections
**A-Check (500 FH or 3 months):**
- Visual inspection: External tank surface for damage
- Leak check: H₂ detector survey around fittings
- Vacuum pressure: Record reading in maintenance log
- Cycle count verification: ACMS vs. logbook reconciliation

**C-Check (6,000 FH or 24 months):**
- All A-Check items PLUS:
- Insulation panel removal: Detailed visual inspection of tank surface
- NDT (if damage suspected): Ultrasonic thickness measurement
- Support lug inspection: Check for cracks, corrosion
- H₂ leak detector calibration check

**Major Check (12,000 FH or 60 months):**
- All C-Check items PLUS:
- Tank support structure detailed inspection
- Piping connection torque check
- Vacuum pump down test (if vacuum degraded)
- ACMS software version verification

### 2.2 Tank Removal Procedure
**AMM Task:** 28-11-00-400-801  
**Duration:** 16 man-hours (2 mechanics, 8 hours)  
**Special Equipment Required:**
- Overhead crane (5-ton capacity)
- Tank lifting sling (P/N AMPEL-TOOL-28-001)
- H₂ gas detector (portable, calibrated)
- GN₂ purge cart (with flow meter)
- Personal protective equipment (PPE): Cryogenic gloves, face shield, insulated coveralls

**Step-by-Step Procedure:**
1. **Safety Preparation:**
   - Establish 10m exclusion zone
   - Post "CRYOGENIC HAZARD" signs
   - Ensure fire extinguishers available (Class D for metal fires)
   - Verify GN₂ supply available (minimum 500 liters liquid)

2. **H₂ Drain:**
   - Connect vent line to flare stack
   - Open drain valve (slowly to prevent pressure surge)
   - Monitor H₂ concentration (target: < 100 ppm in work area)
   - Duration: Approximately 2 hours for full drain + warm-up

3. **GN₂ Purge:**
   - Close drain valve, connect GN₂ supply
   - Purge at 2 bar pressure, 50 liters/min flow rate
   - Sample internal atmosphere: Target O₂ < 2% (explosion prevention)
   - Continue purge until 3 consecutive samples meet criteria

4. **Disconnect Utilities:**
   - Electrical: Disconnect sensor harnesses (8 connectors)
   - Mechanical: Remove piping (fill/drain, vent, fuel feed)
   - Support lugs: Remove 16× M20 bolts (torque wrench required for reinstall)

5. **Tank Removal:**
   - Attach lifting sling to 4 lift points on tank
   - Hoist slowly (max 10 cm/min) to clear support structure
   - Translate forward out of fuselage (via cargo door)
   - Lower onto transport cradle

6. **Post-Removal:**
   - Cap all openings (prevent moisture ingress)
   - Attach "REMOVED FROM SERVICE" tag with aircraft data
   - Record tank S/N, FC, TC, and CY in logbook
   - Prepare shipping documentation for OEM facility

### 2.3 Tank Installation Procedure
**AMM Task:** 28-11-00-400-802  
**Duration:** 20 man-hours (includes leak test)

**Step-by-Step Procedure:**
1. **Receiving Inspection:**
   - Verify tank S/N matches shipping documentation
   - Check for shipping damage (visual + dye penetrant if suspect)
   - Verify zero-time certificate from OEM
   - Confirm calibration stickers on sensors

2. **Pre-Installation:**
   - Remove protective caps
   - Lubricate support lug bearings (MIL-PRF-81322 grease)
   - Install new gaskets at all piping connections

3. **Tank Installation:**
   - Hoist tank into position (reverse of removal)
   - Align support lugs with fuselage attachment points
   - Install and torque bolts: 245 Nm ± 10 Nm (M20 Grade 12.9)
   - Verify spherical bearing free rotation (no binding)

4. **Connect Utilities:**
   - Piping connections: Torque per AMM torque table
   - Electrical harnesses: 8 connectors (ensure locking clips engaged)
   - Support ground strap: Resistance < 2.5 milliohms

5. **System Checkout:**
   - Vacuum integrity test: Achieve < 1×10⁻⁵ torr
   - Pressure test: 6.6 bar (1.2× design) hold 5 minutes, zero decay
   - Leak test: Helium mass spectrometer (1×10⁻⁹ atm·cc/s sensitivity)
   - Sensor functional test: Verify all readings on ACMS

6. **Documentation:**
   - Logbook entry: "LH₂ tank P/N 28-100-001, S/N [XXX], installed. Zero-time entry. Complies with ALS 04-50-01."
   - ACMS cycle counter: Reset to 0 FC and 0 TC
   - Permanent record: Update tank S/N and installation date
   - Form 1 (Maintenance Release): Certify installation per AMM

### 2.4 Troubleshooting Common Issues

**Issue: Vacuum Pressure Exceeds 1×10⁻³ torr**
- **Cause:** Micro-leak in inner vessel or vacuum port seal
- **Action:** Refer to AMM Task 28-21-00-710-002 (Vacuum System Troubleshooting)
- **Disposition:** If cannot restore vacuum to spec, remove tank within 50 FH

**Issue: H₂ Leak Detected (> 100 ppm concentration)**
- **Cause:** Fitting loose, gasket failure, or vessel wall penetration
- **Action:** IMMEDIATE - Shutdown fuel system, evacuate H₂
- **Disposition:** Investigate leak source. If vessel wall leak, retire tank immediately.

**Issue: ACMS Cycle Count Discrepancy**
- **Cause:** Software glitch, power interruption, or data corruption
- **Action:** Refer to AMM Task 45-31-02-860-001 (ACMS Data Recovery)
- **Disposition:** Use manual logbook as source of truth, reprogram ACMS

**Issue: Thermal Cycle Counter Not Incrementing**
- **Cause:** FMS software bug or level sensor failure
- **Action:** Manual increment procedure per AMM Task 28-31-05-850-001
- **Disposition:** Report to OEM, incorporate Service Bulletin fix

## 3.0 Retired Tank Disposition

### 3.1 Shipping to OEM
**Procedure:** AMPEL-PROC-SHIP-H2-TANK-001

**Packaging Requirements:**
- Custom shipping cradle (P/N AMPEL-SHIP-28-001)
- Over-pack container (UN4G certified for cryogenic vessels)
- Inert atmosphere (GN₂ purge bag)
- Desiccant packs (prevent moisture ingress)
- Shock indicators (monitor shipping damage)

**Shipping Documentation:**
- Bill of lading
- Material Safety Data Sheet (MSDS) for residual H₂
- Tank removal report (FC, TC, CY, reason for removal)
- Maintenance history (copy of logbook entries)

**Transport Mode:**
- Ground transport: Hazmat-certified carrier
- Air transport: NOT PERMITTED (IATA DGR restriction)

### 3.2 OEM Teardown Analysis
**Purpose:** Validate life prediction models and identify unexpected degradation

**Inspection Program:**
1. External visual inspection (document all damage)
2. Radiographic inspection (100% coverage of welds)
3. Section cuts (12 locations for metallurgical analysis)
4. Fractography (if cracks found)
5. Material property testing (tensile, toughness, hardness)
6. Weld quality evaluation (microstructure, grain size)

**Data Feedback:**
- Findings incorporated into design improvements
- Life limit revision if warranted by data
- Service bulletin issued if fleet action required

## 4.0 Logbook Entries

### 4.1 Standard Entry Format

**At Tank Installation:**
```
Date: [YYYY-MM-DD]
Aircraft S/N: [XXX]
Work Performed: Installation of LH₂ tank inner vessel
Part Number: 28-100-001
Serial Number: [XXX]
Date of Manufacture: [YYYY-MM-DD]
Cycle Count: 0 FC, 0 TC
Life Limit: 50,000 FC or 20 CY or 75,000 TC, whichever first
Reference: ALS Section 04-50-01, AMM Task 28-11-00-400-802
Certification: This work complies with approved data and is safe for flight.
Signature: [Certifying Mechanic], License [XXX]
```

**At Tank Removal:**
```
Date: [YYYY-MM-DD]
Aircraft S/N: [XXX]
Work Performed: Removal of LH₂ tank inner vessel at life limit
Part Number: 28-100-001
Serial Number: [XXX]
Removal Reason: LIFE LIMIT REACHED
Cycle Count: [XX,XXX] FC, [XX,XXX] TC, [XX.X] CY
Disposition: Shipped to OEM for teardown analysis
Reference: ALS Section 04-50-01, AMM Task 28-11-00-400-801
Signature: [Certifying Mechanic], License [XXX]
```

### 4.2 Audit Trail
**Records Retention:**
- Aircraft logbook: Permanent (lifetime + 20 years)
- Maintenance records: 5 years after component removal
- Tank teardown report: Permanent (engineering archive)

**Regulatory Inspection:**
- Authority: EASA or FAA inspector may audit at any time
- Compliance verification: Cycle counts, installation dates, logbook entries
- Penalty for discrepancies: Possible grounding of aircraft

## 5.0 Training Requirements

### 5.1 Maintenance Personnel
**Course:** AMPEL-TRAIN-H2-SYS-001 (40 hours)

**Curriculum:**
- H₂ safety and hazards
- Cryogenic system handling
- Tank removal/installation procedures
- Leak detection and testing
- Logbook documentation
- Emergency procedures

**Certification:** Valid 2 years, recurrent training required

### 5.2 Flight Crew
**Course:** AMPEL-TRAIN-PILOT-H2-001 (8 hours)

**Curriculum:**
- H₂ fuel system overview
- ACMS cycle count monitoring
- Pre-flight checks
- In-flight H₂ leak procedures
- Emergency landing considerations

**Certification:** Initial + annual recurrent

## 6.0 Compliance Auditing

**Operator Self-Audit:** Quarterly review of cycle tracking accuracy

**Regulatory Audit:** Annual inspection by airworthiness authority

**OEM Fleet Audit:** Continuous monitoring via ACMS data link (if equipped)

**Non-Compliance Reporting:** Mandatory 24-hour notification to authority if limit exceeded
