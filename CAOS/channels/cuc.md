# CUC – Config & Update Channel

**Channel Type:** Downstream Update Distribution (Fleet Core → Regional → Ground → Aircraft)  
**Safety Classification:** Ground-install only (Parked/Maintenance state)  
**Related Standard:** AMPEL360-FAirCCC-ARCH-001 §4.1, §8

## Purpose

The Config & Update Channel (CUC) distributes signed model bundles, configuration updates, and change logs from Fleet Core to aircraft through a controlled, phased deployment process with human-in-the-loop approval.

## Key Characteristics

* **Direction:** F→R→G→A (Fleet Core to Regional to Ground to Aircraft)
* **Data Type:** Signed model bundles, configuration, change logs
* **Update Rate:** Bulk transfer at gate (disabled airborne)
* **Safety Impact:** Ground-only installation with maintenance approval

## S0 Authority Model

* **Sole Signer:** Fleet Core (FAirCCC-F) is the only entity authorized to sign releases
* **HSM-Backed:** All signatures generated via Hardware Security Module
* **Centralized Control:** No regional or ground authority to create releases
* **Human Approval:** Maintenance/dispatch approval gates installation

## Update Bundle Contents

Each CUC package contains:
1. `model.weights` – Model delta or full weights
2. `model.meta` – Model ID, version, compatibility info
3. `eval_report.json` – Metrics, datasets, robustness results
4. `safety_case.md` – Assurance arguments and operational limits
5. `changelog.md` – Human-readable change description
6. `signature.sig` – Fleet Core HSM signature (Ed25519)

## Deployment Phases

1. **Shadow Mode:** New model runs in parallel, outputs logged only
2. **Canary Deployment:** Limited subset of aircraft (test fleet)
3. **Staged Rollout:** Gradual fleet-wide deployment
4. **Full Deployment:** Complete fleet coverage

## Installation Policy

* **State Requirement:** Aircraft must be in Parked or Maintenance mode
* **Recording:** Installation logged by CM/DM systems
* **Rollback:** Always available; one-click via Ground station
* **Verification:** Post-install health checks mandatory

## Use Cases

* ML model updates (maintenance, efficiency, operations)
* Configuration parameter updates
* Non-safety system optimizations
* Advisory system improvements

## Security & Validation

### Ground Station (FAirCCC-G)
- Signature verification (Fleet Core public key)
- Bundle integrity checks (SHA-256 hashes)
- Compatibility validation (aircraft type, firmware version)
- Installation state verification (Parked/Maintenance)

### Aircraft (FAirCCC-A)
- Signature verification before installation
- Rollback point creation
- Post-install validation
- Operational limits enforcement

## Data Schema

*Detailed CUC manifest schema in AMPEL360-FAirCCC-ARCH-001 §8.1 and §16*

## Security & Transport

* **Encryption:** mTLS (TLS 1.3)
* **Encoding:** Bundle metadata in JSON/CBOR, weights in binary format
* **Authentication:** Certificate pinning for Fleet Core identity
* **Integrity:** SHA-256 hashes for all bundle components
* **Signature:** Ed25519 signatures from Fleet Core HSM

## Threat Mitigations

* Supply-chain tampering protection (SLSA attestations)
* Rogue update prevention (HSM-only signing)
* Rollback capability (always maintained)
* Phased deployment (canary testing)
* Kill-switches (per-model, per-tail)

## Data Schema
### Message Format
```json
{
  "header": {
    "channel_id": "string",
    "timestamp": "ISO8601",
    "sequence_number": "integer",
    "source_node": "string",
    "destination_node": "string"
  },
  "payload": {
    // Channel-specific payload structure
  },
  "signature": "base64"
}
```

## Protocol Details
### Communication Flow (F→R→G→A (Fleet Core to Regional to Ground to Aircraft))

1. **Connection Establishment**: mTLS handshake with mutual authentication
2. **Data Transmission**: CBOR-encoded messages with signature verification
3. **Acknowledgment**: Receiver confirms receipt and validation
4. **Error Recovery**: Automatic retry with exponential backoff

## Error Handling
### Error Codes

| Code | Description | Recovery Action |
|------|-------------|------------------|
| E001 | Authentication failure | Re-establish mTLS connection |
| E002 | Invalid signature | Reject message, log incident |
| E003 | Malformed payload | Request retransmission |
| E004 | Sequence number gap | Request missing messages |
| E005 | Timeout | Retry with exponential backoff |

## Performance Metrics
### Expected Performance

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| Latency | < 100ms (p95) | End-to-end message timing |
| Throughput | ≥ 1000 msg/sec | Messages per second |
| Reliability | 99.99% | Successful transmissions |
| Data Loss | < 0.01% | Missing sequence numbers |

## Implementation Notes
### Client Implementation

```python
# Example client implementation
class ChannelClient:
    def __init__(self, node_id: str, tpm_cert_path: str):
        self.node_id = node_id
        self.cert = load_tpm_certificate(tpm_cert_path)
        self.connection = None
    
    def connect(self):
        # Establish mTLS connection
        pass
    
    def send_message(self, payload: dict):
        # Send CBOR-encoded message
        pass
```

## Testing & Validation
### Test Scenarios

1. **Happy Path Testing**
   - Normal message transmission
   - Acknowledgment handling
   - Performance under load

2. **Error Condition Testing**
   - Network interruption
   - Invalid authentication
   - Malformed messages

3. **Security Testing**
   - Certificate validation
   - Signature verification
   - Replay attack prevention

## Compliance
### Standards Mapping

| Standard | Requirement | Implementation |
|----------|-------------|----------------|
| DO-326A | Security process | mTLS + attestation |
| EASA AI L2 | Advisory scope | Non-safety classification |
| ARP4754A | System architecture | Documented interfaces |



## Related Documents

* [AMPEL360-FAirCCC-ARCH-001 – Federated Architecture](../AMPEL360-FAirCCC-ARCH-001_Federated_Aircraft_Cloud_Computing_Campus.md)
* [OFEC – Operational Flight Envelope Channel](ofec.md)
* [PMT – Predictive Maintenance Telemetry](pmt.md)
* [CFLF-GRAD – Collaborative Federated Learning Fabric (Gradient Channel)](cflf-grad.md)


---

*Last updated: 2025-11-21 by GenCCC continuous generation*
