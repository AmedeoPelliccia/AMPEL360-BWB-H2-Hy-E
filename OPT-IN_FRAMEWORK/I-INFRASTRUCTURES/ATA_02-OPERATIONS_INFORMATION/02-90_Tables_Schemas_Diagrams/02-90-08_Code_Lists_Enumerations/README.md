# 02-90-08: Code Lists and Enumerations

## Purpose

This folder stores standardized code lists and enumerations used throughout the AMPEL360 operations system.

## Scope

Code lists provide standardized values for:

- **ICAO Codes**: Airport, aircraft type, airline codes
- **System Codes**: Error codes, status codes, alert codes, priority levels
- **Operational Codes**: Flight phases, weather codes, fuel grades
- **Translations**: Multi-language code descriptions

All code lists are **publicly sourced or synthetic** examples suitable for development and testing.

## Structure

```
02-90-08_Code_Lists_Enumerations/
├── README.md (this file)
├── 02-90-08-001_ICAO_Code_Lists.md
├── 02-90-08-002_Aircraft_Type_Codes.md
├── 02-90-08-003_Message_Type_Codes.md
└── ASSETS/
    ├── ICAO/              # ICAO-related codes
    ├── System_Codes/      # System-level enumerations
    ├── Operational/       # Operational reference codes
    └── Translations/      # Multi-language translations
```

## ICAO Code Lists

### Airport Codes

[Airport codes](./ASSETS/ICAO/02-90-08-A-001_Airport_Codes.csv) include:

- **ICAO Code**: 4-letter code (e.g., KJFK)
- **IATA Code**: 3-letter code (e.g., JFK)
- **Name**: Airport name
- **City**: City name
- **Country**: Country code

### Aircraft Type Designators

[Aircraft types](./ASSETS/ICAO/02-90-08-A-002_Aircraft_Type_Designators.csv) include:

- **Type Code**: ICAO designator (e.g., B738, A320)
- **Manufacturer**: Aircraft manufacturer
- **Model**: Aircraft model
- **AMPEL360**: Conceptual AMPEL360 family designators

### Airline Codes

[Airline codes](./ASSETS/ICAO/02-90-08-A-003_Airline_Codes.csv) for testing:

- **ICAO Code**: 3-letter airline code
- **IATA Code**: 2-letter airline code
- **Name**: Airline name
- **Country**: Country of registration

## System Codes

### Error Codes

[Error codes](./ASSETS/System_Codes/02-90-08-A-101_Error_Codes.yaml) structure:

```yaml
error_codes:
  - code: "ERR_001"
    severity: "ERROR"
    description: "Database connection failed"
    resolution: "Check database connectivity and credentials"
  
  - code: "ERR_002"
    severity: "WARNING"
    description: "API rate limit approaching"
    resolution: "Reduce request frequency or increase limit"
```

### Status Codes

[Status codes](./ASSETS/System_Codes/02-90-08-A-102_Status_Codes.yaml) for systems:

- **NORMAL**: Operating normally
- **DEGRADED**: Reduced capacity or performance
- **FAILED**: System failure
- **MAINTENANCE**: Scheduled maintenance
- **UNKNOWN**: Status cannot be determined

### Alert Codes

[Alert codes](./ASSETS/System_Codes/02-90-08-A-103_Alert_Codes.yaml) aligned with energy and propulsion monitoring.

### Priority Levels

[Priority levels](./ASSETS/System_Codes/02-90-08-A-104_Priority_Levels.yaml):

- **P0**: Critical - immediate action required
- **P1**: High - urgent attention needed
- **P2**: Medium - attention required soon
- **P3**: Low - can be deferred
- **P4**: Informational - no action required

## Operational Codes

### Flight Phases

[Flight phases](./ASSETS/Operational/02-90-08-A-201_Flight_Phases.yaml):

```yaml
flight_phases:
  - code: "PREFLIGHT"
    name: "Pre-Flight"
    description: "Aircraft preparation and boarding"
    sort_order: 10
  
  - code: "TAXI_OUT"
    name: "Taxi Out"
    description: "Taxi from gate to runway"
    sort_order: 20
```

### Weather Codes

[Weather codes](./ASSETS/Operational/02-90-08-A-202_Weather_Codes.yaml) for internal processing:

- Weather phenomena categories
- Severity levels
- Impact on operations

### Fuel Grades

[Fuel grades](./ASSETS/Operational/02-90-08-A-203_Fuel_Grades.yaml):

- **JET_A**: Conventional jet fuel
- **JET_A1**: Jet fuel with lower freezing point
- **SAF**: Sustainable Aviation Fuel
- **LH2**: Liquid Hydrogen (AMPEL360)
- **GH2**: Gaseous Hydrogen

## Translations

Multi-language support for UI and reports:

- **[English](./ASSETS/Translations/02-90-08-A-301_Code_Translations_EN.json)**: Primary language
- **[German](./ASSETS/Translations/02-90-08-A-302_Code_Translations_DE.json)**: German translations
- **[French](./ASSETS/Translations/02-90-08-A-303_Code_Translations_FR.json)**: French translations

Translation structure:

```json
{
  "codes": {
    "FLIGHT_STATUS": {
      "SCHEDULED": "Scheduled",
      "BOARDING": "Boarding",
      "DEPARTED": "Departed",
      "ARRIVED": "Arrived"
    }
  }
}
```

## Governance

### Update Process

1. **Source verification**: Validate against official sources (ICAO, ISO)
2. **Change request**: Document change rationale
3. **Impact analysis**: Assess impact on systems
4. **Peer review**: Technical review
5. **Deployment**: Update code lists in staging, then production

### Synchronization

Code lists synchronized across:
- Database enumerations
- API specifications
- Application constants
- UI dropdowns

### Versioning

Code lists follow [Semantic Versioning](../02-90-00-004_Schema_Version_Control.md):

- **Major**: Removed codes or changed semantics
- **Minor**: Added codes
- **Patch**: Corrections to descriptions

## Usage

### In Database Schemas

```sql
CREATE TYPE flight_status_enum AS ENUM (
    'SCHEDULED', 'BOARDING', 'DEPARTED', 'ARRIVED', 'CANCELLED'
);

CREATE TABLE flights (
    id_flight BIGSERIAL PRIMARY KEY,
    status flight_status_enum NOT NULL DEFAULT 'SCHEDULED'
);
```

### In API Specifications

```yaml
FlightStatus:
  type: string
  enum:
    - SCHEDULED
    - BOARDING
    - DEPARTED
    - ARRIVED
    - CANCELLED
```

### In Application Code

```python
from enum import Enum

class FlightStatus(Enum):
    SCHEDULED = "SCHEDULED"
    BOARDING = "BOARDING"
    DEPARTED = "DEPARTED"
    ARRIVED = "ARRIVED"
    CANCELLED = "CANCELLED"
```

## Cross-References

- [02-90-00-002 Data Dictionary](../02-90-00-002_Data_Dictionary_Master.md)
- [02-90-01 Database Schemas](../02-90-01_Database_Schemas/README.md)
- [02-90-02 API Specifications](../02-90-02_API_Specifications/README.md)
- [ICAO Standards](https://www.icao.int/)
- [ISO Country Codes](https://www.iso.org/iso-3166-country-codes.html)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
