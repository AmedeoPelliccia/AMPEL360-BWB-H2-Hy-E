# Flight Performance Simulation Models

**Platform:** AMPEL360 Q100  
**Software:** MATLAB/Simulink  
**Status:** Development

## Model Descriptions

### Mission Profile Model (`q100_mission_profile.slx`)

Simulates complete mission from brake release to landing:
- **Taxi and take-off**
- **Climb to cruise altitude**
- **Cruise**
- **Descent**
- **Approach and landing**

**Outputs:**
- Fuel burn per mission segment
- Time and distance
- Range performance

### Climb and Descent Model (`q100_climb_descent.slx`)

Detailed climb and descent performance:
- **Climb schedule:** Speed and altitude profile
- **Rate of climb:** At various weights and altitudes
- **Time to climb:** To cruise altitude
- **Fuel burn:** During climb and descent

**Outputs:**
- Climb performance charts
- OEI drift-down capability
- Step-climb strategy

## Model Inputs

- **Aerodynamic data:** Drag polar, lift curves
- **Engine data:** Thrust and SFC vs. Mach and altitude
- **Weight data:** OEW, payload, fuel capacity
- **Atmospheric data:** ISA conditions

## Usage

Load models in MATLAB/Simulink and run simulations with specified inputs. Refer to model documentation blocks for parameter descriptions.
