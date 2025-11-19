# 95-50-00-007 Installation Standards and Rules

**Document ID:** 95-50-00-007  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active

---

## 1. General Installation Requirements

### 1.1 Workmanship Standards

**Reference Documents:**
- [AC 43.13-1B](https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/99861) - Acceptable Methods, Techniques, and Practices
- [SAE AS50881](https://www.sae.org/standards/content/as50881/) - Wiring Aerospace Vehicle
- [MIL-STD-1312](https://assist.dla.mil/online/start/) - Fastener Test Methods

**Quality Requirements:**
- All installations shall be performed by certified technicians
- Work shall be inspected per quality assurance procedures
- Non-conformances shall be documented and dispositioned

---

## 2. Fastener Installation

### 2.1 Torque Requirements

**Torque Specifications:**
- Per manufacturer specifications or [MIL-STD-1312](https://assist.dla.mil/online/start/)
- Use calibrated [torque wrenches](https://en.wikipedia.org/wiki/Torque_wrench) (±4% accuracy)
- Apply torque seals for inspection

**Tightening Sequence:**
- Multiple-fastener joints: tighten in star pattern
- Large panels: start at center, work outward
- Re-torque after initial assembly settles

### 2.2 Locking Methods

**Self-Locking Fasteners:**
- All-metal prevailing torque nuts (preferred)
- Nylon-insert lock nuts (not for high-temperature applications)
- Maximum 5 installations per self-locking fastener

**Safety Wiring:**
- Required for critical fasteners (flight controls, engine mounts)
- [MS20995](https://en.wikipedia.org/wiki/Safety_wire) lockwire (0.032" or 0.041" diameter)
- Positive twist direction (tends to tighten)

---

## 3. Electrical Bonding and Grounding

### 3.1 Bonding Requirements

**Resistance Limits:**
- Structure-to-structure: ≤2.5 milliohms
- Equipment-to-structure: ≤2.5 milliohms
- Grounding stud-to-bus: ≤2.5 milliohms

**Bonding Methods:**
- Bonding jumpers with lugs crimped per [SAE AS50881](https://www.sae.org/standards/content/as50881/)
- Conductive finishes ([alodine](https://en.wikipedia.org/wiki/Alodine), cadmium plate)
- Star washers or conductive gaskets at interfaces

### 3.2 Grounding Points

**Grounding Philosophy:**
- Single-point grounding for sensitive electronics
- Multi-point grounding for power distribution
- Isolated grounds for analog signals

**Grounding Locations:**
- Designated grounding studs on equipment racks
- Primary structure for lightning protection
- Separate digital and analog ground busses

---

## 4. Cable Routing and Management

### 4.1 Routing Rules

**Separation Requirements:**
- Power wires ≥2 inches from signal wires
- Hydraulic lines ≥6 inches from electrical wires
- Hot structures (>200°F) ≥3 inches from wires

**Support Spacing:**
- Horizontal runs: support every 24 inches
- Vertical runs: support every 36 inches
- Near vibration sources: support every 12 inches

### 4.2 Bend Radius

**Minimum Bend Radius:**
- Power cables: 10× cable diameter
- Coaxial cables: 6× cable diameter
- Fiber optic cables: 20× cable diameter
- Harnesses: 3× harness diameter

### 4.3 Strain Relief

**Methods:**
- Connector backshells with strain relief clamps
- Cable glands at bulkhead penetrations
- Loop slack before connectors (1-2 inches)

---

## 5. Thermal Management

### 5.1 Cooling Air Ducting

**Duct Design:**
- Minimize pressure drop (smooth bends, gradual transitions)
- Seal joints to prevent leakage
- Insulate ducts in cold-soak areas

**Airflow Requirements:**
- IMA racks: 100 CFM per kW of heat dissipation
- Server racks: 150 CFM per kW (higher density)
- Spot cooling for high-power LRUs

### 5.2 Heat Sink Interfaces

**Thermal Interface Materials (TIM):**
- Thermal grease for removable interfaces
- Thermal pads for permanent installations
- Gap fillers for uneven surfaces

**Interface Pressure:**
- Maintain 30-50 psi contact pressure
- Use spring-loaded fasteners for thermal cycling

---

## 6. Access and Maintainability

### 6.1 Access Panel Design

**Quick-Access Panels:**
- Tool-less fasteners (quarter-turn, captive screws)
- Clear labeling of contents
- Gas spring supports for large panels

**Service Doors:**
- Hinged with hold-open mechanism
- Captive fasteners to prevent FOD
- Warning placards for powered equipment

### 6.2 LRU Replacement

**Clearance Requirements:**
- Minimum 6 inches clearance for removal path
- Handles or lifting points on heavy LRUs (>15 lbs)
- Connector accessibility without special tools

---

## 7. Environmental Sealing

### 7.1 Ingress Protection (IP) Ratings

**External Installations:**
- IP67 minimum (dust-tight, water immersion)
- Conformal coating on PCBs
- Sealed connectors (MIL-DTL-38999)

**Internal Installations:**
- IP40 minimum (solid objects >1mm, no water protection)
- Filtered vents for equipment bays
- Drain holes at low points

### 7.2 Sealing Methods

**Gaskets:**
- Neoprene or silicone gaskets for panels
- Continuous bead (no gaps or overlaps)
- Compression to 50-75% of original thickness

**Sealants:**
- Polysulfide sealants for fuel areas (PR-1422)
- Silicone sealants for general use (RTV)
- Acrylic sealants for electrical potting

---

## 8. Safety Requirements

### 8.1 Fire Protection

**Materials:**
- Non-flammable materials in fire zones (per [FAR 25.853](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25/subpart-D/subject-group-ECFR61b1513e00c1bd8/section-25.853))
- Fire-resistant barriers between zones
- Fire detection and suppression integration

### 8.2 Lightning Protection

**External Mounts:**
- Direct attachment to conductive structure
- Lightning diverter strips on composite surfaces
- Bonding to aircraft ground plane

### 8.3 Fail-Safe Design

**Redundancy:**
- Dual load paths for critical structures
- Independent fasteners (no single-point failures)
- Crack stoppers in high-stress areas

---

## 9. Inspection and Test Requirements

### 9.1 Installation Inspection

**Visual Inspection:**
- No damage to parts during installation
- Correct hardware (type, size, material)
- Proper torque and safety wiring

**Functional Testing:**
- Continuity checks for wiring
- Bonding resistance measurements
- Leak testing for sealed installations

### 9.2 Acceptance Criteria

**Workmanship:**
- No cracks, dents, or scratches
- Fasteners flush or properly recessed
- No FOD (foreign object debris) present

---

## 10. Document Control

| Version | Date       | Author                     | Changes                |
|---------|------------|----------------------------|------------------------|
| 1.0     | 2025-11-17 | AMPEL360 Documentation Team | Initial creation       |

---

**Maintained by:** AMPEL360 Structures Team
