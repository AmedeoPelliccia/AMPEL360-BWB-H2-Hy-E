#!/usr/bin/env python3
"""
Enhance 01_OVERVIEW README.md files with YAML metadata and GENCCC tags.

This script adds:
1. YAML front-matter metadata block
2. V&V linkage reference
3. GENCCC automation tags

Usage:
    python enhance_overview_readmes.py [--dry-run] [--file <path>]
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime, timedelta
import argparse


def extract_ata_info(file_path):
    """Extract ATA chapter and system information from file path."""
    parts = Path(file_path).parts
    
    # Find ATA chapter
    ata_chapter = None
    system_name = None
    system_code = None
    
    for part in parts:
        # Match ATA chapter pattern (e.g., ATA_79-OIL)
        ata_match = re.match(r'ATA[_-](\d+)[-_](.+)', part)
        if ata_match:
            ata_chapter = ata_match.group(1)
            system_name = ata_match.group(2).replace('_', ' ').replace('-', ' ').title()
        
        # Match system code pattern (e.g., 79-00-00_GENERAL)
        code_match = re.match(r'(\d{2}-\d{2}-\d{2})[-_](.+)', part)
        if code_match:
            system_code = code_match.group(1)
            if not system_name:
                system_name = code_match.group(2).replace('_', ' ').title()
    
    return ata_chapter, system_name, system_code


def extract_existing_metadata(content):
    """Extract metadata from existing README content."""
    metadata = {}
    
    # Extract title from first heading
    title_match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1).strip()
    
    # Extract ATA Chapter
    ata_match = re.search(r'\*\*ATA Chapter:\*\*\s*(\d+)', content)
    if ata_match:
        metadata['ata_chapter'] = ata_match.group(1)
    
    # Extract System
    system_match = re.search(r'\*\*System:\*\*\s*(.+?)(?:\n|\*\*)', content)
    if system_match:
        metadata['system'] = system_match.group(1).strip()
    
    # Extract Status
    status_match = re.search(r'\*\*Status:\*\*\s*(.+?)(?:\n|\*\*)', content)
    if status_match:
        metadata['status'] = status_match.group(1).strip()
    
    return metadata


def generate_yaml_frontmatter(file_path, existing_content):
    """Generate YAML front-matter for the README file."""
    ata_chapter, system_name, system_code = extract_ata_info(file_path)
    existing_meta = extract_existing_metadata(existing_content)
    
    # Determine identifier
    if system_code:
        identifier = f"{system_code}-001A"
    elif ata_chapter:
        identifier = f"{ata_chapter}-00-01-001A"
    else:
        identifier = "XX-00-01-001A"
    
    # Determine title
    if 'title' in existing_meta and existing_meta['title']:
        title = existing_meta['title']
    elif ata_chapter and system_name:
        title = f"ATA {ata_chapter}-00-01 — {system_name} Overview"
    elif system_name:
        title = f"{system_name} Overview"
    else:
        title = "System Overview"
    
    # Determine scope
    scope_text = "System overview, architecture, and integration with related subsystems"
    if system_name:
        scope_text = f"{system_name} architecture and integration with related subsystems"
    
    # Status
    status = existing_meta.get('status', 'Draft')
    if 'Pending' in status:
        status = 'Draft'
    
    # Dates
    created_at = datetime.now().strftime('%Y-%m-%d')
    next_review = (datetime.now() + timedelta(days=180)).strftime('%Y-%m-%d')
    
    yaml_block = f"""---
title: {title}
identifier: {identifier}
version: 0.1
author: Amedeo Pelliccia
status: {status}
classification: Technical
scope: {scope_text}
created_at: {created_at}
next_review: {next_review}
compliance:
  - ATA iSpec 2200
  - S1000D
  - AMPEL360 OPT-IN Framework
---

"""
    return yaml_block


def generate_vv_linkage(file_path):
    """Generate V&V linkage reference."""
    # Calculate relative path to V&V folder
    current_dir = Path(file_path).parent
    # Go up to the system level (2 levels up from 01_OVERVIEW)
    system_dir = current_dir.parent.parent
    vv_dir = system_dir / "07_V_AND_V"
    
    # Extract system code for traceability matrix filename
    _, _, system_code = extract_ata_info(file_path)
    if system_code:
        matrix_file = f"{system_code}-001A_Traceability_Matrix.csv"
    else:
        matrix_file = "Traceability_Matrix.csv"
    
    vv_link = f"""
> 🔗 **Linked Verification Matrix:** [../../07_V_AND_V/{matrix_file}](../../07_V_AND_V/{matrix_file})

"""
    return vv_link


def generate_genccc_tags():
    """Generate GENCCC automation tags."""
    tags = """<!-- GENCCC_STATUS: pending -->
<!-- GENCCC_SCOPE: system_description, architecture, integration -->

"""
    return tags


def has_yaml_frontmatter(content):
    """Check if content already has YAML front-matter."""
    return content.strip().startswith('---\n') or content.strip().startswith('---\r\n')


def enhance_readme(file_path, dry_run=False):
    """Enhance a single README.md file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has YAML front-matter
        if has_yaml_frontmatter(content):
            print(f"SKIP (already has YAML): {file_path}")
            return False
        
        # Generate enhancements
        yaml_fm = generate_yaml_frontmatter(file_path, content)
        vv_linkage = generate_vv_linkage(file_path)
        genccc_tags = generate_genccc_tags()
        
        # Find where to insert V&V linkage (after "## Purpose" section or at the end of metadata)
        # Insert V&V linkage before first ## heading after the metadata
        purpose_match = re.search(r'\n(##\s+(?:Purpose|Content|Standards))', content)
        if purpose_match:
            insert_pos = purpose_match.start() + 1
            enhanced_content = (
                yaml_fm + 
                genccc_tags +
                content[:insert_pos] + 
                vv_linkage + 
                content[insert_pos:]
            )
        else:
            # If no clear section, insert after first blank line or at start
            enhanced_content = yaml_fm + genccc_tags + vv_linkage + content
        
        if dry_run:
            print(f"WOULD ENHANCE: {file_path}")
            return True
        else:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(enhanced_content)
            print(f"ENHANCED: {file_path}")
            return True
            
    except Exception as e:
        print(f"ERROR processing {file_path}: {e}", file=sys.stderr)
        return False


def find_overview_readmes(root_dir):
    """Find all 01_OVERVIEW/README.md files."""
    overview_files = []
    for root, dirs, files in os.walk(root_dir):
        if '01_OVERVIEW' in Path(root).parts and 'README.md' in files:
            readme_path = os.path.join(root, 'README.md')
            overview_files.append(readme_path)
    return sorted(overview_files)


def main():
    parser = argparse.ArgumentParser(
        description='Enhance 01_OVERVIEW README.md files with metadata and GENCCC tags'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without making changes'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='Process a single file instead of all files'
    )
    parser.add_argument(
        '--root',
        type=str,
        default='.',
        help='Root directory to search (default: current directory)'
    )
    
    args = parser.parse_args()
    
    if args.file:
        # Process single file
        if not os.path.exists(args.file):
            print(f"ERROR: File not found: {args.file}", file=sys.stderr)
            return 1
        
        success = enhance_readme(args.file, args.dry_run)
        return 0 if success else 1
    else:
        # Process all files
        print(f"Searching for 01_OVERVIEW/README.md files in {args.root}...")
        overview_files = find_overview_readmes(args.root)
        
        print(f"Found {len(overview_files)} files to process")
        
        if args.dry_run:
            print("\n=== DRY RUN MODE - No files will be modified ===\n")
        
        success_count = 0
        skip_count = 0
        error_count = 0
        
        for file_path in overview_files:
            result = enhance_readme(file_path, args.dry_run)
            if result:
                success_count += 1
            elif "SKIP" in str(result):
                skip_count += 1
            else:
                error_count += 1
        
        print(f"\n=== Summary ===")
        print(f"Total files: {len(overview_files)}")
        print(f"Enhanced: {success_count}")
        print(f"Skipped: {skip_count}")
        print(f"Errors: {error_count}")
        
        return 0 if error_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
