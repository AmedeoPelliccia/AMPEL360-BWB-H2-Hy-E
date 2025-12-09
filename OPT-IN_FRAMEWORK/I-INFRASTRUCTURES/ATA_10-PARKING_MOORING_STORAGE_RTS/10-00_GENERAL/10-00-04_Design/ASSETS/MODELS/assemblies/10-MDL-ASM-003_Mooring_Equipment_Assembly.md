# 10-MDL-ASM-003 — Mooring Equipment Assembly

## 1. Purpose

This assembly model defines the mooring equipment for the AMPEL360-BWB-H2 aircraft for extended outdoor storage or high-wind conditions. The mooring system provides additional restraint beyond standard tiedown, using mast-based attachment points for enhanced wind load resistance.

## 2. Scope

This model applies to:

- **Aircraft Type**: AMPEL360-BWB-H2-Hy-E
- **Usage Scenarios**:
  - Long-term outdoor storage (weeks to months)
  - High-wind locations (coastal, exposed airfields)
  - Temporary bases without hangar facilities
  - Emergency dispersal operations

**Includes**:
- Mooring mast structures
- High-strength mooring cables
- Aircraft attachment fittings
- Tensioning and adjustment mechanisms

## 3. Model Information

| Parameter | Value |
|-----------|-------|
| Model Number | 10-MDL-ASM-003 |
| Model Type | Assembly |
| CAD System | CATIA V6 |
| Version | 1.0 |
| Status | ACTIVE |
| Created | 2025-12-09 |
| Last Modified | 2025-12-09 |

## 4. Available Formats

| Format | Filename | Location | Checksum |
|--------|----------|----------|----------|
| CATIA V6 | 10-MDL-ASM-003_Mooring_Equipment.CATProduct | `cad-native/catia/` | TBD |
| STEP AP242 | 10-MDL-ASM-003_Mooring_Equipment.step | `exchange-formats/step/` | TBD |
| STL | 10-MDL-ASM-003_Mooring_Equipment.stl | `visualization/stl/` | TBD |

## 5. Assembly Description

### 5.1 Mooring Configuration

The mooring system consists of:

1. **Mooring Masts (4x)**
   - Height: 6m above ground level
   - Location: Positioned around aircraft at 45° angles
   - Construction: Tubular steel, galvanized finish
   - Component: [10-MDL-MR-001 — Mooring Mast](../components/mooring/10-MDL-MR-001_Mooring_Mast.md)

2. **Mooring Cables (8x)**
   - Primary cables: 4x from mast tops to wing points
   - Secondary cables: 4x from mast mid-height to stabilization points
   - Diameter: 16mm wire rope
   - Component: [10-MDL-MR-002 — Mooring Cable](../components/mooring/10-MDL-MR-002_Mooring_Cable.md)

3. **Aircraft Attachment Points (8x)**
   - Compatible with tiedown rings or dedicated mooring fittings
   - Load capacity: 80 kN each
   - Component: [10-MDL-MR-003 — Mooring Clamp](../components/mooring/10-MDL-MR-003_Mooring_Clamp.md)

### 5.2 System Layout

```
                    [Mast NW]
                       /|\
                      / | \
                     /  |  \
                    /   |   \
          [Aircraft BWB Configuration]
                    \   |   /
                     \  |  /
                      \ | /
                       \|/
                    [Mast SE]
```

Masts positioned at:
- North-West (NW): -30m X, +30m Y
- North-East (NE): -30m X, -30m Y
- South-West (SW): +30m X, +30m Y
- South-East (SE): +30m X, -30m Y

## 6. Geometry Description

### 6.1 Mast Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Mast Height | 6000 mm | Above ground level |
| Base Diameter | 250 mm | Tubular steel section |
| Wall Thickness | 12 mm | High-strength steel |
| Foundation Depth | 1500 mm | Below ground level |
| Base Plate Size | 500 x 500 mm | Anchor bolt pattern |

### 6.2 Cable Geometry

| Cable Type | Length Range | Angle | Tension |
|------------|--------------|-------|---------|
| Primary (wing) | 15-20m | 30-40° | 20 kN nominal |
| Secondary (stabilizer) | 10-15m | 20-30° | 10 kN nominal |

## 7. Materials

| Component | Material | Specification | Quantity |
|-----------|----------|---------------|----------|
| Mooring Mast | Steel Tube | ASTM A500 Gr. C | 4 |
| Mast Foundation | Concrete | Compressive strength ≥ 30 MPa | 4 |
| Base Plate | Steel Plate | ASTM A36 | 4 |
| Anchor Bolts | High-Strength Steel | ASTM F1554 Gr. 105 | 16 |
| Mooring Cable | Wire Rope | MIL-DTL-83420 Type II | 8 |
| Cable Fittings | Stainless Steel 316L | AMS 5507 | 16 |
| Tensioning Device | Stainless Steel | ISO 9001 certified | 8 |

## 8. Load Analysis

### 8.1 Design Wind Loads

| Condition | Wind Speed | Total Mooring Load | Per Cable (avg) | Safety Factor |
|-----------|------------|--------------------|-----------------| --------------|
| Normal Storage | 40 m/s | 800 kN | 100 kN | 2.5 |
| Storm Conditions | 60 m/s | 1800 kN | 225 kN | 1.5 |
| Hurricane | 75 m/s | 2800 kN | 350 kN | 1.25 |

**Note**: Mooring system provides significantly higher wind resistance than standard tiedown.

### 8.2 Structural Analysis

See related FEA analysis:
- [10-SIM-FEA-002 — Mooring Stress Analysis](../simulations/fea/10-SIM-FEA-002_Mooring_Stress_Analysis.md)

Key findings:
- Mast foundation critical for system stability
- Cable tension must be balanced to prevent asymmetric loads
- BWB wing box structure adequate for mooring loads
- Fatigue analysis shows 10-year service life under normal conditions

## 9. H2/BWB Considerations

### 9.1 BWB-Specific Design

**Structural Advantages:**
- Large wing area provides multiple stable attachment points
- Integrated wing-body structure distributes loads effectively
- Low center of gravity improves stability

**Design Adaptations:**
- Mast positions optimized for BWB wingspan
- Cable routing avoids BWB trailing edge control surfaces
- Attachment points integrated with wing box structure

### 9.2 H2 Safety Considerations

**Mast Location:**
- All masts positioned outside H2 primary safety zone (10m)
- Secondary H2 safety zone (25m) encompasses mast bases
- H2 detection equipment mounted on mast structures

**Lightning Protection:**
- Mooring masts equipped with lightning rods
- Grounding straps connect aircraft to earth ground
- Bonding cables ensure electrical continuity
- Non-sparking cable clamps used throughout

**Emergency Procedures:**
- Quick-release mechanisms for H2 emergency
- Cable cutters positioned at each mast
- Emergency release accessible from safe distance
- Fire-resistant cable coatings

## 10. Installation and Operation

### 10.1 Installation Procedure

1. **Site Preparation**
   - Survey and mark mast locations
   - Excavate foundation pits (1.5m depth)
   - Install anchor bolts and foundation forms
   - Pour concrete and cure (minimum 7 days)

2. **Mast Erection**
   - Position mast on base plate
   - Align and bolt to foundation
   - Install guy wires if required for stability
   - Install lightning protection system

3. **Aircraft Mooring**
   - Position aircraft in mooring circle
   - Attach primary cables to wing points
   - Attach secondary cables to stabilization points
   - Tension all cables progressively and equally
   - Verify cable tension (target: 20 kN primary, 10 kN secondary)
   - Install safety lockouts on tensioning devices

### 10.2 Operational Procedures

**Daily Checks:**
- Visual inspection of cables for damage
- Check cable tension indicators
- Verify H2 detection equipment operational
- Monitor weather forecast

**Weekly Maintenance:**
- Measure cable tensions with load cells
- Inspect cable clamps and fittings
- Check mast structural condition
- Lubricate tensioning mechanisms

**Storm Preparation:**
- Increase cable tensions per storm protocol
- Position fire suppression equipment
- Brief emergency response team
- Establish 24-hour monitoring

## 11. Comparison with Tiedown System

| Parameter | Tiedown (ASM-002) | Mooring (ASM-003) |
|-----------|-------------------|-------------------|
| Wind Resistance | Up to 40 m/s | Up to 75 m/s |
| Installation Time | 30 minutes | 2 hours (after infrastructure) |
| Infrastructure | Ground anchors | Permanent masts |
| Aircraft Load | Moderate | Higher |
| Typical Use | Short-term parking | Long-term storage |
| Cost | Low | Medium-High |

## 12. Related Documentation

### Related Models
- [10-MDL-ASM-001 — BWB Parking Configuration](./10-MDL-ASM-001_BWB_Parking_Configuration.md)
- [10-MDL-ASM-002 — Tiedown System Assembly](./10-MDL-ASM-002_Tiedown_System_Assembly.md)
- [10-MDL-MR-001 — Mooring Mast](../components/mooring/10-MDL-MR-001_Mooring_Mast.md)
- [10-MDL-MR-002 — Mooring Cable](../components/mooring/10-MDL-MR-002_Mooring_Cable.md)
- [10-MDL-MR-003 — Mooring Clamp](../components/mooring/10-MDL-MR-003_Mooring_Clamp.md)

### Related Simulations
- [10-SIM-FEA-002 — Mooring Stress Analysis](../simulations/fea/10-SIM-FEA-002_Mooring_Stress_Analysis.md)

### Related Specifications
- TBD: REQ-10-300 — Mooring System Requirements
- TBD: REQ-10-310 — Extreme Weather Requirements

### Related Standards
- **ATA 10** — Parking, Mooring, Storage & RTS
- **ASCE 7** — Minimum Design Loads for Buildings and Other Structures
- **MIL-DTL-83420** — Cable Assembly specifications

## 13. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 1.0 | 2025-12-09 | AMPEL360 Design Team | Initial release |

---

## Document Control

- **Document ID**: 10-MDL-ASM-003
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-12-09
- **Owner**: AMPEL360 ATA 10 Design Team
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
