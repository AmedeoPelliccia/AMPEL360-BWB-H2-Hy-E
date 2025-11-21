# 02-90-03: Data Exchange Formats

## Purpose

This folder captures definitions of avionics data exchange formats and mappings into internal schemas for AMPEL360 operations systems.

## Scope

Data exchange format specifications for:

- **AFDX (Avionics Full-Duplex Switched Ethernet)**: Network topology and virtual link configurations
- **ARINC 429**: Legacy avionics data bus message formats
- **Protocol Buffers**: High-performance serialization for telemetry
- **JSON Schema**: Web and application data interchange

All specifications are **non-proprietary, generic examples** without OEM-specific configurations.

## Supported Formats

| Format | Standard | Use Case | Documentation |
|--------|----------|----------|---------------|
| **AFDX** | ARINC 664 Part 7 | Avionics networking | [ARINC 664](https://en.wikipedia.org/wiki/ARINC_664) |
| **ARINC 429** | ARINC 429 | Legacy avionics bus | [ARINC 429 Spec](https://en.wikipedia.org/wiki/ARINC_429) |
| **Protobuf** | Protocol Buffers v3 | High-performance serialization | [Protobuf Docs](https://protobuf.dev/) |
| **JSON Schema** | Draft 7+ | Web/app data validation | [JSON Schema Spec](https://json-schema.org/) |

## Structure

```
02-90-03_Data_Exchange_Formats/
├── README.md (this file)
├── 02-90-03-001_AFDX_Virtual_Links_Catalog.md
├── 02-90-03-002_ARINC_429_Label_Definitions.md
├── 02-90-03-003_Protocol_Buffers_Schemas.md
└── ASSETS/
    ├── AFDX/              # AFDX configuration examples
    ├── ARINC_429/         # ARINC 429 message definitions
    ├── Protobuf/          # .proto schemas
    └── JSON_Schema/       # JSON Schema definitions
```

## AFDX (Avionics Full-Duplex Switched Ethernet)

AFDX provides deterministic Ethernet networking for avionics systems.

### Virtual Links (VL)

Each VL represents a logical connection between data producers and consumers:

- **VL ID**: Unique identifier
- **Source/Destination**: End system identifiers
- **BAG (Bandwidth Allocation Gap)**: Minimum time between transmissions
- **Frame Size**: Maximum Ethernet frame size
- **QoS**: Quality of service parameters

Example: [VL Allocation Table](./ASSETS/AFDX/02-90-03-A-001_VL_Allocation_Table.xlsx)

### Network Topology

See [Network Topology Diagram](./ASSETS/AFDX/02-90-03-A-003_Network_Topology.svg) for logical structure.

## ARINC 429

ARINC 429 is a legacy avionics data bus standard still widely used.

### Message Format

32-bit word structure:
- **Bits 1-8**: Label (octal, identifies data type)
- **Bits 9-10**: SDI (Source/Destination Identifier)
- **Bits 11-29**: Data (payload)
- **Bits 30-31**: SSM (Sign/Status Matrix)
- **Bit 32**: Parity

### Label Dictionary

See [Label Dictionary](./ASSETS/ARINC_429/02-90-03-A-101_Label_Dictionary.xlsx) for message definitions.

## Protocol Buffers

Protocol Buffers provide efficient, language-neutral serialization.

### Schema Organization

- **flight_data.proto**: Flight operational data messages
- **telemetry.proto**: Generic telemetry streams
- **commands.proto**: Command/control messages

### Backward Compatibility

Protobuf schemas maintain compatibility by:
- Never reusing field numbers
- Making new fields optional
- Using reserved field numbers for removed fields

Example:

```protobuf
syntax = "proto3";

message FlightData {
  string flight_number = 1;
  string departure_airport = 2;
  string arrival_airport = 3;
  int64 scheduled_departure_unix = 4;
  
  reserved 5, 6;  // Removed fields
  reserved "old_field_name";
}
```

## JSON Schema

JSON Schema validates JSON documents against defined structures.

### Common Schemas

1. **[FlightPlan.schema.json](./ASSETS/JSON_Schema/02-90-03-A-301_FlightPlan.schema.json)**
   - Aligned with [02-40-15 Flight Planning](../../02-40_Software/02-40-15_Flight_Planning_Software/README.md)
   - GeoJSON for waypoints

2. **[WeatherData.schema.json](./ASSETS/JSON_Schema/02-90-03-A-302_WeatherData.schema.json)**
   - METAR/TAF-derived structures
   - Compatible with [02-40-17 Weather Processor](../../02-40_Software/02-40-17_Weather_Data_Processor/README.md)

3. **[PerformanceData.schema.json](./ASSETS/JSON_Schema/02-90-03-A-303_PerformanceData.schema.json)**
   - Performance calculator inputs/outputs
   - Used by [02-40-13 Performance Calculator](../../02-40_Software/02-40-13_Performance_Calculator/README.md)

## Data Mapping

### AFDX to Internal Schema

AFDX virtual link data is parsed and stored in [database schemas](../02-90-01_Database_Schemas/README.md):

```
AFDX VL → Parse → Validate → Store in PostgreSQL/TimescaleDB
```

### ARINC 429 to Internal Schema

ARINC 429 messages are decoded and mapped:

```
ARINC 429 Label → Decode → Map to field → Store in database
```

### Protobuf to REST API

Protobuf messages can be transcoded to JSON for REST APIs:

```
Protobuf Message → Transcode to JSON → REST API Response
```

## Security Considerations

- **No proprietary configurations**: All examples are generic
- **No real flight data**: Synthetic data only
- **No encryption keys**: Encryption shown conceptually only
- **Validation**: All incoming data must be validated against schemas

## Performance Characteristics

| Format | Serialization Speed | Size | Human Readable | Use Case |
|--------|---------------------|------|----------------|----------|
| AFDX | N/A (network protocol) | Fixed frame | No | Avionics networking |
| ARINC 429 | Fast | 4 bytes | No | Legacy avionics |
| Protobuf | Very Fast | Small | No | High-performance systems |
| JSON | Moderate | Large | Yes | Web/APIs |

## Cross-References

- [02-90-00-002 Data Dictionary](../02-90-00-002_Data_Dictionary_Master.md)
- [02-90-01 Database Schemas](../02-90-01_Database_Schemas/README.md)
- [02-90-02 API Specifications](../02-90-02_API_Specifications/README.md)
- [02-40 Software](../../02-40_Software/README.md)
- [ARINC 664 Part 7](https://en.wikipedia.org/wiki/ARINC_664) – AFDX specification
- [ARINC 429](https://en.wikipedia.org/wiki/ARINC_429) – Digital information transfer system
- [Protocol Buffers](https://protobuf.dev/) – Language-neutral data serialization

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
