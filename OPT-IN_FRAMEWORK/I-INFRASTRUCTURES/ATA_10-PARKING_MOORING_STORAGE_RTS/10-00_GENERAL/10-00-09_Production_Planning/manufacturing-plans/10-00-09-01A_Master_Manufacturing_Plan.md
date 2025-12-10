# 10-00-09-01A Master Manufacturing Plan

## Document Information

- **Document ID**: 10-00-09-01A
- **Title**: Master Manufacturing Plan - ATA 10 Parking, Mooring, Storage & RTS
- **Version**: 1.0 (Revision A)
- **Date**: 2025-12-10
- **Status**: Draft
- **Category**: Manufacturing Plan
- **ATA Chapter**: 10 - Parking, Mooring, Storage & RTS

## Purpose

This Master Manufacturing Plan provides the overarching strategy and framework for the production of ATA 10 Parking, Mooring, Storage, and Return to Service (RTS) systems for the AMPEL360 BWB-H2 aircraft. It establishes the manufacturing philosophy, phase-gate approach, quality management system, and coordination mechanisms across all component categories.

## Scope

This plan covers:

- **Standard Components**: Tiedown fittings, mooring points, jacking pads, covers
- **H2-Specific Components**: Hydrogen safety equipment, detectors, valves for parking operations
- **Cryogenic Systems**: Cryogenic insulation, vacuum-jacketed components, thermal management
- **BWB-Specific Adaptations**: Unique attachment points and load distributions for BWB airframe

### Exclusions

- Aircraft-level final assembly (covered under ATA 04 - Airworthiness Limitations)
- Operational procedures (covered under ATA 10 operations manuals)
- Ground support equipment design (covered under ATA 03)

## Manufacturing Philosophy

### Strategic Principles

1. **Safety First**: All manufacturing processes prioritize safety, especially for H2 and cryogenic components
2. **Quality by Design**: Build quality into processes rather than inspecting it in afterward
3. **Traceability**: Full material and process traceability for all critical components
4. **Lean Manufacturing**: Eliminate waste while maintaining quality and safety
5. **Continuous Improvement**: Iterative refinement based on lessons learned and data

### Risk-Based Approach

Components are classified by risk level to determine manufacturing controls:

| Risk Level | Examples | Key Controls |
|------------|----------|--------------|
| **Critical** | H2 valves, pressure vessels, cryo tanks | 100% inspection, full traceability, NADCAP processes |
| **Major** | Structural fittings, mooring points, jacking pads | First article inspection, in-process checks, sampling |
| **Minor** | Covers, labels, non-structural fasteners | Receiving inspection, final check, statistical sampling |

## Production Phases

### Phase 1: Engineering Development (EIS-36 to EIS-24 months)

**Objectives:**
- Finalize component designs and specifications
- Develop and qualify manufacturing processes
- Establish supplier base and source critical materials
- Build and test prototype components

**Key Activities:**
- Design for Manufacturing and Assembly (DFMA) reviews
- Process FMEA (Failure Mode and Effects Analysis)
- Supplier audits and selection
- First article builds and testing

**Deliverables:**
- Approved component designs and drawings
- Qualified manufacturing processes
- Approved supplier list
- First Article Inspection Reports (AS9102)

### Phase 2: Pre-Production (EIS-24 to EIS-12 months)

**Objectives:**
- Ramp up production capacity
- Validate serial production processes
- Train production workforce
- Establish quality systems and documentation

**Key Activities:**
- Production tooling design and fabrication
- Production Part Approval Process (PPAP per AS9145)
- Workforce training and certification
- Quality system audits (AS9100D)

**Deliverables:**
- Production-ready tooling and fixtures
- Trained and certified workforce
- Production control plans
- PPAP submission packages

### Phase 3: Initial Production (EIS-12 to EIS)

**Objectives:**
- Begin serial production for initial aircraft
- Validate production rates and quality
- Implement continuous improvement processes
- Build initial spare parts inventory

**Key Activities:**
- Serial production of components
- Statistical Process Control (SPC) implementation
- Corrective action systems
- Spare parts production

**Deliverables:**
- Components for initial aircraft (typically 5-10 units)
- Production metrics and KPIs
- Initial spare parts inventory
- Lessons learned documentation

### Phase 4: Full-Rate Production (EIS onward)

**Objectives:**
- Scale to full production rates
- Maintain quality and on-time delivery
- Implement cost reduction initiatives
- Support field operations

**Key Activities:**
- High-volume serial production
- Continuous improvement projects
- Supply chain optimization
- Field support and warranty management

**Deliverables:**
- Components for production aircraft fleet
- Ongoing spare parts supply
- Cost reduction achievements
- Quality and delivery performance

## Manufacturing Strategy by Component Category

### Tiedown and Mooring Systems

**Components**: Tiedown fittings, mooring points, anchor points

**Manufacturing Approach**:
- Forged or machined fittings from high-strength alloys
- CNC machining for precision fit
- Surface treatment for corrosion resistance
- 100% dimensional inspection

**Key Processes**:
- Precision machining
- Heat treatment (stress relief, hardening)
- Surface treatment (anodizing, cadmium plating, or approved alternatives)
- Non-destructive testing (magnetic particle or liquid penetrant)

**Reference**: [10-00-09-02A_Tiedown_Manufacturing_Plan.md](10-00-09-02A_Tiedown_Manufacturing_Plan.md)

### H2 System Components

**Components**: H2 detectors, safety equipment, valves, sensors

**Manufacturing Approach**:
- Clean room assembly (ISO Class 5-6) for critical components
- Orbital TIG welding for H2-compatible joints
- 100% leak testing with helium mass spectrometer
- Full material pedigree and traceability

**Key Processes**:
- Precision cleaning and passivation
- H2-compatible welding (per AWS D17.1 and ASME B31.12)
- Leak testing (≤1×10⁻⁹ std cc/sec)
- Functional testing and calibration

**Reference**: [10-00-09-04A_H2_Components_Manufacturing.md](10-00-09-04A_H2_Components_Manufacturing.md)

### Cryogenic Components

**Components**: Cryo insulation, vacuum-jacketed lines, thermal breaks

**Manufacturing Approach**:
- Material selection for -253°C service
- Impact testing at cryogenic temperatures
- Thermal cycling qualification
- Multi-layer insulation (MLI) installation

**Key Processes**:
- Cryogenic material processing
- Vacuum brazing or electron beam welding
- Thermal cycling tests
- Vacuum leak testing (≤1×10⁻⁸ torr-L/sec)

**Reference**: [10-00-09-05A_Cryo_Components_Manufacturing.md](10-00-09-05A_Cryo_Components_Manufacturing.md)

### BWB-Specific Assemblies

**Components**: BWB fuselage attachment fittings, load distribution brackets

**Manufacturing Approach**:
- Composite layup or machined metallic fittings
- Finite element analysis (FEA) validated designs
- Load testing of first articles
- Fit-check on aircraft mock-ups

**Key Processes**:
- Composite layup and cure (if applicable)
- Precision machining of metallic components
- Assembly and bonding
- Structural testing

## Quality Management System

### AS9100D Compliance

All manufacturing activities comply with AS9100D (Aerospace Quality Management Systems). Key elements:

1. **Management Responsibility**: Quality policy, objectives, and management review
2. **Resource Management**: Competent personnel, infrastructure, and work environment
3. **Product Realization**: Planning, customer requirements, design, purchasing, production
4. **Measurement, Analysis, and Improvement**: Monitoring, control of nonconforming product, continual improvement

### Special Process Controls (NADCAP)

Critical special processes are performed by NADCAP-accredited facilities or personnel:

| Process | NADCAP Code | Key Requirements |
|---------|-------------|------------------|
| Welding | AC7114 | Welder qualification, procedure qualification, process control |
| Heat Treatment | AC7102 | Pyrometry per AMS 2750, furnace surveys, process control |
| Non-Destructive Testing | AC7114/3 (Penetrant), AC7114/4 (Magnetic Particle) | Personnel certification per NAS-410 or equivalent, procedure qualification |
| Chemical Processing | AC7108 | Process control, solution analysis, documentation |

### Inspection and Testing

**Inspection Levels**:

1. **Receiving Inspection**: All incoming materials and purchased parts
2. **In-Process Inspection**: At defined hold points during manufacturing
3. **Final Inspection**: Complete dimensional, functional, and visual inspection
4. **First Article Inspection**: AS9102 for new or changed components

**Non-Destructive Testing (NDT)**:

- **Visual Inspection**: 100% of all components
- **Dimensional Inspection**: Per drawing requirements (typically 100% for critical dimensions)
- **Liquid Penetrant**: Weld seams, high-stress areas on critical components
- **Magnetic Particle**: Ferromagnetic materials, post-heat treatment
- **Radiographic**: 100% of H2 system welds
- **Ultrasonic**: Thick sections, suspected subsurface defects

**Leak Testing**:

- **Pressure Decay**: Initial leak check for all pressure components
- **Helium Mass Spectrometer**: Final leak test for H2 components (≤1×10⁻⁹ std cc/sec)
- **Vacuum Decay**: Cryogenic vacuum-jacketed components (≤1×10⁻⁸ torr-L/sec)

## Supply Chain Management

### Supplier Selection and Qualification

**Selection Criteria**:
- AS9100 or equivalent quality certification
- NADCAP accreditation for special processes
- Financial stability and capacity
- Prior aerospace experience
- Geographic diversity for risk mitigation

**Qualification Process**:
1. Initial assessment (documentation review, questionnaire)
2. On-site audit (for critical suppliers)
3. Sample part evaluation (First Article Inspection)
4. Ongoing performance monitoring (scorecards)

**Approved Supplier List**: See [10-00-09-40A_Approved_Supplier_List.md](../supplier-management/10-00-09-40A_Approved_Supplier_List.md)

### Critical Material Sourcing

**H2-Compatible Materials**:
- 316L Stainless Steel (AMS 5507, AMS 5524)
- Inconel 625 (AMS 5666, AMS 5599)
- Elgiloy (AMS 5876) for springs
- H2-compatible elastomers (Kalrez, PTFE)

**Cryogenic Materials**:
- 316L Stainless Steel (AMS 5507) for -253°C service
- 5083-H321 Aluminum (AMS 4057) for tanks
- Inconel 718 (AMS 5662) for high-stress components
- G-10 fiberglass-epoxy for thermal breaks

**Standard Materials**:
- 2024-T3 Aluminum for brackets and fittings
- 7075-T6 Aluminum for high-strength applications
- 15-5PH Stainless Steel for corrosion-resistant fittings
- Titanium 6Al-4V for weight-critical components

### Supplier Quality Requirements

All suppliers must comply with: [10-00-09-41A_Supplier_Quality_Requirements.md](../supplier-management/10-00-09-41A_Supplier_Quality_Requirements.md)

## Production Capacity and Scheduling

### Capacity Planning

**Initial Production Rate (Year 1-2 post-EIS)**:
- Aircraft: 2-3 units per month
- Component sets: 3-4 per month (includes spares)

**Full-Rate Production (Year 3+ post-EIS)**:
- Aircraft: 5-8 units per month
- Component sets: 8-12 per month (includes spares)

### Lead Times

See detailed lead time analysis: [10-00-09-61A_Component_Lead_Times.md](../production-schedules/10-00-09-61A_Component_Lead_Times.md)

**Typical Lead Times**:
- Raw materials: 8-16 weeks
- Castings/forgings: 12-20 weeks
- Machined components: 6-12 weeks
- H2 components (with testing): 12-18 weeks
- Cryogenic components (with qualification): 14-20 weeks
- Assembly and final test: 2-4 weeks

### Master Production Schedule

See: [10-00-09-60A_Master_Production_Schedule.md](../production-schedules/10-00-09-60A_Master_Production_Schedule.md)

## Tooling and Equipment

### Production Tooling

**Machining**:
- CNC mills and lathes for precision components
- 5-axis machining centers for complex geometries
- EDM (Electrical Discharge Machining) for tight tolerances

**Welding**:
- Orbital TIG welding systems for tube-to-fitting welds
- Manual TIG welding stations for repair and rework
- Electron beam welding (outsourced) for cryogenic joints

**Special Equipment**:
- Cleanroom facilities (ISO 5-6) for H2 component assembly
- Helium mass spectrometer leak detectors (sensitivity ≤1×10⁻¹⁰ std cc/sec)
- Cryogenic test chambers (-253°C capability)
- Impact testing machines (Charpy V-notch at -196°C)

See complete tooling list: [10-00-09-30A_Tooling_List.md](../tooling-equipment/10-00-09-30A_Tooling_List.md)

## Environmental, Health, and Safety (EHS)

### Hydrogen Safety

**Key Hazards**:
- Flammability (4% to 75% in air)
- Embrittlement of certain materials
- Asphyxiation (displacement of oxygen)
- High-pressure release

**Controls**:
- Designated H2 safety zones with explosion-proof equipment
- Continuous H2 detection and monitoring
- Personnel training on H2 safety
- Emergency response procedures

### Cryogenic Safety

**Key Hazards**:
- Frostbite and cold burns
- Asphyxiation (oxygen displacement by vaporized cryogen)
- Material embrittlement at low temperatures
- Rapid pressure rise in confined spaces

**Controls**:
- Personal protective equipment (cryo gloves, face shields)
- Ventilation systems to prevent oxygen deficiency
- Temperature and oxygen monitoring
- Personnel training on cryogenic handling

### General Safety

- Lockout/tagout (LOTO) procedures
- Machine guarding and safety interlocks
- Personal protective equipment (PPE) per task analysis
- Hazardous material handling and disposal

## Training and Competency

### Required Training

**General Production Workforce**:
- AS9100D quality awareness
- Reading engineering drawings and specifications
- Use of precision measuring instruments
- Documentation and traceability requirements

**Special Process Personnel**:
- NADCAP-qualified welders (per AWS D17.1)
- NDT technicians (NAS-410 Level II certification)
- Heat treatment operators (AMS 2750 training)

**H2 and Cryogenic Specialists**:
- H2 safety awareness and emergency response
- Cryogenic handling and PPE use
- Leak testing procedures and equipment
- Cleanroom protocols

### Competency Verification

- Initial qualification testing
- Annual recertification for critical tasks
- Periodic audits and observations
- Documented training records

## Continuous Improvement

### Lean Manufacturing Initiatives

- Value stream mapping to identify waste
- 5S workplace organization
- Kaizen events for process improvement
- Visual management and standardized work

### Metrics and KPIs

**Quality Metrics**:
- First-pass yield (target: >95%)
- Scrap and rework rate (target: <2%)
- Nonconformance rate (target: <1%)
- Customer returns (target: <0.1%)

**Delivery Metrics**:
- On-time delivery (target: >98%)
- Schedule adherence (target: >95%)
- Lead time reduction (target: 5% annual improvement)

**Cost Metrics**:
- Labor hours per unit (target: 5% annual reduction)
- Material utilization (target: >92%)
- Total cost of ownership

### Corrective and Preventive Action (CAPA)

- Root cause analysis (5 Whys, Fishbone, etc.)
- Corrective action implementation and verification
- Preventive actions to avoid recurrence
- Effectiveness checks at defined intervals

## Integration with Lifecycle Framework

### Upstream Dependencies

**From 10-00-04_Design**:
- Component specifications and drawings
- Bills of material (BOMs)
- Interface control documents (ICDs)

**From 10-00-07_V_AND_V**:
- Test results and qualification data
- Design verification evidence
- Lessons learned from prototyping

**From 10-00-08_Prototyping**:
- Prototype build experience
- Manufacturing feasibility assessments
- Tooling and process validation

### Downstream Outputs

**To 10-00-10_Certification**:
- Manufacturing conformity evidence
- Process qualification records
- Quality system certifications

**To 10-00-11_EIS_VERSIONS_TAGS**:
- Configuration management data
- Serial number assignments
- Production effectivity

**To 10-00-12_Services**:
- Spare parts production plans
- Service bulletins and repair procedures
- Warranty and field support data

## Risk Management

### Major Risks and Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Supplier capacity shortage | Schedule slip | Medium | Dual-source critical components; early supplier engagement |
| H2 material certification delays | Cost increase | Medium | Pre-qualify materials early; maintain material inventory |
| NADCAP process delays | Schedule slip | Low | Use NADCAP-accredited suppliers; plan buffer time |
| Workforce skill shortage | Quality issues | Medium | Early training programs; recruit experienced personnel |
| Cryogenic test equipment unavailability | Schedule slip | Low | Secure long-term test facility access; consider in-house capability |

## References

### Internal Documentation

- [10-00-09-02A_Tiedown_Manufacturing_Plan.md](10-00-09-02A_Tiedown_Manufacturing_Plan.md)
- [10-00-09-04A_H2_Components_Manufacturing.md](10-00-09-04A_H2_Components_Manufacturing.md)
- [10-00-09-05A_Cryo_Components_Manufacturing.md](10-00-09-05A_Cryo_Components_Manufacturing.md)
- [10-00-09-20A_Quality_Control_Plan.md](../quality-control/10-00-09-20A_Quality_Control_Plan.md)
- [10-00-09-60A_Master_Production_Schedule.md](../production-schedules/10-00-09-60A_Master_Production_Schedule.md)

### External Standards

- **AS9100D**: Quality Management Systems - Requirements for Aviation, Space and Defense Organizations
- **AS9102**: Aerospace First Article Inspection Requirement
- **AS9145**: Advanced Product Quality Planning (APQP) and Production Part Approval Process (PPAP)
- **AWS D17.1**: Specification for Fusion Welding for Aerospace Applications
- **ASME B31.12**: Hydrogen Piping and Pipelines
- **SAE AS6968**: Hydrogen Aircraft Systems Requirements
- **AMS 2750**: Pyrometry
- **NADCAP**: National Aerospace and Defense Contractors Accreditation Program

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-10

### Revision History

| Revision | Date | Author | Description | Approved By |
|----------|------|--------|-------------|-------------|
| A | 2025-12-10 | AI (GitHub Copilot) / A. Pelliccia | Initial release | TBD |

---

**End of Document**
