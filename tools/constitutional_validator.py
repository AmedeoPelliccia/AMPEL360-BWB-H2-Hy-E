#!/usr/bin/env python3
"""
AMPEL360 Constitutional Governance Validator

This script provides utilities for constitutional compliance:
- Compute constitutional hash for embedding in artifacts
- Validate labor reabsorption calculations
- Check harm precedence configurations
- Generate compliance reports
"""

import argparse
import hashlib
import json
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any


class ConstitutionalValidator:
    """Validator for AMPEL360 Digital Constitution compliance"""
    
    def __init__(self, repo_root: Path):
        self.repo_root = Path(repo_root)
        self.governance_file = self.repo_root / "GOVERNANCE.md"
        self.constitution_config = self.repo_root / ".constitution.yaml"
        
        if not self.governance_file.exists():
            raise FileNotFoundError(f"GOVERNANCE.md not found at {self.governance_file}")
        
        if not self.constitution_config.exists():
            raise FileNotFoundError(f".constitution.yaml not found at {self.constitution_config}")
        
        with open(self.constitution_config, 'r') as f:
            self.config = yaml.safe_load(f)
    
    def compute_constitutional_hash(self) -> str:
        """Compute SHA-256 hash of GOVERNANCE.md"""
        with open(self.governance_file, 'rb') as f:
            content = f.read()
        
        hash_obj = hashlib.sha256(content)
        return hash_obj.hexdigest()
    
    def validate_labor_reabsorption(self, labor_data: Dict) -> Dict[str, Any]:
        """
        Validate labor reabsorption data structure and calculations
        
        Returns:
            Dict with 'valid', 'errors', 'warnings' keys
        """
        result = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        if not labor_data.get('applicable'):
            return result  # Not applicable, skip validation
        
        # Check required fields
        required_fields = ['roles_displaced', 'reabsorption_pathway', 'net_displacement']
        for field in required_fields:
            if field not in labor_data:
                result['errors'].append(f"Missing required field: {field}")
                result['valid'] = False
        
        if not result['valid']:
            return result
        
        # Calculate net displacement
        displaced_fte = sum(
            role.get('fte_equivalent', 0) 
            for role in labor_data.get('roles_displaced', [])
        )
        
        reabsorbed_fte = sum(
            role.get('fte_equivalent', 0)
            for role in labor_data.get('reabsorption_pathway', [])
        )
        
        calculated_net = displaced_fte - reabsorbed_fte
        declared_net = labor_data.get('net_displacement', 0)
        
        # Validate calculation
        if abs(calculated_net - declared_net) > 0.01:  # Allow small floating point errors
            result['errors'].append(
                f"Net displacement calculation error: "
                f"declared {declared_net}, calculated {calculated_net}"
            )
            result['valid'] = False
        
        # Check constitutional requirement: net displacement must be <= 0
        if declared_net > 0:
            # Governance override required
            if 'governance_override' not in labor_data:
                result['errors'].append(
                    f"Net displacement is {declared_net} (> 0) but no governance override provided"
                )
                result['valid'] = False
            else:
                override = labor_data['governance_override']
                required_override_fields = ['justification', 'risk_assessment', 
                                           'mitigation_plan', 'review_date', 'steward_approval']
                
                for field in required_override_fields:
                    if field not in override:
                        result['errors'].append(
                            f"Governance override missing required field: {field}"
                        )
                        result['valid'] = False
        
        # Warnings for quality
        if displaced_fte > 0 and not labor_data.get('roles_displaced'):
            result['warnings'].append("Roles displaced but no detailed role information provided")
        
        for role in labor_data.get('reabsorption_pathway', []):
            if not role.get('transition_plan'):
                result['warnings'].append(
                    f"Reabsorption role '{role.get('new_role', 'unknown')}' lacks transition plan"
                )
        
        return result
    
    def validate_harm_precedence(self, harm_data: Dict) -> Dict[str, Any]:
        """
        Validate harm precedence configuration
        
        Returns:
            Dict with 'valid', 'errors', 'warnings' keys
        """
        result = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        if not harm_data.get('applicable'):
            return result
        
        thresholds = self.config['enforcement']['harm_precedence']['uncertainty_thresholds']
        
        # Check model outputs
        for output in harm_data.get('model_outputs', []):
            # Validate confidence threshold
            conf_threshold = output.get('confidence_threshold', 0)
            escalation_type = output.get('escalation_type', '')
            
            if escalation_type == 'safety_critical' and conf_threshold < thresholds['safety_critical']:
                result['errors'].append(
                    f"Safety critical output has confidence threshold {conf_threshold}, "
                    f"but constitutional minimum is {thresholds['safety_critical']}"
                )
                result['valid'] = False
            
            # Validate responsible role (must be named, not queue)
            responsible = output.get('responsible_role', '')
            if not responsible or 'queue' in responsible.lower() or 'system' in responsible.lower():
                result['errors'].append(
                    f"Escalation for {output.get('output_type', 'unknown')} must specify "
                    f"named role, not queue or system"
                )
                result['valid'] = False
            
            # Validate SLA
            sla = output.get('response_sla_hours', 0)
            if sla <= 0 or sla > 24:
                result['warnings'].append(
                    f"Response SLA of {sla} hours may be inappropriate (should be 1-24 hours)"
                )
            
            # Check fallback chain
            if not output.get('fallback_chain'):
                result['warnings'].append(
                    f"No fallback chain specified for {output.get('output_type', 'unknown')}"
                )
        
        # Check graceful degradation
        degradation = harm_data.get('graceful_degradation', {})
        if not degradation.get('implemented'):
            result['warnings'].append("Graceful degradation not marked as implemented")
        
        if not degradation.get('safe_mode_description'):
            result['warnings'].append("No safe mode description provided")
        
        # Check reversibility
        reversibility = harm_data.get('reversibility', {})
        rollback_hours = reversibility.get('estimated_rollback_hours', 999)
        
        if rollback_hours > 4:
            result['errors'].append(
                f"Estimated rollback time is {rollback_hours} hours, "
                f"but constitutional maximum is 4 hours"
            )
            result['valid'] = False
        
        if not reversibility.get('tested'):
            result['warnings'].append("Rollback procedure not marked as tested")
        
        return result
    
    def generate_sbom_metadata(self) -> Dict:
        """Generate constitutional metadata for SBOM inclusion"""
        const_hash = self.compute_constitutional_hash()
        
        return {
            "constitutional_compliance": {
                "version": self.config['constitution']['version'],
                "hash": const_hash,
                "hash_algorithm": "SHA-256",
                "document_path": "GOVERNANCE.md",
                "effective_date": self.config['constitution']['effective_date'],
                "steward": self.config['constitution']['steward'],
                "enforcement_enabled": {
                    "labor_reabsorption": self.config['enforcement']['labor_reabsorption']['enabled'],
                    "harm_precedence": self.config['enforcement']['harm_precedence']['enabled'],
                    "reversibility": self.config['enforcement']['reversibility']['enabled'],
                    "metrics_tracking": self.config['enforcement']['metrics_tracking']['enabled']
                },
                "compliance_attestation": {
                    "required": True,
                    "format": "DCO-style signed attestation",
                    "template": f"I affirm this derivative work complies with AMPEL360 Digital Constitution v{self.config['constitution']['version']}"
                }
            }
        }
    
    def update_constitutional_hash(self):
        """Update the hash in .constitution.yaml"""
        const_hash = self.compute_constitutional_hash()
        
        self.config['constitution']['hash'] = const_hash
        
        with open(self.constitution_config, 'w') as f:
            yaml.dump(self.config, f, default_flow_style=False, sort_keys=False)
        
        print(f"✅ Updated constitutional hash in .constitution.yaml")
        print(f"   Hash: {const_hash}")


def main():
    parser = argparse.ArgumentParser(
        description="AMPEL360 Constitutional Governance Validator"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Hash command
    hash_parser = subparsers.add_parser('hash', help='Compute constitutional hash')
    hash_parser.add_argument('--update', action='store_true',
                            help='Update hash in .constitution.yaml')
    
    # Validate labor command
    labor_parser = subparsers.add_parser('validate-labor',
                                         help='Validate labor reabsorption data')
    labor_parser.add_argument('file', help='YAML file with labor reabsorption data')
    
    # Validate harm command
    harm_parser = subparsers.add_parser('validate-harm',
                                        help='Validate harm precedence data')
    harm_parser.add_argument('file', help='YAML file with harm precedence data')
    
    # SBOM metadata command
    sbom_parser = subparsers.add_parser('sbom-metadata',
                                        help='Generate constitutional metadata for SBOM')
    sbom_parser.add_argument('--output', default='constitutional_metadata.json',
                            help='Output file for JSON metadata')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    try:
        validator = ConstitutionalValidator(Path.cwd())
        
        if args.command == 'hash':
            const_hash = validator.compute_constitutional_hash()
            print(f"Constitutional Hash (SHA-256):")
            print(const_hash)
            
            if args.update:
                validator.update_constitutional_hash()
        
        elif args.command == 'validate-labor':
            with open(args.file, 'r') as f:
                labor_data = yaml.safe_load(f)
            
            result = validator.validate_labor_reabsorption(labor_data)
            
            print("Labor Reabsorption Validation Results:")
            print("=" * 50)
            
            if result['valid']:
                print("✅ VALID - Labor reabsorption data complies with constitution")
            else:
                print("❌ INVALID - Constitutional violations detected")
            
            if result['errors']:
                print("\nErrors:")
                for error in result['errors']:
                    print(f"  ❌ {error}")
            
            if result['warnings']:
                print("\nWarnings:")
                for warning in result['warnings']:
                    print(f"  ⚠️  {warning}")
            
            return 0 if result['valid'] else 1
        
        elif args.command == 'validate-harm':
            with open(args.file, 'r') as f:
                harm_data = yaml.safe_load(f)
            
            result = validator.validate_harm_precedence(harm_data)
            
            print("Harm Precedence Validation Results:")
            print("=" * 50)
            
            if result['valid']:
                print("✅ VALID - Harm precedence configuration complies with constitution")
            else:
                print("❌ INVALID - Constitutional violations detected")
            
            if result['errors']:
                print("\nErrors:")
                for error in result['errors']:
                    print(f"  ❌ {error}")
            
            if result['warnings']:
                print("\nWarnings:")
                for warning in result['warnings']:
                    print(f"  ⚠️  {warning}")
            
            return 0 if result['valid'] else 1
        
        elif args.command == 'sbom-metadata':
            metadata = validator.generate_sbom_metadata()
            
            with open(args.output, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            print(f"✅ Generated constitutional metadata: {args.output}")
            print("\nMetadata summary:")
            print(f"  Version: {metadata['constitutional_compliance']['version']}")
            print(f"  Hash: {metadata['constitutional_compliance']['hash']}")
            print(f"  Steward: {metadata['constitutional_compliance']['steward']}")
        
        return 0
    
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
