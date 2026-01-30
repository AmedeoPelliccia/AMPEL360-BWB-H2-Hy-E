# ATA 24 — Electrical Power
## SNS Structure Index

**ATA Chapter**: 24 — ELECTRICAL POWER  
**Standard**: ATA iSpec 2200 Standard Numbering System  
**S1000D**: Issue 5.0 Compliant  
**Project**: AMPEL360-AIR-T  
**Model**: BWB-H2-Hy-E (Hydrogen-Electric)

---

## Document Overview

This index provides a complete navigation structure for ATA Chapter 24 (Electrical Power) organized according to the ATA iSpec 2200 Standard Numbering System with S1000D CSDB publication management.

---

## Section Structure

### 24-00 — Electrical Power General

General system overview, architecture philosophy, and program-specific deltas for hydrogen-electric propulsion.

| Subject | Description | Path |
|---------|-------------|------|
| 24-00-00 | Chapter overview | `24-00-electrical-power-general/24-00-00-chapter-overview/` |
| 24-00-01 | Scope & boundaries (ATA 24 vs ATA 21/28/45/46) | `24-00-electrical-power-general/24-00-01-scope-boundaries/` |
| 24-00-02 | Electrical architecture overview (AC/LVDC/HVDC) | `24-00-electrical-power-general/24-00-02-electrical-architecture-overview/` |
| 24-00-03 | Power quality & limits (voltage/frequency/ripple/THD) | `24-00-electrical-power-general/24-00-03-power-quality-and-limits/` |
| 24-00-04 | Load classification (essential / shed / nonessential) | `24-00-electrical-power-general/24-00-04-load-classification/` |
| 24-00-05 | Redundancy & dispatch philosophy (fail-op/fail-safe) | `24-00-electrical-power-general/24-00-05-redundancy-and-dispatch-philosophy/` |
| 24-00-06 | Interfaces & dependencies (fuel cells, batteries, converters) | `24-00-electrical-power-general/24-00-06-interfaces-and-dependencies/` |
| 24-00-07 | Monitoring & BITE overview | `24-00-electrical-power-general/24-00-07-monitoring-and-bite-overview/` |
| 24-00-08 | Safety & compliance basis (arc fault / HV hazards) | `24-00-electrical-power-general/24-00-08-safety-and-compliance-basis/` |
| 24-00-10 | Verification strategy (analysis/test/inspection) | `24-00-electrical-power-general/24-00-10-verification-strategy/` |
| 24-00-90 | **Program Delta**: Fuel-cell transient constraints & buffering | `24-00-electrical-power-general/24-00-90-fuel-cell-transients-and-buffering-program-delta/` |
| 24-00-91 | **Program Delta**: HV architecture & EMI environment | `24-00-electrical-power-general/24-00-91-hv-architecture-and-emi-program-delta/` |
| 24-00-92 | **Program Delta**: Thermal/power derating coordination | `24-00-electrical-power-general/24-00-92-thermal-derating-coordination-program-delta/` |

---

### 24-10 — Generator Drive

Mechanical/electromechanical drive chain producing generator shaft power (motor-generator coupling, gearboxes, turbogenerators).

| Subject | Description | Path |
|---------|-------------|------|
| 24-10-00 | Generator drive overview | `24-10-generator-drive/24-10-00-generator-drive-overview/` |
| 24-10-01 | Drive architecture & variants (IDG/CSD, starter-generator, MG sets) | `24-10-generator-drive/24-10-01-drive-architecture-and-variants/` |
| 24-10-02 | Mechanical interfaces (mounts, shafts, gear trains) | `24-10-generator-drive/24-10-02-mechanical-interfaces/` |
| 24-10-03 | Control & regulation interface (speed control, enable/inhibit) | `24-10-generator-drive/24-10-03-control-and-regulation-interface/` |
| 24-10-04 | Cooling/lubrication interfaces | `24-10-generator-drive/24-10-04-cooling-and-lubrication-interfaces/` |
| 24-10-05 | Monitoring & protections (overspeed, overtemp, vibration) | `24-10-generator-drive/24-10-05-monitoring-and-protections/` |
| 24-10-06 | Maintenance & inspection tasks (service limits, wear indicators) | `24-10-generator-drive/24-10-06-maintenance-and-inspection/` |
| 24-10-10 | Verification & qualification (env, endurance, fault injection) | `24-10-generator-drive/24-10-10-verification-and-qualification/` |
| 24-10-90 | **Program Delta**: Electric MG transient torque limits / regen constraints | `24-10-generator-drive/24-10-90-electric-mg-transient-limits-program-delta/` |

---

### 24-20 — AC Generation

AC generation sources and conditioning (variable frequency, constant frequency, inverter-based AC).

| Subject | Description | Path |
|---------|-------------|------|
| 24-20-00 | AC generation overview | `24-20-ac-generation/24-20-00-ac-generation-overview/` |
| 24-20-01 | AC sources (main, APU/aux, emergency) | `24-20-ac-generation/24-20-01-ac-sources/` |
| 24-20-02 | Regulation & control (voltage/frequency control) | `24-20-ac-generation/24-20-02-regulation-and-control/` |
| 24-20-03 | Paralleling / transfer logic | `24-20-ac-generation/24-20-03-paralleling-and-transfer-logic/` |
| 24-20-04 | AC power quality (harmonics, transients, ride-through) | `24-20-ac-generation/24-20-04-ac-power-quality/` |
| 24-20-05 | Protections (OV/UV/OF/UF, differential, ground fault) | `24-20-ac-generation/24-20-05-protections/` |
| 24-20-07 | BITE & fault isolation | `24-20-ac-generation/24-20-07-bite-and-fault-isolation/` |
| 24-20-10 | Verification (power quality, load steps, EMC tests) | `24-20-ac-generation/24-20-10-verification-and-validation/` |
| 24-20-90 | **Program Delta**: Inverter-dominated grid stability (AC microgrid) | `24-20-ac-generation/24-20-90-inverter-dominated-grid-stability-program-delta/` |

---

### 24-30 — DC Generation

DC generation and conversion chain (rectifiers, DC/DC, HVDC buses, battery charging, fuel cell DC coupling).

| Subject | Description | Path |
|---------|-------------|------|
| 24-30-00 | DC generation overview | `24-30-dc-generation/24-30-00-dc-generation-overview/` |
| 24-30-01 | DC sources (fuel cell stacks, rectified AC, batteries) | `24-30-dc-generation/24-30-01-dc-sources/` |
| 24-30-02 | Conversion stages (rectification, DC/DC, isolation) | `24-30-dc-generation/24-30-02-conversion-stages/` |
| 24-30-03 | Battery charging & energy buffering control | `24-30-dc-generation/24-30-03-battery-charging-and-buffering-control/` |
| 24-30-04 | DC quality (ripple, transients, stability) | `24-30-dc-generation/24-30-04-dc-quality/` |
| 24-30-05 | Protections (OV/UV/OC, arc fault, insulation monitoring) | `24-30-dc-generation/24-30-05-protections/` |
| 24-30-07 | BITE & diagnostics | `24-30-dc-generation/24-30-07-bite-and-diagnostics/` |
| 24-30-10 | Verification (bus stability, load steps, thermal, EMC) | `24-30-dc-generation/24-30-10-verification-and-validation/` |
| 24-30-90 | **Program Delta**: HVDC insulation monitoring & fault containment | `24-30-dc-generation/24-30-90-hvdc-insulation-monitoring-program-delta/` |

---

### 24-40 — External Power

Ground power interfaces (AC and/or DC), connectors, interlocks, contactors, acceptance limits.

| Subject | Description | Path |
|---------|-------------|------|
| 24-40-00 | External power overview | `24-40-external-power/24-40-00-external-power-overview/` |
| 24-40-01 | Interfaces & connectors (ratings, pinouts, interlocks) | `24-40-external-power/24-40-01-interfaces-and-connectors/` |
| 24-40-02 | Acceptance criteria (voltage/frequency/phase/quality) | `24-40-external-power/24-40-02-acceptance-criteria/` |
| 24-40-03 | Switching & contactors (EPC, bus tie behavior) | `24-40-external-power/24-40-03-switching-and-contactors/` |
| 24-40-04 | Ground safety & HV protocols (procedures, lockout/tagout) | `24-40-external-power/24-40-04-ground-safety-and-hv-protocols/` |
| 24-40-07 | Monitoring & BITE | `24-40-external-power/24-40-07-monitoring-and-bite/` |
| 24-40-10 | Verification (interop tests, fault cases, safety tests) | `24-40-external-power/24-40-10-verification-and-validation/` |
| 24-40-90 | **Program Delta**: DC fast-charge / high-power ground service | `24-40-external-power/24-40-90-dc-fast-charge-ground-service-program-delta/` |

---

### 24-50 — AC Electrical Load Distribution

AC bus architecture, contactors, bus ties, load shedding, essential bus rules.

| Subject | Description | Path |
|---------|-------------|------|
| 24-50-00 | AC distribution overview | `24-50-ac-electrical-load-distribution/24-50-00-ac-distribution-overview/` |
| 24-50-01 | Bus topology (main/essential/ground/service buses) | `24-50-ac-electrical-load-distribution/24-50-01-bus-topology/` |
| 24-50-02 | Switching logic (bus ties, transfer, split bus strategy) | `24-50-ac-electrical-load-distribution/24-50-02-switching-logic/` |
| 24-50-03 | Load management & shedding (priorities, sequences) | `24-50-ac-electrical-load-distribution/24-50-03-load-management-and-shedding/` |
| 24-50-04 | Circuit protection & coordination (AC breakers/relays) | `24-50-ac-electrical-load-distribution/24-50-04-circuit-protection-and-coordination/` |
| 24-50-07 | Monitoring, metering & BITE | `24-50-ac-electrical-load-distribution/24-50-07-monitoring-metering-and-bite/` |
| 24-50-10 | Verification (shedding logic, selectivity, fault clearing) | `24-50-ac-electrical-load-distribution/24-50-10-verification-and-validation/` |

---

### 24-60 — DC Electrical Load Distribution

DC buses (LVDC/HVDC), distribution units, contactors/SSPCs, insulation monitoring, fault containment.

| Subject | Description | Path |
|---------|-------------|------|
| 24-60-00 | DC distribution overview | `24-60-dc-electrical-load-distribution/24-60-00-dc-distribution-overview/` |
| 24-60-01 | DC bus topology (HVDC/LVDC/essential/emergency) | `24-60-dc-electrical-load-distribution/24-60-01-dc-bus-topology/` |
| 24-60-02 | Switching devices (contactors/SSPCs) and control | `24-60-dc-electrical-load-distribution/24-60-02-switching-devices-and-control/` |
| 24-60-03 | Load management & shedding (priorities, brownout strategy) | `24-60-dc-electrical-load-distribution/24-60-03-load-management-and-shedding/` |
| 24-60-04 | Protections & selectivity (arc fault, OC, IMD integration) | `24-60-dc-electrical-load-distribution/24-60-04-protections-and-selectivity/` |
| 24-60-05 | Grounding/return paths and bonding considerations | `24-60-dc-electrical-load-distribution/24-60-05-grounding-return-paths-and-bonding/` |
| 24-60-07 | Monitoring, metering & BITE | `24-60-dc-electrical-load-distribution/24-60-07-monitoring-metering-and-bite/` |
| 24-60-10 | Verification (fault clearing, IMD tests, brownout recovery) | `24-60-dc-electrical-load-distribution/24-60-10-verification-and-validation/` |

---

### 24-70 — Primary & Secondary Power

Emergency/standby/secondary sources and essential distribution strategy (batteries, emergency generation, keep-alive architecture).

| Subject | Description | Path |
|---------|-------------|------|
| 24-70-00 | Primary/secondary power overview | `24-70-primary-and-secondary-power/24-70-00-primary-secondary-power-overview/` |
| 24-70-01 | Emergency/standby sources (battery-only, aux gen, etc.) | `24-70-primary-and-secondary-power/24-70-01-emergency-standby-sources/` |
| 24-70-02 | Essential power architecture (essential bus feeding rules) | `24-70-primary-and-secondary-power/24-70-02-essential-power-architecture/` |
| 24-70-03 | Automatic reconfiguration logic (loss of source scenarios) | `24-70-primary-and-secondary-power/24-70-03-automatic-reconfiguration-logic/` |
| 24-70-04 | Endurance/energy budgeting (time-on-essential loads) | `24-70-primary-and-secondary-power/24-70-04-endurance-and-energy-budgeting/` |
| 24-70-07 | Monitoring & BITE | `24-70-primary-and-secondary-power/24-70-07-monitoring-and-bite/` |
| 24-70-10 | Verification (endurance, failure cases, dispatch rules) | `24-70-primary-and-secondary-power/24-70-10-verification-and-validation/` |

---

## Total Subjects by Section

- **24-00**: 13 subjects (including 3 program deltas)
- **24-10**: 9 subjects (including 1 program delta)
- **24-20**: 9 subjects (including 1 program delta)
- **24-30**: 9 subjects (including 1 program delta)
- **24-40**: 8 subjects (including 1 program delta)
- **24-50**: 7 subjects
- **24-60**: 8 subjects
- **24-70**: 7 subjects

**Total**: 70 subjects across 8 sections

---

## Structure Organization

Each subject directory contains:
- **SSOT/**: Single Source of Truth (master content repository)
- **PUB/AMM/**: Aircraft Maintenance Manual publication view
  - CSDB/: S1000D Common Source Database
  - bindings.csv: Publication module bindings
  - csdb.profile.yaml: CSDB profile configuration
- **PUB/IPC/**: Illustrated Parts Catalog publication view
  - (same structure as AMM)

---

## Program-Specific Deltas

The AMPEL360 hydrogen-electric architecture introduces unique challenges addressed in dedicated program delta subjects:

1. **Fuel Cell Integration** (24-00-90): Transient power response and battery buffering
2. **High-Voltage Systems** (24-00-91): HVDC buses, insulation, and EMI management
3. **Thermal Management** (24-00-92): Coordinated power and thermal derating
4. **Electric Motor-Generators** (24-10-90): Regenerative braking and transient limits
5. **Inverter Stability** (24-20-90): AC microgrid behavior and grid-forming control
6. **HVDC Safety** (24-30-90): Insulation monitoring and fault containment
7. **Ground Fast-Charging** (24-40-90): High-power DC charging interfaces

---

## Cross-References

### Related ATA Chapters
- **ATA 21**: Air Conditioning (ECS power loads)
- **ATA 28**: Fuel (H₂ fuel cell interfaces)
- **ATA 45**: Central Maintenance System (BITE integration)
- **ATA 46**: Information Systems (power distribution monitoring)

### Related OPT-IN Framework Sections
- **24-00_GENERAL**: Lifecycle development documentation
- **24-20_Subsystems**: Functional subsystem design details
- **24-40_Software**: Power management control algorithms
- **24-80_Energy**: Energy storage and management systems

---

## References

1. **ATA iSpec 2200 Extract**: [Standard Numbering System](https://publications.airlines.org/products/ispec-2200-extract-ata-standard-numbering-system-revision-2024-1)
2. **ATA 100 Overview**: [Wikipedia](https://en.wikipedia.org/wiki/ATA_100)
3. **ATA Chapters Reference**: [ITLIMS ZSIS](https://itlims-zsis.meil.pw.edu.pl/pomoce/ESL/2016/ATA_Chapters.pdf)
4. **ATA Chapter Guide**: [Todd Heffley Blog](https://toddheffley.com/wordpress/?p=5760)
5. **S1000D Specification**: International specification for technical publications

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Type** | SNS Structure Index |
| **ATA Chapter** | 24 — Electrical Power |
| **Standard** | ATA iSpec 2200 SNS / S1000D Issue 5.0 |
| **Project** | AMPEL360-AIR-T |
| **Model** | BWB-H2-Hy-E |
| **Status** | Active |
| **Version** | 1.0 |
| **Created** | 2026-01-09 |
| **Generated with** | AI assistance (GitHub Copilot), prompted by Amedeo Pelliccia |
| **Repository** | github.com/AmedeoPelliccia/AMPEL360-AIR-T |

---

## Navigation

- **Up**: [ATA 24 README](./README.md)
- **Parent**: [E2-ENERGY](../)
- **Root**: [OPT-IN Framework](../../../../)

---

*For questions or updates to this index, contact the AMPEL360 Documentation Working Group.*
