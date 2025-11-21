# 02-90-01: Database Schemas

## Purpose

This folder consolidates database schema definitions (SQL and NoSQL) used by AMPEL360 operations, performance, energy, and analytics systems.

## Scope

Database schemas provide the physical data storage layer for:

- **Flight Operations**: Flight legs, status, crew assignments
- **Performance Monitoring**: Takeoff, climb, cruise, landing metrics
- **Energy Management**: Power channels, energy counters, battery state
- **Propulsion Telemetry**: Engine parameters, fuel flow, temperatures
- **User Management**: Users, roles, permissions, authentication
- **Audit Logging**: System actions, changes, compliance tracking

All schemas contain **non-proprietary, synthetic, or example data** suitable for testing and development.

## Supported Technologies

| Technology | Version | Use Case | Documentation |
|------------|---------|----------|---------------|
| **PostgreSQL** | 13+ | Relational operational data | [PostgreSQL Docs](https://www.postgresql.org/docs/) |
| **TimescaleDB** | 2.8+ | Time-series telemetry | [TimescaleDB Docs](https://docs.timescale.com/) |
| **MongoDB** | 5.0+ | Semi-structured documents | [MongoDB Docs](https://www.mongodb.com/docs/) |
| **Redis** | 6.2+ | Caching and session data | [Redis Docs](https://redis.io/docs/) |

## Structure

```
02-90-01_Database_Schemas/
├── README.md (this file)
├── 02-90-01-001_PostgreSQL_Schemas.sql          # Example PostgreSQL DDL
├── 02-90-01-002_TimescaleDB_Hypertables.sql     # TimescaleDB time-series schemas
├── 02-90-01-003_MongoDB_Collections.json        # MongoDB document structures
├── 02-90-01-004_Redis_Data_Structures.yaml      # Redis key patterns and TTL
└── ASSETS/
    ├── SQL/                                      # Detailed SQL schemas
    │   ├── 02-90-01-A-001_Flight_Operations_Schema.sql
    │   ├── 02-90-01-A-002_Performance_Data_Schema.sql
    │   ├── 02-90-01-A-003_Energy_Monitoring_Schema.sql
    │   ├── 02-90-01-A-004_Propulsion_Data_Schema.sql
    │   ├── 02-90-01-A-005_User_Management_Schema.sql
    │   └── 02-90-01-A-006_Audit_Log_Schema.sql
    ├── NoSQL/                                    # NoSQL schemas
    │   ├── 02-90-01-A-101_Document_Store_Schema.json
    │   ├── 02-90-01-A-102_Flight_Plans_Schema.json
    │   └── 02-90-01-A-103_Weather_Data_Schema.json
    └── ERD/                                      # Entity-Relationship Diagrams
        ├── 02-90-01-A-201_Operations_ERD.drawio
        ├── 02-90-01-A-202_Operations_ERD.svg
        └── 02-90-01-A-203_Data_Relationships.pdf
```

## Key Schemas

### SQL Schemas

1. **[Flight Operations](./ASSETS/SQL/02-90-01-A-001_Flight_Operations_Schema.sql)**
   - Core flight data (flights, legs, crew)
   - Status tracking and transitions
   - Surrogate keys for data privacy

2. **[Performance Data](./ASSETS/SQL/02-90-01-A-002_Performance_Data_Schema.sql)**
   - Time-series performance metrics
   - Phase of flight segmentation
   - Optimized for TimescaleDB hypertables

3. **[Energy Monitoring](./ASSETS/SQL/02-90-01-A-003_Energy_Monitoring_Schema.sql)**
   - Power channel monitoring
   - Energy accumulation counters
   - Battery state of charge tracking

4. **[Propulsion Data](./ASSETS/SQL/02-90-01-A-004_Propulsion_Data_Schema.sql)**
   - Engine telemetry (N1, N2, EGT, fuel flow)
   - Aggregated and anonymized data
   - Aligned with [02-70 Propulsion](../../02-70_Propulsion/README.md) and [02-80 Energy](../../02-80_Energy/README.md)

5. **[User Management](./ASSETS/SQL/02-90-01-A-005_User_Management_Schema.sql)**
   - User accounts and authentication
   - Role-based access control (RBAC)
   - Session management

6. **[Audit Log](./ASSETS/SQL/02-90-01-A-006_Audit_Log_Schema.sql)**
   - Comprehensive audit trail
   - Compliance with security requirements
   - Immutable log records

### NoSQL Schemas

1. **[Document Store](./ASSETS/NoSQL/02-90-01-A-101_Document_Store_Schema.json)**
   - Generic document storage pattern
   - Metadata + payload structure
   - Flexible schema for semi-structured data

2. **[Flight Plans](./ASSETS/NoSQL/02-90-01-A-102_Flight_Plans_Schema.json)**
   - Waypoints, constraints, alternates
   - Compatible with [02-40-15 Flight Planning](../../02-40_Software/02-40-15_Flight_Planning_Software/README.md)
   - GeoJSON for spatial data

3. **[Weather Data](./ASSETS/NoSQL/02-90-01-A-103_Weather_Data_Schema.json)**
   - METAR/TAF-derived weather information
   - Compatible with [02-20-17 Weather](../../02-20_Subsystems/README.md) and [02-40-17 Weather Processor](../../02-40_Software/02-40-17_Weather_Data_Processor/README.md)
   - Time-series grid data

## Naming Conventions

Follow the [Data Dictionary](../02-90-00-002_Data_Dictionary_Master.md) naming conventions:

- **Tables**: `snake_case` (e.g., `flight_operations`, `energy_channels`)
- **Fields**: `snake_case` with units (e.g., `fuel_quantity_kg`, `temperature_degc`)
- **Primary keys**: `id_<entity>` (e.g., `id_flight`)
- **Foreign keys**: `fk_<referenced_entity>` (e.g., `fk_aircraft`)
- **Timestamps**: `ts_<event>_utc` (e.g., `ts_created_utc`)

## Usage Guidelines

### For Database Administrators

1. **Review ERD** ([Operations ERD](./ASSETS/ERD/02-90-01-A-202_Operations_ERD.svg)) before implementation
2. **Apply schemas** in development/staging environments first
3. **Test migrations** using provided test data
4. **Monitor performance** of indexes and constraints

### For Application Developers

1. **Reference Data Dictionary** for field definitions
2. **Use prepared statements** to prevent SQL injection
3. **Implement connection pooling** for performance
4. **Handle nulls appropriately** per schema constraints
5. **Follow ACID principles** for transactional data

### For Data Analysts

1. **Query read replicas** for analytics workloads
2. **Use materialized views** for complex aggregations
3. **Respect data retention** policies
4. **Anonymize sensitive data** in reports

## Version Control

All schemas follow [Semantic Versioning](../02-90-00-004_Schema_Version_Control.md):

- **Major version**: Breaking changes (field removal, type changes)
- **Minor version**: Backward-compatible additions (new fields, tables)
- **Patch version**: Bug fixes and clarifications

Current schema version: **v1.0.0**

## Security Considerations

- **No real operational data**: All examples use synthetic data
- **No credentials**: Connection strings not included in schemas
- **No PII**: Personal Identifiable Information excluded
- **Encryption**: Enable at-rest and in-transit encryption in production
- **Access control**: Implement least-privilege access

## Performance Optimization

### PostgreSQL
- **Indexes**: Created on foreign keys and frequently queried fields
- **Partitioning**: Time-based partitioning for large tables
- **Vacuuming**: Automated via autovacuum
- **Connection pooling**: PgBouncer or similar

### TimescaleDB
- **Chunk intervals**: 1 day for high-frequency data, 1 week for lower frequency
- **Compression**: Enable after data stabilizes (e.g., older than 7 days)
- **Continuous aggregates**: Pre-compute common time-series queries
- **Data retention**: Automated data retention policies

### MongoDB
- **Indexes**: Compound indexes for common query patterns
- **Sharding**: Horizontal partitioning for large collections
- **Aggregation pipelines**: Optimize with `$match` early
- **Read preference**: Use secondaries for read-heavy workloads

### Redis
- **TTL**: Aggressive TTL for cache data
- **Eviction policies**: LRU (Least Recently Used) for cache
- **Data structures**: Choose appropriate type (Hash vs String vs Sorted Set)
- **Persistence**: AOF for durability, RDB for backups

## Cross-References

- [02-90-00-001 Tables Schemas Overview](../02-90-00-001_Tables_Schemas_Overview.md)
- [02-90-00-002 Data Dictionary Master](../02-90-00-002_Data_Dictionary_Master.md)
- [02-90-00-004 Schema Version Control](../02-90-00-004_Schema_Version_Control.md)
- [02-90-02 API Specifications](../02-90-02_API_Specifications/README.md)
- [02-40 Software Applications](../../02-40_Software/README.md)
- [CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) – Systems and installations

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
