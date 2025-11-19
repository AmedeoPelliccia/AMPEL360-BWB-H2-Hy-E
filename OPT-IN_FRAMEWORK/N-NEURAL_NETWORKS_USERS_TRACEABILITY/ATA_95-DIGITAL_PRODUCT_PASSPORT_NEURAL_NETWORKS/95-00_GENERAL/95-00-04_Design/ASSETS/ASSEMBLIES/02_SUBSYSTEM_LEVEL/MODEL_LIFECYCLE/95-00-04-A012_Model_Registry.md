# Model Registry Sub-Assembly

**Assembly ID**: 95-00-04-A012  
**Parent**: 95-00-04-A010 (Model Lifecycle)  
**Version**: 1.0
**Status**: WORKING

## Purpose

Centralized repository for trained neural network models with blockchain-anchored provenance.

## Components

- **Storage Backend**: S3-compatible object storage (MinIO)
- **Metadata Database**: PostgreSQL with versioning
- **Registry API**: MLflow REST interface
- **Blockchain Anchoring**: Hyperledger Fabric connector

## Registry Schema

```yaml
model_entry:
  model_id: UUID (primary key)
  version: semver string (e.g., "1.2.3")
  artifact_uri: S3 path
  sha256_hash: cryptographic hash
  training_dataset_id: UUID (foreign key)
  performance_metrics: JSON
  certification_status: enum (pending/approved/rejected)
  blockchain_tx_hash: hex string
  created_at: timestamp
  created_by: user_id
```

## Operations

- Register new model version
- Query model by ID or version
- Retrieve model artifacts
- Update certification status
- Verify blockchain anchoring

## Traceability

- **Requirements**: RQ-95-03-002, RQ-95-03-003
- **Parent Assembly**: 95-00-04-A010
- **Interfaces**: Training Pipeline (A011), Deployment Controller (A013)

---

**Document Control**: AI prompted by Amedeo Pelliccia | Status: WORKING
