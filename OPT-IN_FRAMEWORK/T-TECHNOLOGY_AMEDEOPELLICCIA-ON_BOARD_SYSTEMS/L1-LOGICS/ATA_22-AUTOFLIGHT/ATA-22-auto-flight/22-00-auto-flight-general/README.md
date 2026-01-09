# 22-00-auto-flight-general

## Overview

This directory contains general autoflight system documentation following the S1000D Common Source Database (CSDB) structure.

## Purpose

General (22-00) documentation covers:
- System-level information
- Cross-subsystem integration
- Overall autoflight architecture
- Common procedures and definitions
- General troubleshooting
- System-wide applicability

## Structure

```
22-00-auto-flight-general/
└── 22-00-00-auto-flight-general/
    └── PUB/
        ├── AMM/CSDB/    # Maintenance manual CSDB
        └── IPC/CSDB/    # Parts catalog CSDB
```

## Content Scope

### General System Documentation

- **System Overview**: Complete autoflight system description
- **Integration**: Interface with other aircraft systems (flight controls, navigation, etc.)
- **Architecture**: System-level block diagrams and data flow
- **Common Procedures**: Procedures applicable to all subsystems
- **General Warnings**: Safety information for entire autoflight system

### Cross-Subsystem Information

Documentation that applies across multiple autoflight subsystems:
- Shared components and interfaces
- Common test equipment and procedures
- System-wide configuration management
- General troubleshooting approach

## Navigation

Proceed to `22-00-00-auto-flight-general/PUB/` to access publication content.

## Subsystem-Specific Documentation

For subsystem-specific content, see:
- `22-10-autopilot/` - Autopilot system
- `22-20-flight-director/` - Flight director system
- `22-30-yaw-damper/` - Yaw damper system
- *[Other subsystem directories as they are created]*

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 22 (Autoflight)
- **Section**: 00 (General)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
