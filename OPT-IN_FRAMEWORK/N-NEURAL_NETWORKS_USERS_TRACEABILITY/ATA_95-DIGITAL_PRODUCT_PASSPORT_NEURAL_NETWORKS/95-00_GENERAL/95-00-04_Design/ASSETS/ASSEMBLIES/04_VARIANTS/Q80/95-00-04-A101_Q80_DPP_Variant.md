# Q80 DPP+NN Variant Configuration

**Assembly ID**: 95-00-04-A101  
**Aircraft Variant**: Q80 (Cost-Optimized)  
**Version**: 1.0
**Status**: WORKING

## Purpose

Defines a cost-optimized DPP+NN system configuration for the Q80 aircraft variant.

## Configuration Overview

The Q80 variant provides essential DPP+NN capabilities with reduced hardware:

- **Model Lifecycle**: Simplified deployment (no onboard training)
- **Data Pipeline**: Basic telemetry collection
- **Runtime Inference**: Single inference engine (no redundancy)
- **Monitoring**: Essential performance tracking
- **Blockchain DPP**: Lightweight provenance (hash anchoring only)

## Hardware Configuration

```yaml
IMA_Module: Shared partition on standard IMA
NPU_Accelerator: Intel Movidius Myriad X (1 TOPS)
Memory: 256 MB allocated
Storage: 500 MB for model artifacts
Network: AFDX at 100 Mbps
```

## Software Configuration

```yaml
Operating_System: VxWorks 7 (standard configuration)
Runtime: ONNX Runtime Lite
Models_Supported:
  - Essential fuel consumption prediction
  - Basic system health monitoring
Update_Frequency: Quarterly
```

## Performance Targets

- Inference latency: <20ms (P99)
- Throughput: 100 inferences/second
- Model size: Up to 25MB
- Availability: >99%

## Cost Savings

- Reduced NPU hardware cost (~40% savings)
- Simplified certification (single engine)
- Lower operational overhead

## Traceability

- **Parent Assembly**: 95-00-04-A001
- **Requirements**: RQ-95-03-101 (Q80 variant specification)
- **Related**: Q100 (A100), Q120 (A102)

---

**Document Control**: AI prompted by Amedeo Pelliccia | Status: WORKING
