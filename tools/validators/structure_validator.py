"""
Q100 Directory Structure Validator

Validates OPT-IN Framework directory structure compliance.
Ensures the mandatory 14-folder lifecycle and cross-ATA buckets exist.
"""

import os
import logging
from pathlib import Path
from typing import List, Dict, Set, Optional

logger = logging.getLogger(__name__)


class StructureValidator:
    """Validator for Q100 OPT-IN Framework directory structure."""
    
    # Mandatory 14-folder lifecycle for XX-00_GENERAL
    MANDATORY_LIFECYCLE_FOLDERS = [
        '01_Overview',
        '02_Safety',
        '03_Requirements',
        '04_Design',
        '05_Interfaces',
        '06_Engineering',
        '07_V_AND_V',
        '08_Prototyping',
        '09_Production_Planning',
        '10_Certification',
        '11_EIS_Versions_Tags',
        '12_Services',
        '13_Subsystems_Components',
        '14_Ops_Std_Sustain',
    ]
    
    # Mandatory cross-ATA buckets
    MANDATORY_CROSS_ATA_BUCKETS = [
        '10_Operations',
        '20_Subsystems',
        '30_Circularity',
        '40_Software',
        '50_Structures',
        '60_Storages',
        '70_Propulsion',
        '80_Energy',
        '90_Tables_Schemas_Diagrams',
    ]
    
    # Forbidden file extensions
    FORBIDDEN_EXTENSIONS = ['.pdf', '.xlsx', '.xls', '.docx', '.doc', '.pptx']
    
    # Allowed file extensions
    ALLOWED_EXTENSIONS = ['.md', '.csv', '.svg', '.yaml', '.yml', '.json', 
                          '.py', '.js', '.sh', '.step', '.iges', '.jt']
    
    def __init__(self, repo_root: Path):
        """
        Initialize the structure validator.
        
        Args:
            repo_root: Root directory of the repository
        """
        self.repo_root = Path(repo_root)
        self.opt_in_root = self.repo_root / 'OPT-IN_FRAMEWORK'
    
    def validate_ata_chapter(self, ata_path: Path) -> Dict[str, List[str]]:
        """
        Validate an ATA chapter directory structure.
        
        Args:
            ata_path: Path to the ATA chapter directory
            
        Returns:
            Dictionary with 'errors' and 'warnings' lists
        """
        errors = []
        warnings = []
        
        if not ata_path.exists():
            errors.append(f"ATA chapter directory does not exist: {ata_path}")
            return {'errors': errors, 'warnings': warnings}
        
        # Find XX-00_GENERAL directory
        general_dirs = list(ata_path.glob('*-00_GENERAL'))
        
        if not general_dirs:
            errors.append(f"No XX-00_GENERAL directory found in {ata_path.name}")
        else:
            general_dir = general_dirs[0]
            
            # Check for mandatory lifecycle folders
            missing_lifecycle = []
            for folder in self.MANDATORY_LIFECYCLE_FOLDERS:
                # Allow flexible naming (01_Overview or 01_OVERVIEW)
                pattern = f"*-00-{folder.split('_')[0]}_*"
                matches = list(general_dir.glob(pattern))
                
                if not matches:
                    missing_lifecycle.append(folder)
            
            if missing_lifecycle:
                warnings.append(
                    f"Missing lifecycle folders in {general_dir.name}: {', '.join(missing_lifecycle)}"
                )
        
        # Check for cross-ATA buckets
        missing_buckets = []
        for bucket in self.MANDATORY_CROSS_ATA_BUCKETS:
            bucket_pattern = f"*-{bucket.split('_')[0]}_*"
            matches = list(ata_path.glob(bucket_pattern))
            
            if not matches:
                missing_buckets.append(bucket)
        
        if missing_buckets:
            warnings.append(
                f"Missing cross-ATA buckets in {ata_path.name}: {', '.join(missing_buckets)}"
            )
        
        return {'errors': errors, 'warnings': warnings}
    
    def check_file_extensions(self, directory: Path) -> List[str]:
        """
        Check for forbidden file extensions in a directory tree.
        
        Args:
            directory: Directory to check
            
        Returns:
            List of files with forbidden extensions
        """
        forbidden_files = []
        
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = Path(root) / file
                ext = file_path.suffix.lower()
                
                if ext in self.FORBIDDEN_EXTENSIONS:
                    relative_path = file_path.relative_to(self.repo_root)
                    forbidden_files.append(str(relative_path))
        
        return forbidden_files
    
    def validate_all_ata_chapters(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Validate all ATA chapter directories in OPT-IN Framework.
        
        Returns:
            Dictionary mapping ATA chapter name to validation results
        """
        if not self.opt_in_root.exists():
            logger.error(f"OPT-IN_FRAMEWORK directory not found at {self.opt_in_root}")
            return {}
        
        results = {}
        
        # Find all ATA chapter directories
        for axis_dir in self.opt_in_root.iterdir():
            if not axis_dir.is_dir() or axis_dir.name.startswith('.'):
                continue
            
            # Look for ATA_XX directories
            for ata_dir in axis_dir.iterdir():
                if ata_dir.is_dir() and ata_dir.name.startswith('ATA_'):
                    logger.info(f"Validating {ata_dir.name}...")
                    results[ata_dir.name] = self.validate_ata_chapter(ata_dir)
        
        return results
    
    def generate_report(self, results: Dict[str, Dict[str, List[str]]]) -> str:
        """
        Generate a human-readable validation report.
        
        Args:
            results: Validation results from validate_all_ata_chapters
            
        Returns:
            Formatted report string
        """
        lines = ["# Q100 Directory Structure Validation Report\n"]
        
        total_errors = 0
        total_warnings = 0
        
        for ata_chapter, result in sorted(results.items()):
            errors = result.get('errors', [])
            warnings = result.get('warnings', [])
            
            total_errors += len(errors)
            total_warnings += len(warnings)
            
            if errors or warnings:
                lines.append(f"\n## {ata_chapter}")
                
                if errors:
                    lines.append("\n### Errors:")
                    for error in errors:
                        lines.append(f"- ❌ {error}")
                
                if warnings:
                    lines.append("\n### Warnings:")
                    for warning in warnings:
                        lines.append(f"- ⚠️  {warning}")
        
        # Summary
        lines.insert(1, f"\n**Total Errors:** {total_errors}")
        lines.insert(2, f"**Total Warnings:** {total_warnings}\n")
        
        if total_errors == 0 and total_warnings == 0:
            lines.append("\n✅ All ATA chapters have compliant directory structures!")
        
        return '\n'.join(lines)


def validate_directory_structure(repo_root: str) -> bool:
    """
    Convenience function to validate directory structure.
    
    Args:
        repo_root: Root directory of the repository
        
    Returns:
        True if valid (no errors), False otherwise
    """
    validator = StructureValidator(Path(repo_root))
    results = validator.validate_all_ata_chapters()
    
    total_errors = sum(len(r.get('errors', [])) for r in results.values())
    
    if total_errors > 0:
        report = validator.generate_report(results)
        print(report)
        return False
    
    logger.info("✓ Directory structure validation passed")
    return True


if __name__ == '__main__':
    import sys
    
    logging.basicConfig(level=logging.INFO)
    
    repo_root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    
    validator = StructureValidator(Path(repo_root))
    
    # Validate all ATA chapters
    print("Validating OPT-IN Framework directory structure...\n")
    results = validator.validate_all_ata_chapters()
    
    # Generate and print report
    report = validator.generate_report(results)
    print(report)
    
    # Check for forbidden file extensions
    print("\n# Checking for forbidden file extensions...\n")
    forbidden = validator.check_file_extensions(validator.opt_in_root)
    
    if forbidden:
        print("⚠️  Found files with forbidden extensions:")
        for file in forbidden:
            print(f"  - {file}")
        print("\nForbidden extensions:", ', '.join(validator.FORBIDDEN_EXTENSIONS))
    else:
        print("✅ No forbidden file extensions found")
    
    # Exit with error if there are errors
    total_errors = sum(len(r.get('errors', [])) for r in results.values())
    sys.exit(1 if (total_errors > 0 or forbidden) else 0)
