# 85-30-00-003 Materials and Recyclability

## Document Information

- **Document ID**: 85-30-00-003
- **Title**: Materials and Recyclability
- **Version**: 1.0
- **Date**: 2025-11-21
- **Status**: Draft
- **Category**: Technical Specification
- **ATA Chapter**: 85 - Infrastructure Interface Standards
- **Bucket**: 30 - Circularity

## Purpose

This document establishes comprehensive requirements and guidelines for material selection, recyclability assessment, and end-of-life material recovery for all infrastructure systems supporting the AMPEL360 BWB aircraft. It ensures that infrastructure assets are designed and manufactured with circularity principles embedded from material selection through end-of-life processing.

## Scope

This specification applies to:

- All ground support equipment (GSE)
- Hydrogen production, storage, and distribution infrastructure
- CO₂ battery containers and charging systems
- Airport interface equipment (jetways, stands, GPUs, etc.)
- Buildings and fixed infrastructure supporting BWB operations
- Consumables and replacement parts

## Material Selection Framework

### Selection Criteria Hierarchy

Material selection shall prioritize the following criteria in order:

1. **Safety and Performance**: Materials must meet all safety and performance requirements per applicable standards
2. **Environmental Impact**: Minimize lifecycle environmental footprint (embodied carbon, toxicity, resource depletion)
3. **Circularity**: Maximize potential for reuse, remanufacturing, or recycling
4. **Economic Viability**: Optimize total cost of ownership considering acquisition, use phase, and end-of-life
5. **Supply Chain Resilience**: Prefer materials with secure, diversified supply chains

### Material Categories and Guidelines

#### Structural Materials

**Metals**:
- **Aluminum Alloys** (primary structural use):
  - Prefer alloys with high recycled content (e.g., 6061, 6063 with >50% recycled content)
  - Design for disassembly to enable alloy-specific recycling
  - Avoid dissimilar metal contact (galvanic corrosion, separation challenges)
  - Recyclability: >95% with minimal quality loss
  
- **Steel** (frames, supports, heavy-duty components):
  - Use low-alloy or stainless grades with high recycled content potential
  - Avoid chromium/nickel plating where possible (recycling contamination)
  - Design for magnetic separation in recycling streams
  - Recyclability: >90%

- **Advanced Alloys** (high-performance applications):
  - Titanium alloys: Use only where Al/steel insufficient, design for recovery (high value)
  - Magnesium alloys: Limit use due to recycling challenges; if used, ensure traceability
  - Recyclability: Titanium 70-80%, Magnesium 40-60%

**Polymers and Composites**:
- **Thermoplastics** (preferred over thermosets):
  - Polyethylene (PE), Polypropylene (PP): Widely recyclable, low environmental impact
  - Polyamides (PA): Good mechanical properties, growing recycling infrastructure
  - Use single-polymer designs where possible (avoid multi-layer laminates)
  - Recyclability: 60-85% depending on contamination and collection systems

- **Thermoset Composites** (use only where thermoplastics inadequate):
  - Carbon fiber: Design for fiber recovery through pyrolysis or solvolysis
  - Glass fiber: Lower recycling value but acceptable in concrete aggregate
  - Document composite layup for optimized end-of-life processing
  - Recyclability: Fiber recovery 50-70%, matrix typically energy recovery only

- **Bio-based Polymers** (emerging, evaluate on case-by-case basis):
  - Polylactic acid (PLA), cellulose-based materials
  - Ensure composability aligns with local waste infrastructure
  - Verify life cycle environmental benefits (LCA required)

**Concrete and Cementitious Materials**:
- Specify high recycled aggregate content (target: >30%)
- Use supplementary cementitious materials (fly ash, slag) to reduce embodied carbon
- Design for deconstruction (bolted vs. cast-in-place where feasible)
- Recyclability: Aggregate recovery >90%, downcycling typical

#### Functional Materials

**Electrical and Electronic Components**:
- Comply with [EU RoHS Directive](https://ec.europa.eu/environment/topics/waste-and-recycling/rohs-directive_en) (restriction of hazardous substances)
- Prioritize components with manufacturer take-back programs
- Modular design for easy component-level replacement
- [Digital Product Passport](85-30-00-004_DPP_Integration_for_Infrastructure.md) must include WEEE-relevant material data
- Critical materials (rare earths, precious metals) must be traceable and recoverable

**Fluids and Lubricants**:
- Biodegradable hydraulic fluids where performance allows (ester-based)
- Long-life synthetic lubricants to reduce consumption
- Closed-loop collection and recycling systems for used fluids
- Avoid PFAS (per- and polyfluoroalkyl substances) where alternatives exist

**Insulation and Sealing Materials**:
- Halogen-free materials (fire safety without toxic combustion products)
- Avoid mixed material foams (separation challenges); prefer single-material solutions
- Design seals and gaskets for easy removal (no permanent adhesives)

**Coatings and Finishes**:
- Water-based or powder coatings preferred over solvent-based
- Avoid heavy metal pigments (lead, cadmium, chromium VI)
- Design for coating removal prior to recycling (mechanical stripping, chemical processes)
- Consider uncoated/anodized finishes where aesthetics allow

### Prohibited and Restricted Substances

**Prohibited** (shall not be used):
- Asbestos and asbestos-containing materials
- Polychlorinated biphenyls (PCBs)
- Ozone-depleting substances (per [Montreal Protocol](https://ozone.unep.org/treaties/montreal-protocol))
- Intentionally added PFAS (effective 2026, per evolving EU regulations)

**Restricted** (use only with justification and controls):
- Heavy metals: Lead, Mercury, Cadmium, Hexavalent Chromium (per [EU RoHS](https://ec.europa.eu/environment/topics/waste-and-recycling/rohs-directive_en))
  - Exemptions allowed where no technical alternative exists, subject to approval
  - Must be documented in DPP for end-of-life handling
- Brominated flame retardants (BFRs): Restricted classes, prefer alternatives
- Phthalates: Restricted in applications with potential human exposure

**Documentation**: All uses of restricted substances must be:
- Technically justified in design documentation
- Tracked in material declarations and [DPP](85-30-00-004_DPP_Integration_for_Infrastructure.md)
- Managed with specific end-of-life handling procedures

## Recyclability Assessment

### Recyclability Metrics

**Material Circularity Indicator (MCI)**:
Based on [Ellen MacArthur Foundation methodology](https://ellenmacarthurfoundation.org/material-circularity-indicator):

```
MCI = (V_virgin - V_linear + W_feedstock + W_collection × W_utility) / V_virgin

Where:
V_virgin      = Virgin material input (kg or EUR)
V_linear      = Linear flow (material not recovered at end-of-life)
W_feedstock   = Recycled/reused feedstock input
W_collection  = End-of-life collection efficiency
W_utility     = Material utility efficiency (based on product lifetime)
```

**Target MCI**: >0.6 for all major infrastructure equipment

**Recyclability Rate by Mass**:
```
RR_mass = (M_recycled + M_reused) / M_total × 100%

Where:
M_recycled = Mass of material actually recycled to equivalent quality
M_reused   = Mass of components/materials reused directly
M_total    = Total mass of equipment
```

**Target RR_mass**: >90% for metallic equipment, >70% for electronic/composite equipment

**Recyclability Value**:
```
RR_value = (V_recycled + V_reused) / (V_virgin - V_depreciation) × 100%

Where:
V_recycled      = Market value of recycled materials recovered
V_reused        = Market value of reused components
V_virgin        = Virgin material cost at time of manufacture
V_depreciation  = Value loss due to wear/contamination
```

**Target RR_value**: >40% residual value recovery at end-of-life

### Design for Recycling (DfR) Guidelines

**Principle 1: Material Identification**:
- Mark all plastic components >25g with [ISO 11469](https://www.iso.org/standard/64046.html) material codes
- Use color-coding or permanent marking for metal alloys
- Provide material composition documentation in [DPP](85-30-00-004_DPP_Integration_for_Infrastructure.md)

**Principle 2: Disassembly**:
- Design for disassembly (DfD): 90% of mass separable with common hand tools in <30 minutes
- Minimize number of fastener types (target: <5 types per assembly)
- Use reversible fastening: bolts/screws over rivets, snap-fits over adhesives
- Avoid insert molding of dissimilar materials where feasible
- Provide disassembly instructions in maintenance documentation and DPP

**Principle 3: Material Separation**:
- Minimize number of materials (target: <10 material types per assembly)
- Separate incompatible materials (e.g., different aluminum alloys, mixed plastics)
- Design for automated separation where possible (magnetic, density, optical sorting)
- Avoid coatings that cannot be easily removed or are compatible with base material recycling

**Principle 4: Contamination Prevention**:
- Design to prevent fluid contamination of materials (sealed reservoirs, drip-free connections)
- Use sacrificial wear surfaces that can be easily removed before recycling
- Separate electronics from structural materials (no potting, encapsulation if avoidable)

**Principle 5: Hazardous Material Isolation**:
- Battery packs: Easy removal with documented procedures
- Fluids: Drainable without disassembly, with clear labeling
- Capacitors, transformers: Accessible for removal prior to recycling
- Hazardous substance location map included in DPP

## Recycling Infrastructure and Partnerships

### Recycling Technology Matrix

| Material Type | Primary Technology | Secondary Technology | Typical Recovery Rate | Key Challenges |
|---------------|-------------------|---------------------|----------------------|----------------|
| Aluminum alloys | Melting and refining | Decoating + remelting | 95-98% | Alloy segregation |
| Steel | Shredding + magnetic separation + melting | Direct reuse (structural) | 90-95% | Coating removal |
| Titanium | Melting (large parts) | Powder metallurgy (small/mixed) | 70-80% | High energy cost |
| Copper/wiring | Shredding + eddy current + smelting | Granulation + refining | 95-99% | Insulation removal |
| Thermoplastics | Mechanical recycling (shredding, extrusion) | Chemical recycling (pyrolysis) | 60-85% | Contamination, sorting |
| Thermoset composites | Pyrolysis (fiber recovery) | Grinding (filler applications) | 50-70% | Matrix degradation |
| Electronics/WEEE | Manual dismantling + specialized smelting | Component harvesting + refurbishment | 60-80% | Complex assemblies |
| Batteries (Li-ion) | Pyrometallurgy or hydrometallurgy | Direct recycling (advanced) | 50-95% | Safety, varied chemistries |
| Fluids/lubricants | Filtration + re-refining | Controlled burning (energy recovery) | 70-90% | Contamination levels |

### Recycling Partner Qualification

Infrastructure recycling partners shall be qualified based on:

**Environmental and Safety Standards**:
- [ISO 14001](https://www.iso.org/iso-14001-environmental-management.html) Environmental Management System certification
- OHSAS 18001 or [ISO 45001](https://www.iso.org/iso-45001-occupational-health-and-safety.html) Occupational Health and Safety
- Compliance with [EU WEEE Directive](https://ec.europa.eu/environment/topics/waste-and-recycling/waste-electrical-and-electronic-equipment-weee_en) (electronics)
- Compliance with [Basel Convention](https://www.basel.int/) (no illegal waste export)

**Technical Capabilities**:
- Demonstrated material recovery rates meeting or exceeding targets
- Proper handling procedures for hazardous materials
- Traceability systems for material flows
- Quality assurance for recycled materials (compositional analysis)

**Circularity Reporting**:
- Detailed material flow reporting (mass, composition, destination)
- Integration with [DPP system](85-30-00-004_DPP_Integration_for_Infrastructure.md) for lifecycle closure
- Transparency in downstream material use
- Continuous improvement in recovery rates and environmental performance

**Preferred Partner Characteristics**:
- Local/regional presence (minimize transport emissions)
- Closed-loop partnerships (recycled materials returned to supply chain)
- Take-back programs for specific equipment categories
- Research collaboration on advanced recycling technologies

## Material Lifecycle Data Management

### Material Declaration Requirements

All suppliers shall provide:

**Material Composition Data**:
- Complete bill of materials (BoM) with CAS numbers for substances >0.1% by weight
- [International Material Data System (IMDS)](https://www.mdsystem.com/) submission or equivalent
- Declaration of [REACH Substances of Very High Concern (SVHC)](https://echa.europa.eu/candidate-list-table)
- Conflict minerals declaration per [EU Conflict Minerals Regulation](https://ec.europa.eu/trade/policy/in-focus/conflict-minerals-regulation/)

**Environmental Product Declaration (EPD)**:
- Cradle-to-gate lifecycle assessment per [ISO 14025](https://www.iso.org/standard/38131.html)
- Global Warming Potential (GWP), Abiotic Depletion Potential (ADP), other key indicators
- Based on representative production data (not generic database values where possible)
- Third-party verified for equipment >EUR 100,000

**Recyclability Documentation**:
- Material Circularity Indicator (MCI) calculation
- Disassembly instructions with time estimates
- Identification of recyclable fractions and recommended processes
- Hazardous materials locations and handling procedures

### Integration with Digital Product Passport

Material data shall be embedded in [DPP](85-30-00-004_DPP_Integration_for_Infrastructure.md):

**At Manufacturing**:
- Complete material composition (BoM)
- EPD and LCA data
- Recyclability assessment (MCI, RR_mass)
- Supplier declarations (REACH, RoHS, conflict minerals)

**During Use**:
- Consumables and replacement parts added (cumulative material inventory)
- Contamination events logged (fluid spills, environmental exposure)

**At End-of-Life**:
- Actual disassembly time and process
- Material recovery results (mass, quality, destination)
- Challenges encountered (inform future design improvements)
- Recycled material certifications from processors

## Economic Aspects of Material Circularity

### Material Cost-Benefit Analysis

**Recycled Material Cost Dynamics**:
- Aluminum: Recycled content typically -10% to -30% cost vs. virgin
- Steel: Recycled scrap integral to steelmaking, minimal premium/discount
- Plastics: Recycled typically -20% to -50% cost but with performance trade-offs
- Composites: Recycled fibers -40% to -60% vs. virgin but limited applications

**Design for Circularity Cost Impacts**:
- Modular design: +5% to +15% upfront cost, -20% to -40% maintenance/upgrade cost
- Material marking/DfD: +1% to +3% upfront cost, +10% to +30% end-of-life recovery value
- Single-material designs: Variable (sometimes cost-neutral, sometimes +10% for alternatives)

**Total Cost of Ownership Benefits**:
- Longer service life through better maintainability: -15% to -25% TCO
- Higher residual value: -5% to -10% TCO
- Lower environmental compliance costs: -2% to -5% TCO
- **Net TCO Impact: -20% to -35%** for well-executed circular design

### Material Recovery Revenue

**Expected Recovery Values** (% of virgin material cost at end-of-life):
- Aluminum: 60-80% (high value, well-established recycling)
- Copper/brass: 70-90% (high value, easy separation)
- Stainless steel: 50-70% (moderate value, alloying element recovery)
- Carbon steel: 30-50% (commodity, but large volumes)
- Electronics: 20-40% (precious metals, but processing-intensive)
- Plastics: 10-30% (low value, contamination challenges)
- Composites: 5-15% (fiber recovery emerging, low value applications)

**Value Maximization Strategies**:
- Clean, sorted materials command premium pricing
- Traceability (alloy grades, polymer types) enables higher-value recycling
- Volume and consistency enable direct supplier partnerships (closed-loop)
- Local processing reduces transport costs

## Implementation Roadmap

### Phase 1: Foundation (2025-2026)
- Establish material selection criteria and restricted substance list
- Develop [DPP](85-30-00-004_DPP_Integration_for_Infrastructure.md) material data templates
- Qualify initial recycling partners
- Baseline current equipment recyclability (MCI assessment)

### Phase 2: Integration (2027-2028)
- Mandate MCI >0.5 for all new equipment procurements
- Implement supplier material declaration requirements
- Pilot closed-loop material partnerships (e.g., aluminum scrap return to suppliers)
- Achieve >80% recyclability rate for new GSE

### Phase 3: Optimization (2029-2030)
- Achieve MCI >0.6 target across fleet
- Establish regional recycling infrastructure at major hubs
- Demonstrate economic viability of circular material flows
- Industry leadership: Publish case studies and best practices

## Key Performance Indicators (KPIs)

### Material Selection KPIs
- **Recycled Content**: % recycled material input (target: >40% by 2030)
- **Restricted Substances**: # exemptions required annually (target: <10)
- **EPD Coverage**: % equipment value with EPD (target: >90% by 2028)

### Recyclability KPIs
- **Material Circularity Indicator**: Average MCI (target: >0.6)
- **Recyclability Rate by Mass**: % (target: >90% for metallic, >70% for electronic/composite)
- **Disassembly Time**: Average minutes to 90% mass separation (target: <30 min)

### End-of-Life Recovery KPIs
- **Actual Recovery Rate**: % materials recycled/reused at end-of-life (target: >85%)
- **Recovery Value**: EUR per tonne recovered (target: >500 EUR/tonne average)
- **Landfill Diversion**: % equipment diverted from landfill (target: >95%)

Detailed tracking in [ASSETS/Metrics_and_KPIs/](ASSETS/Metrics_and_KPIs/).

## Related Documents

### Framework Documents
- [85-30-00-001 Circularity Framework Overview](85-30-00-001_Circularity_Framework_Overview.md)
- [85-30-00-002 Lifecycle Management Strategy](85-30-00-002_Lifecycle_Management_Strategy.md)
- [85-30-00-004 DPP Integration for Infrastructure](85-30-00-004_DPP_Integration_for_Infrastructure.md)

### Implementation Guides
- [85-30-02-001 Material Selection Criteria](85-30-02_Materials_and_Reuse/85-30-02-001_Material_Selection_Criteria.md)
- [85-30-02-002 Component Remanufacturing Strategy](85-30-02_Materials_and_Reuse/85-30-02-002_Component_Remanufacturing_Strategy.md)
- [85-30-02-003 Recycling and Recovery Processes](85-30-02_Materials_and_Reuse/85-30-02-003_Recycling_and_Recovery_Processes.md)
- [85-30-02-004 Hazardous Materials Management](85-30-02_Materials_and_Reuse/85-30-02-004_Hazardous_Materials_Management.md)

### Cross-References
- [ATA 85-00-06 Engineering](../85-00_GENERAL/85-00-06_Engineering/)
- [ATA 95 Digital Product Passport](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)

## References and Standards

- [ISO 11469:2016 Plastics - Generic Identification and Marking](https://www.iso.org/standard/64046.html)
- [ISO 14025:2006 Environmental Labels and Declarations - Type III](https://www.iso.org/standard/38131.html)
- [EU RoHS Directive 2011/65/EU](https://ec.europa.eu/environment/topics/waste-and-recycling/rohs-directive_en)
- [EU REACH Regulation EC 1907/2006](https://echa.europa.eu/regulations/reach/understanding-reach)
- [EU WEEE Directive 2012/19/EU](https://ec.europa.eu/environment/topics/waste-and-recycling/waste-electrical-and-electronic-equipment-weee_en)
- [Ellen MacArthur Foundation - Material Circularity Indicator](https://ellenmacarthurfoundation.org/material-circularity-indicator)
- [Basel Convention on Hazardous Wastes](https://www.basel.int/)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21

---
