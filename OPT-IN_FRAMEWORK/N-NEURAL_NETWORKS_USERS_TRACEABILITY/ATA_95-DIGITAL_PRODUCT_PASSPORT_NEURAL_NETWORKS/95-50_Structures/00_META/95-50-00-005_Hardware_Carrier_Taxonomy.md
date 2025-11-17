# 95-50-00-005 Hardware Carrier Taxonomy

**Document ID:** 95-50-00-005  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active

---

## 1. Introduction

This document defines the taxonomy for **hardware carriers** – the specific racks, chassis, and mounting systems that carry NN computing hardware, sensors, and data acquisition equipment.

---

## 2. Carrier Classes

### 2.1 IMA Racks (Class: IMA-R)

**Purpose:** House Integrated Modular Avionics LRUs

**Standard Dimensions:**
- Width: 19 inches (482.6 mm)
- Height: Multiple of 1.75 inches (44.45 mm) - "rack units" (U)
- Depth: 24-36 inches (610-914 mm)

**Features:**
- Backplane for LRU interconnection
- Forced air cooling
- EMI shielding
- Built-in health monitoring

**Example:** `95-50-42-R-001` IMA Rack Primary

### 2.2 Server Racks (Class: SRV-R)

**Purpose:** House information system servers and network equipment

**Standard Dimensions:**
- Width: 19 inches (482.6 mm)
- Height: 42U standard (73.5 inches / 1866 mm)
- Depth: 36-48 inches (914-1219 mm)

**Features:**
- Cable management arms
- PDU integration
- Liquid cooling option
- Hot-swap capability

**Example:** `95-50-46-R-001` Information Systems Server Rack

### 2.3 Electrical Cabinets (Class: ELEC-C)

**Purpose:** House power distribution, circuit breakers, and electrical busses

**Features:**
- Fire-resistant construction
- Arc fault protection
- Bus bar distribution
- Circuit breaker panels

**Example:** `95-50-24-R-001` Main Electrical Cabinet

### 2.4 Sensor Mounts (Class: SENS-M)

**Purpose:** Position sensors for optimal measurement

**Types:**
- **Probe mounts** – Temperature, pressure, flow sensors
- **Camera mounts** – Vision systems, inspection cameras
- **Antenna mounts** – RF antennas, GPS antennas

**Example:** `95-50-57-M-001` Wing Ice Detection Sensor Mount

### 2.5 Data Acquisition Modules (Class: DAQ-M)

**Purpose:** House data acquisition electronics near sensors

**Features:**
- Compact form factor
- Environmental sealing (IP67)
- Low power consumption
- Local data buffering

**Example:** `95-50-21-M-010` ECS Zone DAQ Module

---

## 3. Carrier Attributes

### 3.1 Physical Attributes

**Dimensions:**
- Width (W) in mm
- Height (H) in mm
- Depth (D) in mm
- Weight (empty) in kg
- Weight (fully loaded) in kg

**Mounting:**
- Floor-mounted
- Wall-mounted
- Ceiling-mounted
- Suspended

### 3.2 Electrical Attributes

**Power:**
- Input voltage (e.g., 28V DC, 115V AC)
- Maximum power consumption (W)
- Backup power capability (battery minutes)

**Data:**
- Interface types (AFDX, Ethernet, CAN, RS-485)
- Data rate (Mbps)
- Protocol support

### 3.3 Environmental Attributes

**Operating Range:**
- Temperature: -55°C to +71°C (DO-160 Category B3)
- Altitude: Sea level to 60,000 ft
- Humidity: 0-95% RH (non-condensing)

**Vibration:**
- Random vibration per DO-160 (Category R)
- Sinusoidal vibration per DO-160 (Category S)

**EMI/EMC:**
- Conducted emissions per DO-160 Section 21
- Radiated emissions per DO-160 Section 21
- Susceptibility per DO-160 Sections 18-20

---

## 4. Standardization

### 4.1 Standard Rack Sizes

**Small Racks:**
- 6U height (10.5 inches / 267 mm)
- For line-replaceable units (LRUs)
- Quick-release mounting

**Medium Racks:**
- 12U height (21 inches / 533 mm)
- For avionics and electrical cabinets
- Standard 4-post mounting

**Large Racks:**
- 24U+ height (42+ inches / 1067+ mm)
- For server and information systems
- Heavy-duty floor-mounted

### 4.2 Standard Mounting Patterns

**IMA Rack Mounting:**
- ARINC 600 form factor
- 1 MCU (Modular Concept Unit) = 1.0" width
- Standard depths: 8, 12, 16 MCU

**Sensor Mount Patterns:**
- 4-bolt square pattern (50mm x 50mm)
- 3-bolt triangular pattern (60mm sides)
- Clamp-type for circular probes

---

## 5. Lifecycle Management

### 5.1 Configuration Control

**Baseline Configuration:**
- As-designed configuration in CAD model
- As-built configuration for each aircraft serial number
- As-maintained configuration after modifications

**Change Management:**
- Engineering change orders (ECOs) for design changes
- Service bulletins (SBs) for fleet-wide modifications
- Airworthiness directives (ADs) for mandatory changes

### 5.2 Maintenance Planning

**Scheduled Maintenance:**
- Visual inspection at A-check (every 500 flight hours)
- Functional test at C-check (every 5,000 flight hours)
- Overhaul or replacement at D-check (every 20,000 flight hours)

**Unscheduled Maintenance:**
- Fault isolation procedures
- LRU replacement procedures
- Troubleshooting guides

---

## 6. Digital Twin Integration

### 6.1 CAOS Carrier Data

**Static Data:**
- 3D position (X, Y, Z) in aircraft coordinates
- Weight and center of gravity
- Installed LRU list

**Dynamic Data:**
- Temperature (inlet, outlet, internal)
- Vibration (accelerometers on mounts)
- Power consumption (real-time)

**Predictive Analytics:**
- Thermal trending for cooling system health
- Vibration trending for mount integrity
- Power trending for capacity planning

---

## 7. Document Control

| Version | Date       | Author                     | Changes                |
|---------|------------|----------------------------|------------------------|
| 1.0     | 2025-11-17 | AMPEL360 Documentation Team | Initial creation       |

---

**Maintained by:** AMPEL360 Structures Team
