# Constitutional Validation Examples

This directory contains example data files for testing constitutional compliance validation.

## Labor Reabsorption Example

See `labor_reabsorption_example.yaml` for a complete example of how to document labor displacement and reabsorption pathways.

## Harm Precedence Example

See `harm_precedence_example.yaml` for a complete example of how to document AI/ML safety mechanisms.

## Usage

Validate labor reabsorption:
```bash
python3 tools/constitutional_validator.py validate-labor examples/constitutional/labor_reabsorption_example.yaml
```

Validate harm precedence:
```bash
python3 tools/constitutional_validator.py validate-harm examples/constitutional/harm_precedence_example.yaml
```

Generate SBOM metadata:
```bash
python3 tools/constitutional_validator.py sbom-metadata --output constitutional_metadata.json
```
