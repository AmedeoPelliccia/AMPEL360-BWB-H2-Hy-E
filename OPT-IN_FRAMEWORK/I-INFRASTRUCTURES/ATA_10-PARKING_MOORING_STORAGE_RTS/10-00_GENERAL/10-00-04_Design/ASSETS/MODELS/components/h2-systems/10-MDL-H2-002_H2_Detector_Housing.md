# 10-MDL-H2-002 — H2 Detector Housing

## 1. Purpose

Weatherproof housing for hydrogen leak detection sensors used during aircraft parking and storage. Protects sensitive electronics while allowing rapid H2 gas detection.

## 2. Scope

This component applies to:

- **Aircraft Type**: AMPEL360-BWB-H2-Hy-E
- **System**: H2 leak detection system
- **Quantity**: 8 housings per aircraft parking spot
- **Environment**: Outdoor, all-weather

## 3. Model Information

| Parameter | Value |
|-----------|-------|
| Model Number | 10-MDL-H2-002 |
| Model Type | Component |
| Component Category | H2 System |
| CAD System | SolidWorks |
| Version | 1.0 |
| Status | ACTIVE |

## 4. Available Formats

| Format | Filename | Location | Checksum |
|--------|----------|----------|----------|
| SolidWorks | 10-MDL-H2-002_H2_Detector_Housing.sldprt | `cad-native/solidworks/` | TBD |
| STEP | 10-MDL-H2-002_H2_Detector_Housing.step | `exchange-formats/step/` | TBD |
| STL | 10-MDL-H2-002_H2_Detector_Housing.stl | `visualization/stl/` | TBD |

## 5. Geometry Description

**Housing Type:** IP67 rated enclosure with vented sensor chamber

**Dimensions:**
- Length: 200 mm
- Width: 150 mm
- Height: 120 mm
- Weight: 1.5 kg
- Mounting: Wall/pole mount bracket

**Features:**
- Vented sensor chamber (0.2 micron filter)
- LCD display window
- Audible alarm (85 dB)
- Visual alarm (LED beacon)
- Cable glands (2x M20)
- Tamper-resistant fasteners

## 6. Materials

| Part | Material | Specification |
|------|----------|---------------|
| Housing Body | Aluminum Alloy 6061-T6 | AMS 4027 |
| Cover | Polycarbonate | UV stabilized, clear |
| Gasket | Silicone | IP67 rated |
| Sensor Filter | Sintered Stainless Steel | 0.2 micron |
| Mounting Bracket | Stainless Steel 316 | ASTM A240 |

**Environmental Rating:**
- Ingress Protection: IP67
- Temperature Range: -40°C to +70°C
- Humidity: 0-100% RH
- UV Resistance: Excellent
- Corrosion Resistance: Marine environment

## 7. H2/BWB Considerations

**H2 Detection Features:**
- Detection Range: 0-4% H2 by volume
- Response Time: < 1 second
- Alarm Levels: 1% (warning), 2% (alarm), 4% (evacuation)
- Self-test function
- Calibration gas port

**Mounting Locations (BWB Aircraft):**
- Near fuel tank vents (4x)
- Below aircraft belly (2x)
- Ground equipment areas (2x)

**Integration:**
- Wireless communication to central monitoring
- Battery backup (8 hours)
- Solar panel option for remote installations
- Lightning protection

## 8. Related Documentation

### Related Assemblies
- [10-MDL-ASM-004 — H2 Safety Equipment Assembly](../../assemblies/10-MDL-ASM-004_H2_Safety_Equipment_Assembly.md)

### Related Components
- [10-MDL-H2-001 — H2 Vent Valve](./10-MDL-H2-001_H2_Vent_Valve.md)
- [10-MDL-H2-003 — Cryo Insulation Cover](./10-MDL-H2-003_Cryo_Insulation_Cover.md)

### Related Simulations
- [10-SIM-CFD-001 — H2 Dispersion Analysis](../../simulations/cfd/10-SIM-CFD-001_H2_Dispersion_Analysis.md)

### Related Specifications
- TBD: REQ-10-410 — H2 Detection System Requirements

### Related Standards
- **IEC 60079-29-1** — Gas detectors — Performance requirements
- **EN 60529** — IP ratings
- **SAE AS6968** — Hydrogen aircraft systems

## 9. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 1.0 | 2025-12-09 | AMPEL360 H2 Systems Team | Initial release |

---

## Document Control

- **Document ID**: 10-MDL-H2-002
- **Version**: 1.0
- **Status**: ACTIVE
- **Classification**: Safety Critical
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
