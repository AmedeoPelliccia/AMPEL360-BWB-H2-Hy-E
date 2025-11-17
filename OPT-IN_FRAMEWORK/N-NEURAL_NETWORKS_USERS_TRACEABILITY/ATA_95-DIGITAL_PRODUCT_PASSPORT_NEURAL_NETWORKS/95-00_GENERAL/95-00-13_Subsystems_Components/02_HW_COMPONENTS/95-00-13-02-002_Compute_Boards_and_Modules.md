# 95-00-13-02-002: Compute Boards and Modules

## Document Information
- **Document ID**: 95-00-13-02-002
- **Title**: Compute Boards and Modules
- **Version**: 1.0
- **Status**: Active
- **Last Updated**: 2025-11-17

## Compute Platform Architecture

### Primary Flight Computer
- **Model**: Custom AMPEL360 FC-P100
- **Processor**: Dual-core ARM Cortex-A72 @ 1.5 GHz
- **Memory**: 8 GB DDR4 ECC RAM
- **Storage**: 256 GB industrial SSD
- **Criticality**: DAL-A
- **Redundancy**: Triple modular redundancy (TMR)

### IMA Core Modules
- **Standard**: ARINC 653 compliant
- **Partitioning**: Time and space partitioning
- **Real-time OS**: PikeOS or VxWorks 653
- **Communication**: ARINC 664 backplane

### AI Accelerator Modules
- **GPU**: NVIDIA Jetson AGX Orin
- **AI Performance**: 275 TOPS
- **Power**: 15-60W configurable
- **Applications**: Object detection, path planning
- **Criticality**: DAL-B

## Related Documents

- 95-00-13-02-001: HW Components Overview
- ASSETS/95-00-13-02-A-001_HW_Components_List.xlsx

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Documentation WG | Initial release |
