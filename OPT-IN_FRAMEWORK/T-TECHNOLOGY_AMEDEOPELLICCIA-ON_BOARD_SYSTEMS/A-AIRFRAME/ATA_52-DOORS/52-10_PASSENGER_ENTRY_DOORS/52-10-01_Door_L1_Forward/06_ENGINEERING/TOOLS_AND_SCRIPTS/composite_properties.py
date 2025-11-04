#!/usr/bin/env python3
"""
Composite Properties Calculator
Based on Classical Laminate Theory (CLT)
WARNING: Simplified approximations only
"""

class CompositeLaminate:
    """
    Calculate equivalent properties for composite laminates
    Uncertainty: ±30-40%
    """
    
    def __init__(self, E11, E22, G12, nu12, t_ply):
        """
        Initialize with unidirectional ply properties
        
        Args:
            E11: Fiber direction modulus (GPa)
            E22: Transverse modulus (GPa)
            G12: Shear modulus (GPa)
            nu12: Poisson's ratio
            t_ply: Ply thickness (mm)
        """
        self.E11 = E11
        self.E22 = E22
        self.G12 = G12
        self.nu12 = nu12
        self.nu21 = nu12 * E22 / E11
        self.t_ply = t_ply
        
    def quasi_isotropic_properties(self):
        """
        Calculate properties for [45/0/-45/90]_ns layup
        Simplified closed-form solution
        """
        
        # Quasi-isotropic approximations
        E_x = (3*self.E11 + 3*self.E22 + 2*self.G12 + 4*self.nu12*self.E11) / 8
        E_y = E_x  # Symmetric
        G_xy = (self.E11 + self.E22 + 2*self.G12 - 4*self.nu12*self.E11) / 8
        nu_xy = (self.E11 + self.E22 + 6*self.nu12*self.E11 - 2*self.G12) / (2 * E_x)
        
        return {
            'E_x_GPa': E_x,
            'E_y_GPa': E_y,
            'G_xy_GPa': G_xy,
            'nu_xy': nu_xy,
            'layup': '[45/0/-45/90]_ns',
            'uncertainty': '±30%',
            'note': 'Requires CLT software for accuracy'
        }
    
    def laminate_thickness(self, n_plies):
        """Calculate total laminate thickness"""
        return n_plies * self.t_ply
    
    def equivalent_modulus_sandwich(self, t_face, t_core, E_core=0.08):
        """
        Calculate equivalent bending modulus for sandwich panel
        
        Args:
            t_face: Face sheet thickness (mm)
            t_core: Core thickness (mm)
            E_core: Core modulus (GPa), default 80 MPa
        
        Returns:
            Equivalent properties
        """
        
        # Distance between face centroids
        d = t_core + t_face
        
        # Flexural rigidity (per unit width)
        E_eq = self.quasi_isotropic_properties()['E_x_GPa']
        I_face = 2 * (t_face**3 / 12 + t_face * (d/2)**2)
        I_core = t_core**3 / 12
        
        D = E_eq * I_face * 1000 + E_core * I_core * 1000  # Convert to N⋅m
        
        return {
            'D_Nm_per_m': D,
            'equivalent_thickness_mm': d,
            'note': 'Simplified - does not include core shear'
        }

if __name__ == "__main__":
    print("Composite Properties Calculator")
    print("=" * 50)
    
    # Example: M21E/IMA CFRP
    laminate = CompositeLaminate(
        E11=165,  # GPa
        E22=9.2,  # GPa
        G12=5.3,  # GPa
        nu12=0.33,
        t_ply=0.25  # mm
    )
    
    print("\nQuasi-isotropic properties:")
    props = laminate.quasi_isotropic_properties()
    for key, value in props.items():
        print(f"{key}: {value}")
    
    print("\n16-ply laminate thickness:", laminate.laminate_thickness(16), "mm")
    
    print("\nSandwich panel properties:")
    sandwich = laminate.equivalent_modulus_sandwich(t_face=4, t_core=40)
    for key, value in sandwich.items():
        print(f"{key}: {value}")
    
    print("\n⚠️  WARNING: These are approximations. Use dedicated CLT software for production.")
