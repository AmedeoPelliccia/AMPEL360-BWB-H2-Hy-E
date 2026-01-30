# GSE Information to UTCS/DPP Integration Assembly

**Assembly ID**: 03-00-04-ASM-003  
**Integration**: GSE Information System ↔ UTCS/DPP (Unified Traceability & Circularity System / Digital Product Passport)  
**Version**: 1.0  
**Status**: DRAFT

## Purpose

Defines the integration architecture between the Ground Support Equipment (GSE) Information System and UTCS/DPP (Unified Traceability & Circularity System / Digital Product Passport), enabling comprehensive lifecycle tracking, sustainability metrics, and compliance documentation for GSE assets.

## UTCS/DPP Overview

The **Digital Product Passport (DPP)** is a digital record that follows a product throughout its lifecycle, from manufacturing through end-of-life. For GSE equipment, the DPP captures:

- **Provenance**: Manufacturing origin, materials, suppliers
- **Configuration**: Technical specifications, capabilities, modifications
- **Operational History**: Usage logs, performance metrics, location history
- **Maintenance Records**: Repairs, parts replacements, inspections
- **Sustainability Metrics**: Energy consumption, carbon footprint, circular economy indicators
- **Compliance**: Certifications, regulatory approvals, safety records

The **Unified Traceability & Circularity System (UTCS)** is the enterprise platform that manages DPPs across all AMPEL360 assets, including aircraft, GSE, and components.

## Integration Objectives

### Primary Goals
1. **Complete Lifecycle Traceability**: Track GSE from procurement to disposal
2. **Sustainability Reporting**: Enable carbon accounting and circular economy metrics
3. **Compliance Documentation**: Maintain regulatory records and certifications
4. **Asset Optimization**: Inform procurement, maintenance, and retirement decisions

### Key Benefits
- **Regulatory Compliance**: Meet EU Battery Regulation, CSRD, and future DPP mandates
- **Sustainability Leadership**: Demonstrate environmental responsibility with data
- **Cost Optimization**: Data-driven decisions on equipment lifecycle management
- **Enhanced Resale Value**: Comprehensive records increase secondary market value

## Architecture Overview

### Integration Pattern: Event-Driven Updates with Periodic Synchronization

```
┌─────────────────────────┐          ┌─────────────────────────┐
│   GSE Info System       │          │     UTCS/DPP Platform   │
│                         │          │                         │
│  ┌──────────────────┐   │          │  ┌──────────────────┐   │
│  │  Lifecycle       │───┼──────────┼─▶│  DPP Record      │   │
│  │  Event Producer  │   │  Events  │  │  Manager         │   │
│  └──────────────────┘   │          │  └──────────────────┘   │
│                         │          │           │             │
│  ┌──────────────────┐   │          │           ▼             │
│  │  DPP Query       │◀──┼──────────┼──┌──────────────────┐   │
│  │  Client          │   │   API    │  │  Blockchain/     │   │
│  └──────────────────┘   │          │  │  Ledger Storage  │   │
│                         │          │  └──────────────────┘   │
└─────────────────────────┘          └─────────────────────────┘
```

## Data Flows

### 1. Equipment Onboarding → DPP Creation

**Direction**: GSE Info System → UTCS/DPP  
**Trigger**: New equipment added to GSE fleet  
**Protocol**: RESTful API (synchronous)

**Data Elements**:
```json
{
  "event_type": "equipment_onboarding",
  "timestamp": "2025-12-07T10:00:00Z",
  "equipment": {
    "id": "GSE-TUG-025",
    "type": "aircraft_tug",
    "manufacturer": "TLD",
    "model": "JetGo 75",
    "serial_number": "TLD-JG75-2025-1234",
    "manufacturing_date": "2025-08-15",
    "purchase_date": "2025-11-01",
    "purchase_cost": 125000.00,
    "currency": "EUR"
  },
  "specifications": {
    "power_type": "electric",
    "battery_capacity_kwh": 150,
    "towing_capacity_kg": 75000,
    "max_speed_kmh": 25,
    "charging_type": "CCS2"
  },
  "sustainability": {
    "material_composition": {
      "steel": 60,
      "aluminum": 20,
      "composites": 10,
      "electronics": 5,
      "other": 5
    },
    "recyclability_percentage": 85,
    "embodied_carbon_kg_co2": 12500
  }
}
```

**UTCS/DPP Action**: Create new DPP record with unique identifier, store on blockchain/ledger

### 2. Operational Events → DPP Updates

**Direction**: GSE Info System → UTCS/DPP  
**Trigger**: Significant operational milestones  
**Protocol**: Event streaming (Apache Kafka)  
**Frequency**: Real-time (on event occurrence)

**Event Types**:
- **Usage Event**: Equipment used for service task
- **Maintenance Event**: Scheduled/unscheduled maintenance performed
- **Location Change**: Equipment transferred between facilities
- **Configuration Change**: Hardware/software modification
- **Incident Event**: Accident, damage, safety occurrence

**Example - Usage Event**:
```json
{
  "event_type": "usage_event",
  "timestamp": "2025-12-07T14:30:00Z",
  "equipment_id": "GSE-TUG-025",
  "dpp_id": "DPP-GSE-TUG-025-UUID",
  "usage": {
    "task_type": "aircraft_tow",
    "aircraft_type": "A320",
    "duration_minutes": 18,
    "distance_km": 2.5,
    "energy_consumed_kwh": 4.2,
    "operator_id": "OPS-12345",
    "location": "JFK_Terminal_4"
  },
  "cumulative": {
    "total_operating_hours": 1250.5,
    "total_distance_km": 3420,
    "total_energy_kwh": 5680
  }
}
```

**Example - Maintenance Event**:
```json
{
  "event_type": "maintenance_event",
  "timestamp": "2025-12-07T09:00:00Z",
  "equipment_id": "GSE-TUG-025",
  "dpp_id": "DPP-GSE-TUG-025-UUID",
  "maintenance": {
    "type": "scheduled",
    "work_order": "WO-2025-12-001",
    "description": "Annual inspection and battery health check",
    "technician_id": "TECH-567",
    "parts_replaced": [
      {
        "part_number": "TLD-BRAKE-PAD-001",
        "quantity": 4,
        "cost": 320.00
      }
    ],
    "labor_hours": 6.5,
    "total_cost": 1100.00,
    "next_due_date": "2026-12-07"
  }
}
```

### 3. DPP Query → Retrieve Equipment History

**Direction**: GSE Info System ← UTCS/DPP  
**Trigger**: Operator/manager requests equipment history  
**Protocol**: RESTful API (synchronous)

**Request**:
```http
GET /api/v1/dpp/gse/GSE-TUG-025?include=history,maintenance,sustainability
Authorization: Bearer <JWT_TOKEN>
```

**Response**:
```json
{
  "dpp_id": "DPP-GSE-TUG-025-UUID",
  "equipment_id": "GSE-TUG-025",
  "current_status": "operational",
  "location": "JFK_Terminal_4",
  "manufacturing": {
    "manufacturer": "TLD",
    "date": "2025-08-15",
    "origin": "France"
  },
  "lifecycle_phase": "operational",
  "age_months": 4,
  "operational_summary": {
    "total_operating_hours": 1250.5,
    "total_distance_km": 3420,
    "utilization_rate_percent": 65,
    "availability_rate_percent": 92
  },
  "maintenance_summary": {
    "last_maintenance": "2025-12-07",
    "next_due": "2026-12-07",
    "total_maintenance_cost": 8200.00,
    "unscheduled_events": 2
  },
  "sustainability_metrics": {
    "total_energy_consumed_kwh": 5680,
    "carbon_footprint_kg_co2": 1420,
    "energy_efficiency_kwh_per_km": 1.66,
    "renewable_energy_percentage": 40
  },
  "recent_events": [
    {
      "timestamp": "2025-12-07T14:30:00Z",
      "type": "usage_event",
      "description": "Aircraft tow - A320 - 18 minutes"
    },
    {
      "timestamp": "2025-12-07T09:00:00Z",
      "type": "maintenance_event",
      "description": "Annual inspection completed"
    }
  ]
}
```

### 4. Sustainability Reporting → Aggregate Metrics

**Direction**: GSE Info System → UTCS/DPP  
**Trigger**: Periodic (daily/monthly) or on-demand  
**Protocol**: Batch API or scheduled ETL

**Aggregated Data**:
- Fleet-wide energy consumption (by equipment type, location)
- Carbon emissions (direct + grid electricity footprint)
- Circular economy indicators (repair rate, parts reuse, end-of-life recycling)
- Compliance status (certifications, inspections, regulatory)

**UTCS/DPP Action**: Generate sustainability reports, feed into corporate ESG reporting

## DPP Data Model

### Core DPP Schema

```yaml
DPP_Record:
  dpp_id: unique identifier (UUID or blockchain hash)
  equipment_id: GSE asset ID
  created_at: timestamp
  updated_at: timestamp
  
  Identity:
    manufacturer: string
    model: string
    serial_number: string
    manufacturing_date: date
    purchase_info:
      date: date
      cost: float
      supplier: string
      warranty_expiration: date
  
  Specifications:
    type: enum [tug, gpu, fueling, cleaning, catering, ...]
    power_type: enum [electric, diesel, hybrid, hydrogen]
    capacity: object (capacity metrics by type)
    dimensions: {length, width, height} in meters
    weight_kg: float
  
  Operational_History:
    total_operating_hours: float
    total_tasks_completed: int
    total_distance_km: float (if applicable)
    utilization_rate: float (percentage)
    availability_rate: float (percentage)
    
  Maintenance_Records:
    - timestamp: datetime
      type: enum [scheduled, unscheduled, inspection, repair]
      work_order: string
      description: text
      technician: string
      parts_replaced: array
      cost: float
      downtime_hours: float
  
  Sustainability:
    energy_consumed_kwh: float
    carbon_footprint_kg_co2: float
    renewable_energy_percentage: float
    material_composition: object (percentages by material)
    recyclability_percentage: float
    end_of_life_plan: text
  
  Compliance:
    certifications: array
      - type: string
        issuer: string
        issue_date: date
        expiration_date: date
        status: enum [valid, expired, pending]
    inspections: array
      - date: date
        inspector: string
        result: enum [pass, fail, conditional]
        notes: text
  
  Lifecycle_Status:
    phase: enum [procurement, commissioning, operational, maintenance, decommissioned]
    condition: enum [excellent, good, fair, poor, unserviceable]
    estimated_remaining_life_years: float
    end_of_life_date: date (estimated or actual)
    disposal_method: enum [resale, refurbishment, recycling, scrapping]
```

## Integration Architecture

### Components

#### 1. DPP Event Publisher (in GSE Info System)
- Monitors operational database for lifecycle events
- Transforms events to DPP-compatible format
- Publishes to UTCS/DPP via Kafka or API
- Implements idempotency (prevents duplicate events)

#### 2. DPP Query Client (in GSE Info System)
- Provides interface for operators to access DPP data
- Caches frequently accessed DPP records
- Handles authentication and authorization

#### 3. DPP Record Manager (in UTCS/DPP Platform)
- Ingests events from GSE and other systems
- Updates DPP records in database and blockchain
- Enforces data validation and business rules
- Provides API for queries and reports

#### 4. Blockchain Ledger (Optional, in UTCS/DPP)
- Stores immutable hashes of critical DPP events
- Provides tamper-proof audit trail
- Enables third-party verification (regulators, auditors, buyers)

### Technology Stack

**Message Broker**: Apache Kafka  
**DPP Database**: PostgreSQL (operational), MongoDB (document store)  
**Blockchain**: Hyperledger Fabric or Ethereum (private chain)  
**API Gateway**: GraphQL (flexible queries) + REST (standard CRUD)  
**Authentication**: OAuth 2.0 / OpenID Connect  
**Data Format**: JSON / JSON-LD (for linked data)

## Use Cases

### Use Case 1: Regulatory Compliance Audit

**Scenario**: Aviation authority requests proof of GSE equipment safety certifications

**Steps**:
1. Auditor queries UTCS/DPP for all GSE equipment at specific airport
2. System returns DPP records with certification status, inspection dates
3. Auditor verifies blockchain hashes for tamper-proof records
4. Report generated showing compliance status for each piece of equipment

### Use Case 2: Sustainability Reporting (ESG/CSRD)

**Scenario**: AMPEL360 prepares annual sustainability report

**Steps**:
1. Finance team requests GSE fleet carbon footprint from UTCS/DPP
2. System aggregates energy consumption, applies emission factors
3. Report shows: total emissions, trend over time, comparison to targets
4. Data exported to corporate ESG reporting platform

### Use Case 3: Equipment End-of-Life Decision

**Scenario**: GSE-TUG-025 reaches 10 years of age, decision needed on future

**Steps**:
1. Maintenance manager queries DPP for equipment history
2. System shows: total operating hours, maintenance costs, current condition
3. Financial analysis: residual value vs. repair costs vs. replacement
4. Decision: Refurbish and redeploy or sell on secondary market
5. DPP updated with end-of-life plan and eventual disposition

### Use Case 4: Parts Traceability

**Scenario**: Defective battery recall by supplier

**Steps**:
1. Supplier issues recall notice for specific battery lot numbers
2. UTCS/DPP searches all DPP records for affected parts
3. System identifies GSE equipment with recalled batteries
4. Automatic work orders generated for battery replacement
5. DPP records updated with replacement parts and new serial numbers

## Performance Requirements

| Metric | Target | Notes |
|--------|--------|-------|
| Event Ingestion Latency | <10 seconds | From GSE event to DPP update |
| Query Response Time | <500ms | For individual DPP record retrieval |
| Report Generation Time | <5 minutes | For fleet-wide sustainability report |
| Data Retention | Indefinite | Lifecycle data retained permanently |
| Blockchain Confirmation | <1 minute | For critical events requiring immutability |

## Security & Privacy

### Data Classification
- **Public**: Equipment type, manufacturer, general specifications
- **Internal**: Operational metrics, maintenance costs, utilization
- **Confidential**: Purchase prices, supplier contracts, incident details

### Access Control
- **Operators**: Read access to operational data
- **Maintenance**: Read/write access to maintenance records
- **Managers**: Read access to all data, write access to configuration
- **Auditors**: Read-only access with audit trail logging
- **Third Parties**: Limited access via API keys (e.g., for resale verification)

### Data Protection
- Encryption at rest (AES-256) and in transit (TLS 1.3)
- GDPR compliance: Anonymize operator personal data
- Blockchain privacy: Only hashes stored on-chain, full data off-chain

## Compliance & Standards

### Regulatory Alignment
- **EU Battery Regulation**: Track battery lifecycle, sustainability metrics
- **CSRD (Corporate Sustainability Reporting Directive)**: ESG data capture
- **EU Digital Product Passport**: Future-ready for DPP mandates
- **ISO 14001**: Environmental management system integration

### Industry Standards
- **ISO 55000**: Asset management best practices
- **IATA Ground Operations Manual (IGOM)**: GSE operational standards
- **SAE standards**: For equipment specifications and testing

## Testing & Validation

### Integration Testing
- Mock UTCS/DPP environment for GSE system testing
- Synthetic event generation to validate data flows
- End-to-end traceability tests (onboarding to disposal)

### Data Quality Testing
- Validation of event schema compliance
- Duplicate detection and prevention
- Data completeness checks (required fields populated)

### Performance Testing
- Load testing (1000+ events per minute)
- Query performance (sub-second response for 10,000+ DPP records)
- Blockchain scalability (transaction throughput)

### Acceptance Criteria
- [ ] All lifecycle events captured in DPP within 10 seconds
- [ ] 100% of equipment has complete DPP record
- [ ] Sustainability reports accurate within ±5%
- [ ] Blockchain audit trail verifiable by external parties

## Traceability

- **Parent Assembly**: [03-00-04-ASM-001_GSE_Info_System_Assembly.md](./03-00-04-ASM-001_GSE_Info_System_Assembly.md)
- **Related Requirements**: RQ-03-04-005 (DPP integration requirement)
- **Related Assemblies**: [03-00-04-ASM-004_GSE_Info_Circularity_Assembly.md](./03-00-04-ASM-004_GSE_Info_Circularity_Assembly.md)
- **Related Systems**: ATA 95 (Digital Product Passport architecture)
- **Verification**: Test cases in `../../../03-00-07_V_AND_V/`

## Open Issues & Future Work

- [ ] Define data retention policies for decommissioned equipment
- [ ] Evaluate public blockchain vs. private consortium chain
- [ ] Establish interoperability standards for DPP data exchange with OEMs
- [ ] Plan for integration with supplier DPP systems (battery, tire manufacturers)
- [ ] Investigate AI-powered anomaly detection in DPP data (fraud, inconsistencies)

## Document Control

- **Version**: 1.0
- **Status**: DRAFT – Subject to human review and approval
- **Author**: Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia
- **Last Updated**: 2025-12-07
- **Approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

**Related Documents**:
- [03-00-04-ASM-001_GSE_Info_System_Assembly.md](./03-00-04-ASM-001_GSE_Info_System_Assembly.md)
- [03-00-04-ASM-002_GSE_Info_to_CAOS_Assembly.md](./03-00-04-ASM-002_GSE_Info_to_CAOS_Assembly.md)
- [03-00-04-ASM-004_GSE_Info_Circularity_Assembly.md](./03-00-04-ASM-004_GSE_Info_Circularity_Assembly.md)
- [ATA 95 Digital Product Passport](../../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)
