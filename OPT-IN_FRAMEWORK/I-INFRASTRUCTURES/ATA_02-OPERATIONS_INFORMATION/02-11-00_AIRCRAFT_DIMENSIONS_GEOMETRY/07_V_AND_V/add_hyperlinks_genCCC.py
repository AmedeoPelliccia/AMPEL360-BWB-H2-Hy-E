#!/usr/bin/env python3
"""
GenCCC: Generative Chain of Contextualized Content
Adds hyperlinks to cross-references and generates missing referenced content

Author: COPILOT Agent prompted by Amedeo Pelliccia
Date: 2025-11-11
Version: 1.0
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set

class GenCCC:
    """Generative Chain of Contextualized Content processor"""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.v_and_v_path = self.base_path
        self.project_root = self.base_path.parent.parent.parent.parent.parent
        self.cross_refs_found = []
        self.missing_content = set()
        
    def find_all_cross_references(self) -> List[Dict]:
        """Scan all markdown files for cross-references"""
        print("Scanning for cross-references...")
        
        patterns = {
            'verification_doc': (r'VER-02-11-(\d{3})', self._resolve_ver_path),
            'validation_doc': (r'VAL-02-11-(\d{3})', self._resolve_val_path),
            'requirement': (r'REQ-02-11-(\d{3})', self._resolve_req_path),
            'csv_file': (r'([\w_]+\.csv)', self._resolve_csv_path),
            'json_file': (r'(baseline_dimensions\.json)', self._resolve_json_path),
        }
        
        for md_file in self.v_and_v_path.rglob('*.md'):
            if md_file.name == 'Cross_Reference_Report.md':
                continue
                
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                
                for line_num, line in enumerate(lines, 1):
                    for ref_type, (pattern, resolver) in patterns.items():
                        for match in re.finditer(pattern, line):
                            # Skip if already a markdown link
                            if self._is_already_linked(line, match.start()):
                                continue
                                
                            ref_text = match.group(0)
                            target_path = resolver(match, md_file)
                            
                            self.cross_refs_found.append({
                                'file': md_file,
                                'line_num': line_num,
                                'line': line,
                                'ref_type': ref_type,
                                'ref_text': ref_text,
                                'target_path': target_path,
                                'exists': target_path.exists() if target_path else False
                            })
                            
                            if target_path and not target_path.exists():
                                self.missing_content.add(target_path)
        
        print(f"Found {len(self.cross_refs_found)} cross-references")
        print(f"Identified {len(self.missing_content)} missing files")
        return self.cross_refs_found
    
    def _is_already_linked(self, line: str, pos: int) -> bool:
        """Check if reference is already in a markdown link"""
        # Look backwards for '[' and forwards for ']('
        before = line[max(0, pos-20):pos]
        after = line[pos:min(len(line), pos+50)]
        return '[' in before and '](' in after
    
    def _resolve_ver_path(self, match, source_file: Path) -> Path:
        """Resolve VER document path"""
        ver_num = match.group(1)
        
        # Determine which subdirectory based on number
        if ver_num in ['001', '002', '003', '004', '005']:
            subdir = 'DIMENSION_VERIFICATION'
        elif ver_num in ['201', '202', '203']:
            subdir = 'CLEARANCE_VERIFICATION'
        elif ver_num in ['301', '302']:
            subdir = 'COORDINATE_SYSTEM_VALIDATION'
        elif ver_num in ['401', '402']:
            subdir = 'COMPLIANCE_VERIFICATION'
        else:
            return None
        
        filename = f"VER-02-11-{ver_num}_*.md"
        target_dir = self.v_and_v_path / subdir
        matches = list(target_dir.glob(filename))
        return matches[0] if matches else target_dir / f"VER-02-11-{ver_num}.md"
    
    def _resolve_val_path(self, match, source_file: Path) -> Path:
        """Resolve VAL document path"""
        val_num = match.group(1)
        filename = f"VAL-02-11-{val_num}_*.md"
        target_dir = self.v_and_v_path / 'GEOMETRY_VALIDATION'
        matches = list(target_dir.glob(filename))
        return matches[0] if matches else target_dir / f"VAL-02-11-{val_num}.md"
    
    def _resolve_req_path(self, match, source_file: Path) -> Path:
        """Resolve requirement path"""
        # Requirements are in ../03_REQUIREMENTS/
        req_dir = self.v_and_v_path.parent / '03_REQUIREMENTS'
        
        # Map requirement numbers to files
        req_num = int(match.group(1))
        if req_num <= 6:
            return req_dir / 'Dimensional_Requirements.csv'
        elif req_num <= 12:
            return req_dir / 'BWB_Geometry_Requirements.csv'
        elif req_num <= 18:
            return req_dir / 'Ground_Clearance_Requirements.csv'
        elif req_num <= 24:
            return req_dir / 'Reference_System_Requirements.csv'
        elif req_num <= 30:
            return req_dir / 'Airport_Compatibility_Requirements.csv'
        else:
            return req_dir / 'Tolerance_Requirements.csv'
    
    def _resolve_csv_path(self, match, source_file: Path) -> Path:
        """Resolve CSV file path"""
        csv_name = match.group(1)
        
        # Common CSV locations
        locations = [
            self.v_and_v_path.parent / '01_OVERVIEW' / 'PRINCIPAL_DIMENSIONS' / csv_name,
            self.v_and_v_path.parent / '01_OVERVIEW' / 'TABLES' / csv_name,
            self.v_and_v_path.parent / '01_OVERVIEW' / 'BWB_GEOMETRY' / csv_name,
            self.v_and_v_path.parent / '03_REQUIREMENTS' / csv_name,
            # Within V&V structure
            source_file.parent / csv_name,
        ]
        
        for loc in locations:
            if loc.exists():
                return loc
        
        # Default: assume it's in the same directory or TABLES
        return self.v_and_v_path.parent / '01_OVERVIEW' / 'TABLES' / csv_name
    
    def _resolve_json_path(self, match, source_file: Path) -> Path:
        """Resolve JSON file path"""
        return self.v_and_v_path.parent / '01_OVERVIEW' / 'baseline_dimensions.json'
    
    def add_hyperlinks_to_file(self, file_path: Path, dry_run: bool = True) -> int:
        """Add hyperlinks to a single markdown file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = 0
        
        # Get all cross-refs for this file
        file_refs = [r for r in self.cross_refs_found if r['file'] == file_path]
        
        # Sort by position (reverse to maintain positions during replacement)
        file_refs.sort(key=lambda x: x['line_num'], reverse=True)
        
        for ref in file_refs:
            if ref['exists']:
                # Calculate relative path
                rel_path = os.path.relpath(ref['target_path'], file_path.parent)
                
                # Create markdown link
                link = f"[{ref['ref_text']}]({rel_path})"
                
                # Replace in content (be careful with multiple occurrences)
                # Use word boundaries to avoid partial matches
                pattern = r'\b' + re.escape(ref['ref_text']) + r'\b'
                
                # Only replace if not already a link
                if link not in content:
                    content = re.sub(pattern, link, content, count=1)
                    changes += 1
        
        if changes > 0 and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated {file_path.name}: {changes} links added")
        elif changes > 0:
            print(f"  Would update {file_path.name}: {changes} links")
        
        return changes
    
    def generate_missing_content(self, dry_run: bool = True) -> Dict[str, str]:
        """Generate missing referenced files using GenCCC"""
        generated = {}
        
        for missing_path in sorted(self.missing_content):
            if missing_path.suffix == '.csv':
                content = self._generate_csv_template(missing_path)
            elif missing_path.suffix == '.md':
                content = self._generate_md_template(missing_path)
            else:
                continue
            
            generated[str(missing_path)] = content
            
            if not dry_run:
                missing_path.parent.mkdir(parents=True, exist_ok=True)
                with open(missing_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Generated {missing_path}")
            else:
                print(f"  Would generate {missing_path}")
        
        return generated
    
    def _generate_csv_template(self, path: Path) -> str:
        """Generate contextualized CSV template based on filename and usage"""
        filename = path.name
        
        if 'Dimensional_Requirements' in filename:
            return self._gen_dimensional_requirements_csv()
        elif 'BWB_Geometry_Requirements' in filename:
            return self._gen_bwb_geometry_requirements_csv()
        elif 'Ground_Clearance_Requirements' in filename:
            return self._gen_ground_clearance_requirements_csv()
        elif 'Reference_System_Requirements' in filename:
            return self._gen_reference_system_requirements_csv()
        elif 'Airport_Compatibility_Requirements' in filename:
            return self._gen_airport_compatibility_requirements_csv()
        elif 'Tolerance_Requirements' in filename:
            return self._gen_tolerance_requirements_csv()
        else:
            return self._gen_generic_csv()
    
    def _gen_dimensional_requirements_csv(self) -> str:
        return """Requirement_ID,Description,Parameter,Value,Unit,Tolerance,Source,Verification_Method,Priority
REQ-02-11-001,Wingspan Specification,Wingspan,52.0,m,±0.1,Principal_Dimensions_Table.csv,VER-02-11-001,High
REQ-02-11-002,Overall Length Specification,Overall_Length,38.2,m,±0.1,Principal_Dimensions_Table.csv,VER-02-11-002,High
REQ-02-11-003,Overall Height Specification,Overall_Height,14.5,m,±0.05,Principal_Dimensions_Table.csv,VER-02-11-003,High
REQ-02-11-004,Center Body Width Specification,Center_Body_Width,38.0,m,±0.1,Principal_Dimensions_Table.csv,VER-02-11-004,High
REQ-02-11-005,Wing Area Specification,Wing_Area,845,m²,±5,Geometry_Parameters.csv,VAL-02-11-101,High
REQ-02-11-006,ICAO Code E Compliance,Wingspan_Range,52-65,m,—,ICAO_Annex_14,VER-02-11-401,High
"""
    
    def _gen_bwb_geometry_requirements_csv(self) -> str:
        return """Requirement_ID,Description,Parameter,Value,Unit,Tolerance,Source,Verification_Method,Priority
REQ-02-11-007,Wing Area Requirement,Wing_Area,845,m²,±5,Design_Specification,VAL-02-11-101,High
REQ-02-11-008,Aspect Ratio Requirement,Aspect_Ratio,3.2,—,±0.05,Design_Specification,VAL-02-11-101,High
REQ-02-11-009,Wing Chord Distribution,Taper_Ratio,0.1,—,±0.01,Design_Specification,VAL-02-11-103,Medium
REQ-02-11-010,Wing Sweep Angles,LE_Sweep,37,deg,±0.5,Design_Specification,VAL-02-11-103,Medium
REQ-02-11-011,Airfoil Thickness Ratio,Root_t_c,0.18,—,±0.01,Design_Specification,VAL-02-11-102,Medium
REQ-02-11-012,Center Body Depth,Max_Depth,4.2,m,±0.05,Design_Specification,VAL-02-11-104,High
"""
    
    def _gen_ground_clearance_requirements_csv(self) -> str:
        return """Requirement_ID,Description,Location,Min_Clearance_m,Condition,Verification_Method,Priority
REQ-02-11-013,Minimum Ground Clearance,Belly_Min,1.8,MTOW_Level,VER-02-11-201,Critical
REQ-02-11-014,Tail Strike Angle Limit,Aft_Body,14,deg,Max_Rotation,VER-02-11-201,Critical
REQ-02-11-015,Wingtip Ground Clearance,Wingtip,1.2,MTOW_Fueled,VER-02-11-202,High
REQ-02-11-016,Maximum Wingtip Droop,Wingtip,0.15,m,Max_Fuel,VER-02-11-202,High
REQ-02-11-017,Engine Intake Clearance,Engine_Intake,2.8,Ground_Ops,VER-02-11-203,Critical
REQ-02-11-018,Door Sill Height,Passenger_Door,4.3,Boarding,VER-02-11-203,High
"""
    
    def _gen_reference_system_requirements_csv(self) -> str:
        return """Requirement_ID,Description,System,Definition,Verification_Method,Priority
REQ-02-11-019,Body Axis System Implementation,Body_Axis,X_Forward_Y_Starboard_Z_Down,VER-02-11-301,High
REQ-02-11-020,Coordinate System Consistency,STA_BL_WL,All_Documents_Consistent,VER-02-11-302,High
REQ-02-11-021,Traceability Requirements,Data_Consistency,Traceable_Across_All_Docs,VER-02-11-402,High
REQ-02-11-022,Station System Implementation,Station,Longitudinal_Positions,VER-02-11-301,Medium
REQ-02-11-023,Buttline System Implementation,Buttline,Lateral_Positions,VER-02-11-301,Medium
REQ-02-11-024,Waterline System Implementation,Waterline,Vertical_Positions,VER-02-11-301,Medium
"""
    
    def _gen_airport_compatibility_requirements_csv(self) -> str:
        return """Requirement_ID,Description,Parameter,Requirement,Source,Verification_Method,Priority
REQ-02-11-025,ICAO Code E Wingspan,Wingspan,52-65_m,ICAO_Annex_14,VER-02-11-401,Critical
REQ-02-11-026,Taxiway Width Compatibility,Taxiway_Width,23_m_Code_E,ICAO_Annex_14,VER-02-11-401,High
REQ-02-11-027,Gate Compatibility,Gate_Width,Compatible_Code_E_F,Airport_Standards,VER-02-11-401,High
REQ-02-11-028,Turning Radius,Min_Turning_Radius,42_m,Design_Requirement,VER-02-11-401,Medium
REQ-02-11-029,Runway Width Compatibility,Runway_Width,45_m_min,ICAO_Annex_14,VER-02-11-401,High
REQ-02-11-030,Pavement Strength,ACN_PCN,Code_E_Compatible,ICAO_Annex_14,VER-02-11-401,Medium
"""
    
    def _gen_tolerance_requirements_csv(self) -> str:
        return """Requirement_ID,Description,Parameter,Tolerance,Type,Verification_Method,Priority
REQ-02-11-031,Manufacturing Tolerance,Dimensional,±0.1_m,Manufacturing,VER-02-11-005,High
REQ-02-11-032,Assembly Tolerance,Alignment,±0.05_m,Assembly,VER-02-11-005,High
REQ-02-11-033,Measurement Accuracy,Instruments,±0.015_mm,Metrology,All_VER,Critical
REQ-02-11-034,Coordinate Consistency,Data,±0.05_m,Documentation,VER-02-11-302,Medium
REQ-02-11-035,Deflection Limits,Structural,Per_Analysis,Operational,VER-02-11-202,High
"""
    
    def _gen_generic_csv(self) -> str:
        return """ID,Description,Value,Unit,Notes
ITEM-001,Template Entry,TBD,—,Generated by GenCCC
"""
    
    def _generate_md_template(self, path: Path) -> str:
        """Generate markdown template for missing documents"""
        filename = path.stem
        return f"""# {filename}

**Status:** Auto-generated Template (GenCCC)  
**Author:** COPILOT Agent prompted by Amedeo Pelliccia  
**Date:** 2025-11-11

---

## Purpose

This document was automatically generated by the GenCCC (Generative Chain of Contextualized Content) system because it was referenced in the V&V framework but did not exist.

## Content Required

Please populate this document with:
1. Detailed description
2. Relevant parameters and specifications
3. References to source documents
4. Verification or validation criteria

## References

- See Cross_Reference_Report.md for references to this document

---

**Document Control:**
- Version: 1.0 (Auto-generated)
- Status: Template - Requires Content
- Generated: 2025-11-11
"""
    
    def run(self, add_links: bool = True, generate_content: bool = True, dry_run: bool = False):
        """Execute the full GenCCC workflow"""
        print("\n" + "="*70)
        print("GenCCC: Generative Chain of Contextualized Content")
        print("="*70 + "\n")
        
        # Step 1: Find all cross-references
        self.find_all_cross_references()
        
        # Step 2: Add hyperlinks
        if add_links:
            print(f"\n{'DRY RUN: ' if dry_run else ''}Adding hyperlinks...")
            total_changes = 0
            for md_file in self.v_and_v_path.rglob('*.md'):
                if md_file.name != 'Cross_Reference_Report.md':
                    changes = self.add_hyperlinks_to_file(md_file, dry_run)
                    total_changes += changes
            print(f"Total links {'would be ' if dry_run else ''}added: {total_changes}")
        
        # Step 3: Generate missing content
        if generate_content:
            print(f"\n{'DRY RUN: ' if dry_run else ''}Generating missing content...")
            generated = self.generate_missing_content(dry_run)
            print(f"Total files {'would be ' if dry_run else ''}generated: {len(generated)}")
        
        # Step 4: Report summary
        print("\n" + "="*70)
        print("Summary")
        print("="*70)
        print(f"Cross-references found: {len(self.cross_refs_found)}")
        print(f"Existing targets: {len([r for r in self.cross_refs_found if r['exists']])}")
        print(f"Missing targets: {len(self.missing_content)}")
        if add_links:
            print(f"Links added: {total_changes}")
        if generate_content:
            print(f"Files generated: {len(generated)}")
        print("="*70 + "\n")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="GenCCC: Add hyperlinks and generate missing content")
    parser.add_argument('--dry-run', action='store_true', help="Preview changes without modifying files")
    parser.add_argument('--no-links', action='store_true', help="Skip adding hyperlinks")
    parser.add_argument('--no-generate', action='store_true', help="Skip generating missing content")
    parser.add_argument('--path', default='.', help="Path to V&V directory")
    
    args = parser.parse_args()
    
    gen_ccc = GenCCC(args.path)
    gen_ccc.run(
        add_links=not args.no_links,
        generate_content=not args.no_generate,
        dry_run=args.dry_run
    )
