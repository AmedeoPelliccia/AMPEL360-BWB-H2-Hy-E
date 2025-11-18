# DPP+NN System Assembly (System Level)

**Assembly ID**: 95-00-04-A001  
**Version**: 1.0  
**Status**: WORKING  
**Owner**: AMPEL360 Neural Networks WG

## Purpose

Top-level system assembly integrating:
- **Digital Product Passport** (DPP) infrastructure
- **Neural Network** lifecycle management
- **Blockchain provenance** anchoring
- **Cross-ATA interfaces** for AMPEL360 BWB H2 Hy-E Q100

## System Context

```
┌─────────────────────────────────────────────────────────────┐
│                    AMPEL360 Aircraft                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  ATA 28      │  │  ATA 42      │  │  ATA 45      │     │
│  │  Fuel System │◄─┤  IMA/AFDX    │◄─┤  Maintenance │     │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘     │
│         │                  │                  │              │
│         └──────────────────┼──────────────────┘              │
│                            │                                 │
│                    ┌───────▼──────────┐                     │
│                    │   ATA 95 DPP+NN  │                     │
│                    │  System Assembly  │                     │
│                    └───────┬──────────┘                     │
│                            │                                 │
│         ┌──────────────────┼──────────────────┐             │
│         │                  │                  │              │
│  ┌──────▼───────┐  ┌──────▼──────┐  ┌───────▼──────┐      │
│  │ Model        │  │ Blockchain  │  │ Monitoring   │      │
│  │ Lifecycle    │  │ DPP Chain   │  │ & Telemetry  │      │
│  └──────────────┘  └─────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
         │                     │                    │
         ▼                     ▼                    ▼
    Ground Ops          Certification         Cloud Analytics
```

## Constituent Assemblies

| Assembly ID | Name | Description | Trace to Req |
|------------|------|-------------|--------------|
| **95-00-04-A010** | Model Lifecycle | Training, registry, deployment | RQ-95-03-001 |
| **95-00-04-A020** | Data Pipeline | Ingestion, preprocessing, features | RQ-95-03-010 |
| **95-00-04-A030** | Runtime Inference | Onboard inference engines | RQ-95-03-020 |
| **95-00-04-A040** | Monitoring/Telemetry | Performance, drift, logging | RQ-95-03-030 |
| **95-00-04-A050** | Blockchain DPP | Provenance chain, anchors | RQ-95-03-040 |

## Interfaces

### Internal (Onboard)
- **ATA 42**: Neural partition on IMA (ARINC 653)
- **ATA 31**: Event recording (ARINC 767)
- **ATA 28**: H2 fuel level prediction
- **ATA 45**: Predictive maintenance analytics

### External (Ground/Cloud)
- **Ground Ops**: Model updates, data sync
- **OEM Portal**: Certification artifact access
- **Regulatory**: EASA AI Act compliance queries
- **Supply Chain**: Component DPP verification

## Design Principles

1. **Deterministic Inference**: All onboard inference <10ms latency
2. **Immutable Provenance**: Every model version blockchain-anchored
3. **Privacy by Design**: Federated learning with differential privacy
4. **Fail-Safe Defaults**: Graceful degradation to rule-based fallback
5. **CAOS Integration**: Decision support for crew and maintenance

## Certification Strategy

- **DO-178C**: DAL B for inference runtime (A031, A032, A033)
- **DO-254**: DAL B for NPU hardware interfaces
- **EU AI Act**: Level 2+ transparency and explainability
- **EASA AI Roadmap**: Phase 2 compliance (operational AI)

## Traceability

### Requirements Satisfied
- RQ-95-03-001: Neural network lifecycle management
- RQ-95-03-002: Digital product passport integration
- RQ-95-03-005: Blockchain provenance anchoring
- RQ-95-03-008: Cross-ATA interface compatibility

### Verification Methods
- System integration testing (SIT)
- Hardware-in-the-loop (HIL) simulation
- Iron bird testing
- Flight test validation

## Machine-Readable Spec
See: [`95-00-04-A001_DPP_NN_System_Assembly.json`](95-00-04-A001_DPP_NN_System_Assembly.json)

## Related Diagrams
- [`95-00-04-A001_DPP_NN_System_Assembly.drawio`](95-00-04-A001_DPP_NN_System_Assembly.drawio)

## Related Documents
- [Design Principles](../../../DESIGN_PRINCIPLES.md)
- [Architecture Overview](../../../ARCHITECTURE_OVERVIEW.md)
- [Model Lifecycle Assembly](../../02_SUBSYSTEM_LEVEL/MODEL_LIFECYCLE/95-00-04-A010_Model_Lifecycle_Assembly.md)
- [Blockchain DPP Assembly](../../02_SUBSYSTEM_LEVEL/BLOCKCHAIN_DPP/95-00-04-A050_Blockchain_Assembly.md)

---

## Document Control
- **Originator**: AI prompted by Amedeo Pelliccia
- **Toolchain**: GitHub Copilot + MCP Doc Control Server
- **Related file**: `95-00-04-A001_DPP_NN_System_Assembly.md`
- **Status**: `WORKING`
- **Notes**: This document must be reviewed by AMPEL360 Chief Systems Architect 
  before baseline. All cross-ATA interfaces require coordination with respective 
  chapter owners.
