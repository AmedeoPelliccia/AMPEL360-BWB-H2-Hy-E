# 02-20-16-003: CAOS Dispatch Interfaces

> **ID:** 02-20-16-003  
> **Title:** CAOS Dispatch Interfaces & API Contracts  
> **System:** ATA 02-20 (Operations / IT Integration)  
> **Revision:** 1.0  
> **Status:** DRAFT / API SPEC  
> **Protocol:** REST (JSON) over HTTPS / ARINC 633 (XML) over ACARS

---

## 1. Interface Architecture

The CAOS Dispatch Gateway operates on a **Dual-Protocol** basis to ensure compatibility with modern Airline Operations Centers (AOC) while maintaining safety-critical links to the aircraft.

1.  **Ground Segment (REST API):** High-bandwidth JSON API for Pre-flight planning, optimization simulation, and dashboard integration.
2.  **Air Segment (ARINC 633):** Low-bandwidth XML extensions for uploading final loadsheets and operational data to the aircraft FMS via ACARS/IP.

---

## 2. JSON API Specification (Ground Segment)

### 2.1 Endpoint: Initialize Flight Envelope
**POST** `/api/v1/dispatch/envelope`

Calculates the dynamic weight limits based on the aircraft's current physical state (H₂ tank temp, Sorbent health).

#### Request Payload
```json
{
  "flight_id": "AMP360",
  "tail_number": "N360H2",
  "route_distance_nm": 1250,
  "planned_payload_kg": 18500,
  "departure_time_utc": "2026-11-21T14:00:00Z",
  "alternate_airport": "EGLL"
}
```

#### Response Payload (The "Dynamic Mass" Envelope)
```json
{
  "status": "CALCULATED",
  "envelope_id": "env_8823_adj",
  "constraints": {
    "max_takeoff_weight_kg": 165000,
    "max_landing_weight_kg": 142000,
    "max_zero_fuel_weight_kg": 138000
  },
  "hydrogen_requirements": {
    "min_energy_mj": 185000,
    "estimated_mass_kg": 1540,
    "boil_off_reserve_kg": 45,
    "tank_pressure_limit_bar": 3.8
  },
  "carbon_capture_limits": {
    "sorbent_health_percent": 98.5,
    "max_capture_capacity_kg": 4200,
    "recommended_capture_cap_kg": 3800,
    "reason": "LIMITED_BY_LANDING_WEIGHT"
  }
}
```
> **Note:** The `recommended_capture_cap_kg` is the critical output. It tells Dispatch that although the battery *can* hold 4,200kg of CO₂, capturing that much would make the plane too heavy to land safely given the high payload.

---

### 2.2 Endpoint: Submit Dispatch Decision
**POST** `/api/v1/dispatch/decision`

Logs the dispatcher's authority to accept risk or modify parameters (e.g., accepting a lower CO₂ capture target to carry more cargo).

#### Request Payload
```json
{
  "envelope_id": "env_8823_adj",
  "dispatcher_id": "DISP_044",
  "action": "APPROVE_REDUCED_CAPTURE",
  "parameters": {
    "set_capture_limit_kg": 3800,
    "auth_venting_if_delay_gt_mins": 45
  },
  "digital_signature": "sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
}
```

---

## 3. ARINC 633 Extensions (Air Segment)

Standard ARINC 633 defines the "Operational Flight Plan" (OFP). AMPEL360 requires custom extensions under the `<Extension>` tag to handle Cryogenic and Carbon data.

### 3.1 XML Schema Fragment

```xml
<FlightPlan>
  <!-- Standard Header -->
  <FlightInfo>
    <FlightNumber>AMP360</FlightNumber>
    <Origin>LFBO</Origin>
    <Destination>EDDF</Destination>
  </FlightInfo>

  <!-- Standard Fuel (Modified for H2) -->
  <FuelInfo>
    <TaxiFuel>
      <Weight unit="KG">45</Weight> <!-- Boil-off equivalent -->
    </TaxiFuel>
    <TripFuel>
      <Weight unit="KG">1200</Weight>
    </TripFuel>
  </FuelInfo>

  <!-- AMPEL360 Extensions -->
  <Extensions>
    <Ampel360Data xmlns="http://ampel360.aero/schema/ops/v1">
      <HydrogenState>
        <EnergyDensity unit="MJ/KG">120</EnergyDensity>
        <TankTemperature unit="C">-251.5</TankTemperature>
        <BoilOffRate unit="KG/HR">2.1</BoilOffRate>
      </HydrogenState>
      
      <CarbonCapture>
        <TargetCapture unit="KG">3800</TargetCapture>
        <Mode>BALANCED</Mode> <!-- Options: MAX_CAPTURE, ECO, OFF -->
        <SorbentPreLoad>FALSE</SorbentPreLoad>
      </CarbonCapture>
      
      <CenterOfGravity>
        <TakeoffMAC percent="22.5"/>
        <ProjectedLandingMAC percent="24.1"/> <!-- Accounts for CO2 mass shift -->
      </CenterOfGravity>
    </Ampel360Data>
  </Extensions>
</FlightPlan>
```

---

## 4. Interface Data Dictionary

| Field Name | Type | Unit | Description |
|:---|:---|:---|:---|
| `min_energy_mj` | Float | Megajoules | The actual flight requirement. Mass is derived from this based on tank thermodynamics. |
| `sorbent_health_percent` | Float | % | Efficiency of the solid-state battery. <80% requires maintenance (ATA 21-80). |
| `max_capture_capacity_kg` | Float | Kg | Physical limit of the battery voids. |
| `recommended_capture_cap_kg` | Float | Kg | Operational limit enforced by MLW constraints. |
| `boil_off_reserve_kg` | Float | Kg | Fuel mass allocated to be lost (vented or auxiliary burned) during ground ops. |
| `auth_venting_if_delay_gt_mins` | Int | Minutes | Dispatcher pre-authorization to vent fuel if departure delay exceeds X minutes. |

---

## 5. Error Codes & Exception Handling

| Code | Message | Cause | Recovery Action |
|:---|:---|:---|:---|
| `ERR_DISP_001` | `MLW_VIOLATION_PREDICTED` | Payload + Planned Capture > Max Landing Weight. | Reduce Payload OR Reduce Capture Target via `/dispatch/decision`. |
| `ERR_DISP_002` | `CRYO_ENERGY_MISMATCH` | H2 Mass sufficient, but Energy density too low (warm fuel). | Trigger "Sub-Cooling" ground procedure (ATA 02-50). |
| `ERR_DISP_003` | `SORBENT_SATURATION` | Flight distance generates more CO₂ than battery can hold. | Flight Plan Rejected. Route must be shortened or battery swapped. |
| `ERR_DISP_004` | `CG_OUT_OF_TRIM_LANDING` | CO₂ accumulation in rear battery shifts CG too far aft. | Dispatch must limit Capture Target to maintain CG envelope. |

---

## 6. Traceability to ATA 95

Every transaction on the `/dispatch/decision` endpoint generates a hash that is anchored in the **Digital Product Passport (ATA 95)**.

*   **Why?** To prove "Carbon Negative" status. If a dispatcher lowers the capture target to carry more cargo, that specific flight might only be "Net Zero" or "Low Carbon."
*   **Audit:** The hash links the Flight ID to the specific CO₂ mass collected, preventing double-counting of carbon credits.
```
