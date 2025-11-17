# 95-00-13-02-004: Power and Thermal HW Interfaces

## Document Information
- **Document ID**: 95-00-13-02-004
- **Title**: Power and Thermal HW Interfaces
- **Version**: 1.0
- **Status**: Active
- **Last Updated**: 2025-11-17

## Power Distribution

### Primary Power Bus
- **Voltage**: 28 VDC nominal (22-32 VDC operating range)
- **Source**: H₂ fuel cells
- **Capacity**: 50 kW continuous, 75 kW peak
- **Protection**: Circuit breakers, fuses

### Secondary Power Rails
- **+5V**: Digital logic, sensors
- **+12V**: Actuators, motors
- **+15V/-15V**: Analog circuits
- **+3.3V**: Low-power digital

## Thermal Management

### Cooling Methods
- **Forced Air**: Compute modules, power electronics
- **Liquid Cooling**: High-power AI accelerators
- **Heat Sinks**: Passive cooling for low-power components

### Temperature Limits
- **Operating**: -40°C to +85°C
- **Storage**: -55°C to +125°C
- **Critical Shutdown**: +95°C

## Related Documents

- 95-00-13-02-001: HW Components Overview
- 95-00-13-02-003: Sensors Actuators and IO

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Documentation WG | Initial release |
