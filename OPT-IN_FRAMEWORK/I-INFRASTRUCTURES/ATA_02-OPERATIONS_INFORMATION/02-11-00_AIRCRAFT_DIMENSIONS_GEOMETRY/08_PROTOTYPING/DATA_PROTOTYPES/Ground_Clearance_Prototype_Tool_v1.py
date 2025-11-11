#!/usr/bin/env python3
"""
Ground Clearance Prototype Tool v1.0

Component: ATA 02-11-00 - AIRCRAFT_DIMENSIONS_GEOMETRY
Purpose: Ground clearance analysis and validation tool for BWB aircraft
Platform: AMPEL360 BWB H2 Hy-E Q100 INTEGRA

This tool analyzes ground clearance at critical points during various 
aircraft attitudes and loading conditions to ensure safe ground operations.

Author: AMPEL360 Engineering Team
Date: 2025-11-11
Version: 1.0
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Dict, List, Tuple
from enum import Enum


class LoadingCondition(Enum):
    """Aircraft loading conditions"""
    EMPTY = "Empty Weight"
    TYPICAL = "Typical Payload"
    MTOW = "Maximum Take-Off Weight"
    MLW = "Maximum Landing Weight"


@dataclass
class ClearancePoint:
    """Represents a critical clearance measurement point"""
    name: str
    x_position: float  # meters from datum
    y_position: float  # meters from centerline
    z_nominal: float   # meters above ground at level attitude
    criticality: str   # LOW, MEDIUM, HIGH, CRITICAL


@dataclass
class AircraftAttitude:
    """Aircraft attitude parameters"""
    pitch_angle: float = 0.0  # degrees, positive nose-up
    roll_angle: float = 0.0   # degrees, positive right-wing-down
    gear_compression: float = 0.0  # meters, positive for compression


class GroundClearanceTool:
    """Tool for analyzing ground clearance for BWB aircraft"""
    
    def __init__(self):
        # BWB-specific geometry
        self.overall_length = 52.0  # meters
        self.wingspan = 65.0  # meters
        self.nominal_height = 15.5  # meters
        
        # Define critical clearance points
        self.clearance_points = self._define_clearance_points()
        
        # Minimum allowable clearances (meters)
        self.min_clearances = {
            'CRITICAL': 0.5,
            'HIGH': 1.0,
            'MEDIUM': 1.5,
            'LOW': 2.0
        }
        
    def _define_clearance_points(self) -> List[ClearancePoint]:
        """Define critical clearance measurement points for BWB"""
        points = [
            # Wingtips
            ClearancePoint("Left Wingtip", -15.0, -32.5, 2.5, "HIGH"),
            ClearancePoint("Right Wingtip", -15.0, 32.5, 2.5, "HIGH"),
            
            # Belly sections
            ClearancePoint("Forward Belly", -20.0, 0.0, 1.8, "CRITICAL"),
            ClearancePoint("Center Belly", 0.0, 0.0, 1.8, "CRITICAL"),
            ClearancePoint("Aft Belly", 20.0, 0.0, 1.8, "CRITICAL"),
            
            # Engine intakes (if applicable)
            ClearancePoint("Left Engine Intake", -10.0, -8.0, 2.0, "CRITICAL"),
            ClearancePoint("Right Engine Intake", -10.0, 8.0, 2.0, "CRITICAL"),
            
            # Tail/aft extremity
            ClearancePoint("Aft Tail Tip", 26.0, 0.0, 3.2, "HIGH"),
            
            # Landing gear doors (when retracted)
            ClearancePoint("Nose Gear Door", -15.0, 0.0, 1.5, "MEDIUM"),
            ClearancePoint("Left Main Gear Door", 5.0, -6.0, 1.5, "MEDIUM"),
            ClearancePoint("Right Main Gear Door", 5.0, 6.0, 1.5, "MEDIUM"),
            
            # BWB specific - wing trailing edge tips
            ClearancePoint("Left TE Tip", 10.0, -30.0, 2.8, "MEDIUM"),
            ClearancePoint("Right TE Tip", 10.0, 30.0, 2.8, "MEDIUM"),
        ]
        
        return points
    
    def calculate_clearance_at_attitude(self, point: ClearancePoint, 
                                       attitude: AircraftAttitude,
                                       loading: LoadingCondition = LoadingCondition.TYPICAL) -> float:
        """
        Calculate ground clearance at a specific point for given attitude
        
        Args:
            point: ClearancePoint to analyze
            attitude: Aircraft attitude parameters
            loading: Loading condition
            
        Returns:
            Ground clearance in meters
        """
        # Convert angles to radians
        pitch_rad = np.radians(attitude.pitch_angle)
        roll_rad = np.radians(attitude.roll_angle)
        
        # Calculate height change due to pitch
        pitch_effect = point.x_position * np.tan(pitch_rad)
        
        # Calculate height change due to roll
        roll_effect = point.y_position * np.tan(roll_rad)
        
        # Adjust for gear compression
        compression_effect = -attitude.gear_compression
        
        # Adjust for loading condition (affects suspension compression)
        loading_factor = {
            LoadingCondition.EMPTY: 1.05,
            LoadingCondition.TYPICAL: 1.0,
            LoadingCondition.MTOW: 0.92,
            LoadingCondition.MLW: 0.94
        }[loading]
        
        # Calculate total clearance
        clearance = (point.z_nominal + pitch_effect + roll_effect + 
                    compression_effect) * loading_factor
        
        return clearance
    
    def check_clearance_compliance(self, attitude: AircraftAttitude,
                                   loading: LoadingCondition = LoadingCondition.TYPICAL) -> Dict:
        """
        Check clearance compliance for all critical points
        
        Args:
            attitude: Aircraft attitude
            loading: Loading condition
            
        Returns:
            Dictionary with compliance results
        """
        results = {
            'compliant': True,
            'violations': [],
            'warnings': [],
            'clearances': {}
        }
        
        for point in self.clearance_points:
            clearance = self.calculate_clearance_at_attitude(point, attitude, loading)
            min_required = self.min_clearances[point.criticality]
            
            results['clearances'][point.name] = {
                'actual': clearance,
                'required': min_required,
                'margin': clearance - min_required,
                'criticality': point.criticality
            }
            
            if clearance < min_required:
                results['compliant'] = False
                results['violations'].append({
                    'point': point.name,
                    'clearance': clearance,
                    'required': min_required,
                    'deficit': min_required - clearance
                })
            elif clearance < min_required * 1.2:  # Within 20% of minimum
                results['warnings'].append({
                    'point': point.name,
                    'clearance': clearance,
                    'margin': clearance - min_required
                })
        
        return results
    
    def analyze_attitude_envelope(self, pitch_range: Tuple[float, float],
                                  roll_range: Tuple[float, float],
                                  num_points: int = 20) -> np.ndarray:
        """
        Analyze clearance across range of pitch and roll attitudes
        
        Args:
            pitch_range: (min, max) pitch angles in degrees
            roll_range: (min, max) roll angles in degrees
            num_points: Number of points to sample in each dimension
            
        Returns:
            3D array of minimum clearances [pitch, roll, min_clearance]
        """
        pitch_values = np.linspace(pitch_range[0], pitch_range[1], num_points)
        roll_values = np.linspace(roll_range[0], roll_range[1], num_points)
        
        results = np.zeros((num_points, num_points))
        
        for i, pitch in enumerate(pitch_values):
            for j, roll in enumerate(roll_values):
                attitude = AircraftAttitude(pitch_angle=pitch, roll_angle=roll)
                
                # Find minimum clearance across all points
                min_clearance = float('inf')
                for point in self.clearance_points:
                    clearance = self.calculate_clearance_at_attitude(point, attitude)
                    min_clearance = min(min_clearance, clearance)
                
                results[i, j] = min_clearance
        
        return results
    
    def visualize_clearance_envelope(self, pitch_range: Tuple[float, float] = (-5, 10),
                                    roll_range: Tuple[float, float] = (-5, 5),
                                    save_path: str = None):
        """
        Create visualization of clearance envelope
        
        Args:
            pitch_range: Range of pitch angles to analyze
            roll_range: Range of roll angles to analyze
            save_path: Optional path to save figure
        """
        print("Analyzing clearance envelope...")
        results = self.analyze_attitude_envelope(pitch_range, roll_range)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Contour plot
        pitch_values = np.linspace(pitch_range[0], pitch_range[1], 20)
        roll_values = np.linspace(roll_range[0], roll_range[1], 20)
        
        contour = ax1.contourf(roll_values, pitch_values, results, 
                               levels=20, cmap='RdYlGn')
        ax1.contour(roll_values, pitch_values, results, 
                   levels=[0.5, 1.0, 1.5, 2.0], colors='black', linewidths=1)
        plt.colorbar(contour, ax=ax1, label='Minimum Clearance (m)')
        ax1.set_xlabel('Roll Angle (deg)', fontsize=12)
        ax1.set_ylabel('Pitch Angle (deg)', fontsize=12)
        ax1.set_title('Ground Clearance Envelope', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
        ax1.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
        
        # Critical points bar chart
        attitude = AircraftAttitude()  # Level attitude
        clearances = []
        names = []
        colors = []
        
        for point in self.clearance_points:
            clearance = self.calculate_clearance_at_attitude(point, attitude)
            clearances.append(clearance)
            names.append(point.name.replace(' ', '\n'))
            
            # Color based on criticality
            if point.criticality == 'CRITICAL':
                colors.append('red')
            elif point.criticality == 'HIGH':
                colors.append('orange')
            elif point.criticality == 'MEDIUM':
                colors.append('yellow')
            else:
                colors.append('green')
        
        bars = ax2.barh(range(len(names)), clearances, color=colors, alpha=0.7)
        ax2.set_yticks(range(len(names)))
        ax2.set_yticklabels(names, fontsize=8)
        ax2.set_xlabel('Clearance (m)', fontsize=12)
        ax2.set_title('Critical Point Clearances (Level)', fontsize=14, fontweight='bold')
        ax2.grid(True, axis='x', alpha=0.3)
        ax2.axvline(x=1.0, color='r', linestyle='--', linewidth=2, label='Min Critical')
        ax2.legend()
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Visualization saved to {save_path}")
        else:
            plt.show()
        
        plt.close()
    
    def generate_clearance_report(self) -> str:
        """Generate comprehensive clearance analysis report"""
        report = []
        report.append("=" * 80)
        report.append("AMPEL360 BWB H2 Hy-E Q100 - GROUND CLEARANCE ANALYSIS REPORT")
        report.append("ATA 02-11-00: AIRCRAFT DIMENSIONS GEOMETRY")
        report.append("=" * 80)
        report.append("")
        
        # Analyze level attitude
        level_attitude = AircraftAttitude()
        
        report.append("GROUND CLEARANCE AT LEVEL ATTITUDE (TYPICAL LOADING):")
        report.append("-" * 80)
        report.append(f"{'Point Name':<30} {'Clearance':<12} {'Min Required':<12} {'Margin':<10} {'Status'}")
        report.append("-" * 80)
        
        for point in self.clearance_points:
            clearance = self.calculate_clearance_at_attitude(point, level_attitude)
            min_req = self.min_clearances[point.criticality]
            margin = clearance - min_req
            status = "✓ OK" if margin >= 0 else "✗ VIOLATION"
            
            report.append(f"{point.name:<30} {clearance:>8.2f} m   {min_req:>8.2f} m   "
                        f"{margin:>7.2f} m   {status}")
        
        report.append("")
        
        # Check various loading conditions
        report.append("CLEARANCE COMPLIANCE BY LOADING CONDITION:")
        report.append("-" * 80)
        
        for loading in LoadingCondition:
            results = self.check_clearance_compliance(level_attitude, loading)
            status = "✓ COMPLIANT" if results['compliant'] else "✗ NON-COMPLIANT"
            report.append(f"{loading.value:<30} {status}")
            
            if results['violations']:
                report.append(f"  Violations: {len(results['violations'])}")
            if results['warnings']:
                report.append(f"  Warnings: {len(results['warnings'])}")
        
        report.append("")
        report.append("=" * 80)
        
        return "\n".join(report)


def main():
    """Main function for tool demonstration"""
    print("Ground Clearance Prototype Tool v1.0")
    print("ATA 02-11-00: AIRCRAFT DIMENSIONS GEOMETRY\n")
    
    # Initialize tool
    tool = GroundClearanceTool()
    
    # Generate report
    report = tool.generate_clearance_report()
    print(report)
    
    # Generate visualization
    print("\nGenerating clearance envelope visualization...")
    tool.visualize_clearance_envelope(save_path="Ground_Clearance_Envelope.png")
    
    # Test specific attitude
    print("\nTesting extreme attitude (5° pitch, 3° roll):")
    test_attitude = AircraftAttitude(pitch_angle=5.0, roll_angle=3.0)
    results = tool.check_clearance_compliance(test_attitude)
    
    print(f"Compliant: {results['compliant']}")
    print(f"Violations: {len(results['violations'])}")
    print(f"Warnings: {len(results['warnings'])}")
    
    if results['violations']:
        print("\nViolations detected:")
        for v in results['violations']:
            print(f"  - {v['point']}: {v['clearance']:.2f}m (deficit: {v['deficit']:.2f}m)")


if __name__ == "__main__":
    main()
