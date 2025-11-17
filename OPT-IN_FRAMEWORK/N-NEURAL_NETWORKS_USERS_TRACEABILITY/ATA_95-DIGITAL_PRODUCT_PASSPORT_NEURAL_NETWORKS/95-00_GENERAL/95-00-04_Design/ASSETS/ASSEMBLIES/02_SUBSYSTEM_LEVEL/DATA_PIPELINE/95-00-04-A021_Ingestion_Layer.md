# Ingestion Layer Sub-Assembly

**Assembly ID**: 95-00-04-A021  
**Parent**: 95-00-04-A020 (Data Pipeline)  
**Version**: 1.0
**Status**: WORKING

## Purpose

Collects and validates incoming data from aircraft and ground sources.

## Components

- Apache Kafka for streaming ingestion
- Schema validation (Avro/Protobuf)
- Data quality checks
- Deduplication and error handling

## Data Sources

- Flight Data Recorder (FDR) via ACARS
- Quick Access Recorder (QAR)
- Maintenance logs and reports
- Weather and navigation data
- Ground test data

## Traceability

- **Requirements**: RQ-95-03-010
- **Parent Assembly**: 95-00-04-A020

---

**Document Control**: AI prompted by Amedeo Pelliccia | Status: WORKING
