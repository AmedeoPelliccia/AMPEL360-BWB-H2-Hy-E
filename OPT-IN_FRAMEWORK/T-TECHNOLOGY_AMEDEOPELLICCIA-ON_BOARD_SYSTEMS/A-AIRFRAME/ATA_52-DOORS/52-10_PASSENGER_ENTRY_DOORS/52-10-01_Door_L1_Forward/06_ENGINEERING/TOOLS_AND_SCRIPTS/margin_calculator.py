#!/usr/bin/env python3
"""
Margin of Safety Calculator
Calculates structural margins with uncertainty
"""

import pandas as pd

def margin_of_safety(allowable, applied, factor_of_safety=1.0):
    """
    Calculate margin of safety
    
    Args:
        allowable: Allowable stress/load
        applied: Applied stress/load
        factor_of_safety: Safety factor (default 1.0)
    
    Returns:
        Margin of safety
    """
    ms = (allowable / (applied * factor_of_safety)) - 1
    return ms

def margin_with_uncertainty(allowable, applied, uncertainty_pct, factor_of_safety=1.0):
    """
    Calculate margin considering uncertainty
    
    Args:
        allowable: Allowable stress/load
        applied: Applied stress/load (nominal)
        uncertainty_pct: Uncertainty as percentage (e.g., 40 for ±40%)
        factor_of_safety: Safety factor
    
    Returns:
        dict with nominal, worst-case, and best-case margins
    """
    
    # Nominal margin
    ms_nominal = margin_of_safety(allowable, applied, factor_of_safety)
    
    # Worst case (applied stress could be higher)
    applied_worst = applied * (1 + uncertainty_pct/100)
    ms_worst = margin_of_safety(allowable, applied_worst, factor_of_safety)
    
    # Best case (applied stress could be lower)
    applied_best = applied * (1 - uncertainty_pct/100)
    ms_best = margin_of_safety(allowable, applied_best, factor_of_safety)
    
    return {
        'ms_nominal': ms_nominal,
        'ms_worst_case': ms_worst,
        'ms_best_case': ms_best,
        'applied_nominal': applied,
        'applied_worst': applied_worst,
        'applied_best': applied_best,
        'uncertainty_pct': uncertainty_pct
    }

def evaluate_margin(ms):
    """Evaluate margin status"""
    if ms >= 0.15:
        return "PASS - Good margin"
    elif ms >= 0.0:
        return "PASS - Marginal"
    else:
        return "FAIL - Negative margin"

def process_margin_summary(csv_file):
    """Process margin summary CSV and add evaluations"""
    
    try:
        df = pd.read_csv(csv_file)
        
        print("Margin Summary Analysis")
        print("=" * 70)
        
        for _, row in df.iterrows():
            component = row['Component']
            ms = row['Margin_of_Safety']
            
            # Parse MS (handle +/- and numeric values)
            try:
                ms_value = float(str(ms).replace('+', ''))
                evaluation = evaluate_margin(ms_value)
                
                print(f"\n{component}:")
                print(f"  Load Case: {row['Load_Case']}")
                print(f"  Applied: {row['Applied_Stress_MPa']} MPa")
                print(f"  Allowable: {row['Allowable_MPa']} MPa")
                print(f"  MS: {ms}")
                print(f"  Status: {evaluation}")
                
            except (ValueError, TypeError):
                print(f"\n{component}: MS = {ms} (non-numeric)")
        
        # Summary statistics
        print("\n" + "=" * 70)
        print("Summary:")
        pass_count = len(df[df['Status'] == 'PASS'])
        fail_count = len(df[df['Status'] == 'FAIL'])
        print(f"  PASS: {pass_count}")
        print(f"  FAIL: {fail_count}")
        
        if fail_count > 0:
            print("\n⚠️  WARNING: Design has negative margins - redesign required!")
        else:
            print("\n✓ All margins positive")
        
    except FileNotFoundError:
        print(f"Error: {csv_file} not found")

if __name__ == "__main__":
    print("Margin of Safety Calculator")
    print("=" * 70)
    
    # Example calculation
    print("\nExample: Panel stress with uncertainty")
    result = margin_with_uncertainty(
        allowable=2724,  # MPa
        applied=348,     # MPa
        uncertainty_pct=40,
        factor_of_safety=1.0
    )
    
    print(f"Nominal MS: {result['ms_nominal']:+.2f}")
    print(f"Worst case MS: {result['ms_worst_case']:+.2f}")
    print(f"Best case MS: {result['ms_best_case']:+.2f}")
    print(f"Status: {evaluate_margin(result['ms_worst_case'])}")
    
    # Process actual margin summary
    print("\n" + "=" * 70)
    csv_file = "../STRUCTURAL_ANALYSIS/Margin_Summary.csv"
    process_margin_summary(csv_file)
