#!/usr/bin/env python3
"""
Stress Calculator for AMPEL360 Fuselage Structure
Calculates stress and strain in fuselage components under various load conditions.

Usage:
    python stress_calculator.py --component 53-10-01 --load-case ultimate
"""

import argparse
import math
from typing import Dict, Tuple


class StressCalculator:
    """Calculate stresses in fuselage structural components."""
    
    # Material properties
    MATERIALS = {
        'CFRP_T800_M21': {
            'E_long': 165e9,  # Pa - Longitudinal modulus
            'E_trans': 8.5e9,  # Pa - Transverse modulus
            'G': 5.5e9,       # Pa - Shear modulus
            'nu': 0.3,        # Poisson's ratio
            'density': 1580,  # kg/m³
            'strength_tensile': 2800e6,  # Pa
            'strength_compressive': 1450e6,  # Pa
            'strength_shear': 140e6  # Pa
        },
        'AL_7075_T6': {
            'E': 71.7e9,      # Pa - Elastic modulus
            'G': 26.9e9,      # Pa - Shear modulus
            'nu': 0.33,       # Poisson's ratio
            'density': 2810,  # kg/m³
            'yield_strength': 503e6,  # Pa
            'ultimate_strength': 572e6  # Pa
        },
        'TI_6AL_4V': {
            'E': 113.8e9,     # Pa
            'G': 44e9,        # Pa
            'nu': 0.342,      # Poisson's ratio
            'density': 4430,  # kg/m³
            'yield_strength': 880e6,  # Pa
            'ultimate_strength': 950e6  # Pa
        }
    }
    
    # Load cases
    LOAD_CASES = {
        'limit': {
            'load_factor': 2.5,
            'cabin_pressure': 58.6e3  # Pa (8.5 psi)
        },
        'ultimate': {
            'load_factor': 3.75,
            'cabin_pressure': 117.2e3  # Pa (17 psi - 2x limit)
        }
    }
    
    def __init__(self):
        """Initialize the stress calculator."""
        pass
    
    def calculate_hoop_stress(self, radius: float, thickness: float, 
                            pressure: float) -> float:
        """
        Calculate hoop stress in a cylindrical or BWB pressure vessel.
        
        Args:
            radius: Radius of curvature (m)
            thickness: Wall thickness (m)
            pressure: Internal pressure (Pa)
            
        Returns:
            Hoop stress (Pa)
        """
        if thickness <= 0:
            raise ValueError("Thickness must be positive")
        
        hoop_stress = (pressure * radius) / thickness
        return hoop_stress
    
    def calculate_longitudinal_stress(self, radius: float, thickness: float,
                                     pressure: float) -> float:
        """
        Calculate longitudinal stress in a pressure vessel.
        
        Args:
            radius: Radius of curvature (m)
            thickness: Wall thickness (m)
            pressure: Internal pressure (Pa)
            
        Returns:
            Longitudinal stress (Pa)
        """
        if thickness <= 0:
            raise ValueError("Thickness must be positive")
        
        long_stress = (pressure * radius) / (2 * thickness)
        return long_stress
    
    def calculate_bending_stress(self, moment: float, distance: float,
                                second_moment: float) -> float:
        """
        Calculate bending stress using beam theory.
        
        Args:
            moment: Bending moment (N·m)
            distance: Distance from neutral axis (m)
            second_moment: Second moment of area (m⁴)
            
        Returns:
            Bending stress (Pa)
        """
        if second_moment <= 0:
            raise ValueError("Second moment of area must be positive")
        
        bending_stress = (moment * distance) / second_moment
        return bending_stress
    
    def calculate_shear_stress(self, force: float, area: float) -> float:
        """
        Calculate average shear stress.
        
        Args:
            force: Shear force (N)
            area: Cross-sectional area (m²)
            
        Returns:
            Shear stress (Pa)
        """
        if area <= 0:
            raise ValueError("Area must be positive")
        
        shear_stress = force / area
        return shear_stress
    
    def calculate_von_mises_stress(self, sigma_x: float, sigma_y: float,
                                  tau_xy: float) -> float:
        """
        Calculate von Mises equivalent stress for 2D stress state.
        
        Args:
            sigma_x: Normal stress in x-direction (Pa)
            sigma_y: Normal stress in y-direction (Pa)
            tau_xy: Shear stress (Pa)
            
        Returns:
            von Mises stress (Pa)
        """
        von_mises = math.sqrt(sigma_x**2 - sigma_x*sigma_y + 
                             sigma_y**2 + 3*tau_xy**2)
        return von_mises
    
    def calculate_margin_of_safety(self, applied_stress: float,
                                   allowable_stress: float) -> float:
        """
        Calculate margin of safety.
        
        Args:
            applied_stress: Applied stress (Pa)
            allowable_stress: Allowable stress (Pa)
            
        Returns:
            Margin of safety (dimensionless)
        """
        if applied_stress <= 0:
            return float('inf')
        
        ms = (allowable_stress / applied_stress) - 1.0
        return ms
    
    def analyze_nose_cone(self, load_case: str = 'limit') -> Dict:
        """
        Analyze stress in nose cone (53-10-01).
        
        Args:
            load_case: 'limit' or 'ultimate'
            
        Returns:
            Dictionary with stress analysis results
        """
        # Nose cone geometry (simplified)
        radius = 0.8  # m - average radius
        thickness = 0.044  # m - sandwich panel thickness
        material = 'CFRP_T800_M21'
        
        # Load conditions
        loads = self.LOAD_CASES[load_case]
        pressure = loads['cabin_pressure']
        load_factor = loads['load_factor']
        
        # Calculate stresses
        hoop_stress = self.calculate_hoop_stress(radius, thickness, pressure)
        long_stress = self.calculate_longitudinal_stress(radius, thickness, pressure)
        
        # Aerodynamic bending (simplified)
        aero_moment = 5000 * load_factor  # N·m
        second_moment = 2e-5  # m⁴ (simplified)
        bending_stress = self.calculate_bending_stress(aero_moment, radius, second_moment)
        
        # Combined stress
        total_stress = abs(hoop_stress) + abs(bending_stress)
        
        # Allowable stress (with safety factor built into ultimate)
        allowable = self.MATERIALS[material]['strength_tensile']
        
        # Margin of safety
        ms = self.calculate_margin_of_safety(total_stress, allowable)
        
        results = {
            'component': '53-10-01 Nose Cone',
            'load_case': load_case,
            'material': material,
            'hoop_stress_MPa': hoop_stress / 1e6,
            'longitudinal_stress_MPa': long_stress / 1e6,
            'bending_stress_MPa': bending_stress / 1e6,
            'total_stress_MPa': total_stress / 1e6,
            'allowable_stress_MPa': allowable / 1e6,
            'margin_of_safety': ms,
            'status': 'PASS' if ms > 0 else 'FAIL'
        }
        
        return results
    
    def analyze_bwb_skin_panel(self, load_case: str = 'limit') -> Dict:
        """
        Analyze stress in BWB outer skin panel (53-20-03).
        
        Args:
            load_case: 'limit' or 'ultimate'
            
        Returns:
            Dictionary with stress analysis results
        """
        # BWB skin panel geometry
        width = 11.25  # m - half-width of center body
        thickness = 0.044  # m - sandwich panel
        material = 'CFRP_T800_M21'
        
        # Load conditions
        loads = self.LOAD_CASES[load_case]
        pressure = loads['cabin_pressure']
        load_factor = loads['load_factor']
        
        # Approximate as flat panel with curvature
        radius_curvature = 15.0  # m - effective radius
        
        # Calculate stresses
        hoop_stress = self.calculate_hoop_stress(radius_curvature, thickness, pressure)
        
        # Wing bending contribution (major load)
        wing_moment = 2e7 * load_factor  # N·m
        distance_to_neutral = 1.5  # m
        second_moment = 0.5  # m⁴
        bending_stress = self.calculate_bending_stress(wing_moment, 
                                                       distance_to_neutral,
                                                       second_moment)
        
        # Shear from aerodynamic loads
        shear_force = 5e5 * load_factor  # N
        shear_area = width * thickness
        shear_stress = self.calculate_shear_stress(shear_force, shear_area)
        
        # von Mises combined stress
        von_mises = self.calculate_von_mises_stress(bending_stress, 
                                                    hoop_stress,
                                                    shear_stress)
        
        # Allowable stress
        allowable = self.MATERIALS[material]['strength_tensile']
        
        # Margin of safety
        ms = self.calculate_margin_of_safety(von_mises, allowable)
        
        results = {
            'component': '53-20-03 BWB Skin Panel',
            'load_case': load_case,
            'material': material,
            'hoop_stress_MPa': hoop_stress / 1e6,
            'bending_stress_MPa': bending_stress / 1e6,
            'shear_stress_MPa': shear_stress / 1e6,
            'von_mises_stress_MPa': von_mises / 1e6,
            'allowable_stress_MPa': allowable / 1e6,
            'margin_of_safety': ms,
            'status': 'PASS' if ms > 0 else 'FAIL'
        }
        
        return results
    
    def print_results(self, results: Dict):
        """Print stress analysis results in formatted table."""
        print("\n" + "="*70)
        print(f"STRESS ANALYSIS RESULTS: {results['component']}")
        print("="*70)
        print(f"Load Case: {results['load_case'].upper()}")
        print(f"Material: {results['material']}")
        print("-"*70)
        
        for key, value in results.items():
            if key in ['component', 'load_case', 'material', 'status']:
                continue
            if 'MPa' in key:
                print(f"{key.replace('_', ' ').title():.<50} {value:>10.2f} MPa")
            elif key == 'margin_of_safety':
                print(f"{key.replace('_', ' ').title():.<50} {value:>10.3f}")
        
        print("-"*70)
        print(f"STATUS: {results['status']}")
        print("="*70 + "\n")


def main():
    """Main function for command-line interface."""
    parser = argparse.ArgumentParser(
        description='Calculate stress in AMPEL360 fuselage components'
    )
    parser.add_argument(
        '--component',
        type=str,
        choices=['53-10-01', '53-20-03'],
        default='53-10-01',
        help='Component to analyze'
    )
    parser.add_argument(
        '--load-case',
        type=str,
        choices=['limit', 'ultimate'],
        default='limit',
        help='Load case to analyze'
    )
    
    args = parser.parse_args()
    
    calculator = StressCalculator()
    
    if args.component == '53-10-01':
        results = calculator.analyze_nose_cone(args.load_case)
    elif args.component == '53-20-03':
        results = calculator.analyze_bwb_skin_panel(args.load_case)
    
    calculator.print_results(results)


if __name__ == '__main__':
    main()
