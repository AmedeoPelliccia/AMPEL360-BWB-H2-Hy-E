# 02-40-16 – Dispatch Interface

## Purpose

This folder contains the dispatch/AOC (Airline Operations Center) interface software that handles bidirectional communication between aircraft and ground via ACARS and SITA networks.

---

## Scope

- **ACARS/SITA Integration**: Message handling over VHF/HF/SATCOM
- **Message Types**: Position reports, weather requests, maintenance messages, AOC uplink/downlink
- **Protocol Support**: ACARS protocols, ARINC standards
- **Reliability**: Message queuing, retries, acknowledgments

---

## Documentation Files

- **[02-40-16-001_Dispatch_Interface_Architecture.md](02-40-16-001_Dispatch_Interface_Architecture.md)**: Dispatch integration architecture
- **[02-40-16-002_ACARS_SITA_Integration.md](02-40-16-002_ACARS_SITA_Integration.md)**: ACARS/SITA protocol details
- **[02-40-16-003_Message_Handling.md](02-40-16-003_Message_Handling.md)**: Message queuing and error handling

---

## ASSETS Structure

### Source_Code/
- **acars_client/**: ACARS client implementation
- **sita_adapter/**: SITA network adapter
- **message_queue/**: Message queue integration (Kafka, RabbitMQ)

---

## References

- [ARINC 618](https://www.arinc.com/) – ACARS Standards
- [SITA Documentation](https://www.sita.aero/)

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: _2025-11-21_.
