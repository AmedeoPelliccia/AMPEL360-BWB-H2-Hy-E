# EU WEEE Compliance
## Waste Electrical and Electronic Equipment Directive 2012/19/EU

### Applicable Components

Door L1 Forward contains electronic components subject to WEEE Directive:

| Part Number | Description | WEEE Category | Treatment Required |
|-------------|-------------|---------------|-------------------|
| PN-52-10-01-301001 | Junction Box | Cat 5 - Small equipment | Standard WEEE |
| PN-52-10-01-301002 | Circuit Breakers | Cat 5 - Small equipment | Standard WEEE |
| PN-52-10-01-302001 | Door Controller | Cat 6 - IT equipment | Special treatment (lead) |
| PN-52-10-01-302002 | Interface Board | Cat 6 - IT equipment | Special treatment (lead) |
| PN-52-10-01-303001 | Position Sensor | Cat 5 - Small equipment | Standard WEEE |
| PN-52-10-01-303002 | Pressure Sensor | Cat 5 - Small equipment | Standard WEEE |
| PN-52-10-01-303003 | Load Cells | Cat 5 - Small equipment | Battery removal required |
| PN-52-10-01-304001 | Main Harness | Cat 5 - Small equipment | Copper recovery |
| PN-52-10-01-304002 | Sensor Harness | Cat 5 - Small equipment | Copper recovery |

### WEEE Requirements

#### Collection
- Separate collection from other waste
- Marked with crossed-out wheeled bin symbol
- Tracking documentation required

#### Treatment
- Licensed WEEE treatment facility
- Depollution of hazardous substances
- Selective treatment of materials
- Recovery/recycling targets met

#### Recovery Targets (Directive Annex V)
- Category 5: 80% recovery, 70% recycling
- Category 6: 80% recovery, 70% recycling
- **Door L1 Actual:** 85% recovery, 75% recycling

#### Documentation
- Transfer notes
- Treatment certificates
- Recovery/recycling evidence
- Annual reporting

### Hazardous Substances

#### Lead Solder (PN-52-10-01-302001, -302002)
- **RoHS Exemption:** Aviation & aerospace (Annex III, Item 7)
- **Quantity:** ~5g per PCB
- **Treatment:** Specialized PCB recycling
- **Recovery:** Smelting process

#### Lithium Batteries (PN-52-10-01-303003)
- **Type:** Lithium ion, 20g
- **Removal:** Before WEEE processing
- **Treatment:** Battery-specific recycling
- **Transport:** UN3090 classification

### Approved WEEE Processors

| Facility | Location | Certification | Specialization |
|----------|----------|---------------|----------------|
| TechWaste Solutions | Hamburg, DE | ISO 14001, WEEELABEX | Aerospace electronics |
| Electronic Recycling EU | Amsterdam, NL | ISO 14001, WEEELABEX | PCB processing |
| AeroWEEE Services | Toulouse, FR | ISO 14001, AS9120 | Aviation systems |

### Process Flow

```
Electronic Component Removal
          ↓
    Hazmat Separation (batteries, capacitors)
          ↓
    Manual Disassembly
          ↓
    Material Sorting
          ↓
┌─────────┴─────────┬──────────┬─────────┐
↓                   ↓          ↓         ↓
PCBs            Aluminum    Copper    Plastics
↓                   ↓          ↓         ↓
Smelting      Metal Recycle  Wire     Energy
(Precious metals)            Recycle   Recovery
```

### Precious Metal Recovery

From PCBs and controllers:
- **Gold:** ~0.3g per kg PCB → €15/kg
- **Silver:** ~3g per kg PCB → €2/kg  
- **Palladium:** ~0.1g per kg PCB → €5/kg
- **Copper:** ~200g per kg PCB → €1.5/kg

**Per Door (3.2 kg electronics):**
- Precious metals: €25 estimated
- Copper: €5
- **Total:** €30

### Compliance Documentation

Each disposal must include:
1. **Transfer Note**
   - Waste description
   - Weight
   - Producer identification
   - Transporter details
   - Facility details

2. **Treatment Certificate**
   - Processing method
   - Recovery/recycling rates achieved
   - Hazmat handling confirmation
   - Date of processing

3. **Evidence of Recovery**
   - Material outputs by type
   - Destination of materials
   - Recovery percentages

### Producer Responsibilities

AMPEL360 as producer must:
- Register with national authorities
- Finance collection and treatment
- Provide product information
- Mark products with WEEE symbol
- Report annually on quantities

### National Contacts

| Country | Authority | Registration Required |
|---------|-----------|----------------------|
| Germany | Stiftung EAR | Yes |
| France | Ecologic | Yes |
| UK | Environment Agency | Yes |
| Netherlands | Wecycle | Yes |

### Annual Reporting

Required data per country:
- Number of units placed on market
- Weight of WEEE collected
- Weight recovered/recycled
- Treatment methods used
- Facilities utilized

### Penalties for Non-Compliance

- Fines up to €100,000
- Potential product bans
- Reputational damage
- Loss of certifications

### CAOS Integration

- Automated WEEE tracking
- Digital transfer notes
- Certificate verification
- Compliance reporting
- Predictive waste streams

---

*Part of AMPEL360 OPT-IN Framework*
*Document: WEEE_Compliance.md*
*Version: 1.0*
*Last Updated: 2025-11-03*
