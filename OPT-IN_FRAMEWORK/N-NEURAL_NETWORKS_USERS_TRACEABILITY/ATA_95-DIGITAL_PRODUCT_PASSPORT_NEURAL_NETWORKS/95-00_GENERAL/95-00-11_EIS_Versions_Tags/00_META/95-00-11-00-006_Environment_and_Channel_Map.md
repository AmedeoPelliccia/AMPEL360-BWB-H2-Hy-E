# 95-00-11-00-006: Environment and Channel Map

**Document ID:** 95-00-11-00-006  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**Owner:** AMPEL360 DevOps Team  

---

## 1. Purpose

Define all deployment environments and channels used throughout the AMPEL360 lifecycle, from development through production operations, ensuring clear separation and controlled promotion paths.

---

## 2. Environment Hierarchy

```
Development Environments
├── LOCAL: Developer workstations
├── DEV: Shared development environment
├── CI: Continuous integration pipelines
└── SANDBOX: Experimental features

Test Environments
├── INT: Integration testing
├── SIM: Flight simulator environments
├── HIL: Hardware-in-the-loop test rigs
└── FT: Flight test aircraft

Pre-Production Environments
├── VAL: Validation and verification
├── CERT: Certification submission baseline
└── STAGING: Pre-production mirror

Production Environments
├── PROD-CANARY: Limited rollout (1-5%)
├── PROD-BETA: Early adopters (5-20%)
└── PROD-GA: General availability (100%)
```

---

## 3. Environment Specifications

### 3.1 Development Environments

#### LOCAL
- **Purpose**: Individual developer experimentation
- **Access**: Engineering team members
- **Data**: Synthetic/anonymized only
- **Version Control**: Feature branches
- **Deployment**: Manual, on-demand
- **Monitoring**: Local logs
- **Lifetime**: Ephemeral (deleted when branch merged)

#### DEV
- **Purpose**: Shared development and early integration
- **Access**: Engineering team
- **Data**: Synthetic test data
- **Version Control**: `develop` branch
- **Deployment**: Automated on commit
- **Monitoring**: Basic logging to ELK stack
- **Lifetime**: Persistent
- **Infrastructure**: 
  - 2x Application servers (4 vCPU, 16 GB RAM)
  - 1x PostgreSQL database
  - 1x Redis cache
  - Kubernetes cluster (3 nodes)

#### CI
- **Purpose**: Automated testing and validation
- **Access**: CI/CD pipelines only
- **Data**: Test fixtures and mocks
- **Version Control**: All branches
- **Deployment**: Triggered by commits/PRs
- **Monitoring**: Test results dashboard
- **Lifetime**: Ephemeral (per test run)
- **Tools**: GitHub Actions, Jenkins, pytest, Jest

#### SANDBOX
- **Purpose**: Experimental features not yet in main development
- **Access**: Research team, specific engineers
- **Data**: Synthetic or small production samples (anonymized)
- **Version Control**: `experimental/*` branches
- **Deployment**: Manual approval
- **Monitoring**: Basic logging
- **Lifetime**: Time-boxed (30-90 days)

---

### 3.2 Test Environments

#### INT (Integration)
- **Purpose**: System integration testing across all ATA chapters
- **Access**: Engineering, QA teams
- **Data**: Production-like synthetic data
- **Version Control**: `integration` branch
- **Deployment**: Weekly scheduled releases
- **Monitoring**: Full telemetry, performance metrics
- **Lifetime**: Persistent
- **Infrastructure**:
  - 5x Application servers (8 vCPU, 32 GB RAM)
  - PostgreSQL cluster (primary + replica)
  - Redis cluster (3 nodes)
  - Kubernetes cluster (5 nodes)
  - Simulated aircraft systems (mock hardware)

#### SIM (Simulator)
- **Purpose**: Full flight simulator integration
- **Access**: Flight test team, certification engineers
- **Data**: Real-world scenarios, test flight profiles
- **Version Control**: `release/*` branches
- **Deployment**: Manual, controlled releases
- **Monitoring**: Real-time flight data recording
- **Lifetime**: Persistent
- **Hardware**:
  - Full flight simulator (Level D equivalent)
  - Real-time computation cluster (16x 16-core CPUs)
  - Visual system (220° field of view)
  - Motion platform (6-DOF)

#### HIL (Hardware-in-the-Loop)
- **Purpose**: Integration of actual flight hardware with simulation
- **Access**: Hardware engineers, systems integration team
- **Data**: Component-level test vectors
- **Version Control**: `release/*` branches
- **Deployment**: Manual, firmware flashing
- **Monitoring**: Oscilloscopes, logic analyzers, custom telemetry
- **Lifetime**: Persistent
- **Hardware**:
  - Flight control computers (actual units)
  - Sensor suites (IMU, GPS, air data)
  - Actuator test rigs
  - Power distribution units
  - Real-time simulation host

#### FT (Flight Test)
- **Purpose**: Actual flight testing on test aircraft
- **Access**: Flight test team, certification authorities
- **Data**: Real flight data (stored for certification)
- **Version Control**: `release/*` or `cert/*` branches
- **Deployment**: Manual, with authorities present
- **Monitoring**: Full flight data recording + telemetry downlink
- **Lifetime**: Persistent (data archived permanently)
- **Aircraft**: FT-001 (first conforming prototype)

---

### 3.3 Pre-Production Environments

#### VAL (Validation)
- **Purpose**: Final V&V before certification submission
- **Access**: V&V team, QA, certification engineers
- **Data**: Certification test scenarios
- **Version Control**: `cert/*` branches (frozen)
- **Deployment**: Manual, CCB-approved only
- **Monitoring**: Full audit trail, all logs retained
- **Lifetime**: Persistent until certification complete
- **Compliance**: DO-178C, DO-254, CS-25 procedures

#### CERT (Certification)
- **Purpose**: Configuration submitted to EASA/FAA
- **Access**: Certification team, authorities
- **Data**: Official certification evidence
- **Version Control**: Git tags (immutable)
- **Deployment**: None (baseline reference only)
- **Monitoring**: Read-only audit logs
- **Lifetime**: Permanent (regulatory requirement)
- **Traceability**: Complete requirements → evidence chain

#### STAGING
- **Purpose**: Production mirror for final pre-deployment validation
- **Access**: Operations team, senior engineers
- **Data**: Sanitized production data
- **Version Control**: `main` branch (candidate releases)
- **Deployment**: Automated from main, manual approval gate
- **Monitoring**: Production-identical monitoring
- **Lifetime**: Persistent
- **Infrastructure**: Identical to production (scaled down 25%)

---

### 3.4 Production Environments

#### PROD-CANARY
- **Purpose**: Controlled rollout to minimal fleet (1-5% of aircraft)
- **Access**: Operations team, on-call engineers
- **Aircraft**: Selected test aircraft in revenue service
- **Deployment**: Manual, staged over 24-48 hours
- **Monitoring**: Enhanced monitoring, automatic rollback triggers
- **Rollback**: Automatic if anomalies detected
- **Duration**: 7-14 days before wider rollout
- **Selection**: Early adopter operators, short-haul routes

#### PROD-BETA
- **Purpose**: Expanded rollout to early adopter operators (5-20%)
- **Access**: Operations team
- **Aircraft**: Operators who opted into beta program
- **Deployment**: Staged over 1-2 weeks
- **Monitoring**: Standard production monitoring
- **Rollback**: Manual decision based on fleet performance
- **Duration**: 30-60 days before GA
- **Selection**: Operators with strong maintenance capabilities

#### PROD-GA (General Availability)
- **Purpose**: Full production deployment to entire fleet
- **Access**: Operations team (read-only for most)
- **Aircraft**: All certified aircraft
- **Deployment**: Phased rollout over 4-8 weeks
- **Monitoring**: Standard production monitoring
- **Rollback**: Emergency procedure, requires CCB approval
- **Support**: 24/7 on-call engineering team
- **Infrastructure**: Global deployment
  - Primary datacenter (US-East)
  - Secondary datacenter (EU-West)
  - Edge nodes (5 regions)
  - Full redundancy, 99.99% uptime SLA

---

## 4. Deployment Channels

### 4.1 Channel Definitions

| Channel | Environment(s) | Update Frequency | Stability | Target Users |
|---------|----------------|------------------|-----------|--------------|
| **nightly** | DEV, CI | Daily | Unstable | Developers |
| **weekly** | INT | Weekly | Stabilizing | QA Team |
| **beta** | SIM, HIL, STAGING | Bi-weekly | Stable | Test Engineers |
| **release-candidate** | FT, VAL | Monthly | Very Stable | Certification |
| **production-canary** | PROD-CANARY | Per-release | Production | 1-5% fleet |
| **production-beta** | PROD-BETA | Per-release | Production | 5-20% fleet |
| **production-stable** | PROD-GA | Quarterly | Production | 100% fleet |
| **hotfix** | All PROD | As needed | Emergency | All aircraft |

---

## 5. Promotion Path

```
Developer Commit
    ↓
[nightly] → DEV environment
    ↓
[weekly] → INT environment
    ↓ (QA approval)
[beta] → SIM/HIL environments
    ↓ (Test completion)
[release-candidate] → FT/VAL environments
    ↓ (Certification basis established)
[cert-frozen] → CERT baseline
    ↓ (Authority approval)
[production-canary] → PROD-CANARY
    ↓ (Monitoring period)
[production-beta] → PROD-BETA
    ↓ (Extended validation)
[production-stable] → PROD-GA
```

---

## 6. Environment Configuration

### 6.1 Configuration Management

Each environment has:
- **Environment-specific config files**: `config/env/{ENV_NAME}.yaml`
- **Secrets management**: HashiCorp Vault per environment
- **Feature flags**: LaunchDarkly or custom service
- **Infrastructure as Code**: Terraform/Ansible definitions

### 6.2 Data Segregation

| Environment | Data Type | Retention | Backup |
|-------------|-----------|-----------|--------|
| DEV/CI | Synthetic | 30 days | No |
| INT/SIM | Synthetic + anonymized | 90 days | Weekly |
| HIL/FT | Test data | Permanent | Daily |
| VAL/CERT | Certification data | Permanent | Daily + offsite |
| PROD | Operational data | Per regulation | Continuous + offsite |

---

## 7. Network Topology

```
┌─────────────────────────────────────────────────────────┐
│                    Internet                             │
└────────────────────┬────────────────────────────────────┘
                     │
          ┌──────────┴──────────┐
          │    API Gateway       │
          │  (Rate Limiting)     │
          └──────────┬───────────┘
                     │
      ┌──────────────┼──────────────┐
      │              │              │
  ┌───▼────┐   ┌────▼───┐    ┌─────▼────┐
  │ PROD-  │   │ PROD-  │    │ PROD-GA  │
  │ CANARY │   │ BETA   │    │          │
  └────────┘   └────────┘    └──────────┘
      │              │              │
      └──────────────┼──────────────┘
                     │
          ┌──────────┴──────────┐
          │   Shared Services    │
          │  - DPP Backend       │
          │  - Auth Service      │
          │  - Monitoring        │
          └─────────────────────┘
```

---

## 8. Access Control Matrix

| Role | LOCAL | DEV | CI | INT | SIM | HIL | FT | VAL | CERT | STAGING | PROD |
|------|-------|-----|----|----|-----|----|----|----|------|---------|------|
| Developer | RW | RW | R | R | - | - | - | - | - | - | - |
| QA Engineer | - | R | RW | RW | RW | R | - | R | - | R | - |
| Test Pilot | - | - | - | - | R | - | RW | - | - | - | - |
| Cert Engineer | - | R | R | R | R | R | R | RW | RW | R | - |
| Ops Engineer | - | - | - | - | - | - | - | - | R | RW | RW |
| On-Call SRE | - | R | R | R | R | R | R | R | R | RW | RW |

---

## 9. Monitoring & Observability

Each environment reports to centralized observability platform:

- **Metrics**: Prometheus + Grafana
- **Logs**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Traces**: Jaeger (distributed tracing)
- **Alerts**: PagerDuty integration
- **Dashboards**: Per-environment + global overview

---

## 10. Compliance & Audit

- All production access logged to immutable audit trail
- Certification environments have enhanced logging (DO-178C requirement)
- Access reviews quarterly
- Environment configurations in version control
- Terraform state backed up and versioned

---

## 11. Disaster Recovery

| Environment | RTO | RPO | Backup Frequency | DR Site |
|-------------|-----|-----|------------------|---------|
| DEV/CI | 24h | 24h | Daily | None |
| INT/SIM | 8h | 4h | Every 6h | Same datacenter |
| FT/VAL/CERT | 4h | 1h | Hourly | Geo-redundant |
| PROD | 1h | 0 | Continuous | Active-active |

---

## 12. Document Control

| Revision | Date | Author | Changes |
|----------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 DevOps | Initial environment map |

---

**Document Classification:** Internal Use  
**Next Review Date:** 2026-02-17  
**Contact:** devops@ampel360.aero
