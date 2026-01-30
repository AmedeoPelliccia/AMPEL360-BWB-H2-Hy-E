# GitHub Copilot Setup Guide for AMPEL360 Q100

This guide explains the comprehensive GitHub Copilot instructions and validation tools for the AMPEL360 Q100 BWB H2-Electric Aircraft project.

## 📋 Quick Links

- [Main Copilot Instructions](/.github/copilot.md)
- [Validators Documentation](/tools/validators/README.md)
- [Pre-commit Hooks](/.github/hooks/README.md)

## 🚀 Quick Start

### 1. Install Validation Tools

```bash
pip install -r requirements.txt
```

### 2. Set Up Pre-commit Hooks

```bash
bash .github/hooks/setup-hooks.sh
```

### 3. Test Everything Works

```bash
python tools/validators/drawing_validator.py 57-40-1000_RevC_Q100_ALL_ALL_Spar.svg
python tools/validators/ci_validator.py CI-57-400-SPAR-FWD
python tools/validators/structure_validator.py .
```

## 📚 What's Included

### Copilot Instructions
- Main instructions: `.github/copilot.md`
- Path-specific: `.github/instructions/`

### Validation Tools
1. DrawingValidator: Q100 drawing filenames
2. CIValidator: CI numbers and codes
3. StructureValidator: OPT-IN Framework structure

### GitHub Actions
1. copilot-setup-steps.yml: Environment setup
2. q100-validation.yml: Automated compliance checks

### Pre-commit Hooks
- Q100 model code validation
- File extension checks
- Strategic mission scope validation

## 📖 Resources

- [Validators README](/tools/validators/README.md)
- [Pre-commit Hooks README](/.github/hooks/README.md)
- [OPT-IN Framework](/OPT-IN_FRAMEWORK_STANDARD.md)

---

**Version**: 1.0.0  
**Last Updated**: 2025-11-23  
**Maintained By**: AMPEL360 Q100 Documentation Team
