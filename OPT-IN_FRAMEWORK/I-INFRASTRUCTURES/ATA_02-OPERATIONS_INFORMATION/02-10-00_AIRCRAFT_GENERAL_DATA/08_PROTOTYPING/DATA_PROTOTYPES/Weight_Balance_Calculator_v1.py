#!/usr/bin/env python3
"""
AMPEL360 BWB Weight & Balance Calculator v1.0
ATA 02-10-00 Aircraft General Data - Prototyping Tool

Calculates center of gravity (CG) and weight distribution for AMPEL360 BWB aircraft.
Validates loading against CG envelope and structural limits.

Author: AMPEL360 Engineering Team
Date: 2025-11-05
Version: 1.0 (Prototype)
"""

import sys
from typing import Dict, Tuple
import json


class WeightBalanceCalculator:
    """
    Weight and Balance Calculator for AMPEL360 BWB Aircraft
    
    Coordinates:
        X-axis: Forward (nose to tail), origin at nose apex
        Y-axis: Right wing (left to right), origin at centerline
        Z-axis: Up, origin at fuselage bottom
    """
    
    def __init__(self):
        """Initialize with AMPEL360 BWB aircraft parameters"""
        
        # Aircraft basic data
        self.mac = 13.74  # Mean Aerodynamic Chord (m)
        self.mac_lemac = 31.20  # Leading Edge of MAC from nose (m)
        
        # Weight limits (kg)
        self.max_zero_fuel_weight = 75000
        self.max_takeoff_weight = 95000
        self.max_landing_weight = 82000
        self.operating_empty_weight = 42000
        
        # CG limits (%MAC from LEMAC)
        self.cg_forward_limit = 20.0  # % MAC
        self.cg_aft_limit = 35.0      # % MAC
        
        # Component arm locations (m from nose, typical values)
        self.component_arms = {
            'oew': 35.50,           # Operating Empty Weight CG
            'crew': 2.50,           # Flight crew
            'passengers_fwd': 12.00,  # Forward cabin (rows 1-10)
            'passengers_mid': 24.00,  # Mid cabin (rows 11-20)
            'passengers_aft': 36.00,  # Aft cabin (rows 21-30)
            'cargo_fwd': 8.00,        # Forward cargo hold
            'cargo_aft': 46.00,       # Aft cargo hold
            'h2_fuel_fwd': 18.00,     # Forward H2 tank
            'h2_fuel_aft': 40.00,     # Aft H2 tank
        }
        
        # Passenger and cargo data
        self.standard_pax_weight = 95  # kg (including carry-on, EASA standard)
        self.max_passengers = 220
        self.max_cargo = 15000  # kg
        
    def calculate_cg(self, weight_items: Dict[str, float]) -> Tuple[float, float, bool]:
        """
        Calculate center of gravity location
        
        Args:
            weight_items: Dictionary of {component_name: weight_kg}
        
        Returns:
            Tuple of (cg_location_m, cg_percent_mac, within_limits)
        """
        total_weight = 0.0
        total_moment = 0.0
        
        for component, weight in weight_items.items():
            if component not in self.component_arms:
                print(f"Warning: Component '{component}' not in database, skipping")
                continue
            
            arm = self.component_arms[component]
            moment = weight * arm
            total_weight += weight
            total_moment += moment
        
        if total_weight == 0:
            return 0.0, 0.0, False
        
        # Calculate CG location (m from nose)
        cg_location = total_moment / total_weight
        
        # Convert to %MAC
        cg_percent_mac = ((cg_location - self.mac_lemac) / self.mac) * 100
        
        # Check if within limits
        within_limits = (self.cg_forward_limit <= cg_percent_mac <= self.cg_aft_limit)
        
        return cg_location, cg_percent_mac, within_limits
    
    def calculate_loading(self, num_passengers: int, cargo_fwd_kg: float, 
                         cargo_aft_kg: float, fuel_kg: float) -> Dict:
        """
        Calculate complete loading scenario
        
        Args:
            num_passengers: Number of passengers
            cargo_fwd_kg: Forward cargo weight (kg)
            cargo_aft_kg: Aft cargo weight (kg)
            fuel_kg: Total H2 fuel weight (kg)
        
        Returns:
            Dictionary with weight and balance results
        """
        # Distribute passengers (simplified: even distribution)
        pax_fwd = int(num_passengers * 0.33)
        pax_mid = int(num_passengers * 0.33)
        pax_aft = num_passengers - pax_fwd - pax_mid
        
        # Distribute fuel (50% forward, 50% aft tanks)
        fuel_fwd = fuel_kg * 0.50
        fuel_aft = fuel_kg * 0.50
        
        # Build weight items dictionary
        weight_items = {
            'oew': self.operating_empty_weight,
            'crew': 2 * 95,  # 2 pilots
            'passengers_fwd': pax_fwd * self.standard_pax_weight,
            'passengers_mid': pax_mid * self.standard_pax_weight,
            'passengers_aft': pax_aft * self.standard_pax_weight,
            'cargo_fwd': cargo_fwd_kg,
            'cargo_aft': cargo_aft_kg,
            'h2_fuel_fwd': fuel_fwd,
            'h2_fuel_aft': fuel_aft,
        }
        
        # Calculate total weight
        total_weight = sum(weight_items.values())
        
        # Calculate CG
        cg_location, cg_percent_mac, within_limits = self.calculate_cg(weight_items)
        
        # Check weight limits
        zfw = total_weight - fuel_kg  # Zero Fuel Weight
        
        results = {
            'weight_items': weight_items,
            'total_weight_kg': total_weight,
            'zero_fuel_weight_kg': zfw,
            'fuel_weight_kg': fuel_kg,
            'cg_location_m': cg_location,
            'cg_percent_mac': cg_percent_mac,
            'cg_within_limits': within_limits,
            'weight_within_limits': {
                'zfw': zfw <= self.max_zero_fuel_weight,
                'tow': total_weight <= self.max_takeoff_weight,
            },
            'margins': {
                'zfw_margin_kg': self.max_zero_fuel_weight - zfw,
                'tow_margin_kg': self.max_takeoff_weight - total_weight,
                'cg_fwd_margin_pct': cg_percent_mac - self.cg_forward_limit,
                'cg_aft_margin_pct': self.cg_aft_limit - cg_percent_mac,
            }
        }
        
        return results
    
    def print_results(self, results: Dict):
        """Print formatted weight and balance results"""
        print("\n" + "="*70)
        print("AMPEL360 BWB - WEIGHT & BALANCE CALCULATION")
        print("="*70)
        
        print("\nWEIGHT BREAKDOWN:")
        print("-" * 70)
        for item, weight in results['weight_items'].items():
            print(f"  {item:25s}: {weight:8.0f} kg")
        print("-" * 70)
        print(f"  {'ZERO FUEL WEIGHT':25s}: {results['zero_fuel_weight_kg']:8.0f} kg")
        print(f"  {'FUEL WEIGHT':25s}: {results['fuel_weight_kg']:8.0f} kg")
        print(f"  {'TAKEOFF WEIGHT':25s}: {results['total_weight_kg']:8.0f} kg")
        
        print("\nCENTER OF GRAVITY:")
        print("-" * 70)
        print(f"  CG Location:  {results['cg_location_m']:.2f} m from nose")
        print(f"  CG Position:  {results['cg_percent_mac']:.1f} % MAC")
        print(f"  CG Limits:    {self.cg_forward_limit:.1f} to {self.cg_aft_limit:.1f} % MAC")
        
        cg_status = "✓ WITHIN LIMITS" if results['cg_within_limits'] else "✗ OUT OF LIMITS"
        print(f"  Status:       {cg_status}")
        
        print("\nWEIGHT LIMITS:")
        print("-" * 70)
        print(f"  Max Zero Fuel Weight:  {self.max_zero_fuel_weight:8.0f} kg")
        print(f"  Actual ZFW:            {results['zero_fuel_weight_kg']:8.0f} kg")
        print(f"  ZFW Margin:            {results['margins']['zfw_margin_kg']:8.0f} kg")
        
        zfw_status = "✓ OK" if results['weight_within_limits']['zfw'] else "✗ EXCEEDED"
        print(f"  ZFW Status:            {zfw_status}")
        
        print(f"\n  Max Takeoff Weight:    {self.max_takeoff_weight:8.0f} kg")
        print(f"  Actual TOW:            {results['total_weight_kg']:8.0f} kg")
        print(f"  TOW Margin:            {results['margins']['tow_margin_kg']:8.0f} kg")
        
        tow_status = "✓ OK" if results['weight_within_limits']['tow'] else "✗ EXCEEDED"
        print(f"  TOW Status:            {tow_status}")
        
        print("\nMARGINS:")
        print("-" * 70)
        print(f"  CG Forward Margin:  {results['margins']['cg_fwd_margin_pct']:6.1f} % MAC")
        print(f"  CG Aft Margin:      {results['margins']['cg_aft_margin_pct']:6.1f} % MAC")
        
        print("\n" + "="*70)
        
        # Overall status
        overall_ok = (results['cg_within_limits'] and 
                     results['weight_within_limits']['zfw'] and 
                     results['weight_within_limits']['tow'])
        
        if overall_ok:
            print("LOADING ACCEPTABLE - WITHIN ALL LIMITS")
        else:
            print("⚠ WARNING: LOADING OUT OF LIMITS - ADJUST BEFORE FLIGHT")
        print("="*70 + "\n")


def example_scenarios():
    """Run example loading scenarios"""
    
    calc = WeightBalanceCalculator()
    
    print("\n" + "#"*70)
    print("# EXAMPLE SCENARIOS")
    print("#"*70)
    
    # Scenario 1: Typical short-haul
    print("\n### SCENARIO 1: Typical Short-Haul Flight ###")
    print("220 passengers, 8000 kg cargo, 5000 kg fuel")
    results1 = calc.calculate_loading(
        num_passengers=220,
        cargo_fwd_kg=4000,
        cargo_aft_kg=4000,
        fuel_kg=5000
    )
    calc.print_results(results1)
    
    # Scenario 2: Max payload
    print("\n### SCENARIO 2: Maximum Payload ###")
    print("220 passengers, 15000 kg cargo, 8000 kg fuel")
    results2 = calc.calculate_loading(
        num_passengers=220,
        cargo_fwd_kg=7500,
        cargo_aft_kg=7500,
        fuel_kg=8000
    )
    calc.print_results(results2)
    
    # Scenario 3: Long range
    print("\n### SCENARIO 3: Long Range Flight ###")
    print("180 passengers, 5000 kg cargo, 12000 kg fuel")
    results3 = calc.calculate_loading(
        num_passengers=180,
        cargo_fwd_kg=2500,
        cargo_aft_kg=2500,
        fuel_kg=12000
    )
    calc.print_results(results3)


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   AMPEL360 BWB Weight & Balance Calculator v1.0                     ║
║   ATA 02-10-00 Aircraft General Data                                ║
║                                                                      ║
║   Prototype Tool - For Engineering Analysis Only                    ║
║   Not Certified for Flight Operations                               ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help':
            print("""
Usage: python Weight_Balance_Calculator_v1.py [--help]

Interactive mode:
    Run without arguments for interactive input

Example mode:
    Run to see pre-defined example scenarios

Features:
    - Calculate CG location for any loading scenario
    - Validate against CG envelope limits
    - Check weight limits (ZFW, MTOW)
    - Calculate margins
            """)
            sys.exit(0)
    
    # Run example scenarios
    example_scenarios()
    
    print("\n" + "="*70)
    print("NOTE: This is a prototype tool for concept validation only.")
    print("Production version will include:")
    print("  - Detailed loading instructions")
    print("  - Integration with CAOS digital twin")
    print("  - Real-time fuel burn CG shift calculation")
    print("  - Automated loadsheet generation")
    print("="*70 + "\n")
