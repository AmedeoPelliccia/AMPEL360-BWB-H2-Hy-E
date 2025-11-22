# 85-60-01 — H2 Storage Systems

## System Metadata

```yaml
system_id: "85-60-01"
name: "H2_Storage_Systems"
description: "Ground infrastructure hydrogen storage including liquid H2 tanks, gaseous storage, cryogenic equipment, and pressure management"
parent_ata: "ATA 85"
criticality: "DAL-A"
status: "active"
version: "1.0"
last_updated: "2025-11-22"
```

## Purpose

The H2 Storage Systems provide ground infrastructure for safe, efficient storage and delivery of hydrogen fuel to support aircraft refueling operations for the AMPEL360 BWB-H2-Hy-E aircraft. This system is **safety-critical (DAL-A)** due to the catastrophic consequences of uncontrolled hydrogen release or fire.

## Key Capabilities

- **Liquid H2 Storage:** Cryogenic tanks for bulk LH2 storage at -253°C
- **Gaseous H2 Storage:** High-pressure vessels for compressed H2 (350-700 bar)
- **Cryogenic Equipment:** Vacuum-insulated transfer lines, pumps, and vaporizers
- **Vaporization Systems:** LH2 to gaseous H2 conversion for refueling
- **Pressure Management:** Compression, regulation, and safety relief systems

## Criticality

**Design Assurance Level:** DAL-A (Catastrophic)

**Rationale:** Failure of H2 storage systems can result in:
- Large-scale H2 release (fire or explosion hazard)
- Loss of multiple lives and significant property damage
- Extended airport operational disruption
- Environmental contamination

See: [85-20-00-004_Subsystem_Criticality_Classification.md](../../85-20_Subsystems/85-20-00-004_Subsystem_Criticality_Classification.md)

## System Components

### 1. Liquid H2 Tanks

Cryogenic storage vessels for bulk liquid hydrogen storage.

Document: [85-60-01-001_Liquid_H2_Tanks.md](./85-60-01-001_Liquid_H2_Tanks.md)

**Key Features:**
- Double-wall vacuum-insulated construction
- Typical capacity: 50,000 - 500,000 liters
- Operating pressure: 1-10 bar
- Boil-off management and recovery systems

### 2. Gaseous H2 Storage

High-pressure vessels for compressed hydrogen gas storage.

Document: [85-60-01-002_Gaseous_H2_Storage.md](./85-60-01-002_Gaseous_H2_Storage.md)

**Key Features:**
- Composite overwrapped pressure vessels (COPV)
- Storage pressure: 350-700 bar
- Cascade storage systems for efficient dispensing
- Pressure cycling and fatigue management

### 3. Cryogenic Equipment

Specialized equipment for handling liquid hydrogen at cryogenic temperatures.

Document: [85-60-01-003_Cryogenic_Equipment.md](./85-60-01-003_Cryogenic_Equipment.md)

**Key Features:**
- Vacuum-insulated transfer lines
- Cryogenic pumps and valves
- LH2 level measurement systems
- Thermal management and insulation

### 4. Vaporization Systems

Equipment for converting liquid hydrogen to gaseous hydrogen for aircraft refueling.

Document: [85-60-01-004_Vaporization_Systems.md](./85-60-01-004_Vaporization_Systems.md)

**Key Features:**
- Ambient air vaporizers
- Electric vaporizers (backup)
- Temperature control systems
- Flow rate capacity matching refueling demand

### 5. Pressure Management

Systems for compressing, regulating, and safely managing hydrogen pressure.

Document: [85-60-01-005_Pressure_Management.md](./85-60-01-005_Pressure_Management.md)

**Key Features:**
- High-pressure compressors (multi-stage)
- Pressure regulators and control valves
- Safety relief valves and burst discs
- Pressure monitoring and alarming

## ASSETS

Technical assets for H2 Storage Systems:

### Tank Specifications

- [85-60-01-A-001_Tank_Specifications.csv](./ASSETS/85-60-01-A-001_Tank_Specifications.csv) — LH2 and GH2 tank capacities, materials, and ratings

### Safety Systems

- [85-60-01-A-002_Safety_Systems.md](./ASSETS/85-60-01-A-002_Safety_Systems.md) — Safety instrumented systems, interlocks, and emergency procedures

### Thermal Analysis

- [85-60-01-A-003_Thermal_Analysis.csv](./ASSETS/85-60-01-A-003_Thermal_Analysis.csv) — Heat ingress calculations, boil-off rates, and insulation performance

### Capacity Planning

- [85-60-01-A-004_Capacity_Planning.md](./ASSETS/85-60-01-A-004_Capacity_Planning.md) — Storage capacity sizing, refueling cycle analysis, and demand forecasting

## Integration

### Primary Dependencies

**Internal (ATA 85 Subsystems):**
- [85-20-01 H2 Refueling Interface](../../85-20_Subsystems/85-20-01_H2_Refueling_Interface_Subsystem/README.md) — Delivers H2 from storage to aircraft (Priority 1)
- [85-20-08 Safety and Monitoring](../../85-20_Subsystems/85-20-08_Safety_and_Monitoring_Subsystem/README.md) — H2 detection and safety systems (Priority 1)
- [85-80_Energy](../../85-80_Energy/README.md) — Electrical power for compressors and pumps

**Operational Interfaces:**
- [85-10-02 H2 Ground Operations](../../85-10_Operations/85-10-02_H2_Ground_Operations/README.md) — Refueling operations and procedures
- [85-30_Circularity](../../85-30_Circularity/README.md) — H2 production, delivery logistics, and sustainability

## Safety Requirements

### Hazard Zones

**Zone Classification per [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) and [IEC 60079](https://webstore.iec.ch/publication/628):**

- **Zone 0:** Continuous H2 presence (inside vessels and piping)
- **Zone 1:** Occasional H2 release (near relief valves, vents)
- **Zone 2:** Abnormal H2 release only (general storage area)

### Safety Systems

**Fire Detection and Suppression:**
- Flame detectors (UV/IR)
- Thermal imaging cameras
- Automated water deluge systems (cooling, not fire suppression)
- Foam application for LH2 spills

**H2 Detection:**
- Fixed H2 sensors at critical locations (per [85-20-08](../../85-20_Subsystems/85-20-08_Safety_and_Monitoring_Subsystem/README.md))
- Detection threshold: 0.4% H2 by volume (10% LEL)
- Automatic shutdown on detection

**Emergency Response:**
- Emergency shutdown systems (ESD)
- Pressure relief and flaring systems
- Emergency isolation valves
- Firefighting equipment (ARFF coordination)

### Separation Distances

Per [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) and local regulations:

- **LH2 tanks to occupied buildings:** Minimum 50 meters
- **GH2 storage to ignition sources:** Minimum 25 meters
- **Between H2 storage vessels:** Minimum 3 meters or vessel diameter (whichever is greater)
- **H2 storage to property line:** Per risk assessment and local codes

## Standards and Compliance

### Applicable Standards

- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) — Hydrogen Technologies Code
- [ISO 22734](https://www.iso.org/standard/73573.html) — Hydrogen generators using water electrolysis — Industrial, commercial, and residential applications
- [ISO 16111](https://www.iso.org/standard/76336.html) — Transportable gas storage devices — Hydrogen absorbed in reversible metal hydride
- [ASME BPVC Section VIII](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-viii-division-1-rules-construction-pressure-vessels) — Pressure Vessel Code (for tank design)
- [IEC 60079](https://webstore.iec.ch/publication/628) — Explosive atmospheres (electrical equipment in hazardous areas)
- [EN 13458](https://standards.cencenelec.eu/) — Cryogenic vessels — Static vacuum insulated vessels

### Regulatory Compliance

- [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) (by reference for ground support of CS-25 aircraft)
- Local fire codes and building regulations
- [EU Pressure Equipment Directive (PED) 2014/68/EU](https://single-market-economy.ec.europa.eu/single-market/european-standards/harmonised-standards/pressure-equipment-directive_en)
- National environmental regulations (emissions, discharge)

## Operational Procedures

### Normal Operations

1. **LH2 Delivery and Fill:**
   - Receive LH2 tanker truck
   - Connect transfer hose with vapor return
   - Transfer LH2 to storage tank
   - Monitor fill level and pressure
   - Disconnect and purge transfer lines

2. **Gaseous H2 Production:**
   - Vaporize LH2 to produce GH2
   - Compress GH2 to refueling pressure (350 or 700 bar)
   - Store in cascade system for efficient dispensing
   - Monitor system performance and efficiency

3. **Aircraft Refueling:**
   - Dispense GH2 from cascade storage
   - Maintain target pressure and flow rate
   - Monitor H2 detection and safety systems
   - Log refueling transactions

### Maintenance

**Daily:**
- Visual inspection of tanks and equipment
- Check H2 detection system functionality
- Review safety system status

**Weekly:**
- Inspect pressure relief valves
- Check cryogenic equipment for frost or leaks
- Test emergency shutdown systems

**Monthly:**
- Calibrate H2 sensors
- Inspect insulation integrity
- Review boil-off rates and trends

**Annual:**
- Pressure vessel inspection (per ASME or EN standards)
- Safety valve testing and recertification
- Full system safety assessment

## Training Requirements

### Operations Personnel

- H2 safety fundamentals (8 hours)
- LH2 and GH2 handling procedures (16 hours)
- Emergency response procedures (8 hours with ARFF)
- Recurrent training (annual)

### Maintenance Technicians

- H2 storage system design and operation (16 hours)
- Cryogenic equipment maintenance (16 hours)
- Pressure vessel inspection (per ASME/EN requirements)
- Recurrent training (annual)

### Emergency Responders (ARFF)

- H2 properties and hazards (4 hours)
- H2 fire and leak response tactics (8 hours)
- Storage facility layout and emergency systems (4 hours)
- Joint exercises (quarterly)

## Change Log

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-11-22 | Initial H2 Storage Systems documentation | AI (GitHub Copilot) / Amedeo Pelliccia |

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-22

---

*Reference: [OPT-IN Framework Documentation Standard](../../../../../AMPEL360_DOCUMENTATION_STANDARD.md)*
