# 10-INST-TD-003 - Tiedown Hardware Specifications

## 1. Purpose

This document specifies hardware requirements, materials, and specifications for tiedown systems on the AMPEL360-BWB-H2 aircraft.

## 2. Scope

- Tiedown fitting materials and specifications
- Fastener requirements and torque values
- Rope, chain, and cable specifications
- Ground anchor requirements
- Inspection and replacement criteria

**Effectivity**: All AMPEL360-BWB-H2 aircraft configurations

## 3. Applicable Documents

- **MIL-STD-970** - Tiedown provisions for aircraft
- **NASM 1312-XX** - Fastener specifications
- **AMS 5643** - Titanium alloy bar, forgings
- **SAE AS8879** - Tiedown rope requirements

## 4. Safety Precautions

⚠️ **WARNINGS**
- Use only approved hardware with traceability documentation
- Never substitute materials without engineering approval
- Inspect hardware before each use for damage or wear
- Replace hardware at specified intervals regardless of condition

## 5. Hardware Specifications

### 5.1 Tiedown Fittings (Aircraft-Mounted)

| Component | Material | Part Number | Specification |
|-----------|----------|-------------|---------------|
| Main Tiedown Fitting | Ti-6Al-4V Titanium | AMPEL-10-TD-001-A | AMS 5643, Heat treated |
| Backup Fitting | Ti-6Al-4V Titanium | AMPEL-10-TD-001-B | AMS 5643, Redundant design |
| Shackle Assembly | Alloy Steel | MS24633-XX | 12,000 lb capacity min |
| Swivel Fitting | Stainless Steel 17-4PH | AMPEL-10-TD-002-A | Self-lubricating bushing |

**Material Selection Rationale**:
- Titanium for aircraft fittings: High strength-to-weight ratio, corrosion resistance
- Alloy steel for ground equipment: High load capacity, cost-effective
- Stainless steel for swivel: Corrosion resistance, low maintenance

### 5.2 Fasteners

| Type | Specification | Size Range | Torque | Notes |
|------|---------------|------------|--------|-------|
| Structural Bolts | NAS6604 | 1/4" - 5/8" | Per table | Titanium, 160 ksi |
| Washers (Flat) | NAS1149 | Match bolt | N/A | Plain, no plating |
| Lock Washers | MS35338 | Match bolt | N/A | Split lock type |
| Nuts | NAS1291 | Match bolt | Per table | Self-locking |

**Torque Values** (Dry installation, titanium):

| Bolt Size | Torque (ft-lb) | Torque (Nm) |
|-----------|----------------|-------------|
| 1/4-28    | 60-70          | 81-95       |
| 5/16-24   | 110-130        | 149-176     |
| 3/8-24    | 200-230        | 271-312     |
| 1/2-20    | 450-500        | 610-678     |
| 5/8-18    | 850-950        | 1153-1288   |

### 5.3 Tiedown Ropes and Cables

| Type | Specification | Diameter | Break Strength | Application |
|------|---------------|----------|----------------|-------------|
| Nylon Rope | SAE AS8879 Type I | 3/4" - 1" | 9,000-16,000 lb | General use |
| Wire Rope | MIL-DTL-83420 | 5/8" | 14,400 lb | High wind |
| Synthetic Cable | SAE AS8879 Type III | 3/4" | 12,000 lb | H2 areas (non-sparking) |
| Chain | Grade 80 Alloy | 5/8" | 18,100 lb | Permanent installation |

**Selection Guide**:
- **Normal conditions**: Nylon rope (3/4" minimum)
- **High wind (>40 knots)**: Wire rope or chain
- **Near H2 systems**: Synthetic cable only (non-sparking)
- **Permanent/long-term**: Chain with corrosion protection

### 5.4 Ground Anchors

| Type | Load Capacity | Installation | Notes |
|------|---------------|--------------|-------|
| Concrete Anchor | 20,000 lb | Embedded in concrete | Permanent installation |
| Screw Anchor | 15,000 lb | Soil, 5 ft depth | Portable, soil dependent |
| Mobile Anchor | 12,000 lb | Surface weight | Equipment-based |
| Multi-Point Anchor | 25,000 lb | Distributed load | For BWB wingspan |

**BWB-Specific**: Due to wide wingspan, recommend multi-point anchor systems with distributed loads rather than single-point anchors.

## 6. Inspection and Replacement Criteria

### 6.1 Pre-Use Inspection

**Inspect before each use**:
- No cracks, deformation, or corrosion
- All markings legible
- Swivel/articulation moves freely
- No thread damage on fasteners
- Rope/cable no fraying, cuts, or deterioration

### 6.2 Periodic Inspection

**Inspect every 6 months or 500 flight hours**:
- Magnetic particle inspection of fittings
- Ultrasonic inspection of critical load paths
- Thread inspection with thread gauges
- Corrosion inspection
- Dimensional verification

### 6.3 Replacement Criteria

**Replace immediately if**:
- Any crack detected (zero tolerance)
- Corrosion depth >0.010"
- Deformation or permanent set visible
- Load markings illegible
- Rope/cable strength <80% of new

**Replace at life limit**:
- Fittings: 15 years or 10,000 cycles
- Ropes: 5 years or 1,000 cycles
- Cables: 10 years or 5,000 cycles
- Fasteners: At fitting replacement

## 7. H2/BWB Considerations

### 7.1 BWB Configuration

- Increased load capacity for wing fittings (15,000 lb min)
- Longer tiedown equipment for increased wingspan
- Multi-point ground anchors recommended

### 7.2 H2 Safety

- Use non-sparking synthetic cables near H2 systems
- Verify electrical bonding of all metallic components
- No aluminum components near LH2 (embrittlement)

## 8. Quality Assurance

- All hardware must have material traceability certificates
- Calibrated inspection equipment required
- Independent inspection for critical items
- Document serial numbers for life-limited parts

## 9. Cross-References

- **10-INST-TD-001** - Tiedown Points Installation
- **10-INST-TD-002** - BWB Tiedown Locations
- **10-INST-TD-004** - Tiedown Load Requirements

## 10. Revision History

| Rev | Date       | Author              | Description          |
|-----|------------|---------------------|----------------------|
| A   | 2025-12-09 | Amedeo Pelliccia    | Initial release      |

---

## Document Control

- **Document ID**: 10-INST-TD-003
- **Revision**: A
- **Status**: DRAFT - Subject to human review and approval
- **Owner**: AMPEL360 Documentation WG
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
