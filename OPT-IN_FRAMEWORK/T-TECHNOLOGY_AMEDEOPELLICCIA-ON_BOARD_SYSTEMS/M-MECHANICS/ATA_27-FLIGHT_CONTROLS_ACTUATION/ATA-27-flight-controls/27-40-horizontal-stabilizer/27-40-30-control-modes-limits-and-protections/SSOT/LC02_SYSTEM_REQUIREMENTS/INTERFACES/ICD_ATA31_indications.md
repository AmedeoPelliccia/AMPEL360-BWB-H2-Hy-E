# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Amedeo Pelliccia <amedeo.pelliccia@icloud.com>

# ICD — ATA 31 Indicating/Recording Systems Interface

## Overview

This Interface Control Document defines the interface between ATA 27 Flight Controls (27-40-30-control-modes-limits-and-protections) and ATA 31 Indicating/Recording Systems.

## ECAM/EICAS Messages

| Message ID | Condition | Severity | Display Text |
|:-----------|:----------|:---------|:-------------|
| FCS_FAULT | FCS failure detected | Warning | F/CTL FAULT |
| ACT_FAIL | Actuator failure | Caution | ACT x FAIL |
| REVERSION | Mode reversion | Advisory | F/CTL DIRECT |

## Display Interfaces

- **Primary Display**: ECAM/EICAS (Flight Warning Computer)
- **Secondary Display**: MFD System Page
- **Data Bus**: ARINC 429 / AFDX

## Flight Data Recording

| Parameter | Sample Rate | Resolution |
|:----------|:------------|:-----------|
| Surface Position | 8 Hz | 0.1° |
| Actuator Status | 1 Hz | Discrete |
| FCS Mode | On change | Discrete |

## Document Control

- **Subject**: 27-40-30-control-modes-limits-and-protections
- **Interface**: ATA 31 Indicating/Recording
- **Status**: Placeholder
- **Last Updated**: 2026-01-09
