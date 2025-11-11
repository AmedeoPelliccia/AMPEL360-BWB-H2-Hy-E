#!/usr/bin/env python3
"""
Station, Buttline, Waterline Visualizer v1.0

Component: ATA 02-11-00 - AIRCRAFT_DIMENSIONS_GEOMETRY
Purpose: Reference system visualization tool for BWB coordinate system
Platform: AMPEL360 BWB H2 Hy-E Q100 INTEGRA

This tool visualizes the aircraft reference coordinate system (Station,
Buttline, Waterline) and provides utilities for coordinate transformations
and measurement point visualization.

Author: AMPEL360 Engineering Team
Date: 2025-11-11
Version: 1.0
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict
import json


@dataclass
class ReferencePoint:
    """A reference measurement point in aircraft coordinates"""
    name: str
    station: float      # FS (Fuselage Station) - longitudinal, positive forward
    buttline: float     # BL (Buttline) - lateral, positive right
    waterline: float    # WL (Waterline) - vertical, positive up
    description: str = ""
    category: str = "general"  # structural, systems, interface, etc.


class AircraftReferenceSystem:
    """Aircraft reference coordinate system for BWB"""
    
    def __init__(self):
        # Datum locations (all in meters)
        self.fs_datum = 0.0  # Forward perpendicular at nose
        self.bl_datum = 0.0  # Aircraft centerline
        self.wl_datum = 0.0  # Ground line when aircraft is level
        
        # Aircraft extremes
        self.fs_min = -5.0   # Forward extreme
        self.fs_max = 52.0   # Aft extreme
        self.bl_min = -32.5  # Left wingtip
        self.bl_max = 32.5   # Right wingtip
        self.wl_min = 0.0    # Ground level
        self.wl_max = 15.5   # Top of aircraft
        
        # Define reference points
        self.reference_points = self._define_reference_points()
        
    def _define_reference_points(self) -> List[ReferencePoint]:
        """Define key reference measurement points for BWB"""
        points = [
            # Structural datums
            ReferencePoint("Nose Datum", 0.0, 0.0, 0.0, 
                          "Primary reference datum", "structural"),
            ReferencePoint("Main Gear Center", 15.0, 0.0, 0.0,
                          "Main landing gear centerline", "structural"),
            ReferencePoint("CG Nominal", 22.0, 0.0, 8.0,
                          "Nominal center of gravity location", "structural"),
            
            # Door locations
            ReferencePoint("Door L1 Sill", 8.0, -10.0, 2.5,
                          "Left forward passenger door", "interface"),
            ReferencePoint("Door R1 Sill", 8.0, 10.0, 2.5,
                          "Right forward passenger door", "interface"),
            ReferencePoint("Emergency Exit L3", 35.0, -12.0, 2.8,
                          "Left aft emergency exit", "interface"),
            ReferencePoint("Emergency Exit R3", 35.0, 12.0, 2.8,
                          "Right aft emergency exit", "interface"),
            
            # Wing reference points
            ReferencePoint("Wing Root LE", 10.0, 0.0, 6.0,
                          "Wing root leading edge", "structural"),
            ReferencePoint("Left Wingtip", 15.0, -32.5, 6.5,
                          "Left wing tip", "structural"),
            ReferencePoint("Right Wingtip", 15.0, 32.5, 6.5,
                          "Right wing tip", "structural"),
            
            # H2 fuel system
            ReferencePoint("H2 Tank 1 Center", 20.0, 0.0, 10.0,
                          "Forward hydrogen tank center", "systems"),
            ReferencePoint("H2 Tank 2 Center", 28.0, 0.0, 10.0,
                          "Aft hydrogen tank center", "systems"),
            ReferencePoint("H2 Fill Port Left", 18.0, -8.0, 12.0,
                          "Left H2 refueling port", "systems"),
            ReferencePoint("H2 Fill Port Right", 18.0, 8.0, 12.0,
                          "Right H2 refueling port", "systems"),
            
            # Fuel cell locations
            ReferencePoint("Fuel Cell Stack 1", 12.0, -6.0, 8.0,
                          "Left fuel cell stack", "systems"),
            ReferencePoint("Fuel Cell Stack 2", 12.0, 6.0, 8.0,
                          "Right fuel cell stack", "systems"),
            
            # Control surfaces
            ReferencePoint("Elevator Hinge Line", 45.0, 0.0, 8.0,
                          "Elevator hinge centerline", "structural"),
            ReferencePoint("Left Elevon", 40.0, -20.0, 7.0,
                          "Left elevon reference", "structural"),
            ReferencePoint("Right Elevon", 40.0, 20.0, 7.0,
                          "Right elevon reference", "structural"),
            
            # Avionics bay
            ReferencePoint("Avionics Bay Center", 5.0, 0.0, 9.0,
                          "Central avionics compartment", "systems"),
            
            # Cargo compartments
            ReferencePoint("Forward Cargo", 12.0, 0.0, 2.0,
                          "Forward cargo hold", "interface"),
            ReferencePoint("Aft Cargo", 32.0, 0.0, 2.0,
                          "Aft cargo hold", "interface"),
            
            # Engine/propulsion
            ReferencePoint("Left Propulsor", 48.0, -8.0, 7.0,
                          "Left electric propulsor", "systems"),
            ReferencePoint("Right Propulsor", 48.0, 8.0, 7.0,
                          "Right electric propulsor", "systems"),
        ]
        
        return points
    
    def convert_to_xyz(self, station: float, buttline: float, 
                      waterline: float) -> Tuple[float, float, float]:
        """
        Convert aircraft coordinates to Cartesian XYZ
        
        Args:
            station: Fuselage station (positive forward)
            buttline: Buttline (positive right)
            waterline: Waterline (positive up)
            
        Returns:
            (x, y, z) coordinates
        """
        x = station
        y = buttline
        z = waterline
        return (x, y, z)
    
    def convert_from_xyz(self, x: float, y: float, z: float) -> Tuple[float, float, float]:
        """
        Convert Cartesian XYZ to aircraft coordinates
        
        Args:
            x, y, z: Cartesian coordinates
            
        Returns:
            (station, buttline, waterline)
        """
        return (x, y, z)
    
    def get_points_by_category(self, category: str) -> List[ReferencePoint]:
        """Get all reference points of a specific category"""
        return [p for p in self.reference_points if p.category == category]
    
    def visualize_3d(self, save_path: Optional[str] = None, 
                    categories: Optional[List[str]] = None):
        """
        Create 3D visualization of reference points
        
        Args:
            save_path: Optional path to save figure
            categories: Optional list of categories to display (None = all)
        """
        fig = plt.figure(figsize=(15, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Filter points by category if specified
        if categories:
            points_to_plot = [p for p in self.reference_points 
                            if p.category in categories]
        else:
            points_to_plot = self.reference_points
        
        # Category colors
        category_colors = {
            'structural': 'blue',
            'systems': 'red',
            'interface': 'green',
            'general': 'gray'
        }
        
        # Plot reference points
        for point in points_to_plot:
            x, y, z = self.convert_to_xyz(point.station, point.buttline, 
                                         point.waterline)
            color = category_colors.get(point.category, 'gray')
            ax.scatter(x, y, z, c=color, marker='o', s=100, alpha=0.7,
                      label=point.category if point == points_to_plot[0] else "")
        
        # Draw coordinate grid planes
        # XY plane (WL 0 - ground plane)
        xx, yy = np.meshgrid(
            np.linspace(self.fs_min, self.fs_max, 10),
            np.linspace(self.bl_min, self.bl_max, 10)
        )
        ax.plot_surface(xx, yy, np.zeros_like(xx), alpha=0.1, color='gray')
        
        # Draw reference axes
        # FS axis (red)
        ax.plot([self.fs_min, self.fs_max], [0, 0], [0, 0], 
               'r-', linewidth=2, label='FS Axis')
        # BL axis (green)
        ax.plot([0, 0], [self.bl_min, self.bl_max], [0, 0], 
               'g-', linewidth=2, label='BL Axis')
        # WL axis (blue)
        ax.plot([0, 0], [0, 0], [self.wl_min, self.wl_max], 
               'b-', linewidth=2, label='WL Axis')
        
        # Draw aircraft outline (simplified BWB shape)
        self._draw_bwb_outline(ax)
        
        # Labeling
        ax.set_xlabel('Station (FS) [m]', fontsize=12, fontweight='bold')
        ax.set_ylabel('Buttline (BL) [m]', fontsize=12, fontweight='bold')
        ax.set_zlabel('Waterline (WL) [m]', fontsize=12, fontweight='bold')
        ax.set_title('AMPEL360 BWB - Reference System (Station/Buttline/Waterline)',
                    fontsize=14, fontweight='bold')
        
        # Set equal aspect ratio
        ax.set_box_aspect([1, 1, 0.3])
        
        # Remove duplicate legend entries
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), loc='upper right')
        
        ax.grid(True, alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"3D visualization saved to {save_path}")
        else:
            plt.show()
        
        plt.close()
    
    def _draw_bwb_outline(self, ax):
        """Draw simplified BWB outline on 3D plot"""
        # Center body outline (top view projection)
        center_length = 45.0
        center_width = 28.0
        
        # Draw center body
        center_corners = [
            [5, -center_width/2, 0],
            [5, center_width/2, 0],
            [5 + center_length, center_width/2, 0],
            [5 + center_length, -center_width/2, 0],
            [5, -center_width/2, 0]
        ]
        center_array = np.array(center_corners)
        ax.plot(center_array[:, 0], center_array[:, 1], center_array[:, 2],
               'k-', linewidth=1, alpha=0.5)
        
        # Draw wing outline (simplified)
        wing_points_left = [
            [10, -center_width/2, 6],
            [15, -32.5, 6.5],
            [42, -30, 7],
            [45, -12, 7],
            [10, -center_width/2, 6]
        ]
        
        wing_points_right = [
            [10, center_width/2, 6],
            [15, 32.5, 6.5],
            [42, 30, 7],
            [45, 12, 7],
            [10, center_width/2, 6]
        ]
        
        wing_left = np.array(wing_points_left)
        wing_right = np.array(wing_points_right)
        
        ax.plot(wing_left[:, 0], wing_left[:, 1], wing_left[:, 2],
               'k-', linewidth=1, alpha=0.5)
        ax.plot(wing_right[:, 0], wing_right[:, 1], wing_right[:, 2],
               'k-', linewidth=1, alpha=0.5)
    
    def visualize_section_views(self, save_path: Optional[str] = None):
        """
        Create traditional engineering section views (Front, Side, Top)
        
        Args:
            save_path: Optional path to save figure
        """
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Category colors
        category_colors = {
            'structural': 'blue',
            'systems': 'red',
            'interface': 'green',
            'general': 'gray'
        }
        
        # Top view (FS vs BL)
        ax_top = axes[0, 0]
        for point in self.reference_points:
            color = category_colors.get(point.category, 'gray')
            ax_top.scatter(point.station, point.buttline, c=color, 
                          s=80, alpha=0.7, edgecolors='black', linewidth=0.5)
            ax_top.annotate(point.name, (point.station, point.buttline),
                           fontsize=6, alpha=0.6, xytext=(2, 2),
                           textcoords='offset points')
        ax_top.set_xlabel('Station (FS) [m]', fontsize=10)
        ax_top.set_ylabel('Buttline (BL) [m]', fontsize=10)
        ax_top.set_title('Top View', fontsize=12, fontweight='bold')
        ax_top.grid(True, alpha=0.3)
        ax_top.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
        ax_top.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
        ax_top.set_aspect('equal')
        
        # Side view (FS vs WL)
        ax_side = axes[0, 1]
        for point in self.reference_points:
            color = category_colors.get(point.category, 'gray')
            ax_side.scatter(point.station, point.waterline, c=color,
                           s=80, alpha=0.7, edgecolors='black', linewidth=0.5)
            ax_side.annotate(point.name, (point.station, point.waterline),
                            fontsize=6, alpha=0.6, xytext=(2, 2),
                            textcoords='offset points')
        ax_side.set_xlabel('Station (FS) [m]', fontsize=10)
        ax_side.set_ylabel('Waterline (WL) [m]', fontsize=10)
        ax_side.set_title('Side View', fontsize=12, fontweight='bold')
        ax_side.grid(True, alpha=0.3)
        ax_side.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
        ax_side.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
        
        # Front view (BL vs WL)
        ax_front = axes[1, 0]
        for point in self.reference_points:
            color = category_colors.get(point.category, 'gray')
            ax_front.scatter(point.buttline, point.waterline, c=color,
                            s=80, alpha=0.7, edgecolors='black', linewidth=0.5)
            ax_front.annotate(point.name, (point.buttline, point.waterline),
                             fontsize=6, alpha=0.6, xytext=(2, 2),
                             textcoords='offset points')
        ax_front.set_xlabel('Buttline (BL) [m]', fontsize=10)
        ax_front.set_ylabel('Waterline (WL) [m]', fontsize=10)
        ax_front.set_title('Front View', fontsize=12, fontweight='bold')
        ax_front.grid(True, alpha=0.3)
        ax_front.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
        ax_front.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
        ax_front.set_aspect('equal')
        
        # Legend
        ax_legend = axes[1, 1]
        ax_legend.axis('off')
        legend_elements = [plt.Line2D([0], [0], marker='o', color='w',
                                     markerfacecolor=color, markersize=10,
                                     label=category.title())
                          for category, color in category_colors.items()]
        ax_legend.legend(handles=legend_elements, loc='center', fontsize=12,
                        title='Reference Point Categories')
        ax_legend.text(0.5, 0.3, 'AMPEL360 BWB H2 Hy-E Q100\nReference System Visualization',
                      ha='center', va='center', fontsize=14, fontweight='bold',
                      transform=ax_legend.transAxes)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Section views saved to {save_path}")
        else:
            plt.show()
        
        plt.close()
    
    def export_reference_points(self, filepath: str, format: str = 'json'):
        """
        Export reference points to file
        
        Args:
            filepath: Output file path
            format: 'json' or 'csv'
        """
        if format == 'json':
            data = {
                'aircraft': 'AMPEL360 BWB H2 Hy-E Q100',
                'reference_system': 'Station-Buttline-Waterline',
                'datum': {
                    'fs': self.fs_datum,
                    'bl': self.bl_datum,
                    'wl': self.wl_datum
                },
                'points': [
                    {
                        'name': p.name,
                        'station': p.station,
                        'buttline': p.buttline,
                        'waterline': p.waterline,
                        'description': p.description,
                        'category': p.category
                    }
                    for p in self.reference_points
                ]
            }
            
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
                
        elif format == 'csv':
            with open(filepath, 'w') as f:
                f.write("Name,Station,Buttline,Waterline,Description,Category\n")
                for p in self.reference_points:
                    f.write(f'"{p.name}",{p.station},{p.buttline},{p.waterline},'
                          f'"{p.description}",{p.category}\n')
        
        print(f"Reference points exported to {filepath}")
    
    def generate_coordinate_report(self) -> str:
        """Generate text report of reference coordinate system"""
        report = []
        report.append("=" * 80)
        report.append("AMPEL360 BWB H2 Hy-E Q100 - REFERENCE COORDINATE SYSTEM")
        report.append("ATA 02-11-00: AIRCRAFT DIMENSIONS GEOMETRY")
        report.append("=" * 80)
        report.append("")
        
        report.append("COORDINATE SYSTEM DEFINITION:")
        report.append(f"  Station (FS):  Longitudinal axis, positive forward from datum")
        report.append(f"  Buttline (BL): Lateral axis, positive to the right")
        report.append(f"  Waterline (WL): Vertical axis, positive upward")
        report.append("")
        
        report.append("DATUM LOCATIONS:")
        report.append(f"  FS Datum: {self.fs_datum:.2f} m (Nose reference)")
        report.append(f"  BL Datum: {self.bl_datum:.2f} m (Centerline)")
        report.append(f"  WL Datum: {self.wl_datum:.2f} m (Ground line, level attitude)")
        report.append("")
        
        report.append("AIRCRAFT ENVELOPE:")
        report.append(f"  FS Range: {self.fs_min:.2f} to {self.fs_max:.2f} m")
        report.append(f"  BL Range: {self.bl_min:.2f} to {self.bl_max:.2f} m")
        report.append(f"  WL Range: {self.wl_min:.2f} to {self.wl_max:.2f} m")
        report.append("")
        
        # Group by category
        report.append("REFERENCE POINTS BY CATEGORY:")
        report.append("-" * 80)
        
        categories = set(p.category for p in self.reference_points)
        for category in sorted(categories):
            report.append(f"\n{category.upper()}:")
            points = self.get_points_by_category(category)
            
            for point in sorted(points, key=lambda p: p.station):
                report.append(f"  {point.name:<30} FS {point.station:>7.2f}  "
                            f"BL {point.buttline:>7.2f}  WL {point.waterline:>7.2f}")
                if point.description:
                    report.append(f"    → {point.description}")
        
        report.append("")
        report.append("=" * 80)
        
        return "\n".join(report)


def main():
    """Main function for tool demonstration"""
    print("Station/Buttline/Waterline Visualizer v1.0")
    print("ATA 02-11-00: AIRCRAFT DIMENSIONS GEOMETRY\n")
    
    # Initialize reference system
    ref_system = AircraftReferenceSystem()
    
    # Generate report
    report = ref_system.generate_coordinate_report()
    print(report)
    
    # Generate visualizations
    print("\nGenerating 3D visualization...")
    ref_system.visualize_3d(save_path="Reference_System_3D.png")
    
    print("\nGenerating section views...")
    ref_system.visualize_section_views(save_path="Reference_System_Sections.png")
    
    # Export data
    print("\nExporting reference points...")
    ref_system.export_reference_points("Reference_Points.json", format='json')
    ref_system.export_reference_points("Reference_Points.csv", format='csv')
    
    print("\nVisualization and export complete!")


if __name__ == "__main__":
    main()
