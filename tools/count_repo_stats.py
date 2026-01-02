#!/usr/bin/env python3
"""
Repository Statistics Counter

This script counts the total number of files and folders in the AMPEL360 repository.

Usage:
    python count_repo_stats.py [--verbose] [--path PATH]
"""

import argparse
import sys
from pathlib import Path


def count_files_and_folders(root_path, verbose=False):
    """
    Count all files and folders in the given directory.
    
    Args:
        root_path: Path object pointing to the repository root
        verbose: If True, print detailed statistics
        
    Returns:
        tuple: (file_count, folder_count)
    """
    file_count = 0
    folder_count = 0
    
    try:
        # Count all files
        for item in root_path.rglob('*'):
            if item.is_file():
                file_count += 1
            elif item.is_dir():
                folder_count += 1
        
        return file_count, folder_count
    except Exception as e:
        print(f"Error counting items: {e}", file=sys.stderr)
        return 0, 0


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Count total number of files and folders in the repository'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Print detailed statistics'
    )
    parser.add_argument(
        '--path', '-p',
        type=str,
        default='.',
        help='Path to the repository root (default: current directory)'
    )
    
    args = parser.parse_args()
    
    # Get the repository root
    repo_root = Path(args.path).resolve()
    
    if not repo_root.exists():
        print(f"Error: Path does not exist: {repo_root}", file=sys.stderr)
        return 1
    
    if args.verbose:
        print(f"Scanning repository at: {repo_root}")
        print("This may take a moment for large repositories...")
        print()
    
    # Count files and folders
    file_count, folder_count = count_files_and_folders(repo_root, args.verbose)
    
    # Print results
    print("=" * 60)
    print("AMPEL360 Repository Statistics")
    print("=" * 60)
    print(f"Total Files:   {file_count:,}")
    print(f"Total Folders: {folder_count:,}")
    print(f"Total Items:   {file_count + folder_count:,}")
    print("=" * 60)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
