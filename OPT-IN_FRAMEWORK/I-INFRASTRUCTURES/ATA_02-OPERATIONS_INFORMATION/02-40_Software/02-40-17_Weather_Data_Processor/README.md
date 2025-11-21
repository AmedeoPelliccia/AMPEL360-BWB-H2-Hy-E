# 02-40-17 – Weather Data Processor

## Purpose

This folder contains the weather data processing services that ingest, parse, normalize, and distribute meteorological data (METAR, TAF, GRIB, radar, satellite) to operational systems and the EFB.

---

## Scope

- **Data Ingestion**: Real-time ingestion from multiple meteo providers
- **METAR/TAF Parser**: Decoding and normalization with QA checks
- **GRIB Processing**: Gridded weather data processing
- **Graphical Weather**: Generation of map tiles and overlays
- **Caching**: Efficient caching with TTL rules

---

## Documentation Files

- **[02-40-17-001_Weather_Architecture.md](02-40-17-001_Weather_Architecture.md)**: Weather processing architecture
- **[02-40-17-002_Data_Ingestion.md](02-40-17-002_Data_Ingestion.md)**: Ingestion of meteo feeds
- **[02-40-17-003_METAR_TAF_Parser.md](02-40-17-003_METAR_TAF_Parser.md)**: METAR/TAF parsing and normalization
- **[02-40-17-004_Graphical_Weather.md](02-40-17-004_Graphical_Weather.md)**: Graphical product generation

---

## ASSETS Structure

### Source_Code/
- **parsers/**: Weather data parsers (METAR, TAF, GRIB)
- **visualization/**: Map tile generation and overlay services
- **caching/**: Caching layer with TTL management

---

## Integration

Provides data to:
- **[02-40-11 EFB Software](../02-40-11_EFB_Software/)**: Weather display
- **[02-40-15 Flight Planning](../02-40-15_Flight_Planning_Software/)**: Route weather

External sources:
- NOAA Weather Service
- MeteoGroup or commercial providers
- ICAO meteo services

---

## References

- [WMO Standards](https://public.wmo.int/) – World Meteorological Organization
- [ICAO Annex 3](https://www.icao.int/) – Meteorological Service for International Air Navigation

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: _2025-11-21_.
