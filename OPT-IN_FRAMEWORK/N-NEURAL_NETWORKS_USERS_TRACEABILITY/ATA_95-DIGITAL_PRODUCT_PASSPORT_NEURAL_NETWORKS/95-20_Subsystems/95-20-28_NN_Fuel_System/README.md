# 95-20-28 NN Fuel System

**Scope:** Neural network–based functions supporting [ATA 28 Fuel System](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) for AMPEL360 BWB H₂ Hy-E.

This subsystem covers:

- Fuel quantity estimation and cross-checking
- Leak and abnormal consumption detection
- Fuel transfer optimization and balancing
- Fuel temperature prediction and conditioning
- Integration with ATA 28 classical control & monitoring

## Structure

- `00_META/` – Index, traceability maps, meta-information
- `95-20-28-0XX_*.md` – Component specifications per NN function
- `ASSETS/` – Model cards, diagrams, reports
- `Data/` – Training, validation and synthetic datasets (incl. digital twin scenarios)
- `Models/` – Source code, configs, trained ONNX artifacts and deployment scripts
- `Tests/` – Unit, integration and scenario-based tests

## Cross-ATA Integration

- Primary integration: **[ATA 28 Fuel System](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)**
- Safety and certification linkage: see `95-20-28-008_Safety_and_Certification.md`
- Neural Networks governance: ATA 95-00-00 GENERAL framework

## Subsystem Metadata

```yaml
subsystem_id: "95-20-28"
name: "NN_Fuel_System"
description: "Fuel system neural networks for fuel quantity estimation, leak detection, transfer optimization, and temperature prediction"
parent_ata: "ATA 28"
criticality: "DAL-C"
status: "active"
version: "1.0"
last_updated: "2025-11-18"
```

## Key Capabilities

- Fuel Quantity Estimation: ±2% accuracy
- Leak Detection: Real-time anomaly monitoring
- Transfer Optimization: Optimal fuel balancing
- Temperature Prediction: Fuel conditioning support
- Water Contamination Detection: Enhanced safety

## Architecture

### Components

See individual component documents:
- `95-20-28-001_Fuel_System_NN_Overview.md` — Architecture and overview
- `95-20-28-002_Fuel_Quantity_Estimator.md` — Fuel level estimation
- `95-20-28-003_Leak_Detection_Monitor.md` — Leak detection
- `95-20-28-004_Fuel_Transfer_Optimizer.md` — Transfer optimization
- `95-20-28-005_Fuel_Temperature_Predictor.md` — Temperature prediction
- `95-20-28-006_Water_Contamination_Detector.md` — Water detection
- `95-20-28-007_Integration_with_ATA_28.md` — Integration with parent ATA chapter
- `95-20-28-008_Safety_and_Certification.md` — Safety and certification
- `95-20-28-009_Operational_Procedures.md` — Operations procedures

### ASSETS

- Diagrams: `ASSETS/Diagrams/`
- Model Cards: `ASSETS/Model_Cards/95-20-28-A-1XX_*.yaml`
- Reports: `ASSETS/Reports/`

## Integration

### Dependencies

See `../95-20-00-003_Cross_ATA_Dependencies.csv` for complete dependency matrix.

**Primary Dependencies**:
- 95-20-01 (NN Core Platform): Model deployment and inference
- 95-20-02 (NN DPP Blockchain): Model provenance
- 95-20-42 (NN IMA Integration): Compute resources

### Interface to Parent ATA

**Parent ATA**: ATA 28

- **Input Sensors**: See `95-20-28-005_Integration_with_ATA 28.md`
- **Control Outputs**: See `95-20-28-005_Integration_with_ATA 28.md`
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
- `95-20-28-A-2XX_ModelName_vX.Y.yaml`

### Model Lifecycle

1. **Training**: Offline with [95-00-13 component data](../../95-00_GENERAL/95-00-13_Subsystems_Components/)
2. **Validation**: Per [95-00-07 V&V procedures](../../95-00_GENERAL/95-00-07_V_AND_V/)
3. **Deployment**: Via [95-20-01 model registry](../95-20-01_NN_Core_Platform/)
4. **Monitoring**: Real-time via [95-20-01 monitoring framework](../95-20-01_NN_Core_Platform/)
5. **Provenance**: Logged to [95-20-02 blockchain](../95-20-02_NN_DPP_Blockchain/)

## Certification

### Compliance

- **[DO-178C](https://www.rtca.org/product/do-178c/)**: Software Considerations in Airborne Systems and Equipment Certification (DAL-C)
- **[DO-333](https://www.rtca.org/product/do-333/)**: Formal Methods Supplement to DO-178C
- **[EASA SC-AI](https://www.easa.europa.eu/en/document-library/general-publications/special-condition-sc-ai)**: AI/ML certification guidance
- **[FAA AC 20-115D](https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1026670)**: Airborne Software Development Assurance

### Evidence

Certification evidence is maintained in:
- [95-00-10_Certification](../../95-00_GENERAL/95-00-10_Certification/)
- [95-20-02 blockchain provenance chain](../95-20-02_NN_DPP_Blockchain/)

## References

- [95-20-00-001_Subsystems_Overview.md](../95-20-00-001_Subsystems_Overview.md) — Overall architecture
- [95-20-00-002_Subsystems_Integration_Map.md](../95-20-00-002_Subsystems_Integration_Map.md) — Integration patterns
- [95-20-00-003_Cross_ATA_Dependencies.csv](../95-20-00-003_Cross_ATA_Dependencies.csv) — Dependencies
- [00_META/95-20-00-004_Subsystems_Taxonomy.md](../00_META/95-20-00-004_Subsystems_Taxonomy.md) — Classification
- [ATA 28](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — Parent ATA chapter documentation

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-18_.

---

**For detailed component specifications, see individual documents in this directory.**
