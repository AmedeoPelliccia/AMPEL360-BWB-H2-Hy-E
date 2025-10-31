# Safety: 04-50-01 - LH₂ Tank Inner Vessel Life Limit

## 1.0 Safety Classification
- **Safety Effect:** CATASTROPHIC (SAE ARP4761 Level 1)
- **Failure Mode:** Uncontained rupture of pressurized LH₂ tank
- **Hazard Classification:** Flight Critical

## 2.0 Failure Scenarios

### 2.1 Fatigue Crack Propagation Beyond Life Limit
**Event:** Operation of tank beyond 50,000 flight cycles without retirement

**Hazard Chain:**
1. Fatigue crack initiates at high-stress location (dome-cylinder weld)
2. Crack propagates through vessel wall over subsequent flights
3. Through-wall crack causes rapid depressurization
4. LH₂ leak into insulation annulus
5. Potential fire/explosion if ignition source present
6. Loss of propulsion power mid-flight

**Severity:** CATASTROPHIC (aircraft loss possible)

**Probability without Mitigation:** PROBABLE (life limit establishes this threshold)

**Mitigation:**
- **Primary:** Mandatory retirement at 50,000 FC (reduces probability to EXTREMELY IMPROBABLE)
- **Secondary:** Leak detection system provides early warning
- **Tertiary:** Fire suppression system in fuel system compartment

**Residual Risk:** ACCEPTABLE per CS-25.1309 (probability < 10⁻⁹ per flight hour)

### 2.2 Hydrogen Embrittlement Accelerated Failure
**Event:** Material fracture toughness degradation over 20 calendar years

**Hazard Chain:**
1. Long-term H₂ exposure causes atomic hydrogen absorption into Al-Li lattice
2. Fracture toughness (K_IC) degrades below critical threshold
3. Tank becomes susceptible to brittle fracture under normal loads
4. Sudden catastrophic failure without warning

**Severity:** CATASTROPHIC

**Probability without Mitigation:** REMOTE (based on accelerated aging tests)

**Mitigation:**
- **Primary:** 20-year calendar life limit (3× margin on observed degradation)
- **Secondary:** Material qualification testing per ASTM E1820
- **Tertiary:** Service bulletin program for early fleet monitoring

**Residual Risk:** ACCEPTABLE

### 2.3 Thermal Cycle Fatigue Accumulation
**Event:** Exceeding 75,000 thermal cycles due to inadequate tracking

**Hazard Chain:**
1. Repeated cryogenic cycling causes low-cycle fatigue
2. Plastic deformation accumulates at dome radius
3. Ratcheting leads to geometric distortion
4. Stress concentration increases
5. Premature fatigue failure

**Severity:** CATASTROPHIC

**Probability without Mitigation:** REMOTE

**Mitigation:**
- **Primary:** FMS automatic thermal cycle counter
- **Secondary:** Manual logbook tracking requirement
- **Tertiary:** Annual maintenance check of cycle count accuracy

**Residual Risk:** ACCEPTABLE

## 3.0 System Safety Assessment

### 3.1 Fault Tree Analysis (FTA)
**Top Event:** Uncontained LH₂ tank rupture in flight

**Critical Failure Path:**
- Tank operated beyond life limit (P = 10⁻⁶ per flight, assuming compliance monitoring)
- AND Fatigue crack present (P = 1.0 when beyond limit)
- AND Leak detection system failed (P = 10⁻⁴ per flight, dual redundant)
- **Result:** P_top = 10⁻¹⁰ per flight ✓ ACCEPTABLE

### 3.2 Failure Modes and Effects Analysis (FMEA)
**Component:** LH₂ Tank Inner Vessel

| Failure Mode | Effect | Detection | Severity | Occurrence | RPN |
|--------------|--------|-----------|----------|------------|-----|
| Fatigue crack | LH₂ leak | Leak detector | 10 | 1 (with limit) | 10 ✓ |
| Corrosion penetration | LH₂ leak | Visual inspection | 9 | 2 | 18 ✓ |
| Weld defect | LH₂ leak | Pre-service NDT | 10 | 1 | 10 ✓ |
| Overpressure burst | Catastrophic | Relief valve | 10 | 1 | 10 ✓ |

**All RPN < 100:** Design meets safety targets

### 3.3 Common Cause Analysis
**Identified Common Causes:**
1. **Maintenance Error:** Failure to track cycles correctly
   - **Mitigation:** Dual tracking (ACMS + manual logbook)
2. **Design Error:** Incorrect life prediction
   - **Mitigation:** 3× test margin + conservative analysis assumptions
3. **Manufacturing Defect:** Weld quality issue in production fleet
   - **Mitigation:** 100% NDT of critical welds + first article testing

## 4.0 Regulatory Compliance

### 4.1 Applicable Standards
- **CS-25.981:** Fuel tank ignition prevention
- **CS-25.963:** Fuel tank tests
- **CS-25.1309:** Equipment, systems, and installations (safety analysis)
- **CS-25.1529:** Instructions for continued airworthiness
- **SAE ARP4761:** Guidelines for conducting SSA

### 4.2 Certification Credit
Life limit demonstration provides compliance credit for:
- **CS-25.571(a)(3):** Fail-safe evaluation not required for safe-life components
- **CS-25.571(b):** Replacement time established by analysis and testing

## 5.0 Operator Safety Responsibilities

### 5.1 Mandatory Actions
Operators MUST:
1. Track flight cycles and thermal cycles per ATA 45 ACMS procedures
2. Record tank serial number and installation date at each replacement
3. Maintain logbook entries demonstrating continuous compliance
4. Ground aircraft immediately if cycle count exceeds limits
5. Report any detected H₂ leaks to OEM and regulatory authorities within 24 hours

### 5.2 Penalties for Non-Compliance
Operation beyond life limit constitutes **willful violation** of airworthiness regulations:
- Aircraft Certificate of Airworthiness: **REVOKED**
- Operator certificate: Subject to **SUSPENSION**
- Civil penalties: Up to **€4,000/day (EASA)** or **$50,000/violation (FAA)**
- Criminal liability: Possible if results in accident with injuries

## 6.0 Emergency Procedures

### 6.1 In-Flight LH₂ Leak Detected
**Immediate Actions:**
1. Fuel cell system: **SHUTDOWN**
2. LH₂ tank isolation valves: **CLOSE**
3. Cabin depressurization: **INITIATE** (prevent hydrogen accumulation)
4. Emergency descent: **COMMENCE** (land ASAP)
5. Declare emergency with ATC

**Do Not:**
- Attempt to restart fuel cell system
- Delay landing for fuel dumping (risk > benefit)

### 6.2 Post-Landing Procedures
1. Evacuate aircraft immediately
2. Establish 300m safety perimeter
3. Notify fire services of hydrogen leak (specialized equipment required)
4. Do NOT approach aircraft until H₂ concentration < 1% LEL

## 7.0 Lessons Learned Integration

### 7.1 Service Bulletin Monitoring
OEM maintains active monitoring program:
- **Fleet Leader Aircraft:** First 10 production aircraft with enhanced instrumentation
- **Early Inspection:** Tanks removed at 25,000 FC for destructive testing
- **Data Sharing:** Anonymous service data pooled across operators
- **Limit Adjustment:** Life limit may be revised (up or down) based on service experience

### 7.2 Incident Reporting
All events to be reported to OEM Safety Department:
- H₂ leaks (any quantity)
- Vacuum loss events
- Thermal cycle counter anomalies
- Tank damage during maintenance

**Contact:** safety@ampel360.aero (24/7 hotline)
