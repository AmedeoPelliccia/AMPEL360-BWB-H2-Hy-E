# Interface Requirements - Door L3 Aft Emergency Exit

**Document ID:** AMPEL360-52-20-01-REQ-INT  
**Version:** 1.0  
**Date:** 2025-11-04

## RQ-INTERFACE Requirements

### Structural Interfaces

#### RQ-52-20-01-070 Fuselage_Structural_Interface
- **Description:** Interface with BWB fuselage frames 42-44
- **Type:** Mechanical/Structural
- **Load Transfer:** 150% ultimate design loads
- **Verification:** FEA + Test

#### RQ-52-20-01-071 Door_Frame_Mounting
- **Description:** 12 attachment points minimum
- **Distribution:** Uniform around perimeter
- **Redundancy:** Loss of 2 points tolerable
- **Verification:** Analysis

#### RQ-52-20-01-072 Floor_Beam_Interface
- **Description:** Lower sill attachment
- **Load Cases:** Evacuation loads + panic
- **Special:** Slide girt bar loads
- **Verification:** Test

### System Interfaces

#### RQ-52-20-01-073 Electrical_Power_28VDC
- **Description:** Primary power interface
- **Voltage:** 28VDC nominal (22-29V)
- **Current:** 15A peak, 2A standby
- **Protection:** Circuit breaker 20A
- **Verification:** Test

#### RQ-52-20-01-074 Emergency_Power_Bus
- **Description:** Independent emergency power
- **Source:** Essential bus
- **Duration:** 30 minutes minimum
- **Priority:** Load shed protected
- **Verification:** Demo

#### RQ-52-20-01-075 ARINC_429_Data_Bus
- **Description:** Digital communication
- **Speed:** Low speed (12.5 kbps)
- **Channels:** 2 (Tx/Rx)
- **Labels:** Per ATA 52 allocation
- **Verification:** Test

### Mechanical Interfaces

#### RQ-52-20-01-076 Latch_Striker_Interface
- **Description:** Latch engagement points
- **Count:** 8 minimum
- **Adjustment:** ±3mm
- **Material:** Titanium
- **Verification:** Inspect

#### RQ-52-20-01-077 Hinge_System_Interface
- **Description:** Door pivot points
- **Type:** Translating arc
- **Lubrication:** Sealed bearings
- **Life:** 20,000 cycles
- **Verification:** Test

#### RQ-52-20-01-078 Seal_Interface
- **Description:** Pressure seal groove
- **Type:** Dual seal system
- **Compression:** 30% nominal
- **Surface:** 32 Ra finish
- **Verification:** Test

### Environmental Interfaces

#### RQ-52-20-01-079 ECS_Interface
- **Description:** Cabin environment
- **Pressure:** 0-8.6 psi differential
- **Temperature:** -20 to +50°C cabin
- **Humidity:** 5-95% RH
- **Verification:** Analysis

#### RQ-52-20-01-080 Drainage_Interface
- **Description:** Water management
- **Channels:** Door and frame
- **Flow:** 1 liter/minute
- **Freeze Protection:** Heated if required
- **Verification:** Test

### Slide Interfaces

#### RQ-52-20-01-081 Slide_Bustle_Interface
- **Description:** Slide pack mounting
- **Location:** Lower door interior
- **Release:** Automatic on opening
- **Manual Backup:** Red handle
- **Verification:** Demo

#### RQ-52-20-01-082 Girt_Bar_Floor_Interface
- **Description:** Slide attachment
- **Type:** Quick release fittings
- **Strength:** 30,000 lbf minimum
- **Shear:** Ditching disconnect
- **Verification:** Test

### Operational Interfaces

#### RQ-52-20-01-083 Cockpit_Display_Interface
- **Description:** EICAS/ECAM display
- **Status:** Door position, armed state
- **Warnings:** Unsafe conditions
- **Format:** ATA 52 standard
- **Verification:** Demo

#### RQ-52-20-01-084 Cabin_Crew_Panel
- **Description:** Local indicators
- **Display:** Armed, pressure, faults
- **Location:** Adjacent to door
- **Visibility:** Day/night
- **Verification:** Inspect

#### RQ-52-20-01-085 Ground_Interface
- **Description:** Ground handling
- **Access:** External controls
- **Power:** Ground power compatible
- **Tools:** Standard only
- **Verification:** Demo

### Lightning/EMI Protection

#### RQ-52-20-01-086 Lightning_Bonding
- **Description:** Electrical continuity
- **Resistance:** <3 milliohms
- **Current:** 200kA capability
- **Path:** Dual redundant
- **Verification:** Test

#### RQ-52-20-01-087 EMI_Shielding
- **Description:** Electromagnetic compatibility
- **Standard:** DO-160G Cat M
- **Shielding:** 60dB minimum
- **Grounding:** Single point
- **Verification:** Test

### Emergency Interfaces

#### RQ-52-20-01-088 Emergency_Lighting
- **Description:** Exit identification
- **Illumination:** Per CS 25.812
- **Power:** Independent battery
- **Duration:** 10 minutes minimum
- **Verification:** Test

#### RQ-52-20-01-089 Escape_Path_Interface
- **Description:** Clear evacuation route
- **Width:** 20 inches minimum
- **Height:** Floor to exit
- **Marking:** Photoluminescent
- **Verification:** Inspect

### CAOS Interfaces

#### RQ-52-20-01-090 CAOS_Data_Interface
- **Description:** Digital twin connection
- **Protocol:** Ethernet 1Gbps
- **Data Rate:** 100Hz parameters
- **Security:** Encrypted
- **Verification:** Test

#### RQ-52-20-01-091 Sensor_Network
- **Description:** Health monitoring
- **Sensors:** 24 minimum
- **Types:** Position, load, temperature
- **Sampling:** 1kHz maximum
- **Verification:** Demo
