# 95-20-31 — NN Recording Systems

**Scope:** Neural network–based functions supporting **[ATA 31 – Indicating/Recording Systems](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)** for AMPEL360 BWB H₂ Hy-E.

This subsystem covers NN functions that operate on:

- Cockpit Voice Recorder (CVR) audio streams
- Flight Data Recorder (FDR) and related parameters
- Maintenance/health recording streams
- Event detection, tagging and summarization for post-flight analysis

## Structure

- `00_META/` – Index, traceability maps, meta-information for ATA 95-20-31.
- `95-20-31-0XX_*.md` – Component specifications per NN function (transcription, event detection, etc.).
- `ASSETS/` – Model cards, system diagrams, safety & certification reports.
- `Data/` – Training/validation datasets and digital-twin synthetic scenarios.
- `Models/` – Source code, configs, trained ONNX artefacts, inspection & deployment scripts.
- `Tests/` – Unit, integration and scenario-based tests.

## Cross-ATA Integration

- Primary integration: **[ATA 31 – Indicating/Recording Systems](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)**
- Links to:
  - ATA 45 – Central Maintenance System (if applicable)
  - ATA 23 – Communications (for audio routing)
- Governance and traceability: see [ATA 95 General](../../95-00_GENERAL/).

## Subsystem Metadata

```yaml
subsystem_id: "95-20-31"
name: "NN_Recording_Systems"
description: "Neural network–based functions for CVR transcription, FDR anomaly detection, event segmentation, data compression, and maintenance log summarization"
parent_ata: "ATA 31"
criticality: "DAL-C"
status: "active"
version: "1.0"
last_updated: "2025-11-18"
```

## Key Capabilities

- **CVR Transcription**: Speech-to-text + event/keyword tagging for cockpit audio
- **FDR Anomaly Detection**: 99.5% recall rate for abnormal flight parameter patterns
- **Event Segmentation**: Automated detection and segmentation of relevant recording intervals
- **Data Compression**: 10:1 ratio (lossless for safety-critical parameters)
- **Maintenance Summarization**: Automated log generation from recorded events
- **Integration**: ARINC 717 interface for FDR/CVR systems

## Integration

### Dependencies

See `../95-20-00-003_Cross_ATA_Dependencies.csv` for complete dependency matrix.

**Primary Dependencies**:
- [95-20-01 (NN Core Platform)](../95-20-01_NN_Core_Platform/): Model deployment and inference
- [95-20-02 (NN DPP Blockchain)](../95-20-02_NN_DPP_Blockchain/): Model provenance
- [95-20-42 (NN IMA Integration)](../95-20-42_NN_IMA_Integration/): Compute resources

### Interface to Parent ATA

**Parent ATA**: [ATA 31](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)

- **Input Sensors**: See [95-20-31-007_Integration_with_ATA_31.md](95-20-31-007_Integration_with_ATA_31.md)
- **Control Outputs**: See [95-20-31-007_Integration_with_ATA_31.md](95-20-31-007_Integration_with_ATA_31.md)
- **Data Schema**: Defined in [95-90 Tables/Schemas](../../95-90_Tables_Schemas_Diagrams/)

## Operational Context

### Design Assurance Level

**Criticality**: DAL-C

### Deployment

- **Runtime Environment**: IMA Partition (via [95-20-42](../95-20-42_NN_IMA_Integration/))
- **Latency Requirements**: See component specifications
- **Resource Allocation**: See [95-20-42 IMA Integration](../95-20-42_NN_IMA_Integration/)

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
- `95-20-31-A-1XX_ModelName_vX.Y.yaml`

### Model Lifecycle

1. **Training**: Offline with [95-00-13 component data](../../95-00_GENERAL/95-00-13_Subsystems_Components/)
2. **Validation**: Per [95-00-07 V&V procedures](../../95-00_GENERAL/95-00-07_V_AND_V/)
3. **Deployment**: Via [95-20-01 model registry](../95-20-01_NN_Core_Platform/)
4. **Monitoring**: Real-time via [95-20-01 monitoring framework](../95-20-01_NN_Core_Platform/)
5. **Provenance**: Logged to [95-20-02 blockchain](../95-20-02_NN_DPP_Blockchain/)

## Certification

### Compliance

- **[DO-178C](https://www.rtca.org/product/do-178c/)**: Software DAL-C
- **[DO-333](https://www.rtca.org/product/do-333/)**: Model-based development
- **[EASA SC-AI](https://www.easa.europa.eu/en/document-library/general-publications/special-condition-sc-ai)**: AI/ML certification guidance
- **[FAA AC 20-115D](https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1026670)**: Airborne software

### Evidence

Certification evidence is maintained in:
- [95-00-10_Certification](../../95-00_GENERAL/95-00-10_Certification/)
- [95-20-02 blockchain provenance chain](../95-20-02_NN_DPP_Blockchain/)

## References

- [95-20-00-001_Subsystems_Overview.md](../95-20-00-001_Subsystems_Overview.md) — Overall architecture
- [95-20-00-002_Subsystems_Integration_Map.md](../95-20-00-002_Subsystems_Integration_Map.md) — Integration patterns
- [95-20-00-003_Cross_ATA_Dependencies.csv](../95-20-00-003_Cross_ATA_Dependencies.csv) — Dependencies
- [ATA 31](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — Parent ATA chapter documentation

## Document Control

- **Owner**: AMPEL360 NN_Recording_Systems Team
- **Version**: 1.0
- **Status**: Active
- **Classification**: Technical Reference
- **AI Assistance**: Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Last AI Update**: 2025-11-18

---

**For detailed component specifications, see individual documents in this directory.**
