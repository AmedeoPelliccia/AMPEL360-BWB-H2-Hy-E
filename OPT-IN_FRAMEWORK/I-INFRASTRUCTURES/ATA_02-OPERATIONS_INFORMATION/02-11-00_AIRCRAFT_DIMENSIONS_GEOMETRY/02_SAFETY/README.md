# 02_SAFETY - AIRCRAFT DIMENSIONS GEOMETRY

**Component Code:** 02-11-00  
**Component Name:** AIRCRAFT_DIMENSIONS_GEOMETRY  
**Folder:** 02_SAFETY

## Purpose

This folder contains comprehensive safety documentation for the AMPEL360 BWB aircraft dimensions and geometry, addressing unique aspects of the BWB configuration including wide wingspan (52m), wide center body (38m), and low ground clearances.

## Status

✅ **Complete**

All safety documentation and supporting files have been implemented per ATA 02-11-00 requirements.

## Document Structure

### Main Safety Documents

1. **Dimensional_Safety_Overview.md** (AMPEL360-02-11-00-SAF-001)
   - Critical safety dimensions and clearances
   - BWB-specific safety concerns (52m wingspan, 38m center body, 1.2m wingtip clearance)
   - Risk assessment matrix
   - Safety requirements and compliance (CS-25, ICAO Annex 14)

2. **Ground_Clearance_Safety.md** (AMPEL360-02-11-00-SAF-002)
   - Minimum ground clearances (static and dynamic conditions)
   - CAOS monitoring system
   - Pavement requirements
   - Clearance-related incident prevention

3. **Ground_Handling_Safety.md** (AMPEL360-02-11-00-SAF-004)
   - Taxi procedures and speed limits
   - Marshalling requirements (enhanced for BWB)
   - Service vehicle operations
   - Weather limitations

4. **BWB_Specific_Safety.md** (AMPEL360-02-11-00-SAF-003)
   - Wide center body considerations (38m)
   - Low aspect ratio wing characteristics (AR 3.2)
   - Large planform area effects (845 m²)
   - BWB-specific procedures (towing, jacking, emergency egress)

### CLEARANCE_REQUIREMENTS/

- **Minimum_Clearances.csv** - Clearance data table with min/normal values
- **Critical_Clearance_Points.md** (SAF-010) - Primary and secondary critical points
- **Ground_Equipment_Clearances.md** (SAF-011) - GSE clearance requirements
- **Wingtip_Clearance_Safety.md** (SAF-012) - Wingtip-specific procedures (52m wingspan)
- **Belly_Clearance_Requirements.md** (SAF-013) - Belly clearance monitoring and limits

### HAZARD_ZONES/

- **Danger_Zones_Map.svg** - Visual diagram of ground operations danger zones
- **Ground_Operations_Hazards.md** (SAF-020) - Comprehensive hazard categorization
- **Propeller_Clearance_Zones.md** (SAF-021) - Electric propulsor safety zones
- **Engine_Intake_Hazards.md** (SAF-022) - Intake zone safety procedures
- **Exhaust_Zones.md** (SAF-023) - H₂ fuel cell exhaust characteristics

### BWB_SAFETY_CONSIDERATIONS/

- **Wide_Body_Ground_Operations.md** (SAF-030) - 38m center body operations
- **Wing_Strike_Prevention.md** (SAF-031) - 52m wingspan strike prevention
- **Tail_Strike_Analysis.md** (SAF-032) - BWB-specific pitch limitations
- **Ground_Attitude_Limits.md** (SAF-033) - Pitch and roll limits
- **Oversize_Aircraft_Procedures.md** (SAF-034) - Code 4E airport operations

### STRUCTURAL_SAFETY/

- **Load_Limits_by_Station.csv** - Structural load limits by station
- **Jacking_Points_Safety.md** (SAF-040) - Four-point jacking procedures
- **Towing_Attachment_Safety.md** (SAF-041) - Dual tow bar system
- **Ground_Support_Limits.md** (SAF-042) - GSE structural limitations

### EMERGENCY_CONSIDERATIONS/

- **Emergency_Egress_Geometry.md** (SAF-005) - 12 exit configuration (6 Type A, 6 Type III)
- **Slide_Deployment_Clearances.md** (SAF-051) - Slide clearance requirements
- **Fire_Access_Points.md** (SAF-052) - ARFF access points and procedures
- **Rescue_Approach_Zones.csv** - Emergency vehicle approach zones

## Key Safety Features

### CAOS Ground Monitoring System
- Real-time clearance calculations
- Wingtip proximity alerts
- Belly clearance warnings
- Pitch/roll attitude monitoring

### BWB-Specific Challenges
- 52m wingspan (ICAO Code E)
- 38m center body width (unprecedented)
- 1.2m wingtip clearance (MTOW)
- Multiple simultaneous service operations

### Safety Systems Integration
- CAOS ground clearance monitoring
- Wingtip proximity sensors
- Tail strike protection system (TSPS)
- H₂ safety zone enforcement (50m radius)

## Training Requirements

All documentation includes comprehensive training requirements for:
- Flight crew
- Ground operations personnel
- Wing walkers
- Maintenance personnel
- ARFF personnel

## Regulatory Compliance

Documentation addresses:
- CS-25 certification requirements
- ICAO Annex 14 aerodrome standards
- H₂ safety regulations (ISO 19881)
- BWB-specific special conditions

## Related Documents

- Parent Component: 02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY
- ATA Chapter: 02 - Operations Information
- Related Chapters: ATA 06 (Dimensions), ATA 09 (Towing/Taxiing), ATA 28 (H₂ Fuel System)
- AMPEL360 Platform: BWB H2 Hy-E Q100 INTEGRA

---

**Document Control:**
- Version: 2.0
- Status: ✅ Complete
- Last Updated: 2025-11-06
- Completion: 02-11-00 / 02_SAFETY complete ✅
