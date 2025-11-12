# Dynamic Ground Clearance Simulation Models

**Platform:** AMPEL360 Q100  
**Software:** Adams / Simscape Multibody  
**Status:** Development

## Model Purpose

Simulate aircraft dynamic response during ground operations to verify clearances:
- Landing impact and gear stroke
- Taxi over rough surfaces
- Crosswind ground handling
- Take-off rotation dynamics

## Model Components

### Aircraft Structure
- Rigid body representation of airframe
- Mass properties (weight, CG, inertia)
- Flexibility representation (optional)

### Landing Gear
- Main landing gear (MLG): Strut, shock absorber, wheels
- Nose landing gear (NLG): Strut, shock absorber, wheels, steering actuator
- Tire models: Vertical stiffness and damping, rolling resistance

### Ground Contact
- Runway surface profile (smooth, bump, rough)
- Tire-ground interaction forces

## Simulation Scenarios

1. **Landing impact:** Various sink rates (design: 10 ft/s, hard: 12 ft/s)
2. **Taxi bump:** 4-inch bump at taxi speed per CS-25.491
3. **Crosswind taxi:** 30 kt crosswind
4. **Take-off rotation:** Rotation to VR

## Outputs

- Gear stroke and compression
- Pitch, roll, and heave motion
- Ground clearances (belly, wingtip, tail)
- Gear loads and reactions

## Files Location

Model files: `Taxi_Kinematics_Models/q100_taxi_clearance_model.slx`
