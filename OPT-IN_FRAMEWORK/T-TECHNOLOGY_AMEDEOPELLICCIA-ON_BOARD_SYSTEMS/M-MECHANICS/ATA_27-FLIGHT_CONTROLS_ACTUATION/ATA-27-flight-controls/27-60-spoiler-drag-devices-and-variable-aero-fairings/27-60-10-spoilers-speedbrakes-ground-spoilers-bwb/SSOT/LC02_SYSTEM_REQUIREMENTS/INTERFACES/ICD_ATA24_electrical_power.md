# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Amedeo Pelliccia <amedeo.pelliccia@icloud.com>

# ICD — ATA 24 Electrical Power Interface

## Overview

This Interface Control Document defines the interface between ATA 27 Flight Controls (27-60-10-spoilers-speedbrakes-ground-spoilers-bwb) and ATA 24 Electrical Power System.

## Power Requirements

| Consumer | Voltage | Current (Nom) | Current (Peak) | Bus Type |
|:---------|:--------|:--------------|:---------------|:---------|
| EHA Actuator | 270 VDC | TBD | TBD | HV DC Bus |
| EMA Actuator | 28 VDC | TBD | TBD | Essential DC |
| FCCs | 28 VDC | TBD | TBD | Essential DC |
| Sensors | 28 VDC | TBD | TBD | Essential DC |

## Electrical Interfaces

- **Primary Power**: 270 VDC (High Voltage DC)
- **Secondary Power**: 28 VDC (Essential Bus)
- **Emergency Power**: Battery backup (TBD)

## Document Control

- **Subject**: 27-60-10-spoilers-speedbrakes-ground-spoilers-bwb
- **Interface**: ATA 24 Electrical Power
- **Status**: Placeholder
- **Last Updated**: 2026-01-09
