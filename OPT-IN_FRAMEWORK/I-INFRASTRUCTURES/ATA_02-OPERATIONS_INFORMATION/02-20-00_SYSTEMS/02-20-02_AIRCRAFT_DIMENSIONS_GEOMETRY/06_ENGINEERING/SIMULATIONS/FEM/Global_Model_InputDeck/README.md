# Global FEM Model Input Deck

**Model:** AMPEL360 BWB H₂ Hy-E Q100 Global Structural Model  
**Software:** MSC Nastran  
**Status:** In Development

## Files

- `ampel360_q100_global_model.dat` - Main Nastran input deck
- `ampel360_q100_load_cases.inp` - Load case definitions
- Additional include files for materials, properties, and boundary conditions

## Model Statistics

- **Nodes:** ~500,000
- **Elements:** ~450,000
- **Materials:** Aluminum 7075-T6, Ti-6Al-4V, Carbon/Epoxy composites
- **Load cases:** 25+ per CS-25 requirements

## Usage

```bash
nastran ampel360_q100_global_model.dat
```

Refer to MSC Nastran documentation for detailed analysis procedures.
