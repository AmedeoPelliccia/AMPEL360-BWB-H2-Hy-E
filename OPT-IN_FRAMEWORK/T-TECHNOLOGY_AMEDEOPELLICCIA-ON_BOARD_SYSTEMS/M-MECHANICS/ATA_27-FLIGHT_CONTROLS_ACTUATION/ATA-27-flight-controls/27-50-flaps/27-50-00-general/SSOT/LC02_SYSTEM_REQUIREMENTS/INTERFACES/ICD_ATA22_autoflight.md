# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Amedeo Pelliccia <amedeo.pelliccia@icloud.com>

# ICD — ATA 22 Autoflight Interface

## Overview

This Interface Control Document defines the interface between ATA 27 Flight Controls (27-50-00-general) and ATA 22 Autoflight System.

## Interface Signals

| Signal Name | Direction | Type | Description |
|:------------|:----------|:-----|:------------|
| AP_ENGAGE_CMD | ATA22→ATA27 | Discrete | Autopilot engage command |
| AP_DISCONNECT | ATA27→ATA22 | Discrete | Autopilot disconnect indication |
| PITCH_CMD | ATA22→ATA27 | Analog | Pitch command from AP |
| ROLL_CMD | ATA22→ATA27 | Analog | Roll command from AP |
| YAW_CMD | ATA22→ATA27 | Analog | Yaw damper command |
| SURFACE_POS_FB | ATA27→ATA22 | Analog | Surface position feedback |
| FCS_STATUS | ATA27→ATA22 | Discrete | Flight control system status |

## Data Bus Interfaces

- **Bus Type**: ARINC 429 / AFDX
- **Message Rate**: TBD
- **Latency Requirement**: TBD

## Document Control

- **Subject**: 27-50-00-general
- **Interface**: ATA 22 Autoflight
- **Status**: Placeholder
- **Last Updated**: 2026-01-09
