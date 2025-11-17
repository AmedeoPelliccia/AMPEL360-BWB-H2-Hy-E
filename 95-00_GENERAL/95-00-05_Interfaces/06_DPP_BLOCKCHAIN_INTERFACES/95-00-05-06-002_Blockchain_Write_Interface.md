# 95-00-05-06-002 Blockchain Write Interface

**Document ID:** 95-00-05-06-002
**Title:** Blockchain Write Interface for Digital Product Passport
**Version:** 1.0.0
**Status:** ACTIVE
**Date:** 2025-11-17
**Criticality:** DAL D

---

## 1. Overview

This interface enables writing AI/ML provenance data and model metadata to blockchain for immutable Digital Product Passport (DPP) records.

**Blockchain:** Ethereum-compatible (Layer 2 for cost efficiency)

---

## 2. Smart Contract Interface

### 2.1 Model Registry Contract

**Contract:** `ModelRegistry.sol`

**ABI:**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ModelRegistry {
    struct ModelMetadata {
        string modelId;
        string version;
        bytes32 weightsHash;      // SHA-256 of model weights
        bytes32 trainingDataHash; // SHA-256 of training dataset
        uint256 timestamp;
        address deployer;
        string certificationStatus;
    }

    mapping(bytes32 => ModelMetadata) public models;

    event ModelRegistered(
        bytes32 indexed modelHash,
        string modelId,
        string version,
        uint256 timestamp
    );

    function registerModel(
        string memory _modelId,
        string memory _version,
        bytes32 _weightsHash,
        bytes32 _trainingDataHash,
        string memory _certificationStatus
    ) public returns (bytes32) {
        bytes32 modelHash = keccak256(abi.encodePacked(_modelId, _version));

        require(models[modelHash].timestamp == 0, "Model already registered");

        models[modelHash] = ModelMetadata({
            modelId: _modelId,
            version: _version,
            weightsHash: _weightsHash,
            trainingDataHash: _trainingDataHash,
            timestamp: block.timestamp,
            deployer: msg.sender,
            certificationStatus: _certificationStatus
        });

        emit ModelRegistered(modelHash, _modelId, _version, block.timestamp);

        return modelHash;
    }

    function getModel(bytes32 _modelHash)
        public
        view
        returns (ModelMetadata memory)
    {
        require(models[_modelHash].timestamp != 0, "Model not found");
        return models[_modelHash];
    }
}
```

---

## 3. Write API

### 3.1 Register Model

**Endpoint:** `POST /blockchain/register-model`

**Request:**
```json
{
  "model_id": "h2_leak_predictor_v2.1",
  "version": "2.1.0",
  "weights_hash": "0x1234...abcd",
  "training_data_hash": "0x5678...ef01",
  "certification_status": "EASA_APPROVED"
}
```

**Response:**
```json
{
  "transaction_hash": "0xabcd...1234",
  "model_hash": "0x9876...5432",
  "block_number": 12345678,
  "timestamp": "2025-11-17T14:32:15.123Z",
  "gas_used": 125000,
  "status": "SUCCESS"
}
```

---

## 4. Provenance Tracking

### 4.1 Inference Audit Trail

**Event Emitted:**
```solidity
event InferenceRecorded(
    bytes32 indexed inferenceId,
    bytes32 indexed modelHash,
    bytes32 inputHash,
    bytes32 outputHash,
    uint256 timestamp
);
```

**Off-Chain Storage:**
- Detailed inference data stored in IPFS
- On-chain: IPFS content hash + metadata

---

## 5. Query Interface

**Endpoint:** `GET /blockchain/model/{model_hash}`

**Response:**
```json
{
  "model_id": "h2_leak_predictor_v2.1",
  "version": "2.1.0",
  "weights_hash": "0x1234...abcd",
  "deployed_at": "2025-11-17T14:32:15.123Z",
  "deployer": "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
  "certification_status": "EASA_APPROVED",
  "inference_count": 1234567
}
```

---

## 6. Gas Optimization

**Layer 2 Solution:** Optimism or Arbitrum for lower gas costs

**Batching:** Aggregate multiple writes into single transaction

**Estimated Costs:**
- Model Registration: ~$0.50 USD
- Inference Audit (batch of 100): ~$0.10 USD

---

**Related Documents:**
- 95-00-05-06-001 DPP Data Model
- 95-00-05-06-003 Blockchain Query Interface
- 95-00-05-06-004 Smart Contract ABI

---

**End of Document**
