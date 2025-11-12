# Manufacturer Serial Number (MSN) Assignment Process

**Component Code:** 02-10-00  
**Component Name:** AIRCRAFT_GENERAL_DATA  
**Subfolder:** 09_PRODUCTION_PLANNING/SERIAL_NUMBER_MANAGEMENT  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100 INTEGRA

## Overview

This document establishes the process for assigning, managing, and tracking Manufacturer Serial Numbers (MSN) for AMPEL360 aircraft throughout the production lifecycle. Proper serial number management is critical for traceability, configuration control, and regulatory compliance.

## Serial Number Structure

### MSN Format
**Format:** AMPEL360-[Model]-[Sequential Number]

**Components:**
- **Manufacturer Prefix:** AMPEL360 (company identifier)
- **Model Code:** Q100 (aircraft model designation)
- **Sequential Number:** 001, 002, 003... (unique aircraft identifier)

**Example:** AMPEL360-Q100-001 (First production aircraft)

### Alternative Short Format
**Format:** MSN-[Number]

**Example:** MSN-001, MSN-002, etc.

**Usage:** Internal documentation, shop floor identification, shorthand reference

### Civil Registration
**Format:** Country-dependent (e.g., D-XXXX for Germany, N-XXXXX for USA)

**Note:** Civil registration is assigned by operator/owner and is separate from MSN, but must be tracked alongside MSN.

## MSN Assignment Authority

### Responsibility
- **Primary Authority:** Program Management Office
- **Assignment Approval:** Chief Engineer or designee
- **Record Keeping:** Configuration Management
- **System Administration:** IT/Database Administrator

### Assignment Criteria
- MSN assigned upon formal start of aircraft production
- Sequential assignment in order of production start
- MSN cannot be reused or reassigned
- Prototype aircraft receive special "P" designation (e.g., MSN-P001)

## MSN Assignment Process

### Step 1: Production Authorization
**Trigger:** Production work order approved for new aircraft

**Activities:**
1. Sales or program management initiates production request
2. Production planning verifies capacity and schedule
3. Chief Engineer approves start of production
4. Finance confirms funding authorization

**Output:** Approved production work order

### Step 2: MSN Reservation
**Trigger:** Production authorization received

**Activities:**
1. Configuration management reserves next available MSN
2. MSN entered into configuration database
3. Placeholder aircraft record created
4. Notification sent to all relevant departments

**Output:** Reserved MSN with placeholder data

### Step 3: MSN Assignment
**Trigger:** First major component production starts

**Activities:**
1. Configuration management formally assigns MSN to aircraft
2. Physical MSN identification plates ordered
3. MSN marked on primary structure
4. All production documentation linked to MSN

**Output:** Formally assigned MSN

### Step 4: MSN Marking
**Trigger:** Primary structure assembly begins

**Activities:**
1. Apply permanent MSN data plate to primary structure
2. Apply temporary MSN markings to sub-assemblies
3. Photograph MSN plate installation
4. Verify MSN marking compliance

**Output:** Physically marked aircraft structure

### Step 5: MSN Activation
**Trigger:** Aircraft final assembly starts

**Activities:**
1. MSN status changed from "assigned" to "in production"
2. All systems and suppliers notified of MSN activation
3. Component traceability to MSN begins
4. Production tracking systems activated

**Output:** Active MSN in production

## MSN Data Plate Requirements

### Primary Data Plate Location
**Location:** Forward fuselage/center body, accessible for inspection

**Content:**
- Manufacturer name: AMPEL360 Aircraft Industries
- Aircraft type/model: AMPEL360 BWB H₂ Hy-E Q100 INTEGRA
- Manufacturer Serial Number: MSN-XXX
- Date of manufacture: [Month/Year]
- Type Certificate number: [TC-XXX]
- Production certificate number: [PC-XXX] (if applicable)

### Data Plate Specifications
- **Material:** Corrosion-resistant stainless steel or aluminum
- **Mounting:** Riveted to primary structure (not removable)
- **Marking:** Engraved or stamped (permanent, legible)
- **Size:** Minimum 100mm x 75mm
- **Compliance:** EASA/FAA data plate requirements

### Secondary Identification
- MSN stenciled on primary structure in multiple locations
- Temporary MSN tags on major sub-assemblies
- Electronic RFID tag embedded (for CAOS tracking)
- QR code for digital access to aircraft data

## MSN Tracking and Management

### Configuration Database
**System:** Product Lifecycle Management (PLM) database

**MSN Record Contents:**
- MSN and aircraft identification
- Production status and milestone dates
- Build standard and configuration
- Installed equipment and serial numbers
- Weight and balance data
- Test and inspection results
- Certification status
- Delivery information

### MSN Status Tracking
**Status Categories:**
1. **Reserved:** MSN reserved but production not started
2. **In Production:** Aircraft in manufacturing process
3. **Final Assembly:** Aircraft in final assembly
4. **Testing:** Aircraft in ground and flight testing
5. **Certification:** Aircraft in certification process
6. **Delivery Preparation:** Aircraft ready for customer delivery
7. **Delivered:** Aircraft delivered to customer
8. **In Service:** Aircraft in operational service

### Status Updates
- Real-time status updates as milestones achieved
- Automated notifications to stakeholders
- Status dashboard for program visibility
- Historical status tracking for analysis

## Prototype and Special Aircraft

### Prototype Designation
**Format:** MSN-P[Number]

**Examples:**
- MSN-P001: First prototype
- MSN-P002: Second prototype (if required)

**Characteristics:**
- Not for commercial sale/operation
- Used for development, testing, certification
- May have non-standard configuration
- Converted to production standard or retired

### Pre-Production Aircraft
**Format:** MSN-PP[Number]

**Examples:**
- MSN-PP001: First pre-production aircraft

**Characteristics:**
- Production-representative configuration
- Used for final certification and validation
- May be converted for customer delivery
- Incorporates lessons learned from prototype

### Test Aircraft
**Format:** MSN-T[Number]

**Purpose:**
- Dedicated structural test articles
- Systems test beds
- Fatigue test articles
- Not for flight operations

## MSN and Component Traceability

### Major Assembly Traceability
**Components with Serial Numbers:**
- Primary structure sections (center body, wing sections)
- Fuel cell stacks and propulsion components
- H₂ storage tanks
- Landing gear assemblies
- Flight control computers
- Major avionics systems

**Traceability Requirements:**
- Component serial number linked to aircraft MSN
- Installation date and location recorded
- Certification documents linked to component
- Removal and replacement history tracked

### Supply Chain Integration
**Supplier Requirements:**
- Suppliers provide component serial numbers
- Traceability documentation with each component
- Material certifications linked to MSN
- Test results and quality records

**Data Flow:**
- Supplier data entered into PLM system
- Automatic link to aircraft MSN
- Real-time visibility to component status
- Digital thread from component to aircraft

## MSN and Regulatory Compliance

### Type Certificate Data Sheet (TCDS)
- MSN range for which TCDS is valid
- Build standard effectivity by MSN
- Configuration differences by MSN block

### Airworthiness Certificate
- MSN on airworthiness certificate
- Certificate specific to MSN
- Renewal and export certificates reference MSN

### Service Bulletins and Airworthiness Directives
- Effectivity defined by MSN range
- Compliance tracking by MSN
- Modification records linked to MSN

## CAOS Integration

### Digital Twin Initialization
- MSN creates unique digital twin instance
- As-built configuration loaded from MSN data
- Real-time synchronization throughout life
- MSN-specific performance models

### Fleet Management
- MSN-based fleet tracking
- Aircraft performance comparison by MSN
- Service experience analysis by MSN
- Predictive maintenance by MSN

### Blockchain Traceability
- MSN and component blockchain records
- Immutable history of aircraft lifecycle
- Digital product passport linked to MSN
- Secure data sharing across stakeholders

## MSN Assignment for Production Phases

### Prototype Phase
- **MSN Range:** MSN-P001 to MSN-P00X
- **Quantity:** 1-3 prototypes
- **Purpose:** Development, testing, certification
- **Disposition:** Converted or retired after certification

### Pre-Production Phase
- **MSN Range:** MSN-PP001 to MSN-PP010
- **Quantity:** Up to 10 aircraft
- **Purpose:** Final validation, early customer deliveries
- **Disposition:** Customer delivery with limited warranty

### Production Phase
- **MSN Range:** MSN-001 to MSN-XXX
- **Quantity:** Serial production run
- **Purpose:** Customer deliveries
- **Disposition:** Operational aircraft

## Quality Assurance

### MSN Assignment Verification
- Dual verification of MSN assignment
- Check for duplicate MSN (system prevents)
- Verify MSN sequence continuity
- Audit trail for all MSN assignments

### Data Plate Installation Verification
- Quality inspector verifies installation
- Photograph of data plate on aircraft
- Legibility and accuracy check
- Compliance with specifications

### MSN Tracking Accuracy
- Periodic audit of MSN database
- Physical verification sample audits
- Reconciliation of MSN records
- Discrepancy investigation and resolution

## Documentation and Reporting

### MSN Assignment Report
**Frequency:** Each assignment

**Content:**
- Assigned MSN
- Customer (if known)
- Production start date
- Expected delivery date
- Initial configuration

### Production Status Report
**Frequency:** Weekly/Monthly

**Content:**
- MSN production status summary
- Milestone completion by MSN
- Issues and delays by MSN
- Forecast delivery dates

### MSN Master List
**Frequency:** Continuous (living document)

**Content:**
- All assigned MSN
- Current status
- Customer assignments
- Delivery dates
- Configuration summary

## Related Documents
- ATA 02-19-00: Aircraft Identification Data
- ATA 95-00-00: Digital Product Passport and Traceability
- Configuration Management Plan
- Production Control Plan
- Quality Assurance Manual

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-05 | AMPEL360 Configuration Management | Initial release |

---

**Document Control:**
- Version: 1.0
- Status: Active
- Classification: Configuration Critical
- Next Review: Prior to first MSN assignment
