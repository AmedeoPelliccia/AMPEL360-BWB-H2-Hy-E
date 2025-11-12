# Build Standard Control

**Component Code:** 02-10-00  
**Component Name:** AIRCRAFT_GENERAL_DATA  
**Subfolder:** 09_PRODUCTION_PLANNING/SERIAL_NUMBER_MANAGEMENT  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100 INTEGRA

## Overview

This document defines the process for establishing, managing, and controlling build standards for AMPEL360 aircraft production. Build standard control ensures configuration consistency, traceability, and efficient implementation of design changes throughout the production lifecycle.

## Build Standard Definition

### What is a Build Standard?

A **Build Standard** is a defined configuration baseline that specifies:
- Engineering design documents and revisions
- Part numbers and specifications
- Manufacturing processes and procedures
- Quality control requirements
- Software versions
- Supplier components and specifications

**Purpose:**
- Ensure aircraft are built to consistent, approved configuration
- Control implementation of design changes
- Define effectivity of modifications
- Support certification and type design compliance

### Build Standard Hierarchy

#### Level 1: Type Design
- Certified type design per Type Certificate
- Defines basic aircraft model
- Establishes certification basis
- Fixed unless major type certificate amendment

#### Level 2: Production Build Standard
- Specific production configuration
- Incorporates approved design changes
- Defines standard equipment and options
- Version controlled (e.g., v1.0, v1.1, v2.0)

#### Level 3: Aircraft-Specific Configuration
- Individual aircraft variations
- Customer-specific options
- Equipment variations within build standard
- Serial number-specific modifications

## Build Standard Structure

### Build Standard Designation
**Format:** [Model]-BS-[Version]

**Example:** Q100-BS-1.0 (First production build standard)

**Version Numbering:**
- **Major version (X.0):** Significant design changes, requires certification review
- **Minor version (X.Y):** Incremental improvements, changes within type design
- **Revision (X.Y.Z):** Editorial corrections, clarifications, no design impact

### Build Standard Contents

#### 1. Configuration Index
- Master list of all design documents
- Part numbers and specifications
- Drawing numbers and revisions
- Software versions
- Material specifications

#### 2. Engineering Change Summary
- List of engineering changes incorporated
- Change effectivity by serial number
- Rationale for each change
- Certification impact assessment

#### 3. Equipment List
- Standard equipment for build standard
- Optional equipment available
- Equipment part numbers and specifications
- Weight and CG effects

#### 4. Manufacturing Instructions
- Assembly procedures applicable to build standard
- Special tooling or processes
- Quality inspection requirements
- Testing and acceptance criteria

#### 5. Supplier Configuration
- Supplier components and versions
- Supplier specifications and standards
- Quality requirements for suppliers
- Component traceability requirements

## Build Standard Development Process

### Phase 1: Initial Build Standard (Prototype)

**Objective:** Establish baseline for prototype aircraft

**Activities:**
1. **Design Freeze**
   - Engineering design documents baselined
   - Critical design reviews completed
   - Manufacturing readiness assessed
   - Preliminary certification compliance demonstrated

2. **Build Standard Documentation**
   - Create prototype build standard document
   - List all design documents and revisions
   - Define manufacturing processes
   - Establish quality control requirements

3. **Approval**
   - Engineering approval of build standard
   - Manufacturing review and acceptance
   - Quality assurance concurrence
   - Program management approval

**Deliverable:** Prototype Build Standard (e.g., Q100-BS-P1.0)  
**Timeline:** Design freeze + 2 months  
**Effectivity:** MSN-P001 (Prototype aircraft)

### Phase 2: Pre-Production Build Standard

**Objective:** Transition from prototype to production-ready configuration

**Activities:**
1. **Prototype Lessons Learned**
   - Review prototype build experience
   - Identify design improvements
   - Assess manufacturing challenges
   - Incorporate test results

2. **Design Changes**
   - Implement prototype lessons learned
   - Optimize for production efficiency
   - Reduce weight if possible
   - Improve manufacturability

3. **Build Standard Update**
   - Update design document list
   - Document all changes from prototype
   - Update manufacturing instructions
   - Revise quality control procedures

4. **Validation**
   - Build pre-production aircraft to new standard
   - Validate manufacturing processes
   - Confirm quality and performance
   - Certification authority review

**Deliverable:** Pre-Production Build Standard (e.g., Q100-BS-PP1.0)  
**Timeline:** Prototype completion + 6 months  
**Effectivity:** MSN-PP001 to MSN-PP010

### Phase 3: Production Build Standard

**Objective:** Establish stable, certified production configuration

**Activities:**
1. **Certification Compliance**
   - Ensure all certification requirements met
   - Document compliance demonstrations
   - Resolve outstanding certification issues
   - Obtain authority approval

2. **Production Optimization**
   - Streamline manufacturing processes
   - Reduce production costs
   - Improve quality and repeatability
   - Optimize supply chain

3. **Build Standard Finalization**
   - Final design document package
   - Complete equipment list
   - Manufacturing process documentation
   - Quality assurance plan

4. **Type Certificate Approval**
   - Build standard approved as part of Type Certificate
   - TCDS references build standard
   - Production Certificate (if applicable)

**Deliverable:** Production Build Standard (e.g., Q100-BS-1.0)  
**Timeline:** Type Certificate issuance  
**Effectivity:** MSN-001 onwards

### Phase 4: Build Standard Updates

**Objective:** Manage ongoing improvements and changes

**Activities:**
1. **Change Evaluation**
   - Review proposed design changes
   - Assess impact on production
   - Determine certification impact
   - Cost-benefit analysis

2. **Effectivity Planning**
   - Determine which aircraft receive change
   - Plan implementation timing
   - Coordinate with production schedule
   - Manage inventory transition

3. **Build Standard Revision**
   - Update build standard documentation
   - Issue new build standard version
   - Communicate to all stakeholders
   - Update configuration database

4. **Implementation**
   - Implement change in production
   - Verify change incorporation
   - Quality control verification
   - Update aircraft records

**Deliverable:** Updated Build Standard (e.g., Q100-BS-1.1, Q100-BS-2.0)  
**Timeline:** As changes are approved and implemented  
**Effectivity:** Specified MSN range for each change

## Build Standard Control Procedures

### Change Control Process

#### Step 1: Change Request
- Engineering or other department submits change request
- Documented justification and benefits
- Initial impact assessment
- Preliminary approval by Chief Engineer

#### Step 2: Change Evaluation
- Detailed technical review
- Manufacturing impact assessment
- Certification impact analysis
- Cost analysis (development, implementation, certification)
- Schedule impact assessment

#### Step 3: Change Approval
- Configuration Control Board (CCB) review
- Approval decision (approve, defer, reject)
- Effectivity determination (which aircraft)
- Implementation plan

#### Step 4: Build Standard Update
- Update build standard documentation
- Assign new build standard version
- Document change in revision history
- Communicate to all stakeholders

#### Step 5: Implementation
- Implement change in production
- Update manufacturing instructions
- Train personnel if required
- Verify correct implementation

#### Step 6: Verification
- Quality assurance verification
- First article inspection (if significant change)
- Performance verification
- Certification compliance check

### Effectivity Management

#### Effectivity Types

**1. Serial Number Effectivity**
- Change effective starting at specific MSN
- Example: "Effective MSN-015 and subsequent"
- Most common for production changes

**2. Modification Effectivity**
- Change incorporated via Service Bulletin
- Retroactive application to earlier aircraft
- Example: "All aircraft, incorporate per SB Q100-01"

**3. Customer Option Effectivity**
- Change only for specific customers
- Optional equipment or configuration
- Example: "MSN-023, 025, 027 (Customer A option)"

**4. Time/Date Effectivity**
- Change effective after specific date
- Used for regulatory compliance changes
- Example: "All aircraft produced after 2030-01-01"

#### Effectivity Documentation
- Clear statement of effectivity in build standard
- Visual indicators in engineering documents
- Database tracking of effectivity
- Production planning integration

### Build Standard Configuration Baseline

**Components of Baseline:**
1. **Design Data**
   - Engineering drawings (with revision level)
   - 3D CAD models (with version)
   - Specifications and standards
   - Analysis and test reports

2. **Manufacturing Data**
   - Manufacturing plans and procedures
   - Work instructions
   - Tooling and equipment specifications
   - Quality control plans

3. **Software/Firmware**
   - Flight control software version
   - Avionics software versions
   - CAOS system software version
   - Ground support software

4. **Supplier Data**
   - Supplier part numbers and revisions
   - Supplier specifications
   - Supplier quality requirements
   - Supplier test requirements

## BWB-Specific Build Standard Considerations

### Composite Structure Build Standards
- Composite material specifications and suppliers
- Layup schedules and curing processes
- Inspection requirements for composite parts
- Repair procedures for composite structure

### H₂ Fuel System Build Standards
- H₂ tank specifications (type, supplier, certification)
- Cryogenic system components
- Safety system requirements
- Ground support equipment compatibility

### Fuel Cell Propulsion Build Standards
- Fuel cell stack type and version
- Electric motor specifications
- Power distribution configuration
- Cooling system specification

### CAOS System Build Standards
- Digital twin software version
- AI algorithm version
- Sensor suite configuration
- Ground station software compatibility

## Integration with Production Systems

### Product Lifecycle Management (PLM)
- Build standard stored in PLM system
- Automatic linkage to aircraft MSN
- Version control and change tracking
- Access control and security

### Manufacturing Execution System (MES)
- Build standard drives work instructions
- Real-time verification of correct parts
- Assembly process guidance
- Quality control checkpoints

### Enterprise Resource Planning (ERP)
- Bill of materials from build standard
- Inventory management by build standard
- Procurement planning
- Cost tracking by build standard

## Quality Assurance

### Build Standard Verification
- Independent verification of build standard content
- Cross-check design data with PLM system
- Verify effectivity and change documentation
- Peer review by senior engineers

### Production Compliance
- First article inspection for new build standard
- Sample audits throughout production
- Traceability verification
- As-built configuration comparison to build standard

### Non-Conformance Management
- Document deviations from build standard
- Engineering disposition of non-conformances
- Tracking of rework and repairs
- Feedback to build standard control

## Reporting and Metrics

### Build Standard Status Report
**Frequency:** Monthly

**Content:**
- Current build standard in production
- Upcoming build standard changes
- Aircraft in production by build standard
- Change implementation status

### Build Standard Change Log
**Frequency:** Continuous

**Content:**
- All changes to build standard
- Effectivity of each change
- Justification and approval
- Implementation status

### Production Configuration Audit
**Frequency:** Quarterly

**Content:**
- Verify aircraft built to correct build standard
- Identify any configuration discrepancies
- Corrective actions required
- Trends and issues

## Related Documents
- Engineering Change Order (ECO) Procedures
- Configuration Management Plan
- Type Certificate Data Sheet (TCDS)
- Service Bulletin Procedures
- ATA 02-12-00: BWB Configuration Data
- ATA 95-00-00: Digital Product Passport

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-05 | AMPEL360 Configuration Management | Initial release |

---

**Document Control:**
- Version: 1.0
- Status: Active
- Classification: Configuration Critical
- Next Review: Prior to prototype build standard freeze
