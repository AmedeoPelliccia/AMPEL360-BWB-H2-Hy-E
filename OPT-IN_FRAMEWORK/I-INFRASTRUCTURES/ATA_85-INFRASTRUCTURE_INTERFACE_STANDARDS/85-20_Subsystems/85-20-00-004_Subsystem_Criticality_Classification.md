# 85-20-00-004 — Subsystem Criticality Classification

## Document Metadata

```yaml
document_id: "85-20-00-004"
title: "Subsystem Criticality Classification"
parent_ata: "ATA 85"
category: "Infrastructure Interface Standards"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-21"
```

## Purpose

This document establishes the safety criticality classification for each ground-aircraft interface subsystem within [ATA 85-20](./85-20-00-001_Subsystems_Overview_and_Architecture.md). Classifications are based on Design Assurance Level (DAL) per [ARP4754A](https://www.sae.org/standards/content/arp4754a/) and [ARP4761](https://www.sae.org/standards/content/arp4761/), considering potential hazards and failure effects on aircraft safety.

## Design Assurance Levels (DAL)

Per ARP4754A, Design Assurance Level (DAL) is assigned based on failure condition severity:

| DAL | Failure Condition | Effect on Aircraft/Crew/Passengers |
|-----|-------------------|-------------------------------------|
| **DAL-A** | Catastrophic | Failure may cause death or multiple fatalities |
| **DAL-B** | Hazardous/Severe-Major | Failure may cause serious injury or significant aircraft damage |
| **DAL-C** | Major | Failure may cause passenger discomfort, significant operational limitations |
| **DAL-D** | Minor | Failure causes minor operational inconvenience |
| **DAL-E** | No Safety Effect | Failure has no impact on safety |

## Subsystem Criticality Summary

| Subsystem | ID | DAL | Primary Hazard | Rationale |
|-----------|-----|-----|----------------|-----------|
| H2 Refueling Interface | 85-20-01 | **A** | H2 fire/explosion | Catastrophic: Uncontrolled H2 release can cause fire/explosion |
| Electrical Power Interface | 85-20-02 | **B** | Electrical fire, shock | Hazardous: High-voltage fault can cause fire or electrocution |
| Passenger Boarding Interface | 85-20-03 | **C** | Passenger fall/injury | Major: Jetway/door failure can cause injuries but not catastrophic |
| Evacuation and Rescue | 85-20-04 | **A** | Impeded evacuation | Catastrophic: Evacuation failure in emergency can cause fatalities |
| Cargo and Servicing | 85-20-05 | **C** | Cargo door failure | Major: Cargo system failure affects operations but unlikely catastrophic |
| Data and Communications | 85-20-06 | **D** | Loss of data link | Minor: Communication loss is inconvenient but not immediately hazardous |
| Stand and Gate Infrastructure | 85-20-07 | **C** | Aircraft/GSE collision | Major: Positioning error can damage aircraft but typically not catastrophic |
| Safety and Monitoring | 85-20-08 | **A** | Undetected H2 leak | Catastrophic: Failure to detect H2 can lead to fire/explosion |
| CO2 Battery Interface | 85-20-09 | **B** | Thermal runaway | Hazardous: Battery fire can cause significant damage and injuries |

## Detailed Criticality Analysis

### 85-20-01: H2 Refueling Interface Subsystem — DAL-A

**Failure Condition Classification:** Catastrophic

**Top-Level Hazards:**
1. **Uncontrolled H2 release during refueling**
   - Failure Effect: H2 accumulation → ignition → fire/explosion
   - Severity: Catastrophic (multiple fatalities, aircraft loss)
   - Likelihood Target: Extremely Improbable (<10⁻⁹ per flight hour)

2. **H2 coupling failure under pressure**
   - Failure Effect: High-velocity H2 jet → ignition source → fire
   - Severity: Catastrophic
   - Likelihood Target: Extremely Improbable

3. **Safety interlock bypass or failure**
   - Failure Effect: Refueling in unsafe conditions → H2 release
   - Severity: Catastrophic
   - Likelihood Target: Extremely Improbable

**Safety Mitigation:**
- Multiple independent H2 leak detection systems (85-20-08)
- Automatic shutoff valves with redundant actuation
- Physical interlocks preventing unsafe operations
- Grounding and bonding to prevent static ignition
- Safety zones and barriers
- Emergency shutdown capability (manual and automatic)

**Development Assurance:**
- Software: DO-178C Level A (if software-controlled)
- Hardware: DO-254 Level A (for critical hardware)
- Safety assessment per ARP4761 (FHA, PSSA, SSA, CCA)
- Qualification testing to failure modes

**References:**
- [85-20-01 H2 Refueling Interface Subsystem](./85-20-01_H2_Refueling_Interface_Subsystem/README.md)
- [ISO 19880-5](https://www.iso.org/standard/71975.html) (H2 refueling safety)

---

### 85-20-02: Electrical Power Interface Subsystem — DAL-B

**Failure Condition Classification:** Hazardous/Severe-Major

**Top-Level Hazards:**
1. **High-voltage fault causing electrical fire**
   - Failure Effect: Fire on aircraft or ground equipment
   - Severity: Hazardous (serious injury, aircraft damage)
   - Likelihood Target: Remote (<10⁻⁵ per flight hour)

2. **Shock hazard to ground crew**
   - Failure Effect: Electrocution from exposed high-voltage
   - Severity: Hazardous (fatality possible)
   - Likelihood Target: Remote

3. **Battery overcharge causing thermal event**
   - Failure Effect: Battery thermal runaway → fire
   - Severity: Hazardous
   - Likelihood Target: Remote

**Safety Mitigation:**
- Ground fault detection and circuit breakers
- Interlocked connectors (cannot disconnect under load)
- Insulation and touch-proof design
- Battery Management System (BMS) monitoring
- Thermal cutoffs and fuses
- Emergency disconnect capability

**Development Assurance:**
- Software: DO-178C Level B
- Hardware: DO-254 Level B
- Safety assessment per ARP4761
- Electrical safety testing per applicable standards

**References:**
- [85-20-02 Electrical Power Interface Subsystem](./85-20-02_Electrical_Power_Interface_Subsystem/README.md)

---

### 85-20-03: Passenger Boarding Interface Subsystem — DAL-C

**Failure Condition Classification:** Major

**Top-Level Hazards:**
1. **Jetway/door misalignment causing fall hazard**
   - Failure Effect: Passenger or crew fall from aircraft door
   - Severity: Major (serious injury possible, but unlikely multiple fatalities)
   - Likelihood Target: Probable (<10⁻³ per flight hour)

2. **Door opening while aircraft moving**
   - Failure Effect: Passenger fall or injury
   - Severity: Major
   - Likelihood Target: Remote

**Safety Mitigation:**
- Visual and physical alignment indicators
- Jetway position sensors and interlocks
- Door arming/disarming procedures
- Ground crew training and visual inspection
- Backup manual controls

**Development Assurance:**
- Software: DO-178C Level C (if applicable)
- Hardware: DO-254 Level C
- Safety assessment per ARP4761

**References:**
- [85-20-03 Passenger Boarding Interface Subsystem](./85-20-03_Passenger_Boarding_Interface_Subsystem/README.md)
- [CS-25.807](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) (Emergency exits)

---

### 85-20-04: Evacuation and Rescue Interface Subsystem — DAL-A

**Failure Condition Classification:** Catastrophic

**Top-Level Hazards:**
1. **Failure to provide emergency egress in time-critical situation**
   - Failure Effect: Passengers unable to evacuate → fatalities in fire/smoke
   - Severity: Catastrophic (multiple fatalities)
   - Likelihood Target: Extremely Improbable (given an emergency event)

2. **ARFF unable to access aircraft for rescue**
   - Failure Effect: Delayed rescue → fatalities
   - Severity: Catastrophic
   - Likelihood Target: Extremely Improbable

**Safety Mitigation:**
- Multiple independent egress paths (slides, doors, rescue access)
- Fail-safe door mechanisms (evacuate mode overrides normal interlocks)
- External emergency controls accessible to ARFF
- Backup power for emergency systems
- Regular inspection and functional testing
- Crew training on emergency procedures

**Development Assurance:**
- Software: DO-178C Level A (for safety-critical automation)
- Hardware: DO-254 Level A
- Safety assessment per ARP4761
- Certification demonstration of evacuation capability

**References:**
- [85-20-04 Evacuation and Rescue Interface Subsystem](./85-20-04_Evacuation_and_Rescue_Interface_Subsystem/README.md)
- [CS-25.803](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) (Emergency evacuation)
- [CS-25.807](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) (Emergency exits)

---

### 85-20-05: Cargo and Servicing Interface Subsystem — DAL-C

**Failure Condition Classification:** Major

**Top-Level Hazards:**
1. **Cargo door opening in flight due to ground interface fault**
   - Failure Effect: Rapid decompression, cargo loss
   - Severity: Major (controlled landing still possible)
   - Likelihood Target: Remote

2. **Contamination of potable water system during servicing**
   - Failure Effect: Passenger illness
   - Severity: Major
   - Likelihood Target: Probable (mitigated by procedures)

**Safety Mitigation:**
- Cargo door locked indication (no dispatch with door unlocked)
- Service connection interlocks and check valves
- Clearly marked and keyed service ports
- Inspection procedures before flight
- Service equipment certification

**Development Assurance:**
- Software: DO-178C Level C
- Hardware: DO-254 Level C
- Safety assessment per ARP4761

**References:**
- [85-20-05 Cargo and Servicing Interface Subsystem](./85-20-05_Cargo_and_Servicing_Interface_Subsystem/README.md)

---

### 85-20-06: Data and Communications Interface Subsystem — DAL-D

**Failure Condition Classification:** Minor

**Top-Level Hazards:**
1. **Loss of ground data link during operations**
   - Failure Effect: Inability to download maintenance data, delay operations
   - Severity: Minor (operational inconvenience)
   - Likelihood Target: Reasonably Probable

2. **Cybersecurity breach via ground data link**
   - Failure Effect: Potential for malicious code upload
   - Severity: Depends on aircraft system affected (can be up to Catastrophic if flight-critical systems compromised)
   - Likelihood Target: Remote (with proper cybersecurity)

**Note:** While data communications itself is DAL-D, **cybersecurity protections must be commensurate with the most critical system accessible via the data link**, potentially requiring DAL-A mitigations.

**Safety Mitigation:**
- Defense-in-depth cybersecurity architecture
- Encryption and authentication per [DO-326A](https://www.rtca.org/content/standards-guidance-materials) / [ED-202A](https://eshop.eurocae.net/eurocae-documents-and-reports/ed-202a/)
- Segregation of flight-critical and non-critical networks
- Intrusion detection and logging
- Regular security audits

**Development Assurance:**
- Software: DO-178C Level D (for data link itself)
- Cybersecurity: Follow DO-326A / ED-202A (threat-based, can require Level A protections)
- Hardware: DO-254 Level D

**References:**
- [85-20-06 Data and Communications Interface Subsystem](./85-20-06_Data_and_Communications_Interface_Subsystem/README.md)
- [DO-326A / ED-202A](https://www.rtca.org/content/standards-guidance-materials) (Airworthiness security process)

---

### 85-20-07: Stand and Gate Infrastructure Subsystem — DAL-C

**Failure Condition Classification:** Major

**Top-Level Hazards:**
1. **Visual guidance system failure causing aircraft collision with GSE or structure**
   - Failure Effect: Aircraft damage, potential injury to ground crew
   - Severity: Major (controlled situation, unlikely catastrophic)
   - Likelihood Target: Probable (mitigated by pilot vigilance and ground crew)

2. **Incorrect stand assignment leading to wing/engine strike**
   - Failure Effect: Aircraft damage
   - Severity: Major
   - Likelihood Target: Remote

**Safety Mitigation:**
- Redundant visual guidance systems
- Ground crew spotters and communication
- Structural clearance indicators and barriers
- Pilot final authority on safe positioning
- Stand compatibility verification

**Development Assurance:**
- Software: DO-178C Level C
- Hardware: DO-254 Level C
- Safety assessment per ARP4761

**References:**
- [85-20-07 Stand and Gate Infrastructure Subsystem](./85-20-07_Stand_and_Gate_Infrastructure_Subsystem/README.md)
- [ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx) (Aerodromes)

---

### 85-20-08: Safety and Monitoring Subsystem — DAL-A

**Failure Condition Classification:** Catastrophic

**Top-Level Hazards:**
1. **Failure to detect H2 leak during refueling**
   - Failure Effect: Undetected H2 accumulation → ignition → fire/explosion
   - Severity: Catastrophic
   - Likelihood Target: Extremely Improbable

2. **False-negative fire detection in critical area**
   - Failure Effect: Undetected fire → catastrophic damage/loss
   - Severity: Catastrophic
   - Likelihood Target: Extremely Improbable

**Rationale for DAL-A:**
The safety monitoring subsystem is a **safety-critical protection layer**. Its failure can allow hazardous conditions to go undetected, leading to catastrophic outcomes. It must be as reliable as the primary systems it monitors.

**Safety Mitigation:**
- Multiple independent sensor systems (dissimilar technology)
- Redundant processing and alerting
- Fail-to-warn state for sensor failures
- Regular functional testing and calibration
- Manual backup procedures (human inspection)

**Development Assurance:**
- Software: DO-178C Level A
- Hardware: DO-254 Level A
- Safety assessment per ARP4761
- Sensor qualification and reliability testing

**References:**
- [85-20-08 Safety and Monitoring Subsystem](./85-20-08_Safety_and_Monitoring_Subsystem/README.md)

---

### 85-20-09: CO2 Battery Interface Subsystem — DAL-B

**Failure Condition Classification:** Hazardous/Severe-Major

**Top-Level Hazards:**
1. **Battery thermal runaway during ground operations**
   - Failure Effect: Battery fire → aircraft damage, injury/fatalities
   - Severity: Hazardous (can be catastrophic if not contained)
   - Likelihood Target: Remote

2. **Battery container mechanical failure during flight**
   - Failure Effect: Loss of electrical power, potential structural damage
   - Severity: Hazardous
   - Likelihood Target: Remote

3. **Incorrect battery installation (reversed polarity, wrong type)**
   - Failure Effect: Electrical system damage, potential fire
   - Severity: Hazardous
   - Likelihood Target: Remote (mitigated by design and procedures)

**Safety Mitigation:**
- Battery Management System (BMS) with thermal monitoring
- Thermal runaway containment design
- Mechanical keying preventing incorrect installation
- Structural design for flight loads
- Emergency battery disconnect
- Fire suppression in battery compartment

**Development Assurance:**
- Software: DO-178C Level B (BMS interface)
- Hardware: DO-254 Level B (high-power electrical)
- Safety assessment per ARP4761
- Battery certification per applicable standards (e.g., RTCA DO-311A for lithium batteries)

**References:**
- [85-20-09 CO2 Battery Interface Subsystem](./85-20-09_CO2_Battery_Interface_Subsystem/README.md)
- [RTCA DO-311A](https://www.rtca.org/content/standards-guidance-materials) (Rechargeable lithium battery systems)

---

## Cross-Subsystem Safety Considerations

### Integrated Hazard Analysis

Some hazards arise only from the interaction of multiple subsystems:

**Example: Concurrent H2 refueling and welding/grinding work**
- Individual subsystems: 85-20-01 (H2 Refueling) and ground maintenance
- Combined hazard: Ignition source near H2 → fire/explosion
- Mitigation: Safety zone enforcement (85-20-08), operational procedures prohibiting incompatible activities

**Integrated Analysis Required:**
- Functional Hazard Assessment (FHA) at system integration level
- Common Cause Analysis (CCA) for shared equipment or utilities
- Particular Risk Analysis (PRA) for novel technologies (H2, high-power batteries)

See: [85-20-00-003_Subsystem_Integration_Approach.md](./85-20-00-003_Subsystem_Integration_Approach.md)

### Common Mode Failures

Systems sharing common elements (e.g., power supply, data bus) must consider common mode failures:

- **Power loss affecting multiple subsystems:** Ground power failure could affect 85-20-01, 85-20-02, 85-20-06, 85-20-08
  - Mitigation: Battery backup for safety-critical functions
  
- **Data bus failure affecting monitoring and control:** Loss of ground data network could affect all subsystems
  - Mitigation: Hard-wired safety interlocks independent of data bus

### Safety Assurance Process

For all DAL-A and DAL-B subsystems:

1. **Functional Hazard Assessment (FHA)** — Identify failure conditions and severity
2. **Preliminary System Safety Assessment (PSSA)** — Allocate safety requirements
3. **System Safety Assessment (SSA)** — Verify safety requirements met
4. **Common Cause Analysis (CCA)** — Identify common mode failures
5. **Compliance Documentation** — Safety assessment reports, test evidence

## Regulatory Compliance

### CS-25.1309 Compliance

[CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) requires that the occurrence of any failure condition be inversely related to its severity:

| Failure Condition | Probability | DAL |
|-------------------|-------------|-----|
| Catastrophic | Extremely Improbable (≤10⁻⁹/FH) | A |
| Hazardous | Remote (≤10⁻⁵/FH) | B |
| Major | Probable (≤10⁻³/FH) | C |
| Minor | Reasonably Probable | D |

Ground interface subsystems must demonstrate compliance through:
- Safety analysis (ARP4761)
- Testing (functional, environmental, reliability)
- Service experience (for mature technologies)

### Certification Plan

Each subsystem requires:
- **Certification Plan** — Scope, approach, milestones
- **Safety Assessment Report** — FHA, PSSA, SSA results
- **Verification and Validation Report** — Test evidence
- **Compliance Matrix** — Requirements to evidence traceability

**Location:** Each subsystem folder, `XX-20-0X-00X_Safety_and_Certification.md`

## Cross-References

- [85-20-00-001 — Subsystems Overview and Architecture](./85-20-00-001_Subsystems_Overview_and_Architecture.md)
- [85-20-00-002 — Subsystem Interface Matrix](./85-20-00-002_Subsystem_Interface_Matrix.md)
- [85-20-00-003 — Subsystem Integration Approach](./85-20-00-003_Subsystem_Integration_Approach.md)
- [ARP4754A](https://www.sae.org/standards/content/arp4754a/) — Development of civil aircraft and systems
- [ARP4761](https://www.sae.org/standards/content/arp4761/) — Safety assessment process

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_.
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-21

---

*Reference: [OPT-IN Framework Documentation Standard](../../../../AMPEL360_DOCUMENTATION_STANDARD.md)*
