# 10-MDL-ASM-002 — Tiedown System Assembly

## 1. Purpose

This assembly model defines the complete aircraft tiedown system for securing the AMPEL360-BWB-H2 aircraft during parking and storage. The system is designed to resist wind loads, prevent aircraft movement, and accommodate the unique structural characteristics of the BWB configuration.

## 2. Scope

This model applies to:

- **Aircraft Type**: AMPEL360-BWB-H2-Hy-E
- **Configuration**: 6-point tiedown system for BWB
- **Load Cases**:
  - Normal wind conditions (up to 25 m/s)
  - Storm conditions (25-40 m/s)
  - Extreme wind events (40+ m/s with evacuation)

**Includes**:
- Aircraft-mounted tiedown rings and fittings
- Tiedown cables and tensioning devices
- Ground anchors and attachment hardware
- Load distribution components

## 3. Model Information

| Parameter | Value |
|-----------|-------|
| Model Number | 10-MDL-ASM-002 |
| Model Type | Assembly |
| CAD System | SolidWorks |
| Version | 1.0 |
| Status | ACTIVE |
| Created | 2025-12-09 |
| Last Modified | 2025-12-09 |

## 4. Available Formats

| Format | Filename | Location | Checksum |
|--------|----------|----------|----------|
| SolidWorks | 10-MDL-ASM-002_Tiedown_System.sldasm | `cad-native/solidworks/` | TBD |
| STEP AP242 | 10-MDL-ASM-002_Tiedown_System.step | `exchange-formats/step/` | TBD |
| STL | 10-MDL-ASM-002_Tiedown_System.stl | `visualization/stl/` | TBD |

## 5. Assembly Description

### 5.1 Tiedown Configuration

The BWB aircraft uses a 6-point tiedown system:

1. **Wing Tiedown Points (4x)**
   - Location: Port and starboard wings, inner and outer positions
   - Spacing: Approximately 15m between inner and outer points
   - Load capacity: 50 kN each (TBD)

2. **Nose Tiedown Point (1x)**
   - Location: Forward fuselage centerline
   - Load capacity: 30 kN (TBD)

3. **Tail Tiedown Point (1x)**
   - Location: Aft fuselage centerline
   - Load capacity: 30 kN (TBD)

### 5.2 Component Breakdown

Each tiedown point includes:
- Aircraft tiedown ring ([10-MDL-TD-001](../components/tiedown/10-MDL-TD-001_Tiedown_Ring.md))
- Tiedown fitting and cable connector ([10-MDL-TD-002](../components/tiedown/10-MDL-TD-002_Tiedown_Fitting.md))
- High-strength steel cable (12mm diameter, Grade 316 stainless steel)
- Tensioning device (turnbuckle or ratchet tensioner)
- Ground anchor ([10-MDL-TD-003](../components/tiedown/10-MDL-TD-003_Ground_Anchor.md))

## 6. Geometry Description

### 6.1 Tiedown Point Locations

| Point ID | Location | X (mm) | Y (mm) | Z (mm) | Notes |
|----------|----------|--------|--------|--------|-------|
| TD-01 | Port Wing Outer | TBD | -30000 | TBD | Port outer wing |
| TD-02 | Port Wing Inner | TBD | -15000 | TBD | Port inner wing |
| TD-03 | Starboard Wing Inner | TBD | +15000 | TBD | Starboard inner wing |
| TD-04 | Starboard Wing Outer | TBD | +30000 | TBD | Starboard outer wing |
| TD-05 | Nose | TBD | 0 | TBD | Forward centerline |
| TD-06 | Tail | TBD | 0 | TBD | Aft centerline |

Coordinates relative to aircraft reference point (nose landing gear).

### 6.2 Cable Routing

- **Cable Length**: Adjustable, typically 3-5m per tiedown
- **Angle**: 30-45 degrees from horizontal (optimal)
- **Clearances**: Minimum 0.5m from aircraft surfaces
- **Tensioning**: Cables must be tensioned equally to prevent load concentration

## 7. Materials

| Component | Material | Specification | Quantity |
|-----------|----------|---------------|----------|
| Tiedown Ring | Aluminum Alloy 7075-T6 | AMS 4078 | 6 |
| Tiedown Fitting | Stainless Steel 316L | AMS 5507 | 6 |
| Cable | Stainless Steel Wire Rope | MIL-DTL-83420 | 6 |
| Ground Anchor | Galvanized Steel | ASTM A123 | 6 |
| Hardware (pins, bolts) | Stainless Steel 316 | MS/AN Standards | Various |

## 8. Load Analysis

### 8.1 Design Loads

| Load Case | Wind Speed | Total Load | Per Point (avg) | Safety Factor |
|-----------|------------|------------|-----------------|---------------|
| Normal Operations | 25 m/s | 180 kN | 30 kN | 2.0 |
| Storm Conditions | 40 m/s | 460 kN | 77 kN | 1.5 |
| Ultimate Load | 50 m/s | 720 kN | 120 kN | 1.25 |

**Note**: Load distribution varies by wind direction and aircraft orientation.

### 8.2 Structural Analysis

See related FEA analysis:
- [10-SIM-FEA-001 — Tiedown Load Analysis](../simulations/fea/10-SIM-FEA-001_Tiedown_Load_Analysis.md)

Key findings:
- Wing tiedown points experience highest loads in crosswind conditions
- Nose/tail points primarily resist longitudinal loads
- BWB structure distributes loads effectively across wing box

## 9. H2/BWB Considerations

### 9.1 BWB-Specific Design

**Structural Integration:**
- Tiedown rings integrated into wing box primary structure
- Load paths designed for distributed BWB structure
- Accessibility for ground crew from wing trailing edge

**Attachment Points:**
- Wing points attached to main wing spars
- Reinforced fittings at attachment locations
- Inspection access provided for structural health monitoring

### 9.2 H2 Safety Considerations

**Equipment Location:**
- All tiedown equipment kept outside H2 safety zones
- Non-sparking materials used near fuel system
- Grounding straps integrated to prevent static buildup

**Emergency Release:**
- Quick-release mechanisms for emergency evacuation
- Accessible release points for rapid deployment
- Fire-resistant cable coatings in critical areas

## 10. Installation and Maintenance

### 10.1 Installation Procedure

1. Position aircraft in parking spot
2. Set parking brake and wheel chocks
3. Attach tiedown cables to aircraft rings (all 6 points)
4. Route cables to ground anchors (verify clearances)
5. Tension cables progressively (equal tension)
6. Verify tension with load indicator (target: 5 kN per cable)
7. Perform final inspection and documentation

### 10.2 Maintenance Requirements

| Item | Inspection Interval | Procedure |
|------|---------------------|-----------|
| Tiedown Rings | 100 flight hours | Visual inspection for cracks, corrosion |
| Cables | Every use | Check for fraying, kinks, corrosion |
| Ground Anchors | Monthly | Verify anchor integrity, torque check |
| Hardware | Every use | Check for wear, replace if damaged |

## 11. Related Documentation

### Related Models
- [10-MDL-ASM-001 — BWB Parking Configuration](./10-MDL-ASM-001_BWB_Parking_Configuration.md)
- [10-MDL-TD-001 — Tiedown Ring](../components/tiedown/10-MDL-TD-001_Tiedown_Ring.md)
- [10-MDL-TD-002 — Tiedown Fitting](../components/tiedown/10-MDL-TD-002_Tiedown_Fitting.md)
- [10-MDL-TD-003 — Ground Anchor](../components/tiedown/10-MDL-TD-003_Ground_Anchor.md)

### Related Simulations
- [10-SIM-FEA-001 — Tiedown Load Analysis](../simulations/fea/10-SIM-FEA-001_Tiedown_Load_Analysis.md)

### Related Specifications
- TBD: REQ-10-200 — Tiedown System Requirements
- TBD: REQ-10-210 — Wind Load Requirements
- TBD: REQ-10-220 — Structural Integrity Requirements

### Related Standards
- **ATA 10** — Parking, Mooring, Storage & RTS
- **MIL-DTL-83420** — Cable Assembly, Tiedown
- **CS-25.561** — Emergency Landing Conditions (reference for loads)
- **AC 43-13-1B** — Acceptable Methods, Techniques, and Practices

## 12. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 1.0 | 2025-12-09 | AMPEL360 Design Team | Initial release |

---

## Document Control

- **Document ID**: 10-MDL-ASM-002
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-12-09
- **Owner**: AMPEL360 ATA 10 Design Team
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
