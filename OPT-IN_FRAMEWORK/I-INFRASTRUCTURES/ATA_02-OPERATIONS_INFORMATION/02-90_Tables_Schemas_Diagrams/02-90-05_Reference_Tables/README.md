# 02-90-05: Reference Tables

## Purpose

This folder centralizes operational reference tables (airports, configurations, performance, environment) used across AMPEL360 operations systems.

## Scope

Reference tables provide static operational data for:

- **Airports**: ICAO/IATA codes, runways, H2 infrastructure
- **Aircraft Configuration**: Weight/balance, seating, fuel tanks
- **Performance Tables**: Takeoff, landing, climb, cruise performance
- **Environmental Data**: ISA atmosphere, wind corrections, temperature adjustments

All data is **non-proprietary, synthetic, or public-domain** suitable for testing and demonstration.

## Structure

```
02-90-05_Reference_Tables/
├── README.md (this file)
├── 02-90-05-001_Airport_Database.md
├── 02-90-05-002_Aircraft_Configuration_Tables.md
├── 02-90-05-003_Performance_Tables.md
└── ASSETS/
    ├── Airports/          # Airport and runway data
    ├── Aircraft_Config/   # Aircraft configurations
    ├── Performance/       # Performance tables
    └── Environmental/     # Environmental reference data
```

## Key Reference Tables

### Airports

- **[Airport Master List](./ASSETS/Airports/02-90-05-A-001_Airport_Master_List.csv)**: ICAO/IATA codes, names, countries
- **[Runway Database](./ASSETS/Airports/02-90-05-A-002_Runway_Database.csv)**: Runway dimensions, surfaces, elevations
- **[H2 Infrastructure](./ASSETS/Airports/02-90-05-A-003_H2_Infrastructure_Airports.csv)**: Airports with hydrogen infrastructure
- **[Airport Geolocation](./ASSETS/Airports/02-90-05-A-004_Airport_Geolocation.geojson)**: GeoJSON for mapping

### Aircraft Configuration

- **[Weight & Balance](./ASSETS/Aircraft_Config/02-90-05-A-101_Weight_Balance_Config.yaml)**: Mass stations and loading schemes
- **[Seating Configurations](./ASSETS/Aircraft_Config/02-90-05-A-102_Seating_Configurations.yaml)**: Seat layouts and classes
- **[Fuel Tank Configuration](./ASSETS/Aircraft_Config/02-90-05-A-103_Fuel_Tank_Configurations.yaml)**: Tank capacities (conceptual)
- **[System Configurations](./ASSETS/Aircraft_Config/02-90-05-A-104_System_Configurations.yaml)**: System option profiles

### Performance Tables

- **[Takeoff Performance](./ASSETS/Performance/02-90-05-A-201_Takeoff_Performance_Tables.xlsx)**: Synthetic takeoff data
- **[Landing Performance](./ASSETS/Performance/02-90-05-A-202_Landing_Performance_Tables.xlsx)**: Synthetic landing data
- **[Cruise Performance](./ASSETS/Performance/02-90-05-A-203_Cruise_Performance_Tables.xlsx)**: Fuel flow, range (conceptual)
- **[Climb Performance](./ASSETS/Performance/02-90-05-A-204_Climb_Performance_Tables.xlsx)**: Climb rates and fuel
- **[H2 Fuel Consumption](./ASSETS/Performance/02-90-05-A-205_H2_Fuel_Consumption_Tables.xlsx)**: Hydrogen consumption estimates

### Environmental

- **[ISA Atmosphere Table](./ASSETS/Environmental/02-90-05-A-301_ISA_Atmosphere_Table.csv)**: Standard atmosphere data
- **[Wind Correction Tables](./ASSETS/Environmental/02-90-05-A-302_Wind_Correction_Tables.xlsx)**: Wind impact on performance
- **[Temperature Correction](./ASSETS/Environmental/02-90-05-A-303_Temperature_Correction_Tables.xlsx)**: Temperature adjustments

## Data Quality

### Standards

- **Accuracy**: Reference data aligned with public standards
- **Currency**: Regular updates for airport/regulatory changes
- **Completeness**: Comprehensive coverage for testing scenarios
- **Consistency**: Cross-referenced with [Data Dictionary](../02-90-00-002_Data_Dictionary_Master.md)

### Validation

- CSV files validated for structure and encoding
- YAML files validated against schema
- GeoJSON validated for WGS84 coordinates
- Excel files include data validation rules

## Usage

### Loading into Databases

Reference tables can be loaded into [database schemas](../02-90-01_Database_Schemas/README.md):

```sql
COPY airports FROM 'Airports/02-90-05-A-001_Airport_Master_List.csv' CSV HEADER;
```

### API Integration

Reference data accessed via [APIs](../02-90-02_API_Specifications/README.md):

```
GET /api/v1/reference/airports?icao=KJFK
GET /api/v1/reference/performance/takeoff?weight=70000&altitude=5000
```

### Application Usage

Applications like [02-40-13 Performance Calculator](../../02-40_Software/02-40-13_Performance_Calculator/README.md) use these tables for calculations.

## Update Process

1. **Source identification**: Verify data source (ICAO, FAA, public databases)
2. **Validation**: Check data quality and consistency
3. **Documentation**: Update metadata and change log
4. **Review**: Peer review for accuracy
5. **Deployment**: Update production reference data

## Cross-References

- [02-90-00-002 Data Dictionary](../02-90-00-002_Data_Dictionary_Master.md)
- [02-90-01 Database Schemas](../02-90-01_Database_Schemas/README.md)
- [02-40-13 Performance Calculator](../../02-40_Software/02-40-13_Performance_Calculator/README.md)
- [02-40-15 Flight Planning](../../02-40_Software/02-40-15_Flight_Planning_Software/README.md)
- [ICAO Aerodrome Reference Code](https://www.icao.int/)
- [ISA Standard Atmosphere](https://en.wikipedia.org/wiki/International_Standard_Atmosphere)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
