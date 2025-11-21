# 02-90-00-002: Master Data Dictionary

## 1. Purpose

This document defines the master data dictionary structure for ATA 02 Operations Information, including conventions for field names, data types, units, and cross-references to schemas and APIs.

## 2. Data Dictionary Principles

### 2.1 Naming Conventions

All field names must follow these rules:

#### Table and Collection Names
- **Format**: `snake_case` for SQL databases, `PascalCase` for document stores
- **Pattern**: `<domain>_<entity>_<qualifier>`
- **Examples**:
  - SQL: `flight_operations_legs`, `energy_monitoring_channels`
  - MongoDB: `FlightPlans`, `WeatherData`

#### Field Names
- **Format**: `snake_case` for all databases
- **Pattern**: `<entity>_<attribute>_<unit_or_type>`
- **Examples**:
  - `flight_departure_time_utc`
  - `fuel_quantity_kg`
  - `temperature_degc`
  - `status_code`

#### Reserved Prefixes
- `id_` – Primary keys and identifiers
- `fk_` – Foreign keys
- `ts_` – Timestamps
- `is_` – Boolean flags
- `cnt_` – Counters
- `amt_` – Amounts (money, quantity)
- `pct_` – Percentages
- `idx_` – Indexes

### 2.2 Data Types

#### Standard SQL Data Types

| Data Type | Use Case | Example |
|-----------|----------|---------|
| `BIGSERIAL` | Auto-incrementing primary keys | `id_flight BIGSERIAL PRIMARY KEY` |
| `UUID` | Globally unique identifiers | `id_transaction UUID DEFAULT gen_random_uuid()` |
| `VARCHAR(n)` | Variable-length text with limit | `airport_code VARCHAR(4)` |
| `TEXT` | Unbounded text | `description TEXT` |
| `INTEGER` | Whole numbers | `passenger_count INTEGER` |
| `NUMERIC(p,s)` | Precise decimal numbers | `fuel_quantity_kg NUMERIC(10,2)` |
| `TIMESTAMP` | Date and time (no timezone) | `created_at TIMESTAMP` |
| `TIMESTAMPTZ` | Date and time (with timezone) | `departure_time_utc TIMESTAMPTZ` |
| `BOOLEAN` | True/false flags | `is_active BOOLEAN DEFAULT true` |
| `JSONB` | JSON data (PostgreSQL) | `metadata JSONB` |
| `ENUM` | Fixed set of values | `status flight_status_enum` |

#### TimescaleDB-Specific
- Use `TIMESTAMPTZ` for time-series primary dimension
- Define appropriate chunk intervals (1 day, 1 week, 1 month)

#### MongoDB Data Types
- `ObjectId` – Document identifiers
- `String` – Text data
- `Number` – Numeric values (Int32, Int64, Double)
- `Date` – ISO 8601 timestamps
- `Boolean` – True/false values
- `Array` – Lists of values
- `Object` – Nested documents

#### Redis Data Structures
- `STRING` – Simple key-value pairs
- `HASH` – Field-value maps
- `LIST` – Ordered collections
- `SET` – Unique unordered collections
- `SORTED SET` – Ordered sets with scores
- `TTL` – Time-to-live (seconds)

### 2.3 Units and Measurements

All physical quantities must specify units using suffixes:

#### Mass
- `_kg` – Kilograms
- `_lb` – Pounds
- `_ton` – Metric tons

#### Distance
- `_m` – Meters
- `_km` – Kilometers
- `_nm` – Nautical miles
- `_ft` – Feet

#### Speed
- `_mps` – Meters per second
- `_kts` – Knots
- `_kmh` – Kilometers per hour

#### Temperature
- `_degc` – Degrees Celsius
- `_degk` – Kelvin
- `_degf` – Degrees Fahrenheit

#### Energy/Power
- `_kwh` – Kilowatt-hours
- `_kw` – Kilowatts
- `_mw` – Megawatts
- `_j` – Joules

#### Pressure
- `_pa` – Pascals
- `_hpa` – Hectopascals
- `_psi` – Pounds per square inch

#### Time
- `_sec` – Seconds
- `_min` – Minutes
- `_hr` – Hours
- `_utc` – UTC timestamp
- `_local` – Local time

#### Dimensionless
- `_pct` – Percentage (0-100)
- `_ratio` – Ratio (0-1)
- `_count` – Integer count

### 2.4 Null Handling

- **Required fields**: Use `NOT NULL` constraint
- **Optional fields**: Allow `NULL`
- **Default values**: Use `DEFAULT` where appropriate
- **Semantic nulls**: Consider special values (e.g., -9999 for "not applicable") with documentation

## 3. Common Field Definitions

### 3.1 Identifiers

```sql
-- Primary key (auto-incrementing)
id_<entity> BIGSERIAL PRIMARY KEY

-- UUID primary key
id_<entity> UUID DEFAULT gen_random_uuid() PRIMARY KEY

-- Foreign key reference
fk_<referenced_entity> BIGINT REFERENCES <table>(id_<entity>)
```

### 3.2 Timestamps

```sql
-- Creation timestamp (immutable)
ts_created_utc TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP

-- Last update timestamp
ts_updated_utc TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP

-- Logical delete timestamp
ts_deleted_utc TIMESTAMPTZ

-- Business event timestamp
ts_event_utc TIMESTAMPTZ NOT NULL
```

### 3.3 Status and State

```sql
-- Enumerated status
status_code VARCHAR(20) NOT NULL
status_description TEXT

-- Boolean flags
is_active BOOLEAN DEFAULT true
is_deleted BOOLEAN DEFAULT false
is_validated BOOLEAN DEFAULT false
```

### 3.4 Audit Fields

```sql
-- User tracking
created_by_user_id BIGINT REFERENCES users(id_user)
updated_by_user_id BIGINT REFERENCES users(id_user)

-- Source tracking
source_system VARCHAR(50)
source_transaction_id VARCHAR(100)
```

### 3.5 Metadata

```sql
-- JSON metadata for extensibility
metadata JSONB

-- Version tracking
version_number INTEGER DEFAULT 1
version_hash VARCHAR(64)
```

## 4. Domain-Specific Dictionaries

### 4.1 Flight Operations

| Field Name | Data Type | Description | Unit | Constraints |
|------------|-----------|-------------|------|-------------|
| `flight_number` | VARCHAR(10) | Flight designator | - | NOT NULL |
| `departure_airport_icao` | VARCHAR(4) | ICAO airport code | - | NOT NULL, CHECK length=4 |
| `arrival_airport_icao` | VARCHAR(4) | ICAO airport code | - | NOT NULL, CHECK length=4 |
| `scheduled_departure_utc` | TIMESTAMPTZ | Scheduled departure time | UTC | NOT NULL |
| `actual_departure_utc` | TIMESTAMPTZ | Actual departure time | UTC | - |
| `fuel_planned_kg` | NUMERIC(10,2) | Planned fuel load | kg | CHECK > 0 |
| `fuel_actual_kg` | NUMERIC(10,2) | Actual fuel at departure | kg | CHECK > 0 |
| `passengers_count` | INTEGER | Number of passengers | - | CHECK >= 0 |
| `cargo_mass_kg` | NUMERIC(10,2) | Cargo mass | kg | CHECK >= 0 |

### 4.2 Performance Data

| Field Name | Data Type | Description | Unit | Constraints |
|------------|-----------|-------------|------|-------------|
| `altitude_ft` | INTEGER | Altitude | feet | CHECK >= 0 |
| `airspeed_kts` | NUMERIC(6,2) | Indicated airspeed | knots | CHECK > 0 |
| `mach_number` | NUMERIC(4,3) | Mach number | - | CHECK > 0 AND < 5 |
| `vertical_speed_fpm` | INTEGER | Vertical speed | ft/min | - |
| `fuel_flow_kgh` | NUMERIC(8,2) | Fuel flow rate | kg/hr | CHECK >= 0 |
| `outside_air_temp_degc` | NUMERIC(5,2) | Outside air temperature | °C | - |

### 4.3 Energy Monitoring

| Field Name | Data Type | Description | Unit | Constraints |
|------------|-----------|-------------|------|-------------|
| `channel_id` | VARCHAR(20) | Energy channel identifier | - | NOT NULL |
| `voltage_v` | NUMERIC(8,3) | Voltage | volts | CHECK >= 0 |
| `current_a` | NUMERIC(8,3) | Current | amperes | - |
| `power_kw` | NUMERIC(10,3) | Power | kilowatts | - |
| `energy_kwh` | NUMERIC(12,4) | Energy consumed | kWh | CHECK >= 0 |
| `power_factor` | NUMERIC(4,3) | Power factor | - | CHECK >= 0 AND <= 1 |
| `frequency_hz` | NUMERIC(6,3) | Frequency | hertz | CHECK > 0 |

### 4.4 Propulsion Data

| Field Name | Data Type | Description | Unit | Constraints |
|------------|-----------|-------------|------|-------------|
| `engine_position` | VARCHAR(10) | Engine position (L1, R1, etc.) | - | NOT NULL |
| `thrust_n` | NUMERIC(10,2) | Thrust | newtons | CHECK >= 0 |
| `n1_pct` | NUMERIC(5,2) | N1 fan speed | % | CHECK >= 0 AND <= 120 |
| `n2_pct` | NUMERIC(5,2) | N2 core speed | % | CHECK >= 0 AND <= 120 |
| `egt_degc` | NUMERIC(6,2) | Exhaust gas temperature | °C | CHECK > 0 |
| `fuel_flow_kg_h` | NUMERIC(8,2) | Fuel flow | kg/hr | CHECK >= 0 |
| `oil_pressure_psi` | NUMERIC(6,2) | Oil pressure | PSI | CHECK >= 0 |
| `oil_temp_degc` | NUMERIC(5,2) | Oil temperature | °C | CHECK > 0 |

## 5. Cross-References

### 5.1 Schema to API Mapping

| Schema | API Specification | Purpose |
|--------|------------------|---------|
| [Flight Operations Schema](./02-90-01_Database_Schemas/ASSETS/SQL/02-90-01-A-001_Flight_Operations_Schema.sql) | [Flight Operations API](./02-90-02_API_Specifications/ASSETS/OpenAPI/02-90-02-A-001_Flight_Operations_API_v1.yaml) | Flight CRUD operations |
| [Performance Data Schema](./02-90-01_Database_Schemas/ASSETS/SQL/02-90-01-A-002_Performance_Data_Schema.sql) | [Performance Calculator API](./02-90-02_API_Specifications/ASSETS/OpenAPI/02-90-02-A-002_Performance_Calculator_API_v1.yaml) | Performance calculations |
| [Energy Monitoring Schema](./02-90-01_Database_Schemas/ASSETS/SQL/02-90-01-A-003_Energy_Monitoring_Schema.sql) | [Energy Monitoring API](./02-90-02_API_Specifications/ASSETS/OpenAPI/02-90-02-A-003_Energy_Monitoring_API_v1.yaml) | Energy data streams |

### 5.2 Code Lists and Enumerations

All code lists are defined in [02-90-08 Code Lists](./02-90-08_Code_Lists_Enumerations/README.md):

- [ICAO Airport Codes](./02-90-08_Code_Lists_Enumerations/ASSETS/ICAO/02-90-08-A-001_Airport_Codes.csv)
- [Aircraft Type Codes](./02-90-08_Code_Lists_Enumerations/ASSETS/ICAO/02-90-08-A-002_Aircraft_Type_Designators.csv)
- [Flight Phases](./02-90-08_Code_Lists_Enumerations/ASSETS/Operational/02-90-08-A-201_Flight_Phases.yaml)
- [Status Codes](./02-90-08_Code_Lists_Enumerations/ASSETS/System_Codes/02-90-08-A-102_Status_Codes.yaml)

## 6. Validation Rules

### 6.1 Automated Validation

All schemas must pass:

1. **SQL Linting**: SQLFluff or similar tool
2. **JSON Schema Validation**: Against JSON Schema Draft 7+
3. **OpenAPI Validation**: Against OpenAPI 3.1 specification
4. **Naming Convention Checks**: Custom validation scripts

### 6.2 Manual Review

Required for:

1. **New entity types**: Architecture review board approval
2. **Breaking changes**: Change control board approval
3. **Cross-ATA impacts**: Multi-domain review

## 7. Deprecation Policy

When fields or tables are deprecated:

1. Mark as `@deprecated` in documentation
2. Set `is_deprecated BOOLEAN DEFAULT false` flag
3. Add `deprecation_date DATE`
4. Document replacement field/table
5. Maintain for minimum 2 major versions

## 8. References

- [02-90-00-001 Tables Schemas Overview](./02-90-00-001_Tables_Schemas_Overview.md)
- [02-90-00-004 Schema Version Control](./02-90-00-004_Schema_Version_Control.md)
- [02-90-01 Database Schemas](./02-90-01_Database_Schemas/README.md)
- [02-90-08 Code Lists Enumerations](./02-90-08_Code_Lists_Enumerations/README.md)
- [CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) – Equipment, systems, and installations
- [DO-178C](https://en.wikipedia.org/wiki/DO-178C) – Software considerations

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
