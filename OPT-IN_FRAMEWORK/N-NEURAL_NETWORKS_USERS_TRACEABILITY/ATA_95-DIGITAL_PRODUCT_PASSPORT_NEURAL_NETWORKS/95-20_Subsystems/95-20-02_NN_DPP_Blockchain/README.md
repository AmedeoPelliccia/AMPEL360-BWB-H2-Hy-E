# 95-20-02 — NN_DPP_Blockchain

## Subsystem Metadata

```yaml
subsystem_id: "95-20-02"
name: "NN_DPP_Blockchain"
description: "Digital Product Passport with blockchain-based model provenance, smart contracts, and audit trail for certification"
parent_ata: "ATA 95"
criticality: "DAL-B"
status: "active"
version: "1.0"
last_updated: "2025-11-17"
```

## Purpose

Digital Product Passport with blockchain-based model provenance, smart contracts, and audit trail for certification

## Key Capabilities

- Blockchain Architecture: Immutable provenance chain
- Smart Contracts: Automated compliance verification
- Query Interface: Audit and certification support
- Evidence Storage: IPFS-based artifact storage

## Architecture

### Components

See individual component documents:
- `95-20-02-001_*_Overview.md` — Architecture and overview
- `95-20-02-002_*` through `95-20-02-00X_*` — Individual components
- `95-20-02-005_Integration_with_ATA 95.md` — Integration with parent ATA chapter

### ASSETS

- Diagrams: `ASSETS/95-20-02-A-001_*.drawio`, `ASSETS/95-20-02-A-002_*.svg`
- Configuration: `ASSETS/95-20-02-A-003_*.json`
- Model Cards: `ASSETS/Model_Cards/95-20-02-A-2XX_*.yaml`

## Integration

### Dependencies

See `../95-20-00-003_Cross_ATA_Dependencies.csv` for complete dependency matrix.

**Primary Dependencies**:
- 95-20-01 (NN Core Platform): Model deployment and inference
- 95-20-02 (NN DPP Blockchain): Model provenance
- 95-20-42 (NN IMA Integration): Compute resources

### Interface to Parent ATA

**Parent ATA**: ATA 95

- **Input Sensors**: See `95-20-02-005_Integration_with_ATA 95.md`
- **Control Outputs**: See `95-20-02-005_Integration_with_ATA 95.md`
- **Data Schema**: Defined in 95-90 Tables/Schemas

## Operational Context

### Design Assurance Level

**Criticality**: DAL-B

### Deployment

- **Runtime Environment**: IMA Partition (via 95-20-42)
- **Latency Requirements**: See component specifications
- **Resource Allocation**: See 95-20-42 IMA Integration

## CAOS Integration

### Discovery

This subsystem is registered in:
- `../00_META/95-20-00-006_Subsystem_Registry.json`
- `../00_META/95-20-00-007_CAOS_Subsystems_Hooks.md`

### MCP Endpoints

- **Capability**: `/.well-known/mcp/capability.json`
- **Health**: `/health`
- **Inference**: `/v1/predict`
- **Metrics**: `/metrics`
- **Models**: `/v1/models`

## Model Information

### Active Models

See `ASSETS/Model_Cards/` for detailed model cards.

Each model card follows the format:
- `95-20-02-A-2XX_ModelName_vX.Y.yaml`

### Model Lifecycle

1. **Training**: Offline with 95-00-13 component data
2. **Validation**: Per 95-00-07 V&V procedures
3. **Deployment**: Via 95-20-01 model registry
4. **Monitoring**: Real-time via 95-20-01 monitoring framework
5. **Provenance**: Logged to 95-20-02 blockchain

## Certification

### Compliance

- **DO-178C**: Software DAL DAL-B
- **DO-333**: Model-based development
- **EASA MOC SC-AI**: AI/ML certification guidance
- **FAA AC 20-115D**: Airborne software

### Evidence

Certification evidence is maintained in:
- 95-00-10_Certification
- 95-20-02 blockchain provenance chain

## References

- [95-20-00-001_Subsystems_Overview.md](../95-20-00-001_Subsystems_Overview.md) — Overall architecture
- [95-20-00-002_Subsystems_Integration_Map.md](../95-20-00-002_Subsystems_Integration_Map.md) — Integration patterns
- [95-20-00-003_Cross_ATA_Dependencies.csv](../95-20-00-003_Cross_ATA_Dependencies.csv) — Dependencies
- [00_META/95-20-00-004_Subsystems_Taxonomy.md](../00_META/95-20-00-004_Subsystems_Taxonomy.md) — Classification
- [ATA 95](../../..) — Parent ATA chapter documentation

## Document Control

- **Owner**: AMPEL360 NN_DPP_Blockchain Team
- **Version**: 1.0
- **Status**: Active
- **Classification**: Technical Reference

---

**For detailed component specifications, see individual documents in this directory.**
