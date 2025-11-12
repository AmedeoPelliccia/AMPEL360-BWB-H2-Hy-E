#!/usr/bin/env python3
"""
Requirement Tracer for AMPEL360 Fuselage Structure
Traces requirements across the ATA 53 structure and generates traceability reports.

Usage:
    python requirement_tracer.py --component 53-10-01
    python requirement_tracer.py --category STRUCTURAL --export trace_matrix.csv
"""

import argparse
import csv
import os
from pathlib import Path
from typing import Dict, List, Set


class RequirementTracer:
    """Trace requirements across fuselage components."""
    
    # Requirement categories
    CATEGORIES = [
        'RQ-STRUCTURAL',
        'RQ-FUNCTIONAL',
        'RQ-INTERFACE',
        'RQ-SAFETY',
        'RQ-PERFORMANCE',
        'RQ-OPERATIONAL',
        'RQ-MAINTENANCE',
        'RQ-CAOS'
    ]
    
    def __init__(self, base_path: str = None):
        """
        Initialize requirement tracer.
        
        Args:
            base_path: Base path to ATA_53-FUSELAGE directory
        """
        if base_path is None:
            # Try to find the ATA_53-FUSELAGE directory
            current = Path(__file__).parent.parent
            self.base_path = current
        else:
            self.base_path = Path(base_path)
        
        self.requirements = {}
        self.components = []
    
    def scan_components(self) -> List[str]:
        """
        Scan for all components with requirement folders.
        
        Returns:
            List of component codes
        """
        components = []
        
        # Scan all subdirectories
        for item in self.base_path.rglob('03_REQUIREMENTS'):
            # Extract component code from path
            parts = item.parts
            for part in parts:
                # Look for ATA code pattern (e.g., 53-10-01)
                if part.startswith('53-') and '-' in part[3:]:
                    components.append(part)
                    break
        
        self.components = sorted(set(components))
        return self.components
    
    def get_requirement_files(self, component_code: str, category: str) -> List[str]:
        """
        Get requirement files for a component and category.
        
        Args:
            component_code: ATA component code
            category: Requirement category
            
        Returns:
            List of requirement file names
        """
        req_files = []
        
        # Search for the component directory
        for comp_dir in self.base_path.rglob(component_code):
            req_path = comp_dir / '03_REQUIREMENTS' / category
            if req_path.exists():
                # List all files in the category directory
                for file in req_path.iterdir():
                    if file.is_file() and file.name.startswith('RQ-'):
                        req_files.append(file.name)
        
        return sorted(req_files)
    
    def parse_requirement_id(self, filename: str) -> Dict:
        """
        Parse requirement ID from filename.
        
        Args:
            filename: Requirement filename (e.g., RQ-53-10-01-001_Ultimate_Load_3.75g)
            
        Returns:
            Dictionary with parsed requirement info
        """
        # Remove file extension if present
        name = filename.replace('.md', '').replace('.txt', '')
        
        parts = name.split('_', 1)
        req_id = parts[0]
        
        req_title = parts[1] if len(parts) > 1 else ''
        
        # Parse requirement ID
        id_parts = req_id.split('-')
        
        return {
            'requirement_id': req_id,
            'ata_chapter': id_parts[1] if len(id_parts) > 1 else '',
            'subsystem': id_parts[2] if len(id_parts) > 2 else '',
            'component': id_parts[3] if len(id_parts) > 3 else '',
            'number': id_parts[4] if len(id_parts) > 4 else '',
            'title': req_title.replace('_', ' ')
        }
    
    def build_requirement_database(self):
        """Build database of all requirements in the structure."""
        self.scan_components()
        
        for component in self.components:
            self.requirements[component] = {}
            
            for category in self.CATEGORIES:
                req_files = self.get_requirement_files(component, category)
                self.requirements[component][category] = []
                
                for req_file in req_files:
                    req_info = self.parse_requirement_id(req_file)
                    req_info['category'] = category
                    req_info['component'] = component
                    req_info['filename'] = req_file
                    self.requirements[component][category].append(req_info)
    
    def count_requirements_by_category(self) -> Dict[str, int]:
        """
        Count requirements by category across all components.
        
        Returns:
            Dictionary mapping category to count
        """
        counts = {cat: 0 for cat in self.CATEGORIES}
        
        for component in self.requirements:
            for category in self.requirements[component]:
                counts[category] += len(self.requirements[component][category])
        
        return counts
    
    def count_requirements_by_component(self) -> Dict[str, int]:
        """
        Count requirements by component.
        
        Returns:
            Dictionary mapping component to count
        """
        counts = {}
        
        for component in self.requirements:
            total = sum(len(self.requirements[component][cat]) 
                       for cat in self.requirements[component])
            counts[component] = total
        
        return counts
    
    def generate_traceability_matrix(self) -> List[List[str]]:
        """
        Generate traceability matrix.
        
        Returns:
            2D list representing the traceability matrix
        """
        # Header row
        matrix = [['Component'] + self.CATEGORIES + ['Total']]
        
        # Data rows
        for component in sorted(self.requirements.keys()):
            row = [component]
            total = 0
            
            for category in self.CATEGORIES:
                count = len(self.requirements[component].get(category, []))
                row.append(str(count))
                total += count
            
            row.append(str(total))
            matrix.append(row)
        
        # Total row
        totals_row = ['TOTAL']
        grand_total = 0
        
        for category in self.CATEGORIES:
            cat_total = sum(len(self.requirements[comp].get(category, [])) 
                          for comp in self.requirements)
            totals_row.append(str(cat_total))
            grand_total += cat_total
        
        totals_row.append(str(grand_total))
        matrix.append(totals_row)
        
        return matrix
    
    def export_traceability_matrix(self, filename: str):
        """
        Export traceability matrix to CSV.
        
        Args:
            filename: Output CSV filename
        """
        matrix = self.generate_traceability_matrix()
        
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(matrix)
        
        print(f"Traceability matrix exported to {filename}")
    
    def print_requirement_summary(self):
        """Print summary of requirements."""
        print("\n" + "="*80)
        print("REQUIREMENT TRACEABILITY SUMMARY - ATA 53 FUSELAGE")
        print("="*80)
        
        # Count by category
        cat_counts = self.count_requirements_by_category()
        
        print("\nRequirements by Category:")
        print("-"*80)
        total_reqs = 0
        for category in self.CATEGORIES:
            count = cat_counts[category]
            total_reqs += count
            print(f"  {category:<30} {count:>6} requirements")
        print("-"*80)
        print(f"  {'TOTAL':<30} {total_reqs:>6} requirements")
        
        # Count by component
        comp_counts = self.count_requirements_by_component()
        
        print("\nRequirements by Component (Top 10):")
        print("-"*80)
        sorted_comps = sorted(comp_counts.items(), key=lambda x: x[1], reverse=True)
        for component, count in sorted_comps[:10]:
            print(f"  {component:<30} {count:>6} requirements")
        
        print("\n" + "="*80 + "\n")
    
    def print_component_requirements(self, component_code: str):
        """
        Print detailed requirements for a specific component.
        
        Args:
            component_code: ATA component code
        """
        if component_code not in self.requirements:
            print(f"Component {component_code} not found in database.")
            return
        
        print("\n" + "="*80)
        print(f"REQUIREMENTS FOR COMPONENT: {component_code}")
        print("="*80)
        
        for category in self.CATEGORIES:
            reqs = self.requirements[component_code].get(category, [])
            
            if reqs:
                print(f"\n{category}:")
                print("-"*80)
                
                for req in reqs:
                    print(f"  {req['requirement_id']}: {req['title']}")
        
        print("\n" + "="*80 + "\n")
    
    def find_requirements_by_keyword(self, keyword: str) -> List[Dict]:
        """
        Find requirements containing a keyword.
        
        Args:
            keyword: Search keyword
            
        Returns:
            List of matching requirements
        """
        matches = []
        
        for component in self.requirements:
            for category in self.requirements[component]:
                for req in self.requirements[component][category]:
                    if keyword.lower() in req['title'].lower():
                        matches.append(req)
        
        return matches
    
    def generate_sample_requirements(self, component_code: str):
        """
        Generate sample requirement structure for a component.
        
        Args:
            component_code: ATA component code (e.g., '53-10-01')
        """
        print(f"\nSample requirements for {component_code}:")
        print("="*70)
        
        # Parse component code
        parts = component_code.split('-')
        ata = parts[0]
        subsys = parts[1]
        comp = parts[2]
        
        # Generate sample requirements for each category
        samples = {
            'RQ-STRUCTURAL': [
                f'RQ-{ata}-{subsys}-{comp}-001_Ultimate_Load_3.75g',
                f'RQ-{ata}-{subsys}-{comp}-002_Limit_Load_2.5g',
                f'RQ-{ata}-{subsys}-{comp}-003_Pressure_Load_8.5psi'
            ],
            'RQ-FUNCTIONAL': [
                f'RQ-{ata}-{subsys}-{comp}-020_Aerodynamic_Shape_Maintenance',
                f'RQ-{ata}-{subsys}-{comp}-021_Pressure_Containment'
            ],
            'RQ-INTERFACE': [
                f'RQ-{ata}-{subsys}-{comp}-070_Forward_Bulkhead_Interface',
                f'RQ-{ata}-{subsys}-{comp}-071_Mounting_Interface'
            ],
            'RQ-SAFETY': [
                f'RQ-{ata}-{subsys}-{comp}-100_Fail_Safe_Load_Path',
                f'RQ-{ata}-{subsys}-{comp}-101_Lightning_Protection'
            ],
            'RQ-PERFORMANCE': [
                f'RQ-{ata}-{subsys}-{comp}-050_Weight_Target',
                f'RQ-{ata}-{subsys}-{comp}-051_Natural_Frequency'
            ]
        }
        
        for category, reqs in samples.items():
            print(f"\n{category}:")
            for req in reqs:
                print(f"  - {req}")
        
        print("\n" + "="*70 + "\n")


def main():
    """Main function for command-line interface."""
    parser = argparse.ArgumentParser(
        description='Requirement tracer for AMPEL360 fuselage structure'
    )
    parser.add_argument(
        '--component',
        type=str,
        help='Show requirements for specific component (e.g., 53-10-01)'
    )
    parser.add_argument(
        '--category',
        type=str,
        choices=RequirementTracer.CATEGORIES,
        help='Filter by requirement category'
    )
    parser.add_argument(
        '--export',
        type=str,
        help='Export traceability matrix to CSV file'
    )
    parser.add_argument(
        '--search',
        type=str,
        help='Search requirements by keyword'
    )
    parser.add_argument(
        '--generate-samples',
        type=str,
        help='Generate sample requirement structure for component'
    )
    
    args = parser.parse_args()
    
    tracer = RequirementTracer()
    tracer.build_requirement_database()
    
    if args.generate_samples:
        tracer.generate_sample_requirements(args.generate_samples)
    elif args.component:
        tracer.print_component_requirements(args.component)
    elif args.search:
        matches = tracer.find_requirements_by_keyword(args.search)
        print(f"\nFound {len(matches)} requirements matching '{args.search}':")
        for req in matches:
            print(f"  {req['component']} / {req['category']}: "
                  f"{req['requirement_id']} - {req['title']}")
        print()
    elif args.export:
        tracer.export_traceability_matrix(args.export)
    else:
        tracer.print_requirement_summary()


if __name__ == '__main__':
    main()
