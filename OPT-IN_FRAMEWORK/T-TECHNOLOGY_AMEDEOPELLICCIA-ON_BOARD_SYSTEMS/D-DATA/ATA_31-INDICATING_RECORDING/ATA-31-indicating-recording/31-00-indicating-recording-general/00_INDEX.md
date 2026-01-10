# ATA 31-00 — Indicating/Recording General

## Overview

This section covers the general aspects of the ATA 31 Indicating and Recording systems, including:

- System architecture and data flow
- Human-Machine Interface (HMI) philosophy
- Time synchronization and event models
- Interfaces with other ATA chapters
- Configuration baselines and compliance

## Subsections

- [31-00-00 — General](./31-00-00-general/) — General description and system overview
- [31-00-10 — System Architecture and Dataflow](./31-00-10-system-architecture-and-dataflow/) — End-to-end architecture from sensors to displays/recorders
- [31-00-20 — HMI Philosophy, Symbology, Colors and Priorities](./31-00-20-hmi-philosophy-symbology-colors-and-priorities/) — Human factors, symbology standards, color coding
- [31-00-30 — Time Sync, Stamping and Event Model](./31-00-30-time-sync-stamping-and-event-model/) — Time synchronization across systems and event correlation
- [31-00-40 — Interfaces: ATA 22, 24, 42, 45, 46](./31-00-40-interfaces-ata22-ata24-ata42-ata45-ata46/) — Interface Control Documents with related systems
- [31-00-90 — Configuration Baselines and Compliance](./31-00-90-configuration-baselines-and-compliance/) — Configuration management and regulatory compliance

## Key Topics

### System Architecture

The ATA 31 system architecture encompasses:

- **Data Acquisition**: Sensor inputs from various aircraft systems
- **Data Concentrators**: Signal conditioning and data aggregation
- **Processing**: Alert logic, prioritization, and display management
- **Presentation**: Visual displays (PFD, ND, MFD, EICAS/ECAM) and aural alerts
- **Recording**: Flight data recording, cockpit voice recording, and health monitoring

### HMI Philosophy

Human-Machine Interface design follows industry best practices:

- Prioritized alerting (Warning > Caution > Advisory)
- Color-coded indications (Red, Amber, White, Green, Cyan, Magenta)
- Standardized symbology per ARINC 661, DO-257, DO-317
- Crew workload management and alert inhibits

### Interfaces

Critical interfaces include:

- **ATA 22** (Autoflight): Alert inhibits, mode transitions
- **ATA 24** (Electrical): Power quality, time sync sources
- **ATA 42** (IMA): Partitioning, hosting, resource allocation
- **ATA 45** (CMS): Fault reporting, BITE data
- **ATA 46** (Information Systems): Datalinks, connectivity

## Document Control

- **Section**: 31-00
- **Status**: Active Development
- **Generated with AI assistance**: GitHub Copilot, prompted by **Amedeo Pelliccia**
- **Last Updated**: 2026-01-09

---

[⬆ Back to ATA 31 Index](../../00_INDEX.md)
