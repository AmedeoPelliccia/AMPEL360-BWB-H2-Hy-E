# CFD Mesh and Boundary Conditions Description

## Mesh Strategy

### Surface Mesh
- **Wing and center body:** Triangular surface mesh, max element size 50 mm
- **High-lift devices:** Refined mesh, max element size 10 mm
- **Engine nacelles:** Max element size 30 mm

### Volume Mesh
- **Boundary layer:** 30 prism layers, growth rate 1.15, y+ < 1
- **Wake region:** Refined box extending 5× aircraft length downstream
- **Far-field:** Coarse tetrahedral mesh

## Boundary Conditions

### Inlet
- **Type:** Velocity inlet or pressure far-field
- **Values:** Mach number, static pressure, static temperature

### Outlet
- **Type:** Pressure outlet
- **Backflow conditions:** Specified

### Aircraft Surface
- **Type:** No-slip wall
- **Thermal condition:** Adiabatic

### Symmetry
- **Type:** Symmetry plane (if half-model used)
- **Location:** Aircraft centerline

## Quality Metrics

- **Aspect ratio:** < 100 in boundary layer
- **Skewness:** < 0.85
- **Orthogonal quality:** > 0.15
