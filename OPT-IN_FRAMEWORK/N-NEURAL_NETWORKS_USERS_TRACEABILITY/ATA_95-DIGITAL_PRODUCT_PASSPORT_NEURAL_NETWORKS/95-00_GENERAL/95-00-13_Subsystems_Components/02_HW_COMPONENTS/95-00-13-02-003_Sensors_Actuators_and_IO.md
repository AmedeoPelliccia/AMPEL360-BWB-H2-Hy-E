# 95-00-13-02-003: Sensors, Actuators and I/O

## Document Information
- **Document ID**: 95-00-13-02-003
- **Title**: Sensors, Actuators and I/O
- **Version**: 1.0
- **Status**: Active
- **Last Updated**: 2025-11-17

## Sensor Inventory

### Inertial Sensors
- **IMU Primary**: 9-DOF MEMS IMU, 1000 Hz, ±16g/±2000°/s
- **IMU Backup**: Redundant unit for fault tolerance
- **Criticality**: DAL-A

### Position Sensors
- **GNSS**: Multi-constellation (GPS, Galileo, BeiDou)
- **Precision**: < 5m CEP (circular error probable)
- **Update Rate**: 10 Hz

### Air Data Sensors
- **Pitot-Static**: Pressure altitude, airspeed
- **Temperature**: Total air temperature (TAT)
- **Angle of Attack**: Vane-type, redundant

## Actuator Inventory

### Flight Control Actuators
- **Type**: Brushless DC servo motors
- **Redundancy**: Dual independent channels
- **Response Time**: < 50 ms
- **Criticality**: DAL-A

### Utility Actuators
- **Landing Gear**: Hydraulic
- **Doors**: Electric
- **Valves**: Solenoid and electric motor

## I/O Mapping

See: ASSETS/95-00-13-02-A-003_HW_IO_Mapping_Table.csv

## Related Documents

- 95-00-13-02-001: HW Components Overview
- 95-00-13-02-004: Power and Thermal HW Interfaces

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Documentation WG | Initial release |
