# Overview: 04-50-01 - LH₂ Tank Inner Vessel Life Limit

## 1.0 Purpose
This component establishes the **mandatory retirement life** for the AMPEL360's cryogenic liquid hydrogen (LH₂) storage tank inner pressure vessel. This is a **SAFE-LIFE component** - operation beyond the specified limit is prohibited.

## 2.0 Limitation Statement

### 2.1 Primary Limit
**RETIRE FROM SERVICE: 50,000 flight cycles OR 20 calendar years, whichever occurs first.**

### 2.2 Supplementary Limits
- **Thermal Cycles:** Maximum 75,000 thermal cycles (cryogenic fill/drain operations)
- **Vacuum Integrity:** If vacuum pressure in annular space exceeds 10⁻³ torr, vessel must be removed for inspection regardless of cycle count
- **Leak Detection:** Any detected hydrogen permeation through inner vessel wall mandates immediate retirement

## 3.0 Rationale

### 3.1 Fatigue Life
The inner vessel is constructed from **Al-Li 2195 alloy** optimized for cryogenic service. Fatigue testing demonstrates:
- **Full-Scale Test Article:** Achieved 150,000 simulated pressure cycles (3× design life)
- **Scatter Factor:** 3.0 applied to test life per FAA AC 23.573-1C
- **Design Service Goal (DSG):** 50,000 cycles established with adequate margin

### 3.2 Thermal Cycling
Each cryogenic fill/drain cycle imposes thermal stress equivalent to 0.67 flight cycles:
- **Temperature Differential:** 20°C (ambient) to -253°C (LH₂)
- **Thermal Strain:** Induces plastic deformation at tank dome radius transitions
- **Cumulative Damage:** Linear accumulation per Palmgren-Miner rule

### 3.3 Environmental Degradation
- **Hydrogen Embrittlement:** Extended exposure to LH₂ reduces fracture toughness
- **Corrosion:** Internal surface protected by anodic coating (MIL-A-8625 Type II), but long-term moisture ingress risk exists
- **Micrometeoroid/Orbital Debris:** Not applicable (suborbital aircraft), but ground handling damage accumulation tracked

## 4.0 Substantiation

### 4.1 Analysis
**Document ID:** AMPEL-STRESS-H2-TANK-001  
**Method:** Finite Element Analysis (FEA) with thermal-structural coupling  
**Software:** ANSYS Mechanical 2024 R1  
**Result:** Maximum von Mises stress = 285 MPa (σ_yield = 420 MPa at -253°C, SF = 1.47)

### 4.2 Testing
**Test Campaign:** AMPEL-TEST-H2-TANK-FSFT  
**Facility:** NASA White Sands Test Facility, Stand 450  
**Specimen:** Full-scale LH₂ tank prototype (P/N 28-100-001)  
**Test Spectrum:** AMPEL360 design mission profile (150,000 cycles @ 1.25× design pressure)  
**Failure Mode:** Fatigue crack initiation at dome-cylinder weld at cycle 147,350

### 4.3 Certification Basis
- **CS-25.981(b):** Fuel tank ignition prevention (H₂ adapted criteria)
- **CS-25.963:** Fuel tank tests (pressure, thermal, vibration)
- **EASA SC-Hydrogen Section 4.2:** Cryogenic tank structural integrity
- **NASA-STD-5001B:** Structural design and test factors for spaceflight hardware (adapted for aviation)

## 5.0 Compliance Tracking

### 5.1 Cycle Counting
- **Flight Cycles:** Recorded by ACMS (Aircraft Condition Monitoring System) per ATA 45
- **Thermal Cycles:** Logged by FMS (Fuel Management System) via cryogenic level sensor state changes
- **Manual Override:** Flight crew can manually increment thermal cycle counter for ground servicing events

### 5.2 Inspection Requirements
**NOT APPLICABLE:** This is a safe-life component. No inspection can restore its service life. Compliance is purely cycle-counting based.

### 5.3 Retirement Process
When limit is reached:
1. **Remove tank assembly** per AMM Task 28-11-00-400-801
2. **Drain residual H₂** per AMM Task 28-12-00-400-001 (controlled venting to flare stack)
3. **Purge with GN₂** until O₂ content < 2% (explosion hazard mitigation)
4. **Ship to OEM facility** for material analysis and lessons-learned program
5. **Install replacement tank** with zero-time logbook entry

## 6.0 Interfaces
- **ATA 05-21-01:** Scheduled replacement task at life limit
- **ATA 28-10-00:** H₂ fuel storage system description
- **ATA 45-31-02:** ACMS cycle counting configuration
- **ATA 12-31-05:** LH₂ tank servicing procedures (thermal cycle tracking)
