# 85-00-07-502: Evacuation Time and Capacity Verification

## 1. Purpose
Verify that the aircraft evacuation system meets the 90-second full cabin evacuation requirement per [CS-25.803](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes).

## 2. Regulatory Requirements
### 2.1 CS-25.803 Evacuation Demonstration
- **Time Limit**: ≤ 90 seconds from signal to last passenger on ground
- **Configuration**: Maximum certified passenger capacity
- **Exits Available**: 50% of exits blocked (worst-case scenario)
- **Cabin Lighting**: Emergency lighting only (cabin darkened)
- **Participants**: Representative passenger demographics (no athletes or trained evacuees)

### 2.2 Exit Capacity
Per [CS-25.807](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes):
- **Type A Exit**: 110 passengers (42" x 72")
- **Type I Exit**: 45 passengers (24" x 48")
- **Type II Exit**: 40 passengers (20" x 44")
- **Type III Exit**: 35 passengers (20" x 36")

## 3. Verification Methods
### 3.1 Analysis
- **Exit Capacity Calculation**: Sum of exit ratings ≥ passenger capacity
- **Flow Rate Modeling**: Passenger throughput per exit type
- **Bottleneck Analysis**: Identify cabin choke points (aisles, cross-aisles)

### 3.2 Simulation
- **Pedestrian Flow Software**: Pathfinder, STEPS, or FDS+Evac
- **Scenarios**: All exits available, 50% exits blocked, crew assistance
- **Sensitivity Analysis**: Vary passenger distribution, mobility, response time

### 3.3 Physical Testing
- **Egress Tests**: Timed trials with volunteer passengers (pre-demonstration)
- **Full Evacuation Demo**: Official certification demonstration per CS-25.803
- **Video Analysis**: Post-test review to identify delays, congestion

## 4. Test Conditions
### 4.1 Aircraft Configuration
- Maximum certified passenger seating
- Emergency lighting operational
- No cabin crew coaching (spontaneous reaction)

### 4.2 Passenger Demographics
- **Age**: Representative distribution (adults, elderly, children)
- **Mobility**: Include passengers with reduced mobility (PRM)
- **Size**: Range of body sizes (5th to 95th percentile)
- **No Special Training**: Passengers not briefed on blocked exits

### 4.3 Environmental
- Darkened cabin (emergency lighting only)
- Ambient temperature (comfortable, not extreme)

## 5. Acceptance Criteria
### 5.1 Primary
- **90-Second Rule**: All passengers evacuated ≤ 90 seconds
- **Exit Balance**: No single exit overloaded (crowd control)
- **Slide Performance**: All slides operational, no injuries due to equipment failure

### 5.2 Secondary
- **Flow Rate**: ≥ design target (e.g., 50 passengers/minute per Type A exit)
- **Crew Effectiveness**: Cabin crew direct passengers efficiently
- **Signage**: Emergency lighting and exit marking clearly visible

## 6. Safety Considerations
- Medical personnel on standby
- Padded landing areas around slides
- Test director with abort authority
- Participant screening (no serious health conditions)

## 7. Documentation
- Certification demonstration video (multi-angle)
- Exit timing data (per exit, per phase)
- Test report: [85-00-07-A-502](./ASSETS/85-00-07-A-502_Evacuation_Test_Reports.xlsx)
- Certification authority witness statement

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
