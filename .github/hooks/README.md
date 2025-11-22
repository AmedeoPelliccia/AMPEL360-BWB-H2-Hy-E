# AMPEL360 Q100 Git Hooks

This directory contains Git hooks for the AMPEL360 Q100 project to ensure code quality, compliance, and strategic mission alignment.

## Available Hooks

### pre-commit

Validates changes before they are committed:

- **Q100 Model Code**: Ensures drawing filenames include the Q100 model identifier
- **File Format Compliance**: Prevents commits of forbidden file extensions (.pdf, .xlsx, .docx, .pptx)
- **Strategic Mission Scope**: Warns if mission-related files lack appropriate commit scope
- **Safety-Critical Code**: Validates DO-178C compliance tags on safety-critical code
- **Python Syntax**: Basic syntax validation for Python files

## Installation

Run the setup script from the repository root:

```bash
bash .github/hooks/setup-hooks.sh
```

This will install the hooks into your local `.git/hooks/` directory.

## Manual Installation

If the automated setup doesn't work, manually create a symlink:

```bash
ln -sf ../../.github/hooks/pre-commit .git/hooks/pre-commit
```

Or copy the file:

```bash
cp .github/hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Bypassing Hooks

If you need to bypass the hooks (not recommended):

```bash
git commit --no-verify
```

## Hook Validations

### Drawing Filename Format

Expected: `XX-XX-XXXX_RevX_Q100_EFF_APP_Description.svg`

Example: `53-40-1000_RevC_Q100_ALL_ALL_Forward_Wing_Spar.svg`

### Commit Message Format

For mission-related changes, use the `mission` scope:

```
feat(mission): Add secondary airport route planning
fix(mission): Correct overtourism relief calculations
docs(mission): Update regional connectivity strategy
```

### Forbidden File Extensions

The following extensions are not allowed (except in specific cases):

- `.pdf` - Use Markdown (.md) instead
- `.xlsx`, `.xls` - Use CSV (.csv) instead
- `.docx`, `.doc` - Use Markdown (.md) instead
- `.pptx` - Use Markdown + SVG instead

### Safety-Critical Code

All files containing `SAFETY-CRITICAL` comments must also include DO-178C compliance tags:

```python
# SAFETY-CRITICAL: DAL A - Catastrophic
# DO-178C Level A verification required
# Requirement: REQ-Q100-28-H2-001
```

## Troubleshooting

### Hook Not Running

Check that the hook is executable:

```bash
ls -l .git/hooks/pre-commit
```

If not, make it executable:

```bash
chmod +x .git/hooks/pre-commit
```

### Hook Errors

If you encounter errors, check:

1. You're in a Git repository
2. The hook file exists in `.github/hooks/`
3. Python 3 is available (for Python validations)
4. Git is properly configured

## Contributing

When adding new hooks or modifying existing ones:

1. Update this README
2. Test the hook thoroughly
3. Document any new validations
4. Update the setup script if needed

---

**Last Updated**: 2025-11-23  
**Maintained By**: AMPEL360 Q100 Documentation Team
