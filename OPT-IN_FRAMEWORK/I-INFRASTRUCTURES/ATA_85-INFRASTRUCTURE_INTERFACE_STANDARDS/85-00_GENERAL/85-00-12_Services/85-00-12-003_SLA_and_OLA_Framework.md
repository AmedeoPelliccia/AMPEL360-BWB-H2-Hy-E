# SLA and OLA Framework (ATA 85)

## Document Information

- **Document ID**: 85-00-12-003
- **Title**: SLA and OLA Framework
- **Version**: 1.0
- **Date**: 2025-11-21
- **Status**: Draft
- **Category**: Services
- **ATA Chapter**: 85 - Infrastructure Interface Standards

---

## 1. Introduction

This document establishes the framework for Service Level Agreements (SLAs) and Operating Level Agreements (OLAs) for ATA 85 Infrastructure Interface Standards. It defines standard service metrics, measurement methods, and agreement structures to ensure consistent service delivery across the BWB ecosystem.

### 1.1 Purpose

- Define standard SLA/OLA structure and components
- Establish service metrics and measurement methodology
- Provide templates for stakeholder-specific agreements
- Enable consistent service level management

---

## 2. SLA Framework Structure

### 2.1 Standard SLA Components

Every SLA for ATA 85 services includes:

1. **Service Description**: Clear definition of services covered
2. **Service Hours**: Availability window (e.g., 24/7, business hours)
3. **Performance Targets**: Quantitative metrics and thresholds
4. **Responsibilities**: Clear roles for service provider and consumer
5. **Escalation Procedures**: Contact points and escalation paths
6. **Measurement and Reporting**: How metrics are calculated and reported
7. **Review and Improvement**: Periodic review cadence and process
8. **Penalties and Credits**: Consequences for SLA breaches (if applicable)
9. **Exceptions**: Exclusions and force majeure conditions

### 2.2 SLA Types

**Type A - External SLAs**: Between OEM and external parties (airlines, airports, infrastructure operators)

**Type B - Internal OLAs**: Between internal teams (engineering, operations, digital services)

**Type C - Underpinning Contracts**: With third-party suppliers and service providers

---

## 3. Service Metrics Framework

### 3.1 Availability Metrics

**Infrastructure Uptime**
- **Definition**: Percentage of time infrastructure interface is operational and available
- **Calculation**: (Total Time - Downtime) / Total Time × 100%
- **Target**: ≥99.5% for critical interfaces (H₂, primary power, data)
- **Measurement Period**: Calendar month
- **Exclusions**: Planned maintenance windows (pre-approved)

**Service Desk Availability**
- **Definition**: Percentage of time service desk is reachable
- **Calculation**: (Calls Answered Within SLA / Total Calls) × 100%
- **Target**: ≥99.0% within 30 seconds
- **Measurement Period**: 24/7 continuous

### 3.2 Response Metrics

**Incident Response Time**
- **Definition**: Time from incident report to initial response
- **Measurement**: Automated timestamp in ticketing system
- **Targets by Priority**:
  - P1 (Critical): <15 minutes
  - P2 (High): <30 minutes
  - P3 (Medium): <2 hours
  - P4 (Low): <8 hours

**On-Site Response Time**
- **Definition**: Time from dispatch to engineer arrival on-site
- **Measurement**: GPS/timestamp verification
- **Targets**:
  - Major Airports (P1/P2): <2 hours
  - Regional Airports (P1/P2): <4 hours
  - All Airports (P3): <24 hours

### 3.3 Resolution Metrics

**Resolution Time**
- **Definition**: Time from incident report to issue resolved
- **Measurement**: Ticket lifecycle in ITSM system
- **Targets by Priority**:
  - P1 (Critical): <4 hours
  - P2 (High): <24 hours
  - P3 (Medium): <1 week
  - P4 (Low): <1 month

**First-Time Fix Rate**
- **Definition**: Percentage of incidents resolved on first contact/visit
- **Calculation**: (First-Time Fixes / Total Resolutions) × 100%
- **Target**: ≥85%

### 3.4 Quality Metrics

**Customer Satisfaction (CSAT)**
- **Definition**: Customer rating of service delivery
- **Measurement**: Post-incident survey (1-5 scale)
- **Target**: ≥4.5/5.0 average
- **Sample**: Minimum 80% response rate for P1/P2 incidents

**Repeat Incident Rate**
- **Definition**: Percentage of incidents recurring within 30 days
- **Calculation**: (Repeat Incidents / Total Incidents) × 100%
- **Target**: <5%

**Escalation Rate**
- **Definition**: Percentage of incidents requiring escalation beyond L1
- **Calculation**: (Escalated Incidents / Total Incidents) × 100%
- **Target**: <20% for L2, <5% for L3

---

## 4. SLA Templates

### 4.1 Airport Interface SLA (Type A)

Reference: [ASSETS/SLAs/85-00-12-A-101_SLA_Template_Airport_Interfaces.md](ASSETS/SLAs/85-00-12-A-101_SLA_Template_Airport_Interfaces.md)

**Parties**: OEM ↔ Airport Authority

**Services Covered**:
- Gate interface systems (power, data, boarding bridges)
- Passenger boarding infrastructure support
- Emergency evacuation interface systems
- Technical support and training

**Key Metrics**:
- Infrastructure Uptime: ≥99.5%
- P1 Response: <15 minutes
- P1 Resolution: <4 hours
- CSAT: ≥4.5/5.0

### 4.2 H₂/CO₂ Provider SLA (Type A)

Reference: [ASSETS/SLAs/85-00-12-A-102_SLA_Template_H2_CO2_Providers.md](ASSETS/SLAs/85-00-12-A-102_SLA_Template_H2_CO2_Providers.md)

**Parties**: OEM ↔ H₂ Infrastructure Operator / CO₂ Battery Provider

**Services Covered**:
- H₂ refueling interface support
- CO₂ cartridge logistics coordination
- Safety system integration
- Joint incident management

**Key Metrics**:
- Refueling System Uptime: ≥99.0%
- CO₂ Cartridge Availability: ≥99.5%
- Joint Incident Response: <30 minutes
- Safety Event Response: Immediate

### 4.3 Internal OLA Template (Type B)

Reference: [ASSETS/SLAs/85-00-12-A-103_OLA_Internal_Teams_Template.md](ASSETS/SLAs/85-00-12-A-103_OLA_Internal_Teams_Template.md)

**Parties**: Service Operations ↔ Internal Teams (Engineering, Digital Services, DPP Team)

**Services Covered**:
- L3 engineering support
- Digital twin data provision
- DPP update services
- Design change support

**Key Metrics**:
- L3 Response: <4 hours (P1)
- Design Authority Decision: <48 hours
- Digital Twin Data Latency: <5 minutes
- DPP Update Completion: <24 hours

---

## 5. Measurement and Reporting

### 5.1 Data Collection

**Automated Collection**:
- ITSM system timestamps (incident lifecycle)
- Infrastructure monitoring systems (uptime, performance)
- Digital twin telemetry (real-time status)
- Survey platform (CSAT scores)

**Manual Collection**:
- On-site arrival verification (GPS/timestamp)
- Customer satisfaction surveys
- Quality audits and spot checks

### 5.2 Reporting Cadence

**Real-Time Dashboards**:
- Current incident status
- SLA compliance indicators
- Infrastructure health status

**Weekly Reports**:
- SLA compliance summary
- Incident volume and trends
- Critical issues and major incidents

**Monthly Reports**:
- Detailed SLA performance against targets
- Trend analysis and patterns
- Service improvement initiatives

**Quarterly Business Reviews**:
- Strategic performance review
- SLA target adjustments
- Service model refinements
- Investment and improvement planning

---

## 6. SLA Breach Management

### 6.1 Breach Classification

**Minor Breach**: Single metric missed by <10% in a month
**Major Breach**: Single metric missed by ≥10% or multiple minor breaches
**Critical Breach**: Safety-related SLA missed or repeated major breaches

### 6.2 Breach Response Process

1. **Detection**: Automated alert from monitoring system
2. **Investigation**: Root cause analysis within 48 hours
3. **Corrective Action**: Implementation plan within 1 week
4. **Customer Communication**: Notification and explanation
5. **Prevention**: Process improvement to prevent recurrence
6. **Documentation**: Breach log and lessons learned

### 6.3 Service Credits (where applicable)

**Minor Breach**: 5% monthly service fee credit
**Major Breach**: 10% monthly service fee credit
**Critical Breach**: 20% monthly service fee credit + accelerated corrective action

Note: Credits apply to commercial agreements only, not internal OLAs.

---

## 7. Service Level Review Process

### 7.1 Monthly Reviews

**Participants**: Service delivery manager, customer representative
**Agenda**:
- SLA performance review
- Incident trend analysis
- Outstanding issues
- Improvement opportunities

**Output**: Action log and improvement plan

### 7.2 Quarterly Business Reviews

**Participants**: Senior stakeholders from both parties
**Agenda**:
- Strategic performance assessment
- Service model effectiveness
- SLA target appropriateness
- Investment needs and priorities
- Roadmap alignment

**Output**: Updated service plan and SLA amendments (if needed)

### 7.3 Annual SLA Refresh

Complete SLA review and negotiation:
- Performance data analysis
- Benchmark against industry standards
- Technology and operational changes
- Cost and pricing adjustments
- Contract renewal or amendment

---

## 8. Exclusions and Exceptions

### 8.1 Planned Maintenance

**Pre-approved Windows**: Maintenance activities scheduled with ≥7 days notice are excluded from uptime calculations

**Emergency Maintenance**: Unplanned maintenance to prevent safety issues or major failures (approval within 4 hours)

### 8.2 Force Majeure

SLA obligations are suspended during:
- Natural disasters (earthquakes, floods, severe weather)
- Acts of war or terrorism
- Pandemics or government-mandated shutdowns
- Utilities failure beyond control (power grid failure)

### 8.3 Customer-Caused Issues

SLA does not apply when:
- Issue caused by customer error or unauthorized changes
- Customer delays response or access
- Customer does not follow agreed procedures
- Third-party issues beyond OEM control (where specified)

---

## 9. Integration with Digital Twin and DPP

### 9.1 Automated SLA Monitoring

Digital twin integration provides:
- Real-time infrastructure status for uptime calculation
- Automated incident detection and logging
- Performance metric collection
- Predictive SLA breach warnings

### 9.2 DPP Integration

Service events update DPP:
- Maintenance activities logged
- Component replacements recorded
- Performance history tracked
- Lifecycle milestones documented

---

## 10. Continuous Improvement

### 10.1 Service Improvement Plans (SIPs)

Developed when:
- SLA consistently missed (3 consecutive months)
- Customer satisfaction below threshold
- Significant operational changes
- New technology or process opportunities

**SIP Components**:
- Current state assessment
- Gap analysis
- Improvement initiatives
- Investment requirements
- Timeline and milestones
- Success metrics

### 10.2 Best Practice Sharing

- Cross-airport service excellence examples
- Lessons learned database
- Innovation showcase (quarterly)
- Industry benchmarking

---

## 11. Related Documents

- [85-00-12-001_Service_Model_Infrastructure_Interfaces.md](85-00-12-001_Service_Model_Infrastructure_Interfaces.md) - Service model overview
- [85-00-12-002_Operational_Support_Model.md](85-00-12-002_Operational_Support_Model.md) - Support structure
- [85-00-12-007_Service_Performance_and_Continuous_Improvement.md](85-00-12-007_Service_Performance_and_Continuous_Improvement.md) - Performance management
- [ASSETS/Monitoring/85-00-12-A-302_Service_KPI_Definitions.xlsx](ASSETS/Monitoring/85-00-12-A-302_Service_KPI_Definitions.xlsx) - Detailed KPI definitions

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (A-LIVE-GP, ATA 85 pattern)
- **Change Authority**: Infrastructure Interfaces CCB (I-CCB-85)
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Last AI update: 2025-11-21.
