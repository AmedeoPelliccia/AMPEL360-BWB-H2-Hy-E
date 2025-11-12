#!/usr/bin/env python3
"""
AMPEL360 BWB CG Envelope Tool v1.0
ATA 02-10-00 Aircraft General Data - Prototyping Tool

Visualizes and validates CG envelope for AMPEL360 BWB aircraft.
Plots CG location vs. weight and checks against limits.

Author: AMPEL360 Engineering Team
Date: 2025-11-05
Version: 1.0 (Prototype)
"""

import sys
from typing import Tuple


class CGEnvelopeTool:
    """
    CG Envelope Tool for AMPEL360 BWB Aircraft
    
    Defines and validates center of gravity limits across weight range.
    """
    
    def __init__(self):
        """Initialize with AMPEL360 BWB CG envelope"""
        
        # Weight limits (kg)
        self.oew = 42000
        self.max_zfw = 75000
        self.mtow = 95000
        self.mlw = 82000
        
        # CG limits (%MAC)
        # Format: (weight_kg, forward_limit_%MAC, aft_limit_%MAC)
        self.cg_envelope = [
            (42000, 25.0, 32.0),   # OEW
            (75000, 20.0, 35.0),   # Max ZFW
            (95000, 20.0, 35.0),   # MTOW
            (82000, 20.0, 35.0),   # MLW
        ]
        
    def get_cg_limits(self, weight_kg: float) -> Tuple[float, float]:
        """
        Get CG limits for a given weight by linear interpolation
        
        Args:
            weight_kg: Aircraft weight
        
        Returns:
            Tuple of (forward_limit_%MAC, aft_limit_%MAC)
        """
        # Find bracketing weights
        envelope_sorted = sorted(self.cg_envelope, key=lambda x: x[0])
        
        # If below minimum or above maximum, use nearest limits
        if weight_kg <= envelope_sorted[0][0]:
            return envelope_sorted[0][1], envelope_sorted[0][2]
        if weight_kg >= envelope_sorted[-1][0]:
            return envelope_sorted[-1][1], envelope_sorted[-1][2]
        
        # Linear interpolation
        for i in range(len(envelope_sorted) - 1):
            w1, fwd1, aft1 = envelope_sorted[i]
            w2, fwd2, aft2 = envelope_sorted[i + 1]
            
            if w1 <= weight_kg <= w2:
                # Interpolation factor
                factor = (weight_kg - w1) / (w2 - w1)
                
                # Interpolated limits
                fwd_limit = fwd1 + factor * (fwd2 - fwd1)
                aft_limit = aft1 + factor * (aft2 - aft1)
                
                return fwd_limit, aft_limit
        
        # Should not reach here
        return 20.0, 35.0
    
    def check_cg(self, weight_kg: float, cg_percent_mac: float) -> Tuple[bool, str]:
        """
        Check if CG is within limits for given weight
        
        Args:
            weight_kg: Aircraft weight
            cg_percent_mac: CG location (%MAC)
        
        Returns:
            Tuple of (within_limits: bool, message: str)
        """
        fwd_limit, aft_limit = self.get_cg_limits(weight_kg)
        
        if cg_percent_mac < fwd_limit:
            margin = fwd_limit - cg_percent_mac
            return False, f"CG TOO FORWARD by {margin:.1f}% MAC (limit {fwd_limit:.1f}% MAC)"
        
        if cg_percent_mac > aft_limit:
            margin = cg_percent_mac - aft_limit
            return False, f"CG TOO AFT by {margin:.1f}% MAC (limit {aft_limit:.1f}% MAC)"
        
        fwd_margin = cg_percent_mac - fwd_limit
        aft_margin = aft_limit - cg_percent_mac
        
        return True, f"CG OK - Fwd margin: {fwd_margin:.1f}% MAC, Aft margin: {aft_margin:.1f}% MAC"
    
    def print_envelope(self):
        """Print CG envelope table"""
        print("\n" + "="*70)
        print("AMPEL360 BWB - CG ENVELOPE")
        print("="*70)
        print("\n{:>15s} {:>15s} {:>15s} {:>15s}".format(
            "Weight (kg)", "Forward Limit", "Aft Limit", "Range"))
        print("-" * 70)
        
        for weight, fwd, aft in sorted(self.cg_envelope):
            weight_name = ""
            if weight == self.oew:
                weight_name = "OEW"
            elif weight == self.max_zfw:
                weight_name = "Max ZFW"
            elif weight == self.mtow:
                weight_name = "MTOW"
            elif weight == self.mlw:
                weight_name = "MLW"
            
            range_width = aft - fwd
            print(f"{weight:>15,.0f} {fwd:>14.1f}% {aft:>14.1f}% {range_width:>14.1f}%  {weight_name}")
        
        print("="*70 + "\n")
    
    def plot_envelope_ascii(self):
        """Generate ASCII art plot of CG envelope"""
        print("\nCG ENVELOPE PLOT (ASCII)")
        print("="*70)
        print("\nWeight (kg) vs. CG Location (%MAC)")
        print("\n      Weight |  15%   20%   25%   30%   35%   40%")
        print("        (kg) |----+----+----+----+----+----+----|")
        
        # Plot envelope points
        for weight, fwd, aft in sorted(self.cg_envelope, reverse=True):
            # Scale to character positions (15-40% MAC = 0-50 chars)
            fwd_pos = int((fwd - 15) * 2)
            aft_pos = int((aft - 15) * 2)
            
            # Build line
            line = " " * 56
            line_list = list(line)
            
            # Mark forward and aft limits
            if 0 <= fwd_pos < 50:
                line_list[fwd_pos] = '['
            if 0 <= aft_pos < 50:
                line_list[aft_pos] = ']'
            
            # Fill between limits
            for i in range(max(0, fwd_pos+1), min(50, aft_pos)):
                if line_list[i] == ' ':
                    line_list[i] = '-'
            
            line = ''.join(line_list)
            
            # Weight label
            if weight == self.mtow:
                label = "MTOW"
            elif weight == self.max_zfw:
                label = "ZFW"
            elif weight == self.mlw:
                label = "MLW"
            elif weight == self.oew:
                label = "OEW"
            else:
                label = ""
            
            print(f"{weight:>12,.0f} | {line} {label}")
        
        print("        (kg) |----+----+----+----+----+----+----|")
        print("             |  15%   20%   25%   30%   35%   40%")
        print("             |         CG Location (%MAC)")
        print("="*70 + "\n")


def example_checks():
    """Run example CG checks"""
    
    tool = CGEnvelopeTool()
    
    print("\n" + "#"*70)
    print("# CG ENVELOPE VALIDATION")
    print("#"*70)
    
    # Print envelope
    tool.print_envelope()
    
    # ASCII plot
    tool.plot_envelope_ascii()
    
    # Test scenarios
    print("EXAMPLE CG CHECKS:")
    print("-" * 70)
    
    test_cases = [
        (95000, 28.0, "MTOW, nominal CG"),
        (95000, 18.0, "MTOW, CG too forward"),
        (95000, 37.0, "MTOW, CG too aft"),
        (75000, 27.5, "Max ZFW, nominal CG"),
        (42000, 28.5, "OEW, nominal CG"),
        (60000, 32.0, "Mid-weight, aft CG"),
    ]
    
    for weight, cg, description in test_cases:
        ok, msg = tool.check_cg(weight, cg)
        status = "✓" if ok else "✗"
        print(f"\n{status} {description}")
        print(f"  Weight: {weight:,.0f} kg | CG: {cg:.1f}% MAC")
        print(f"  {msg}")


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   AMPEL360 BWB CG Envelope Tool v1.0                                ║
║   ATA 02-10-00 Aircraft General Data                                ║
║                                                                      ║
║   Prototype Tool - For Engineering Analysis Only                    ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("""
Usage: python CG_Envelope_Tool_v1.py [--help]

This tool:
    - Displays CG envelope limits
    - Validates CG location for any weight
    - Provides visual representation (ASCII plot)

Features:
    - Linear interpolation of limits between defined points
    - Margin calculations
    - ASCII visualization of envelope
        """)
        sys.exit(0)
    
    example_checks()
    
    print("\n" + "="*70)
    print("NOTE: Production version will include:")
    print("  - Graphical plot (matplotlib)")
    print("  - Import/export of loading data")
    print("  - Integration with Weight_Balance_Calculator")
    print("  - Real-time validation during loading")
    print("="*70 + "\n")
