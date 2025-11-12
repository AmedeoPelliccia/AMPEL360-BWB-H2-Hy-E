#!/usr/bin/env python3
"""
Geometry Envelope Tool v1.0

Component: ATA 02-11-00 - AIRCRAFT_DIMENSIONS_GEOMETRY
Purpose: Aircraft geometry envelope analysis and visualization tool
Platform: AMPEL360 BWB H2 Hy-E Q100 INTEGRA

This tool calculates and visualizes the 3D geometry envelope for the 
Blended Wing Body aircraft, ensuring clearances and dimensional compliance.

Author: AMPEL360 Engineering Team
Date: 2025-11-11
Version: 1.0
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Optional


@dataclass
class BWBAircraftDimensions:
    """BWB Aircraft dimensions based on ATA 02-11-00 requirements"""
    wingspan: float = 65.0  # meters - ICAO Code E
    overall_length: float = 52.0  # meters
    overall_height: float = 15.5  # meters
    wing_area: float = 850.0  # square meters
    aspect_ratio: float = 8.5
    sweep_angle: float = 35.0  # degrees at quarter chord
    center_body_width: float = 28.0  # meters
    
    # Ground clearances (meters)
    wingtip_clearance: float = 2.5
    belly_clearance: float = 1.8
    tail_clearance: float = 3.2
    engine_intake_clearance: float = 2.0


class GeometryEnvelopeTool:
    """Tool for analyzing BWB aircraft geometry envelope"""
    
    def __init__(self, dimensions: BWBAircraftDimensions):
        self.dimensions = dimensions
        self.envelope_points = []
        
    def calculate_wing_profile(self, num_points: int = 100) -> np.ndarray:
        """
        Calculate wing profile points for BWB configuration
        
        Args:
            num_points: Number of points along the span
            
        Returns:
            Array of (x, y, z) coordinates
        """
        # Simplified BWB wing profile
        span = self.dimensions.wingspan / 2
        points = []
        
        for i in range(num_points):
            # Spanwise position
            eta = i / (num_points - 1)
            y = eta * span
            
            # Sweep calculation
            sweep_rad = np.radians(self.dimensions.sweep_angle)
            x = y * np.tan(sweep_rad)
            
            # Chord distribution (elliptical approximation)
            chord = self.dimensions.center_body_width * np.sqrt(1 - (eta ** 2))
            
            # Z position (dihedral effect, minimal for BWB)
            z = y * 0.02  # 2% dihedral
            
            points.append([x, y, z, chord])
            
        return np.array(points)
    
    def calculate_ground_clearance_envelope(self) -> dict:
        """
        Calculate ground clearance envelope at critical points
        
        Returns:
            Dictionary with clearance values at key locations
        """
        clearances = {
            'wingtip_left': self.dimensions.wingtip_clearance,
            'wingtip_right': self.dimensions.wingtip_clearance,
            'belly_forward': self.dimensions.belly_clearance,
            'belly_center': self.dimensions.belly_clearance,
            'belly_aft': self.dimensions.belly_clearance,
            'tail_tip': self.dimensions.tail_clearance,
            'engine_intake_left': self.dimensions.engine_intake_clearance,
            'engine_intake_right': self.dimensions.engine_intake_clearance,
        }
        
        return clearances
    
    def check_airport_gate_compatibility(self, gate_width: float = 80.0, 
                                         gate_height: float = 18.0) -> bool:
        """
        Check if aircraft fits within standard gate envelope
        
        Args:
            gate_width: Gate width in meters (default 80m for Code E)
            gate_height: Gate height in meters
            
        Returns:
            Boolean indicating compatibility
        """
        width_ok = self.dimensions.wingspan <= gate_width
        height_ok = self.dimensions.overall_height <= gate_height
        
        return width_ok and height_ok
    
    def calculate_turning_radius(self, steering_angle: float = 70.0) -> float:
        """
        Calculate minimum turning radius for ground operations
        
        Args:
            steering_angle: Maximum nose gear steering angle in degrees
            
        Returns:
            Minimum turning radius in meters
        """
        # Simplified calculation based on wheelbase
        wheelbase = self.dimensions.overall_length * 0.7  # Approximate
        steering_rad = np.radians(steering_angle)
        
        if steering_rad > 0:
            turning_radius = wheelbase / np.tan(steering_rad)
        else:
            turning_radius = float('inf')
            
        return turning_radius
    
    def visualize_top_view(self, save_path: Optional[str] = None):
        """
        Generate top-view visualization of aircraft geometry
        
        Args:
            save_path: Optional path to save the figure
        """
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Generate wing profile
        wing_profile = self.calculate_wing_profile()
        
        # Plot both wing halves
        ax.plot(wing_profile[:, 0], wing_profile[:, 1], 'b-', linewidth=2, label='Right Wing')
        ax.plot(wing_profile[:, 0], -wing_profile[:, 1], 'b-', linewidth=2, label='Left Wing')
        
        # Center body outline
        center_width = self.dimensions.center_body_width / 2
        center_length = self.dimensions.overall_length / 2
        center_box = plt.Rectangle((-center_length, -center_width), 
                                   2*center_length, 2*center_width,
                                   fill=False, edgecolor='r', linewidth=2, label='Center Body')
        ax.add_patch(center_box)
        
        # Reference axes
        ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='--', alpha=0.3)
        
        ax.set_xlabel('Longitudinal Position (m)', fontsize=12)
        ax.set_ylabel('Lateral Position (m)', fontsize=12)
        ax.set_title('AMPEL360 BWB - Top View Geometry Envelope', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.axis('equal')
        ax.legend()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        else:
            plt.show()
        
        plt.close()
    
    def generate_envelope_report(self) -> str:
        """
        Generate a text report of geometry envelope analysis
        
        Returns:
            Formatted report string
        """
        report = []
        report.append("=" * 70)
        report.append("AMPEL360 BWB H2 Hy-E Q100 - GEOMETRY ENVELOPE REPORT")
        report.append("ATA 02-11-00: AIRCRAFT DIMENSIONS GEOMETRY")
        report.append("=" * 70)
        report.append("")
        
        # Dimensions
        report.append("OVERALL DIMENSIONS:")
        report.append(f"  Wingspan:        {self.dimensions.wingspan:.2f} m")
        report.append(f"  Overall Length:  {self.dimensions.overall_length:.2f} m")
        report.append(f"  Overall Height:  {self.dimensions.overall_height:.2f} m")
        report.append(f"  Wing Area:       {self.dimensions.wing_area:.2f} m²")
        report.append(f"  Aspect Ratio:    {self.dimensions.aspect_ratio:.2f}")
        report.append(f"  Sweep Angle:     {self.dimensions.sweep_angle:.2f}°")
        report.append("")
        
        # Ground clearances
        clearances = self.calculate_ground_clearance_envelope()
        report.append("GROUND CLEARANCES:")
        for location, clearance in clearances.items():
            report.append(f"  {location.replace('_', ' ').title():25s}: {clearance:.2f} m")
        report.append("")
        
        # Airport compatibility
        gate_compatible = self.check_airport_gate_compatibility()
        report.append("AIRPORT COMPATIBILITY:")
        report.append(f"  ICAO Code E Gate: {'✓ COMPATIBLE' if gate_compatible else '✗ NOT COMPATIBLE'}")
        report.append(f"  Turning Radius:   {self.calculate_turning_radius():.2f} m")
        report.append("")
        
        report.append("=" * 70)
        
        return "\n".join(report)


def main():
    """Main function for tool demonstration"""
    print("Geometry Envelope Tool v1.0")
    print("ATA 02-11-00: AIRCRAFT DIMENSIONS GEOMETRY\n")
    
    # Initialize with BWB dimensions
    dimensions = BWBAircraftDimensions()
    tool = GeometryEnvelopeTool(dimensions)
    
    # Generate and print report
    report = tool.generate_envelope_report()
    print(report)
    
    # Generate visualization
    print("\nGenerating top-view visualization...")
    tool.visualize_top_view(save_path="BWB_Top_View_Envelope.png")
    print("Visualization saved as 'BWB_Top_View_Envelope.png'")
    
    # Additional analysis
    print("\nADDITIONAL ANALYSIS:")
    print(f"Wing Profile Points Generated: {len(tool.calculate_wing_profile())}")
    print(f"Center Body Width: {dimensions.center_body_width:.2f} m")
    

if __name__ == "__main__":
    main()
