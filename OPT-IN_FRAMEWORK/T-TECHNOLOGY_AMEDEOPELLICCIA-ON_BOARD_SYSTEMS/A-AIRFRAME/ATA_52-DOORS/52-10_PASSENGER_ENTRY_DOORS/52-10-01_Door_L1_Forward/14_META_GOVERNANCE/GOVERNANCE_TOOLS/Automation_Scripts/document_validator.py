#!/usr/bin/env python3
"""
Document Validation Tool for META Governance
Checks completeness, compliance, and quality
"""

import os
import json
import csv
import re
from datetime import datetime
from pathlib import Path

class DocumentValidator:
    def __init__(self, root_path):
        self.root = Path(root_path)
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'total_docs': 0,
            'valid_docs': 0,
            'issues': [],
            'compliance': {}
        }
    
    def validate_structure(self):
        """Check 14-folder SKELETON compliance"""
        required_folders = [
            '01_OVERVIEW', '02_SAFETY', '03_REQUIREMENTS',
            '04_DESIGN', '05_INTERFACES', '06_ENGINEERING',
            '07_V_AND_V', '08_PROTOTYPING', '09_PRODUCTION_PLANNING',
            '10_CERTIFICATION', '11_OPERATIONS_AND_MAINTENANCE',
            '12_ASSETS_MANAGEMENT', '13_SUBSYSTEMS_AND_COMPONENTS',
            '14_META_GOVERNANCE'
        ]
        
        for folder in required_folders:
            folder_path = self.root / folder
            if not folder_path.exists():
                self.results['issues'].append(
                    f"Missing required folder: {folder}"
                )
            else:
                self.validate_folder_contents(folder_path)
    
    def validate_folder_contents(self, folder_path):
        """Validate documents within folder"""
        for file_path in folder_path.rglob('*'):
            if file_path.is_file():
                self.results['total_docs'] += 1
                if self.validate_document(file_path):
                    self.results['valid_docs'] += 1
    
    def validate_document(self, file_path):
        """Check individual document compliance"""
        valid = True
        
        # Check naming convention
        if not self.check_naming(file_path.name):
            self.results['issues'].append(
                f"Naming violation: {file_path.name}"
            )
            valid = False
        
        # Check file format
        if file_path.suffix in ['.md', '.csv', '.json', '.xml']:
            if not self.check_content(file_path):
                valid = False
        
        return valid
    
    def check_naming(self, filename):
        """Verify naming conventions"""
        # Pattern: Component_Description or DMC format
        pattern1 = r'^[A-Z][A-Za-z0-9_-]+\.(md|csv|json|xml|py|html)$'
        pattern2 = r'^DMC-AMPEL360-[A-Z0-9-]+\.(md|xml)$'
        pattern3 = r'^PN-\d{2}-\d{2}-\d{2}-\d{6}.*\.(md|csv)$'
        pattern4 = r'^_[A-Z][A-Za-z0-9_]+\.(md|csv)$'  # Dashboard files
        pattern5 = r'^[a-z][a-z0-9_]+\.(py|sh)$'  # Scripts
        
        return any([
            re.match(pattern1, filename),
            re.match(pattern2, filename),
            re.match(pattern3, filename),
            re.match(pattern4, filename),
            re.match(pattern5, filename)
        ])
    
    def check_content(self, file_path):
        """Basic content validation"""
        try:
            if file_path.suffix == '.json':
                with open(file_path) as f:
                    json.load(f)
            elif file_path.suffix == '.csv':
                with open(file_path) as f:
                    csv.reader(f)
            elif file_path.suffix == '.xml':
                # Basic XML check
                with open(file_path) as f:
                    content = f.read()
                    if not content.startswith('<?xml'):
                        return False
            return True
        except Exception as e:
            self.results['issues'].append(
                f"Content error in {file_path.name}: {str(e)}"
            )
            return False
    
    def calculate_compliance(self):
        """Calculate compliance scores"""
        if self.results['total_docs'] > 0:
            self.results['compliance']['document'] = (
                self.results['valid_docs'] / 
                self.results['total_docs'] * 100
            )
        
        # Check for critical documents
        critical_docs = [
            'README.md',
            '_Document_Master_Index.csv',
            'Change_Control_Process.md',
            'Risk_Register.csv'
        ]
        
        found = sum(1 for doc in critical_docs 
                   if (self.root / '14_META_GOVERNANCE' / doc).exists() or
                      any((self.root / '14_META_GOVERNANCE').rglob(doc)))
        self.results['compliance']['critical'] = (
            found / len(critical_docs) * 100
        )
    
    def generate_report(self):
        """Generate validation report"""
        self.calculate_compliance()
        
        report = f"""
# Document Validation Report
Generated: {self.results['timestamp']}

## Summary
- Total Documents: {self.results['total_docs']}
- Valid Documents: {self.results['valid_docs']}
- Document Compliance: {self.results['compliance'].get('document', 0):.1f}%
- Critical Document Compliance: {self.results['compliance'].get('critical', 0):.1f}%

## Issues Found
Total Issues: {len(self.results['issues'])}
"""
        
        if self.results['issues']:
            report += "\n### Issue List\n"
            for issue in self.results['issues'][:20]:  # First 20
                report += f"- {issue}\n"
            if len(self.results['issues']) > 20:
                report += f"\n... and {len(self.results['issues']) - 20} more issues\n"
        
        return report

if __name__ == "__main__":
    import sys
    
    # Default path or from command line
    if len(sys.argv) > 1:
        root_path = sys.argv[1]
    else:
        root_path = "./52-10-01_Door_L1_Forward"
    
    validator = DocumentValidator(root_path)
    validator.validate_structure()
    print(validator.generate_report())
    
    # Save detailed results
    output_file = 'validation_results.json'
    with open(output_file, 'w') as f:
        json.dump(validator.results, f, indent=2)
    print(f"\nDetailed results saved to: {output_file}")
