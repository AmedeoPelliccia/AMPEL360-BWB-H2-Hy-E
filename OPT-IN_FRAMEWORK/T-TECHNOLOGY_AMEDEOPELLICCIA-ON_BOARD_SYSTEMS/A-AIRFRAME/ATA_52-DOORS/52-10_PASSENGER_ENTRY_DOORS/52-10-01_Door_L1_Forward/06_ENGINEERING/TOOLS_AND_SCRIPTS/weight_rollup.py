#!/usr/bin/env python3
"""
Weight Rollup Calculator
Aggregates component weights and calculates CG
"""

import pandas as pd
import numpy as np

def load_weight_budget(csv_file):
    """Load weight budget from CSV file"""
    try:
        df = pd.read_csv(csv_file)
        return df
    except FileNotFoundError:
        print(f"Error: {csv_file} not found")
        return None

def calculate_totals(df):
    """Calculate total weights by category"""
    
    # Filter out summary rows
    components = df[df['Component'].str.contains('TOTAL|WEIGHT|MARGIN') == False]
    
    total_mass = components['Total_Mass_kg'].sum()
    
    print("Weight Rollup Summary")
    print("=" * 50)
    print(f"Total Mass: {total_mass:.2f} kg")
    print(f"\nBreakdown by component:")
    
    for _, row in components.iterrows():
        print(f"  {row['Component']}: {row['Total_Mass_kg']:.2f} kg")
    
    return total_mass

def calculate_cg(df, cg_data):
    """
    Calculate center of gravity
    
    Args:
        df: Weight budget DataFrame
        cg_data: Dict with component CG locations {component: (x, y, z)}
    
    Returns:
        Overall CG coordinates (x, y, z)
    """
    
    total_mass = 0
    total_mx = 0
    total_my = 0
    total_mz = 0
    
    for component, mass in zip(df['Component'], df['Total_Mass_kg']):
        if component in cg_data:
            x, y, z = cg_data[component]
            total_mass += mass
            total_mx += mass * x
            total_my += mass * y
            total_mz += mass * z
    
    if total_mass > 0:
        cg_x = total_mx / total_mass
        cg_y = total_my / total_mass
        cg_z = total_mz / total_mass
        
        return (cg_x, cg_y, cg_z)
    else:
        return (0, 0, 0)

def weight_margin_analysis(actual_mass, target_mass):
    """Calculate weight margin"""
    
    margin_kg = target_mass - actual_mass
    margin_percent = (margin_kg / target_mass) * 100
    
    print(f"\nWeight Margin Analysis")
    print("=" * 50)
    print(f"Target Mass: {target_mass:.2f} kg")
    print(f"Actual Mass: {actual_mass:.2f} kg")
    print(f"Margin: {margin_kg:.2f} kg ({margin_percent:.1f}%)")
    
    if margin_kg > 0:
        print("Status: ✓ Under target")
    else:
        print("Status: ✗ Over target - Redesign required")
    
    return margin_kg, margin_percent

if __name__ == "__main__":
    print("Weight Rollup Calculator")
    print("=" * 50)
    
    # Example usage
    csv_file = "../WEIGHT_AND_BALANCE/Weight_Budget.csv"
    
    # Example CG locations (mm from reference point)
    cg_locations = {
        'Face_Sheet_Outer': (940, 560, 0),
        'Face_Sheet_Inner': (940, 560, 48),
        'Core': (940, 560, 24),
        'Lightning_Protection': (940, 560, 0),
        'Edge_Bands': (940, 0, 24),
        'Inserts_Titanium': (940, 0, 24),
        'Adhesive_Film': (940, 560, 2),
        'Paint_Coating': (940, 560, 48),
        'Frame_Assembly': (0, 560, 24)
    }
    
    # Load and process
    df = load_weight_budget(csv_file)
    if df is not None:
        total = calculate_totals(df)
        
        # CG calculation
        cg = calculate_cg(df, cg_locations)
        print(f"\nCenter of Gravity:")
        print(f"  X: {cg[0]:.1f} mm")
        print(f"  Y: {cg[1]:.1f} mm")
        print(f"  Z: {cg[2]:.1f} mm")
        
        # Margin analysis
        target = 140.0  # kg
        weight_margin_analysis(total, target)
