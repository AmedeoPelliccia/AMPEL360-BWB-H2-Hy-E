#!/usr/bin/env python3
"""
Weight Rollup Tool for AMPEL360 Fuselage Structure
Calculates and summarizes weight distribution across fuselage components.

Usage:
    python weight_rollup.py --format table
    python weight_rollup.py --format csv --output weights.csv
"""

import argparse
import csv
from typing import Dict, List
from pathlib import Path


class WeightRollup:
    """Calculate weight rollup for fuselage structure."""
    
    def __init__(self):
        """Initialize with component weight database."""
        self.weights = {
            '53-10-00': {
                'name': 'Forward Fuselage',
                'total': 2450,
                'breakdown': {
                    '53-10-01': {'name': 'Nose Cone', 'weight': 125},
                    '53-10-02': {'name': 'Cockpit Structure', 'weight': 850},
                    '53-10-03': {'name': 'Forward Pressure Bulkhead', 'weight': 420},
                    '53-10-04': {'name': 'Avionics Bay', 'weight': 1055}
                }
            },
            '53-20-00': {
                'name': 'Center Fuselage BWB',
                'total': 8900,
                'breakdown': {
                    '53-20-01': {'name': 'Upper Passenger Deck', 'weight': 1850},
                    '53-20-02': {'name': 'Lower Cargo Deck', 'weight': 1250},
                    '53-20-03': {'name': 'BWB Outer Skin Panels', 'weight': 2100},
                    '53-20-04': {'name': 'Circumferential Frames', 'weight': 980},
                    '53-20-05': {'name': 'Longitudinal Stringers', 'weight': 750},
                    '53-20-06': {'name': 'Keel Beam Structure', 'weight': 1320},
                    '53-20-07': {'name': 'Wing Box Integration', 'weight': 450},
                    '53-20-08': {'name': 'Pressure Deck Floor', 'weight': 200}
                }
            },
            '53-30-00': {
                'name': 'Aft Fuselage',
                'total': 1850,
                'breakdown': {
                    '53-30-01': {'name': 'Aft Pressure Bulkhead', 'weight': 380},
                    '53-30-02': {'name': 'Tail Cone Structure', 'weight': 420},
                    '53-30-03': {'name': 'APU Compartment', 'weight': 520},
                    '53-30-04': {'name': 'CO2 Capture Bay', 'weight': 350},
                    '53-30-05': {'name': 'Aft Equipment Bay', 'weight': 180}
                }
            },
            '53-40-00': {
                'name': 'H2 Tank Integration',
                'total': 1200,
                'breakdown': {
                    '53-40-01': {'name': 'Forward LH2 Tank Bay', 'weight': 280},
                    '53-40-02': {'name': 'Aft LH2 Tank Bay', 'weight': 280},
                    '53-40-03': {'name': 'Tank Support Cradles', 'weight': 320},
                    '53-40-04': {'name': 'Thermal Insulation System', 'weight': 180},
                    '53-40-05': {'name': 'Boiloff Management', 'weight': 85},
                    '53-40-06': {'name': 'Emergency Venting', 'weight': 55}
                }
            },
            '53-50-00': {
                'name': 'BWB Blend Structure',
                'total': 2100,
                'breakdown': {
                    '53-50-01': {'name': 'Center Wing Blend', 'weight': 850},
                    '53-50-02': {'name': 'Outer Wing Blend', 'weight': 680},
                    '53-50-03': {'name': 'Load Transfer Structure', 'weight': 420},
                    '53-50-04': {'name': 'Blend Fairings', 'weight': 110},
                    '53-50-05': {'name': 'Inspection Panels', 'weight': 40}
                }
            },
            '53-60-00': {
                'name': 'Propulsion Integration',
                'total': 650,
                'breakdown': {
                    '53-60-01': {'name': 'Engine Pylon Interface', 'weight': 280},
                    '53-60-02': {'name': 'Nacelle Attachment', 'weight': 150},
                    '53-60-03': {'name': 'Thrust Structure', 'weight': 120},
                    '53-60-04': {'name': 'Vibration Isolation', 'weight': 65},
                    '53-60-05': {'name': 'Access Platforms', 'weight': 35}
                }
            },
            '53-70-00': {
                'name': 'Landing Gear Bays',
                'total': 580,
                'breakdown': {
                    '53-70-01': {'name': 'Nose Gear Bay', 'weight': 120},
                    '53-70-02': {'name': 'Main Gear Bay Left', 'weight': 180},
                    '53-70-03': {'name': 'Main Gear Bay Right', 'weight': 180},
                    '53-70-04': {'name': 'Bay Doors', 'weight': 75},
                    '53-70-05': {'name': 'Wheel Wells', 'weight': 25}
                }
            },
            '53-80-00': {
                'name': 'Structural Joints',
                'total': 320,
                'breakdown': {
                    '53-80-01': {'name': 'Major Splice Joints', 'weight': 140},
                    '53-80-02': {'name': 'Circumferential Joints', 'weight': 85},
                    '53-80-03': {'name': 'Longitudinal Joints', 'weight': 55},
                    '53-80-04': {'name': 'Access Cutouts', 'weight': 25},
                    '53-80-05': {'name': 'Repair Schemes', 'weight': 15}
                }
            },
            '53-90-00': {
                'name': 'Monitoring Systems',
                'total': 150,
                'breakdown': {
                    '53-90-01': {'name': 'Strain Gauge Network', 'weight': 35},
                    '53-90-02': {'name': 'Fiber Optic Sensors', 'weight': 45},
                    '53-90-03': {'name': 'Acoustic Emission', 'weight': 28},
                    '53-90-04': {'name': 'CAOS Integration', 'weight': 22},
                    '53-90-05': {'name': 'Structural Health Dashboard', 'weight': 20}
                }
            }
        }
    
    def calculate_total_weight(self) -> float:
        """Calculate total fuselage weight."""
        total = sum(section['total'] for section in self.weights.values())
        return total
    
    def calculate_section_weight(self, section_code: str) -> float:
        """
        Calculate weight for a specific section.
        
        Args:
            section_code: ATA section code (e.g., '53-10-00')
            
        Returns:
            Section weight in kg
        """
        if section_code not in self.weights:
            raise ValueError(f"Unknown section code: {section_code}")
        
        return self.weights[section_code]['total']
    
    def get_weight_breakdown(self, section_code: str) -> Dict:
        """
        Get detailed weight breakdown for a section.
        
        Args:
            section_code: ATA section code
            
        Returns:
            Dictionary with component weights
        """
        if section_code not in self.weights:
            raise ValueError(f"Unknown section code: {section_code}")
        
        return self.weights[section_code]['breakdown']
    
    def generate_weight_report(self) -> str:
        """
        Generate formatted weight report.
        
        Returns:
            Formatted string report
        """
        report = []
        report.append("\n" + "="*80)
        report.append("AMPEL360 FUSELAGE WEIGHT ROLLUP (ATA 53)")
        report.append("="*80)
        
        total_weight = 0
        
        for section_code in sorted(self.weights.keys()):
            section = self.weights[section_code]
            section_weight = section['total']
            total_weight += section_weight
            
            report.append(f"\n{section_code} - {section['name']}")
            report.append("-"*80)
            
            for comp_code, comp_data in sorted(section['breakdown'].items()):
                comp_name = comp_data['name']
                comp_weight = comp_data['weight']
                percentage = (comp_weight / section_weight) * 100
                report.append(
                    f"  {comp_code}: {comp_name:<40} {comp_weight:>6.1f} kg "
                    f"({percentage:>5.1f}%)"
                )
            
            report.append("-"*80)
            report.append(f"  Section Total: {section_weight:>50.1f} kg\n")
        
        report.append("="*80)
        report.append(f"TOTAL FUSELAGE STRUCTURE WEIGHT: {total_weight:>30.1f} kg")
        report.append("="*80)
        report.append(f"\nTarget Weight: 18,000 kg")
        report.append(f"Actual Weight: {total_weight:,.1f} kg")
        
        delta = total_weight - 18000
        status = "OVER" if delta > 0 else "UNDER"
        report.append(f"Delta: {status} by {abs(delta):,.1f} kg ({abs(delta)/180:.1f}%)")
        
        report.append("\n" + "="*80 + "\n")
        
        return "\n".join(report)
    
    def export_to_csv(self, filename: str):
        """
        Export weight data to CSV file.
        
        Args:
            filename: Output CSV filename
        """
        rows = [['ATA_Code', 'Component_Name', 'Weight_kg', 'Section', 'Section_Total_kg']]
        
        for section_code in sorted(self.weights.keys()):
            section = self.weights[section_code]
            section_name = section['name']
            section_total = section['total']
            
            for comp_code, comp_data in sorted(section['breakdown'].items()):
                rows.append([
                    comp_code,
                    comp_data['name'],
                    comp_data['weight'],
                    section_name,
                    section_total
                ])
        
        # Add total row
        total_weight = self.calculate_total_weight()
        rows.append(['TOTAL', 'All Components', total_weight, '', ''])
        
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        
        print(f"Weight data exported to {filename}")
    
    def generate_weight_chart_data(self) -> List[Dict]:
        """
        Generate data for weight distribution chart.
        
        Returns:
            List of dictionaries with section weights
        """
        chart_data = []
        
        for section_code in sorted(self.weights.keys()):
            section = self.weights[section_code]
            chart_data.append({
                'section_code': section_code,
                'section_name': section['name'],
                'weight_kg': section['total'],
                'percentage': (section['total'] / self.calculate_total_weight()) * 100
            })
        
        return chart_data
    
    def print_weight_distribution(self):
        """Print weight distribution as percentage bar chart."""
        print("\n" + "="*80)
        print("WEIGHT DISTRIBUTION BY SECTION")
        print("="*80)
        
        chart_data = self.generate_weight_chart_data()
        
        for item in chart_data:
            bar_length = int(item['percentage'] / 2)  # Scale to fit in 50 chars
            bar = '█' * bar_length
            
            print(f"{item['section_code']}: {bar:<50} "
                  f"{item['percentage']:>5.1f}% ({item['weight_kg']:>6.0f} kg)")
        
        print("="*80 + "\n")


def main():
    """Main function for command-line interface."""
    parser = argparse.ArgumentParser(
        description='Weight rollup tool for AMPEL360 fuselage structure'
    )
    parser.add_argument(
        '--format',
        type=str,
        choices=['table', 'csv', 'chart'],
        default='table',
        help='Output format'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='fuselage_weights.csv',
        help='Output filename for CSV format'
    )
    parser.add_argument(
        '--section',
        type=str,
        help='Show details for specific section (e.g., 53-10-00)'
    )
    
    args = parser.parse_args()
    
    rollup = WeightRollup()
    
    if args.section:
        # Show specific section details
        try:
            section_weight = rollup.calculate_section_weight(args.section)
            breakdown = rollup.get_weight_breakdown(args.section)
            
            print(f"\n{args.section} - {rollup.weights[args.section]['name']}")
            print("-"*60)
            for comp_code, comp_data in sorted(breakdown.items()):
                print(f"{comp_code}: {comp_data['name']:<40} {comp_data['weight']:>6.1f} kg")
            print("-"*60)
            print(f"Section Total: {section_weight:>40.1f} kg\n")
        except ValueError as e:
            print(f"Error: {e}")
    elif args.format == 'table':
        print(rollup.generate_weight_report())
    elif args.format == 'csv':
        rollup.export_to_csv(args.output)
    elif args.format == 'chart':
        rollup.print_weight_distribution()


if __name__ == '__main__':
    main()
