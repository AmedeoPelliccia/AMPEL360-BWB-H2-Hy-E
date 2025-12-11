# 10-00-12-04A - H2 System Maintenance

## 1. Purpose

This document defines specialized maintenance procedures and requirements for hydrogen fuel system components on the AMPEL360-BWB-H2 aircraft during parking, mooring, and storage operations.

## 2. Scope

- H2 system maintenance tasks and intervals
- H2 leak detection system maintenance
- H2 vent and pressure relief system maintenance
- H2 sensor calibration procedures
- Safety protocols for H2 maintenance
- Special tooling and personnel requirements

## 3. Applicable Standards

- [SAE AS6968](https://www.sae.org/standards/content/as6968/) - Hydrogen Aircraft Ground Support Equipment
- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) - Hydrogen Technologies Code
- [ISO/TS 19880-1](https://www.iso.org/standard/71940.html) - Gaseous Hydrogen Fueling Stations
- [SAE J2601](https://www.sae.org/standards/content/j2601/) - Fueling Protocol for Hydrogen Vehicles

## 4. H2 System Components

### 4.1 H2 Fuel Storage Tanks

**Maintenance Tasks**:
- External visual inspection (every A-Check)
- Thermal protection system inspection (every C-Check)
- Pressure relief valve function test (every 12 months)
- Tank certification renewal (per regulatory requirements)

**Safety Requirements**:
- Tank must be purged and inerted before any intrusive work
- Confined space entry procedures if internal inspection required
- Continuous atmospheric monitoring during work

### 4.2 H2 Leak Detection System

**Maintenance Tasks**:
- Functional test (every A-Check)
- Sensor calibration verification (every B-Check)
- Sensor replacement (every 2,000 FH or 24 months)
- System response time test (every C-Check)

**Calibration Procedure**:
1. Expose sensor to known H2 concentration (typically 1% H2 in air)
2. Verify alarm triggers at correct threshold
3. Check response time (<5 seconds typical)
4. Document calibration results
5. Replace sensor if out of tolerance

### 4.3 H2 Vent Valves

**Maintenance Tasks**:
- Visual inspection (every A-Check)
- Function test (every B-Check)
- Seal replacement (every C-Check or as needed)
- Complete valve overhaul (every 6,000 FH or 60 months)

**Function Test Procedure**:
1. Verify valve opens on command
2. Check valve seating (leak test when closed)
3. Verify manual override function
4. Test redundant vent path (if equipped)

### 4.4 H2 Pressure Regulators

**Maintenance Tasks**:
- External inspection (every A-Check)
- Pressure regulation accuracy test (every B-Check)
- Filter element replacement (every C-Check)
- Regulator overhaul (every 3,000 FH or 36 months)

**Pressure Test**:
- Verify setpoint pressure maintained within ±2%
- Check for pressure creep when system is static
- Verify relief valve operation at overpressure condition

## 5. H2 Safety Protocols

### 5.1 Pre-Work Requirements

Before any H2 system maintenance:

1. **Safety Brief**: All personnel must attend H2 safety briefing
2. **System Isolation**: Verify H2 system purged with inert gas (nitrogen)
3. **Lockout/Tagout**: Tag all H2 valves and electrical systems
4. **Monitoring**: Establish continuous H2 atmospheric monitoring
5. **Fire Protection**: Position H2-rated fire extinguishers
6. **Ventilation**: Ensure adequate ventilation (minimum 6 air changes/hour)

### 5.2 H2 Detection Requirements

- Minimum 2 independent H2 detectors in work area
- Alarm set at 25% LEL (Lower Explosive Limit = 4% H2)
- Visual and audible alarms
- Direct readout visible to all workers
- Detectors calibrated within last 30 days

### 5.3 Personal Protective Equipment (PPE)

Required PPE for H2 maintenance:
- Safety glasses with side shields
- H2-compatible gloves (no petroleum-based materials)
- Static-dissipative clothing
- Steel-toed safety shoes
- Hearing protection (if required)
- Respirator (if H2 concentration >10% LEL)

## 6. Special Tooling Requirements

### 6.1 H2-Rated Tools

- **Spark-Proof Tools**: Brass, bronze, or approved non-sparking alloys
- **Torque Wrenches**: Calibrated within last 12 months
- **Leak Detection**: Portable H2 sniffer with sensitivity <0.1% H2
- **Pressure Gauges**: Certified for H2 service, calibrated annually

### 6.2 Leak Testing Equipment

- **Bubble Test**: H2-compatible leak test solution
- **Ultrasonic Leak Detector**: For inaccessible areas
- **Mass Spectrometer**: For precision leak rate measurement (optional)

## 7. Personnel Qualification Requirements

### 7.1 Minimum Certifications

All personnel performing H2 maintenance must have:

1. **EASA Part 66 License** (or equivalent)
2. **H2 Safety Training** (NFPA 2 compliant)
3. **Aircraft Type Rating** (AMPEL360-BWB-H2)
4. **Current Medical Fitness** (Class 3 minimum)

### 7.2 H2-Specific Training

Required training modules:
- H2 properties and hazards (4 hours)
- H2 leak detection and response (2 hours)
- H2 system maintenance procedures (8 hours)
- Emergency response procedures (4 hours)
- Annual refresher training (4 hours)

See [10-00-12-33A - H2 Safety Training](../training-services/10-00-12-33A_H2_Safety_Training.md) for details.

## 8. H2 Leak Response Procedures

### 8.1 Minor Leak (H2 < 10% LEL)

1. Stop all work immediately
2. Verify source of H2
3. Ventilate area
4. Isolate H2 source if safe to do so
5. Re-assess after H2 level drops below 1% LEL

### 8.2 Major Leak (H2 > 10% LEL)

1. Evacuate area immediately
2. Activate fire alarm
3. Secure H2 supply remotely if possible
4. Establish safety perimeter (minimum 15m radius)
5. Do not re-enter until H2 level confirmed <1% LEL by qualified personnel

## 9. Documentation Requirements

All H2 system maintenance must be documented with:

- Detailed task description
- H2 safety work permit (signed)
- Pre-work H2 purge verification
- Leak test results (if applicable)
- Component serial numbers (removed/installed)
- Calibration certificates (for sensors/instruments)
- Post-maintenance functional test results
- Airworthiness release (EASA Form 1 or equivalent)

## 10. Quality Assurance

### 10.1 Independent Inspection

All H2 system maintenance requires dual inspection:
- Technician performs work
- Independent inspector verifies completion
- Both sign maintenance release

### 10.2 Leak Testing

Mandatory leak test after any H2 system opening:
- Pressure test to 1.5x operating pressure (if pressure component)
- Bubble test on all connections
- Atmospheric test with H2 detector
- Document all test results

## 11. Cross-References

- [10-00-12-01A - Maintenance Services Overview](./10-00-12-01A_Maintenance_Services_Overview.md)
- [10-00-12-05A - Cryo System Maintenance](./10-00-12-05A_Cryo_System_Maintenance.md)
- [10-00-12-14A - H2 Ground Services](../ground-services/10-00-12-14A_H2_Ground_Services.md)
- [10-00-12-23A - H2 Technical Support](../technical-support/10-00-12-23A_H2_Technical_Support.md)
- [10-00-12-33A - H2 Safety Training](../training-services/10-00-12-33A_H2_Safety_Training.md)

## 12. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-11 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-12-11*.

---
