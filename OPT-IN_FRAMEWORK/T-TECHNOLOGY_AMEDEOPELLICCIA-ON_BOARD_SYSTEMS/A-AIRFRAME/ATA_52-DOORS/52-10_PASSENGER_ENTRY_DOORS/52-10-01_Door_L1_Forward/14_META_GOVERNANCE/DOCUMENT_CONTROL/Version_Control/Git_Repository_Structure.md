# Git Repository Structure
## Door L1 Forward Documentation

### Repository Layout

```
AMPEL360-BWB-H2-Hy-E/
└── OPT-IN_FRAMEWORK/
    └── T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/
        └── A-AIRFRAME/
            └── ATA_52-DOORS/
                └── 52-10_PASSENGER_ENTRY_DOORS/
                    └── 52-10-01_Door_L1_Forward/
                        ├── 01_OVERVIEW/
                        ├── 02_SAFETY/
                        ├── 03_REQUIREMENTS/
                        ├── 04_DESIGN/
                        ├── 05_INTERFACES/
                        ├── 06_ENGINEERING/
                        ├── 07_V_AND_V/
                        ├── 08_PROTOTYPING/
                        ├── 09_PRODUCTION_PLANNING/
                        ├── 10_CERTIFICATION/
                        ├── 11_OPERATIONS_AND_MAINTENANCE/
                        ├── 12_ASSETS_MANAGEMENT/
                        ├── 13_SUBSYSTEMS_AND_COMPONENTS/
                        └── 14_META_GOVERNANCE/
```

### Branch Structure

See Branch_Strategy.md for detailed branching guidelines.

### Commit Guidelines

1. **Commit Message Format**
   ```
   <type>(<scope>): <subject>
   
   <body>
   
   <footer>
   ```

2. **Types**
   - feat: New feature
   - fix: Bug fix
   - docs: Documentation changes
   - style: Formatting changes
   - refactor: Code restructuring
   - test: Test additions/changes
   - chore: Maintenance tasks

3. **Examples**
   ```
   feat(design): Add door seal specification
   
   - Added seal material properties
   - Defined seal compression requirements
   - Updated interface document
   
   Refs: DOC-52-10-01-004
   ```

### File Organization

- **Source Files**: Original editable formats (MD, CSV, etc.)
- **Generated Files**: PDFs, reports (in .gitignore)
- **Assets**: Images, diagrams in assets/ subfolder
- **Temporary Files**: In /tmp or local .temp/ (excluded)

### .gitignore Configuration

```
# Generated files
*.pdf
*.docx
validation_results.json

# Temporary files
.temp/
*~
*.tmp

# IDE files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

# Build artifacts
dist/
build/
```

### Hooks

- **pre-commit**: Run document validator
- **pre-push**: Check for sensitive data
- **post-merge**: Update document index

### Large File Handling

For large binary files (>10MB):
- Use Git LFS
- Store in external asset management system
- Reference by URL in documentation
