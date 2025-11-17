# Provenance Chain Sub-Assembly

**Assembly ID**: 95-00-04-A051  
**Parent**: 95-00-04-A050 (Blockchain DPP)  
**Version**: 1.0
**Status**: WORKING

## Purpose

Blockchain ledger infrastructure for immutable provenance tracking.

## Blockchain Platform

**Production**: Hyperledger Fabric
- Permissioned consortium blockchain
- PBFT consensus (crash fault tolerant)
- Private channels for sensitive data
- Chaincode in Go

**Test/Development**: Ethereum Sepolia
- Public testnet for prototyping
- Solidity smart contracts
- ERC-721 for model NFTs

## Ledger Structure

```yaml
Block:
  header:
    block_number: uint64
    previous_hash: bytes32
    timestamp: uint64
    merkle_root: bytes32
  transactions:
    - tx_id: UUID
      type: enum (model_register, certify, deploy, retire)
      payload: JSON
      signature: ECDSA
      from_address: account
```

## Operations

- Transaction submission
- Block validation
- Consensus participation
- Ledger query and verification

## Traceability

- **Requirements**: RQ-95-03-040
- **Parent Assembly**: 95-00-04-A050
- **Related**: Cryptographic Anchors (A052), Smart Contracts (A053)

---

**Document Control**: AI prompted by Amedeo Pelliccia | Status: WORKING
