# 95-00-05_Interfaces

## Purpose

This folder defines all interface specifications for the AMPEL360 BWB H₂ Hy-E Digital Product Passport and Neural Networks system (ATA 95), implementing a strict naming convention for traceability, automation, and certification compliance.

## Scope

This folder is part of the **95-00_GENERAL** layer, which provides governance and lifecycle management for ATA Chapter 95.

## ✅ Complete Corrected Structure with Asset Naming

```
95-00-05_Interfaces/
├── README.md
├── 95-00-05-00-001_Interface_Management_Plan.md
├── 95-00-05-00-002_Change_Control_Process.md
│
├── 00_META/
│   ├── 95-00-05-00-003_Interface_Taxonomy.md
│   ├── 95-00-05-00-004_Cross_ATA_Interface_Map.md
│   ├── 95-00-05-00-005_Interface_Traceability_Matrix.csv
│   ├── 95-00-05-00-006_Interface_Registry.json
│   └── 95-00-05-00-007_CAOS_Interface_Hooks.md
│
├── 01_DATA_INTERFACES/
│   ├── 95-00-05-01-001_Data_Sources_Catalog.md
│   ├── 95-00-05-01-002_Data_Sinks_Catalog.md
│   ├── 95-00-05-01-003_Feature_Schemas.md
│   ├── 95-00-05-01-004_Data_Contracts.md
│   ├── 95-00-05-01-005_Data_Lineage_Map.md
│   ├── 95-00-05-01-006_Interface_Control_Document_ICD.md
│   ├── 95-00-05-01-007_ARINC_664_AFDX_Mapping.md
│   └── ASSETS/
│       ├── 95-00-05-01-A-001_Data_Flow_Diagram.drawio
│       ├── 95-00-05-01-A-002_Data_Flow_Diagram.svg
│       ├── 95-00-05-01-A-003_Data_Contracts_Table.csv
│       ├── 95-00-05-01-A-004_Data_Lineage_Graph.png
│       ├── Feature_Schema_JSON/
│       │   ├── 95-00-05-01-A-101_H2_Sensor_Schema.json
│       │   ├── 95-00-05-01-A-102_Flight_Phase_Schema.json
│       │   └── 95-00-05-01-A-103_Prediction_Output_Schema.json
│       └── Sample_Payloads/
│           ├── 95-00-05-01-A-201_Sample_Input_Packet.bin
│           └── 95-00-05-01-A-202_Sample_Output_Packet.bin
│
├── 02_MODEL_INTERFACES/
│   ├── 95-00-05-02-001_Input_Specifications.md
│   ├── 95-00-05-02-002_Output_Specifications.md
│   ├── 95-00-05-02-003_PrePost_Processing_Pipelines.md
│   ├── 95-00-05-02-004_Embedding_Space_Definition.md
│   ├── 95-00-05-02-005_Model_to_Model_Interfaces.md
│   ├── 95-00-05-02-006_Model_API_Specification.yaml
│   ├── 95-00-05-02-007_ONNX_Runtime_Interface.md
│   └── ASSETS/
│       ├── 95-00-05-02-A-001_NN_IO_Architecture.drawio
│       ├── 95-00-05-02-A-002_NN_IO_Architecture.svg
│       ├── 95-00-05-02-A-003_PrePost_Pipeline_BlockDiagram.drawio
│       ├── 95-00-05-02-A-004_PrePost_Pipeline_BlockDiagram.svg
│       ├── 95-00-05-02-A-005_Interface_Mapping_Table.csv
│       ├── Model_Cards/
│       │   ├── 95-00-05-02-A-101_H2_Predictor_Model_Card.yaml
│       │   ├── 95-00-05-02-A-102_Anomaly_Detector_Model_Card.yaml
│       │   └── 95-00-05-02-A-103_Maintenance_Predictor_Model_Card.yaml
│       └── Sample_Inference_Requests/
│           ├── 95-00-05-02-A-201_Inference_Request_Example.json
│           └── 95-00-05-02-A-202_Inference_Response_Example.json
│
├── 03_SYSTEM_INTERFACES/
│   ├── 95-00-05-03-001_Aircraft_Systems_Interfaces.md
│   ├── 95-00-05-03-002_Avionics_Bus_Integration.md
│   ├── 95-00-05-03-003_Edge_Compute_HW_IF.md
│   ├── 95-00-05-03-004_Ground_Systems_Interfaces.md
│   ├── 95-00-05-03-005_ATA_02_Operations_IF.md
│   ├── 95-00-05-03-006_ATA_28_Fuel_System_IF.md
│   ├── 95-00-05-03-007_ATA_31_Recording_IF.md
│   ├── 95-00-05-03-008_ATA_42_IMA_IF.md
│   ├── 95-00-05-03-009_ATA_45_Maintenance_IF.md
│   └── ASSETS/
│       ├── 95-00-05-03-A-001_System_IF_Architecture.drawio
│       ├── 95-00-05-03-A-002_System_IF_Architecture.pdf
│       ├── 95-00-05-03-A-003_ARINC_825_CAN_Traceability.csv
│       ├── 95-00-05-03-A-004_AFDX_Virtual_Links_Allocation.xlsx
│       ├── 95-00-05-03-A-005_Cross_ATA_Interface_Matrix.csv
│       └── System_Context_Diagrams/
│           ├── 95-00-05-03-A-101_ATA_02_Context.svg
│           ├── 95-00-05-03-A-102_ATA_28_Context.svg
│           ├── 95-00-05-03-A-103_ATA_31_Context.svg
│           ├── 95-00-05-03-A-104_ATA_42_Context.svg
│           └── 95-00-05-03-A-105_ATA_45_Context.svg
│
├── 04_CERTIFICATION_INTERFACES/
│   ├── 95-00-05-04-001_EASA_FAA_IF_Requirements.md
│   ├── 95-00-05-04-002_AI_Compliance_APIs.md
│   ├── 95-00-05-04-003_Explainability_Interface.md
│   ├── 95-00-05-04-004_Human_Factors_Interface.md
│   ├── 95-00-05-04-005_Audit_Trail_Interface.md
│   ├── 95-00-05-04-006_DO_178C_Evidence_IF.md
│   └── ASSETS/
│       ├── 95-00-05-04-A-001_Cert_IF_Flowchart.drawio
│       ├── 95-00-05-04-A-002_Cert_IF_Flowchart.svg
│       ├── 95-00-05-04-A-003_HF_Interaction_Model.drawio
│       ├── 95-00-05-04-A-004_HF_Interaction_Model.pdf
│       ├── 95-00-05-04-A-005_Explainability_Reporting_Spec.csv
│       ├── Sample_Audit_Logs/
│       │   ├── 95-00-05-04-A-101_Model_Deployment_Log.json
│       │   ├── 95-00-05-04-A-102_Inference_Audit_Log.json
│       │   └── 95-00-05-04-A-103_Performance_Drift_Log.json
│       └── Evidence_Package_Template/
│           ├── 95-00-05-04-A-201_Evidence_Manifest.yaml
│           ├── 95-00-05-04-A-202_Test_Results_Template.xlsx
│           └── 95-00-05-04-A-203_Compliance_Checklist.pdf
│
├── 05_SECURITY_PRIVACY_INTERFACES/
│   ├── 95-00-05-05-001_Cybersecurity_Interface.md
│   ├── 95-00-05-05-002_Privacy_Data_Protection_IF.md
│   ├── 95-00-05-05-003_Access_Control_Audit_IF.md
│   ├── 95-00-05-05-004_Crypto_Key_Management_IF.md
│   ├── 95-00-05-05-005_Blockchain_Anchor_IF.md
│   └── ASSETS/
│       ├── 95-00-05-05-A-001_ZeroTrust_Interface_Model.drawio
│       ├── 95-00-05-05-A-002_ZeroTrust_Interface_Model.svg
│       ├── 95-00-05-05-A-003_Audit_Log_Spec.csv
│       ├── 95-00-05-05-A-004_Data_Protection_Flow.drawio
│       ├── 95-00-05-05-A-005_Data_Protection_Flow.png
│       ├── 95-00-05-05-A-006_Key_Management_Lifecycle.pdf
│       └── 95-00-05-05-A-007_Blockchain_Transaction_Schema.json
│
└── 06_DPP_BLOCKCHAIN_INTERFACES/
    ├── 95-00-05-06-001_DPP_Data_Model.md
    ├── 95-00-05-06-002_Blockchain_Write_Interface.md
    ├── 95-00-05-06-003_Blockchain_Query_Interface.md
    ├── 95-00-05-06-004_Smart_Contract_ABI.md
    ├── 95-00-05-06-005_Supply_Chain_IF.md
    └── ASSETS/
        ├── DPP_Schema_JSON/
        │   ├── 95-00-05-06-A-101_DPP_Core_Schema.json
        │   ├── 95-00-05-06-A-102_Model_Provenance_Schema.json
        │   └── 95-00-05-06-A-103_Component_Traceability_Schema.json
        ├── Smart_Contract_Solidity/
        │   ├── 95-00-05-06-A-201_ModelRegistry.sol
        │   ├── 95-00-05-06-A-202_ProvenanceChain.sol
        │   └── 95-00-05-06-A-203_AccessControl.sol
        ├── 95-00-05-06-A-001_Query_API_OpenAPI.yaml
        └── 95-00-05-06-A-002_Supply_Chain_Integration_Diagram.svg
```

## Naming Convention Breakdown

```
95  -  00  -  05  -  01  -  A  -  001  _  Descriptive_Name.ext
│      │      │      │      │      │       │
│      │      │      │      │      │       └─ Human-readable description
│      │      │      │      │      └───────── Sequence (001-999)
│      │      │      │      └──────────────── Type: A=Asset, D=Document, T=Test
│      │      │      └─────────────────────── Section (00=META, 01=DATA, etc.)
│      │      └────────────────────────────── Lifecycle (05=Interfaces)
│      └───────────────────────────────────── Bucket (00=GENERAL)
└──────────────────────────────────────────── ATA Chapter (95)
```

## Asset Type Codes

- **A** = Asset (diagrams, schemas, data files)
- **D** = Document (primary documentation)
- **T** = Test artifact (test cases, scripts)
- **R** = Reference (external standards, citations)
- **C** = Configuration (settings, parameters)

## MCP Link Rules

The following link rules have been added to `tools/doc-meta-enforcer-mcp/src/linkRules.ts`:

```typescript
// ATA 95 Interface Assets
{
  pattern: /(?<!\[)\b(95-00-05-\d{2}-A-\d{3})\b(?!\]\()/g,
  replacement: "[$1](../95-00_GENERAL/95-00-05_Interfaces/**/ASSETS/$1_*)",
  description: "ATA 95 Interface Asset reference"
},

// ATA 95 Interface Documents
{
  pattern: /(?<!\[)\b(95-00-05-\d{2}-\d{3})\b(?!\]\()/g,
  replacement: "[$1](../95-00_GENERAL/95-00-05_Interfaces/**/$1_*.md)",
  description: "ATA 95 Interface Document reference"
},
```

## Benefits of Strict Asset Naming

1. **Traceability**: Every asset traceable to requirements
2. **Version Control**: Git-friendly sequential numbering
3. **Automation**: Scripts can parse and validate structure
4. **Cross-References**: Unambiguous links between documents
5. **Certification**: Auditors can verify complete artifact chains
6. **CAOS Integration**: Automated asset discovery for decision support

## Interface Categories

### 00_META
Meta-level documentation covering interface management strategy, taxonomies, cross-ATA mappings, traceability matrices, and CAOS integration hooks.

### 01_DATA_INTERFACES
Data flow specifications including source/sink catalogs, feature schemas, data contracts, data lineage mapping, ICDs, and ARINC 664 AFDX protocols.

### 02_MODEL_INTERFACES
Neural network model I/O specifications, pre/post-processing pipelines, embedding space definitions, model-to-model interfaces, API specs, and ONNX runtime integration.

### 03_SYSTEM_INTERFACES
Aircraft system integration points including avionics bus protocols, edge compute hardware interfaces, ground systems, and cross-ATA system interfaces (ATA 02, 28, 31, 42, 45).

### 04_CERTIFICATION_INTERFACES
Regulatory compliance interfaces including EASA/FAA requirements, AI compliance APIs, explainability interfaces, human factors integration, audit trails, and DO-178C evidence generation.

### 05_SECURITY_PRIVACY_INTERFACES
Security and privacy integration points including cybersecurity interfaces, data protection mechanisms, access control, cryptographic key management, and blockchain anchoring.

### 06_DPP_BLOCKCHAIN_INTERFACES
Digital Product Passport and blockchain interfaces including DPP data models, blockchain read/write operations, smart contract ABIs, and supply chain integration.

## Status

- **Phase**: Interfaces
- **Lifecycle Position**: 05 of 14
- **Status**: Active
- **Last Updated**: 2025-11-17
- **Files Created**: 102 (with strict naming convention)

## Related Folders

Part of the canonical 14-folder lifecycle:
1. Overview → 2. Safety → 3. Requirements → 4. Design → **5. Interfaces** → 6. Engineering → 7. V&V → 8. Prototyping → 9. Production Planning → 10. Certification → 11. EIS/Versions/Tags → 12. Services → 13. Subsystems/Components → 14. Ops/Std/Sustain

## Document Control

- **Standard**: OPT-IN Framework v1.1 (ATA 95 canonical template) + AMPEL360 Asset Naming Standard
- **Owner**: AMPEL360 Documentation WG
- **Naming Convention**: Fully implemented per AMPEL360_ASSETS_STANDARD.md
