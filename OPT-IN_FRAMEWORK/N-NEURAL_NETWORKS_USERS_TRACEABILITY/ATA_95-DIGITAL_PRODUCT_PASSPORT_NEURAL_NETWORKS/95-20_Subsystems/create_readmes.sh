#!/bin/bash

# Function to create a README for a subsystem
create_readme() {
    local ID=$1
    local NAME=$2
    local DESC=$3
    local ATA=$4
    local DAL=$5
    local CAPS=$6
    
    cat > "${ID}_${NAME}/README.md" << EOF
# ${ID} — ${NAME}

## Subsystem Metadata

\`\`\`yaml
subsystem_id: "${ID}"
name: "${NAME}"
description: "${DESC}"
parent_ata: "${ATA}"
criticality: "${DAL}"
status: "active"
version: "1.0"
last_updated: "2025-11-17"
\`\`\`

## Purpose

${DESC}

## Key Capabilities

${CAPS}

## Architecture

### Components

See individual component documents:
- \`${ID}-001_*_Overview.md\` — Architecture and overview
- \`${ID}-002_*\` through \`${ID}-00X_*\` — Individual components
- \`${ID}-005_Integration_with_${ATA}.md\` — Integration with parent ATA chapter

### ASSETS

- Diagrams: \`ASSETS/${ID}-A-001_*.drawio\`, \`ASSETS/${ID}-A-002_*.svg\`
- Configuration: \`ASSETS/${ID}-A-003_*.json\`
- Model Cards: \`ASSETS/Model_Cards/${ID}-A-2XX_*.yaml\`

## Integration

### Dependencies

See \`../95-20-00-003_Cross_ATA_Dependencies.csv\` for complete dependency matrix.

**Primary Dependencies**:
- 95-20-01 (NN Core Platform): Model deployment and inference
- 95-20-02 (NN DPP Blockchain): Model provenance
- 95-20-42 (NN IMA Integration): Compute resources

### Interface to Parent ATA

**Parent ATA**: ${ATA}

- **Input Sensors**: See \`${ID}-005_Integration_with_${ATA}.md\`
- **Control Outputs**: See \`${ID}-005_Integration_with_${ATA}.md\`
- **Data Schema**: Defined in 95-90 Tables/Schemas

## Operational Context

### Design Assurance Level

**Criticality**: ${DAL}

### Deployment

- **Runtime Environment**: IMA Partition (via 95-20-42)
- **Latency Requirements**: See component specifications
- **Resource Allocation**: See 95-20-42 IMA Integration

## CAOS Integration

### Discovery

This subsystem is registered in:
- \`../00_META/95-20-00-006_Subsystem_Registry.json\`
- \`../00_META/95-20-00-007_CAOS_Subsystems_Hooks.md\`

### MCP Endpoints

- **Capability**: \`/.well-known/mcp/capability.json\`
- **Health**: \`/health\`
- **Inference**: \`/v1/predict\`
- **Metrics**: \`/metrics\`
- **Models**: \`/v1/models\`

## Model Information

### Active Models

See \`ASSETS/Model_Cards/\` for detailed model cards.

Each model card follows the format:
- \`${ID}-A-2XX_ModelName_vX.Y.yaml\`

### Model Lifecycle

1. **Training**: Offline with 95-00-13 component data
2. **Validation**: Per 95-00-07 V&V procedures
3. **Deployment**: Via 95-20-01 model registry
4. **Monitoring**: Real-time via 95-20-01 monitoring framework
5. **Provenance**: Logged to 95-20-02 blockchain

## Certification

### Compliance

- **DO-178C**: Software DAL ${DAL}
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
- [${ATA}](../../..) — Parent ATA chapter documentation

## Document Control

- **Owner**: AMPEL360 ${NAME} Team
- **Version**: 1.0
- **Status**: Active
- **Classification**: Technical Reference

---

**For detailed component specifications, see individual documents in this directory.**
EOF
}

# Create READMEs for all subsystems
create_readme "95-20-01" "NN_Core_Platform" "Core neural network infrastructure providing model registry, inference runtime, and monitoring framework for all NN subsystems" "ATA 95" "DAL-A" "- Model Registry: Centralized catalog with versioning
- Inference Runtime: High-performance execution (ONNX, TensorRT)
- Monitoring Framework: Real-time performance tracking and drift detection
- Version Control: Integration with 95-00-11 EIS versions"

create_readme "95-20-02" "NN_DPP_Blockchain" "Digital Product Passport with blockchain-based model provenance, smart contracts, and audit trail for certification" "ATA 95" "DAL-B" "- Blockchain Architecture: Immutable provenance chain
- Smart Contracts: Automated compliance verification
- Query Interface: Audit and certification support
- Evidence Storage: IPFS-based artifact storage"

create_readme "95-20-21" "NN_ECS" "Environmental Control System neural networks for cabin temperature prediction, air quality monitoring, and HVAC optimization" "ATA 21" "DAL-C" "- Cabin Temperature Prediction: ±0.5°C accuracy
- Air Quality Monitoring: CO₂, humidity, contaminants
- HVAC Optimization: 15% energy reduction
- Integration: ATA 21 environmental control systems"

create_readme "95-20-27" "NN_Flight_Controls" "Flight control neural networks for aerodynamic prediction, control surface optimization, and gust load alleviation" "ATA 27" "DAL-A" "- Aerodynamic Predictor: CFD surrogate model (1000× faster)
- Control Surface Optimizer: Real-time optimization
- Gust Load Alleviation: 30% load reduction
- Failover: <10ms switch to conventional laws"

create_readme "95-20-28" "NN_Fuel_System" "H₂ fuel system neural networks for level prediction, boiloff rate estimation, and fuel optimization" "ATA 28" "DAL-B" "- H₂ Level Prediction: ±2% accuracy
- Boiloff Rate Estimation: Physics-informed NN
- Fuel Optimization: 5% efficiency gain
- Safety Integration: Leak detection, pressure management"

create_readme "95-20-31" "NN_Recording_Systems" "Recording system neural networks for anomaly detection, event classification, and intelligent data compression" "ATA 31" "DAL-C" "- Anomaly Detection: 99.5% recall rate
- Event Classification: Automated labeling
- Data Compression: 10:1 ratio (lossless for critical parameters)
- FDR/CVR Integration: ARINC 717 interface"

create_readme "95-20-42" "NN_IMA_Integration" "IMA integration neural networks for partition management, AFDX traffic prediction, and health monitoring" "ATA 42" "DAL-B" "- Neural Partition Manager: ARINC 653 compliant
- AFDX Traffic Prediction: Network optimization
- Health Monitoring: Real-time status tracking
- Resource Allocation: Dynamic scheduling"

create_readme "95-20-45" "NN_Maintenance" "Maintenance neural networks for predictive maintenance, RUL estimation, and fault diagnosis" "ATA 45" "DAL-C" "- Predictive Maintenance: 500 flight hours prediction horizon
- RUL Estimation: Remaining useful life calculation
- Fault Diagnosis: 85% accuracy
- Fleet Learning: Cross-aircraft intelligence"

create_readme "95-20-49" "NN_APU" "APU neural networks for performance prediction and health monitoring" "ATA 49" "DAL-D" "- APU Performance Prediction: Efficiency optimization
- Health Monitoring: Early fault detection
- Integration: Backup power coordination with 95-20-80"

create_readme "95-20-53" "NN_Structures" "Structural neural networks (GNN) for health monitoring, load distribution prediction, and fatigue estimation" "ATA 53" "DAL-B" "- Structural Health Monitoring: Graph Neural Network (GNN)
- Load Distribution Prediction: Real-time stress analysis
- Fatigue Estimation: Lifecycle tracking
- SHM Integration: Strain gauges, acoustic sensors"

create_readme "95-20-57" "NN_Wing_Systems" "Wing system neural networks (LSTM, vision) for flutter prediction, ice detection, and load alleviation" "ATA 57" "DAL-A" "- Flutter Prediction: LSTM model (10 seconds ahead)
- Ice Detection: Computer vision (95% accuracy)
- Load Alleviation: Active load reduction
- Safety Critical: Flight-critical flutter prevention"

create_readme "95-20-70" "NN_Propulsion" "Propulsion neural networks for engine performance modeling, fuel cell optimization, and thrust prediction" "ATA 70-79" "DAL-A" "- Engine Performance Modeling: Digital twin
- Fuel Cell Optimizer: Stack efficiency maximization
- Thrust Prediction: Real-time control
- H₂ Integration: Coordination with 95-20-28"

create_readme "95-20-80" "NN_Energy_Systems" "Energy system neural networks for power load prediction, battery SOH estimation, and energy management optimization" "ATA 80" "DAL-B" "- Power Load Prediction: 5 minutes ahead
- Battery SOH Estimation: State of health tracking
- Energy Management: Optimization across sources
- Integration: Fuel cells (95-20-70), H₂ (95-20-28), APU (95-20-49)"

echo "All README files created successfully!"
