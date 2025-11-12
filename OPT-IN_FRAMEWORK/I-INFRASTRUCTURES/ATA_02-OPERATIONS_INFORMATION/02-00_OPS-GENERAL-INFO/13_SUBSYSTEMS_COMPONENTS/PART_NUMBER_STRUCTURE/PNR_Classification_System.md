# PNR Classification System

**Document ID:** PNR-CLS-001  
**Version:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

## 1. Overview

The PNR Classification System provides a structured taxonomy for categorizing all parts, assemblies, and systems within the AMPEL360 BWB H₂ Hy-E Q100 INTEGRA operational equipment inventory.

## 2. Classification Hierarchy

### 2.1 Primary Classification (Level 1)

All parts classified by **ATA Chapter** first:

| ATA Chapter | Category | Description |
|-------------|----------|-------------|
| **02** | Operations Information | Ground operations, flight planning, documentation |
| **28** | Fuel Systems | H₂ storage and distribution |
| **71** | Power Plant | Fuel cells and propulsion |
| **95** | Neural Networks | CAOS and digital systems |

### 2.2 Secondary Classification (Level 2)

Within each ATA chapter, parts classified by **System Type**:

#### For ATA 02 - Operations Information:

| Type Code | System Type | Examples |
|-----------|-------------|----------|
| **10** | Flight Planning | Performance calculators, route planning |
| **20** | Weight & Balance | Load management systems |
| **32** | H₂ Operations | Refueling equipment, safety systems |
| **GSE** | Ground Support | Towing, power, air start equipment |
| **EMG** | Emergency | Response kits, fire suppression |
| **DOC** | Documentation | EFB, publications, manuals |
| **TRN** | Training | Simulators, training devices |

### 2.3 Tertiary Classification (Level 3)

Parts further classified by **Functional Category**:

| Category | Description | Typical Items |
|----------|-------------|---------------|
| **Mechanical** | Moving parts, structures | Doors, panels, mechanisms |
| **Electrical** | Power, control circuits | Sensors, actuators, controllers |
| **Electronic** | Computing, data processing | CPUs, displays, interfaces |
| **Software** | Programs, firmware | Applications, operating systems |
| **Pneumatic** | Air/gas systems | Valves, compressors, hoses |
| **Hydraulic** | Fluid power systems | Pumps, cylinders, accumulators |
| **Consumable** | Single-use items | Seals, filters, lubricants |
| **Tools** | Maintenance equipment | Special tools, test equipment |

## 3. Part Type Classification

### 3.1 Physical Part Types

| Type | Definition | Characteristics | Example |
|------|------------|-----------------|---------|
| **System** | Complete integrated system | Multiple subsystems | H₂ Refueling System |
| **Subsystem** | Major functional group | Multiple assemblies | Refueling Control Subsystem |
| **Assembly** | Multi-component unit | 2+ components | Refueling Panel Assembly |
| **Subassembly** | Component group within assembly | Integrated unit | Panel Door Assembly |
| **Component** | Individual functional part | Single item | Lock Actuator |
| **Part** | Basic building block | Cannot be disassembled | Bolt, washer, seal |

### 3.2 Non-Physical Types

| Type | Definition | Example |
|------|------------|---------|
| **Software** | Programs, firmware, code | CAOS Core System v2.0 |
| **Kit** | Collection of parts | Seal Kit, Tool Kit |
| **Set** | Grouped items for specific use | Emergency Response Set |
| **Service** | Support offering | Software license, training |
| **Data** | Information products | Manuals, procedures, databases |

## 4. Lifecycle Classification

### 4.1 Development Status

| Status | Definition | Usage |
|--------|------------|-------|
| **Conceptual** | Initial design phase | Requirements definition |
| **Developmental** | Design in progress | Prototyping, testing |
| **Pre-Production** | Design complete, not certified | Final validation |
| **Production** | Certified for use | Active manufacturing |
| **Mature** | Stable, long-term production | Established design |
| **Sunset** | Phase-out planned | Seeking replacement |
| **Obsolete** | No longer available | Legacy support only |

### 4.2 Operational Status

| Status | Definition | Action Required |
|--------|------------|-----------------|
| **Active** | Currently in use | Standard procurement |
| **Superseded** | Replaced by newer version | Use cross-reference |
| **Discontinued** | Manufacturer stopped | Source alternative |
| **On Hold** | Temporarily unavailable | Wait or substitute |
| **Restricted** | Special approval needed | Regulatory/safety issues |

## 5. Criticality Classification

### 5.1 Safety Criticality

| Level | Definition | Examples | Requirements |
|-------|------------|----------|--------------|
| **Critical** | Failure causes catastrophic hazard | H₂ shutoff valves, fire suppression | Dual source, strict QA |
| **Essential** | Failure causes major safety issue | Leak detectors, emergency lighting | Single source allowed, strict QA |
| **Important** | Failure impacts operations | EFB tablets, communication equipment | Standard QA |
| **Standard** | Failure causes minor impact | Protective cases, stands | Basic QA |

### 5.2 Mission Criticality

| Level | Impact of Failure | Example |
|-------|-------------------|---------|
| **Flight Critical** | Cannot dispatch aircraft | Refueling receptacle |
| **MEL Category A** | Max 24h dispatch | Backup power supply |
| **MEL Category B** | Max 72h dispatch | Secondary display |
| **MEL Category C** | Max 10 days dispatch | Training equipment |
| **MEL Category D** | Indefinite deferral | Convenience items |

## 6. Source Classification

### 6.1 By Origin

| Classification | Definition | Example |
|----------------|------------|---------|
| **OEM Design** | AMPEL360 designed | CAOS software |
| **Custom Manufactured** | Built to AMPEL360 spec | Refueling panel |
| **COTS (Commercial Off-The-Shelf)** | Standard catalog item | NVIDIA GPU |
| **MOTS (Modified Off-The-Shelf)** | COTS with modifications | Custom EFB tablet |
| **Government Furnished** | Provided by authority | Certification test equipment |

### 6.2 By Sourcing Strategy

| Strategy | Definition | Rationale | Example |
|----------|------------|-----------|---------|
| **Single Source** | One approved supplier | Unique capability, IP | CAOS Processing Unit |
| **Sole Source** | Only one supplier available | Market limitation | Specialized H₂ valve |
| **Dual Source** | Two approved suppliers | Risk mitigation | Temperature sensors |
| **Multi Source** | 3+ approved suppliers | Commodity item | Standard fasteners |

## 7. Regulatory Classification

### 7.1 Certification Requirements

| Class | Description | Standards | Examples |
|-------|-------------|-----------|----------|
| **Type Certified** | Part of aircraft certification | CS-25, FAR-25 | Refueling system |
| **TSO Approved** | Technical Standard Order | TSO-CXXX | Avionics components |
| **PMA Approved** | Parts Manufacturer Approval | FAA PMA | Replacement parts |
| **Standard Parts** | Industry standards | AN, MS, NAS | Fasteners |
| **COTS Qualified** | Commercial qualification | DO-160, DO-178 | Electronic components |

### 7.2 Export Control

| Classification | Description | Requirements |
|----------------|-------------|--------------|
| **EAR99** | Not specifically controlled | Standard export docs |
| **ITAR** | Defense-related | State Dept license |
| **Dual Use** | Commercial/military | Commerce license |
| **EU Controlled** | EU strategic goods | EU approval |

## 8. Maintenance Classification

### 8.1 Maintenance Category

| Category | Description | Typical Actions |
|----------|-------------|-----------------|
| **Line Maintenance** | Quick turnaround | Visual inspection, servicing |
| **Base Maintenance** | Scheduled deeper checks | Component replacement |
| **Shop Maintenance** | Off-aircraft repair | Overhaul, calibration |
| **Depot Maintenance** | Major overhaul | Complete rebuild |

### 8.2 Repair vs Replace

| Classification | Definition | Decision Factors |
|----------------|------------|------------------|
| **Expendable** | Discard after use | Cost, contamination |
| **Consumable** | Limited life, replace | Wear, certification limits |
| **Rotable** | Repair and reuse | Economic, technical feasibility |
| **Repairable** | Can be restored | Cost-effective repair |
| **Non-Repairable** | Discard at failure | Safety, complexity, cost |

## 9. Supply Chain Classification

### 9.1 Inventory Strategy

| Strategy | Description | Typical Items |
|----------|-------------|---------------|
| **Stock to Order** | Purchase on demand | Long-lead, expensive items |
| **Safety Stock** | Minimum on-hand | Critical spares |
| **Consignment** | Supplier-owned inventory | High-volume consumables |
| **JIT (Just-In-Time)** | Delivered as needed | Common COTS items |

### 9.2 Provisioning Priority

| Priority | Description | Stocking Level |
|----------|-------------|----------------|
| **A - Critical** | Must be available | 100% coverage |
| **B - Important** | Should be available | 80% coverage |
| **C - Standard** | Can be procured quickly | 50% coverage |
| **D - Non-Critical** | Order as needed | Minimal/no stock |

## 10. Environmental Classification

### 10.1 Material Category

| Category | Examples | Restrictions |
|----------|----------|--------------|
| **Hazardous Materials** | Batteries, chemicals | MSDS, shipping limits |
| **Restricted Substances** | Lead, mercury | RoHS, REACH compliance |
| **Controlled Materials** | Composites, metals | Import/export rules |
| **Recyclable** | Metals, plastics | End-of-life handling |

### 10.2 Operating Environment

| Environment | Conditions | Examples |
|-------------|------------|----------|
| **Benign** | Office, hangar | EFB tablets, tools |
| **Ground** | Ramp, tarmac | GSE, refueling equipment |
| **Cockpit** | Controlled environment | Displays, controls |
| **Exterior** | Weather exposed | Antennas, sensors |
| **Cargo** | Unpressurized, temperature vary | Cargo equipment |

## 11. Data Management

### 11.1 Classification Fields in Master Registry

Each part in Master_Part_Number_Registry.csv includes:
- Primary: Part_Number, Type, Category
- Source: Manufacturer, CAGE_Code
- Status: Status, Superseded_By
- Technical: Weight, Material, Dimensions
- Supply: Unit_Cost, Lead_Time, MOQ
- Regulatory: Certification, Export_Control
- Maintenance: MTBF, Repair_Level

### 11.2 Classification Updates

- Review quarterly for status changes
- Update on ECO implementation
- Audit annually for accuracy
- Document classification rationale

## 12. Search and Filter Capabilities

### 12.1 Multi-Dimensional Search

Users can find parts by any combination of:
- ATA chapter
- System type
- Functional category
- Part type
- Criticality level
- Source strategy
- Status

### 12.2 Example Queries

**Query:** "All active H₂ refueling components from single sources"
- **Filters:** ATA=02, Subsystem=32, Status=Active, Source=Single

**Query:** "Critical safety parts needing inspection"
- **Filters:** Criticality=Critical, Maintenance=Due

## 13. References

- Part_Number_Management_System.md
- PNR_Nomenclature_Standard.md
- Component_Breakdown_Structure.md
- Master_Part_Number_Registry.csv

---

**Document Control:**
- **Version:** 1.0
- **Status:** Active
- **Approved By:** Configuration Management Lead
- **Next Review Date:** 2026-05-05
- **Owner:** Systems Engineering
