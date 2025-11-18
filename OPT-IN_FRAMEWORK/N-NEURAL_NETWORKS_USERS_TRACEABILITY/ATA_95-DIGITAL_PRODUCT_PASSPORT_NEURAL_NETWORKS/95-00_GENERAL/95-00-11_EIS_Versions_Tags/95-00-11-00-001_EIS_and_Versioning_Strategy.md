# 95-00-11-00-001: EIS and Versioning Strategy

**Document ID:** 95-00-11-00-001  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**Owner:** AMPEL360 Configuration Management Team  

---

## 1. Purpose

This document establishes the overarching strategy for Entry Into Service (EIS) management and versioning within the AMPEL360 BWB H₂ Hy-E aircraft program. It defines how configuration baselines, software/model versions, and Digital Product Passport (DPP) entries are coordinated throughout the aircraft lifecycle—from initial development through EIS, fleet operations, and eventual retirement.

---

## 2. Scope

This strategy applies to:

- **Aircraft Systems**: All ATA chapters and subsystems
- **Neural Networks**: AI/ML models used in CAOS and flight systems
- **Digital Product Passport**: Blockchain-anchored configuration records
- **Software & Firmware**: Avionics, flight control, and support systems
- **Hardware Configurations**: Physical components and variants
- **Data & Training Sets**: ML datasets and versioning
- **Documentation**: Technical publications and operator manuals

---

## 3. Strategic Objectives

### 3.1 Traceability
- Ensure complete traceability from requirements through design, V&V, certification, and operations
- Link every deployed configuration to its certification basis and test evidence
- Maintain audit trails for regulatory compliance (EASA, FAA)

### 3.2 Safety & Airworthiness
- Guarantee that only approved configurations are deployed to aircraft
- Support rapid identification and resolution of safety issues
- Enable efficient Airworthiness Directives (AD) and Service Bulletin (SB) management

### 3.3 Operational Excellence
- Minimize aircraft downtime through predictive version management
- Enable phased rollouts and controlled experiments (A/B testing)
- Support operator-specific and fleet-specific configurations

### 3.4 Innovation Velocity
- Allow rapid iteration in development/test environments
- Provide clear promotion paths from experiment to production
- Support continuous improvement through fleet learning

---

## 4. Core Principles

### 4.1 Semantic Versioning
All versions follow semantic versioning: **MAJOR.MINOR.PATCH**
- **MAJOR**: Breaking changes, recertification required
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, no functional changes

### 4.2 Configuration as Code
- All configurations stored in version-controlled repositories
- Immutable baselines identified by Git tags
- Infrastructure-as-Code for deployment environments

### 4.3 Baseline Management
- **Development Baseline**: Rapidly evolving, experimental
- **Integration Baseline**: Feature-complete, undergoing V&V
- **Certification Baseline**: Frozen, submitted to authorities
- **Production Baseline**: Certified, deployed to fleet
- **Maintenance Baseline**: Production + approved patches

### 4.4 DPP Integration
- Every significant configuration change recorded in DPP
- Blockchain anchoring for immutability and auditability
- Privacy-preserving design (operator data protected)

---

## 5. Version Hierarchy

```
EIS Version (e.g., v2.3.1)
├── Aircraft Configuration Baseline
│   ├── Hardware Version (BOM)
│   ├── Software/Firmware Versions
│   └── Calibration Data
├── Neural Network Models
│   ├── Flight Control NN (v1.4.2)
│   ├── Energy Management NN (v2.1.0)
│   └── Predictive Maintenance NN (v1.3.5)
├── DPP Version
│   ├── Configuration Hash
│   ├── Blockchain Anchor
│   └── Evidence Package
└── Documentation Set
    ├── Flight Manual (Rev C)
    ├── Maintenance Manual (Rev B)
    └── Training Materials (v2.3)
```

---

## 6. EIS Phases

The AMPEL360 program follows a structured EIS approach:

1. **Pre-EIS (Development)**: Initial design and testing
2. **Early EIS (Limited Launch)**: First 3-5 aircraft with launch customer
3. **Progressive EIS**: Phased rollout to additional operators
4. **Full EIS**: General availability to all operators
5. **Mature Operations**: Continuous improvement and fleet-wide learning

---

## 7. Version Control Integration

### 7.1 Git Strategy
- **Main Branch**: Production-ready, certified code
- **Release Branches**: Preparation for certification (`release/v2.3`)
- **Feature Branches**: Development work (`feature/enhanced-autopilot`)
- **Hotfix Branches**: Emergency fixes (`hotfix/v2.3.1-fuel-leak`)

### 7.2 Tagging Convention
```
v{MAJOR}.{MINOR}.{PATCH}-{PHASE}-{ENVIRONMENT}
Examples:
  v2.3.1-prod-flight        # Production release
  v2.4.0-beta-simulator     # Beta in simulator
  v2.3.2-hotfix-fleet-42    # Emergency patch for specific fleet
```

---

## 8. Change Management

All version changes follow the Configuration Control Board (CCB) process:

1. **Change Request (CR)**: Proposed modification
2. **Impact Analysis**: Safety, certification, cost assessment
3. **CCB Review**: Approval/rejection decision
4. **Implementation**: Develop, test, verify
5. **Certification**: If required, authority approval
6. **Deployment**: Phased rollout to fleet
7. **Post-Deployment**: Monitoring and validation

---

## 9. Compliance & Regulatory

This versioning strategy supports:

- **EASA CS-25**: Certification specifications for large aircraft
- **DO-178C**: Software considerations in airborne systems
- **DO-254**: Hardware design assurance
- **EASA CM-SWCEH-001**: Software and complex hardware certification
- **EU AI Act**: Transparency and documentation for high-risk AI
- **EU Digital Product Passport**: Circularity and lifecycle data

---

## 10. Interfaces to Other Documents

- **95-00-11-00-002**: Configuration Management Principles for Neural Networks
- **95-00-11-01-xxx**: Versioning Model details
- **95-00-11-02-xxx**: Tagging and naming conventions
- **95-00-11-03-xxx**: Configuration baselines
- **95-00-11-04-xxx**: EIS phases and rollout strategies
- **95-00-10-xxx**: Certification documentation
- **95-00-07-xxx**: V&V evidence per version

---

## 11. Metrics & KPIs

Success of this strategy measured by:

- **Mean Time to Deploy (MTTD)**: < 48 hours for patches
- **Version Rollback Rate**: < 5% of deployments
- **Configuration Drift**: Zero unauthorized changes
- **Certification Efficiency**: 20% reduction in recertification time
- **Operator Satisfaction**: > 90% approval rating for update process

---

## 12. Governance

- **Strategy Owner**: Chief Engineer, AMPEL360
- **Review Frequency**: Quarterly or upon major program milestone
- **Approval Authority**: Configuration Control Board (CCB)
- **Stakeholders**: Engineering, Operations, Quality, Certification, Operators

---

## 13. Document Control

| Revision | Date | Author | Changes |
|----------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 CM Team | Initial release |

---

## 14. References

- ATA iSpec 2200: Information Standards for Aviation Maintenance
- S1000D: International specification for technical publications
- DO-326A/ED-202A: Airworthiness Security Process Specification
- ISO 10007: Quality management — Guidelines for configuration management
- GAMP 5: Good Automated Manufacturing Practice guide for validation

---

**Document Classification:** Internal Use  
**Next Review Date:** 2026-02-17  
**Contact:** config-mgmt@ampel360.aero
