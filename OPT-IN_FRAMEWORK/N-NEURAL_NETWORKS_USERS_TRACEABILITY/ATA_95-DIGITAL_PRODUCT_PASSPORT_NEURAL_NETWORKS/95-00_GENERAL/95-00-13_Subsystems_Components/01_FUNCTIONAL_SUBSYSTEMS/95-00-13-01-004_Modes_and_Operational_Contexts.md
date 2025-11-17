# 95-00-13-01-004: Modes and Operational Contexts

## Document Information
- **Document ID**: 95-00-13-01-004
- **Title**: Modes and Operational Contexts
- **Version**: 1.0
- **Status**: Active
- **Last Updated**: 2025-11-17

## Operational Modes

### Ground Mode
**Entry**: Aircraft on ground with engines off
**Active Subsystems**: Power (ground power), environmental control (ground), data recording
**Exit**: Engine start initiated

### Taxi Mode
**Entry**: Engines started, ready to taxi
**Active Subsystems**: All primary systems, limited flight control
**Exit**: Takeoff clearance and lineup

### Takeoff Mode
**Entry**: Takeoff power set, rotation initiated
**Active Subsystems**: Full flight control, navigation, power at maximum
**Exit**: Positive rate of climb, gear retraction

### Climb Mode
**Entry**: Gear up and locked, climbing
**Active Subsystems**: All flight systems, cruise optimization inactive
**Exit**: Cruise altitude reached

### Cruise Mode
**Entry**: Level flight at cruise altitude
**Active Subsystems**: All systems, efficiency optimization active
**Exit**: Descent initiated

### Descent Mode
**Entry**: Descent from cruise initiated
**Active Subsystems**: All systems, approach preparation
**Exit**: Approach phase entered

### Approach Mode
**Entry**: Approach clearance, configured for landing
**Active Subsystems**: All systems, precision navigation, landing prep
**Exit**: Landing threshold crossed

### Landing Mode
**Entry**: Touchdown imminent
**Active Subsystems**: Full control authority, landing configuration
**Exit**: Rollout complete, taxi speed

### Emergency Mode
**Entry**: Emergency condition detected
**Active Subsystems**: Essential systems only, fallbacks active
**Exit**: Emergency resolved or landing complete

## Mode Transition Matrix

See: ASSETS/95-00-13-01-A-003_Modes_vs_Subsystems_Matrix.xlsx

## Related Documents

- 95-00-13-01-001: Functional Subsystems Overview
- 95-00-13-01-003: Functional Subsystems List

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Documentation WG | Initial release |
