# Third-Party Notices

This document contains the licenses and notices for third-party software used in the AMPEL360 BWB H₂ Hy-E project.

## Overview

The AMPEL360 project uses various open source libraries and tools. This document provides attribution and license information for these dependencies.

## Direct Dependencies

### Python Dependencies

#### OpenAI Python Client (Optional)
- **Used in:** `tools/genccc/apply.py`, `tools/genccc/agent.py`
- **License:** Apache License 2.0
- **Repository:** https://github.com/openai/openai-python
- **Purpose:** AI-powered content generation for GenCCC

#### PyYAML (Implied, for YAML parsing)
- **License:** MIT License
- **Purpose:** YAML configuration parsing

### GitHub Actions

#### actions/checkout
- **Version:** v4
- **License:** MIT License
- **Repository:** https://github.com/actions/checkout
- **Purpose:** Repository checkout in CI/CD

#### actions/setup-python
- **Version:** v5
- **License:** MIT License
- **Repository:** https://github.com/actions/setup-python
- **Purpose:** Python environment setup in CI/CD

#### actions/upload-artifact
- **Version:** v4
- **License:** MIT License
- **Repository:** https://github.com/actions/upload-artifact
- **Purpose:** Artifact upload in CI/CD

#### actions/download-artifact
- **Version:** v4
- **License:** MIT License
- **Repository:** https://github.com/actions/download-artifact
- **Purpose:** Artifact download in CI/CD

#### actions/github-script
- **Version:** v7
- **License:** MIT License
- **Repository:** https://github.com/actions/github-script
- **Purpose:** GitHub API interaction in workflows

## Transitive Dependencies

Transitive dependencies are managed through pip and are subject to their respective licenses. Key categories include:

- **HTTP/Network:** urllib3, requests, certifi
- **JSON/Data:** jsonschema
- **Utilities:** python-dateutil

For a complete list of Python dependencies and their licenses, run:
```bash
pip-licenses --format=markdown
```

## License Compliance

All dependencies used in this project are compatible with the Apache License 2.0 under which this project is licensed.

### Compatible Licenses
- MIT License
- Apache License 2.0
- BSD Licenses (2-Clause, 3-Clause)
- Python Software Foundation License

## Attribution Requirements

### OpenAI Python Client
```
Copyright (c) OpenAI
Licensed under the Apache License, Version 2.0
```

### GitHub Actions
```
Copyright (c) GitHub, Inc.
Licensed under the MIT License
```

## Notices

This project complies with all license requirements including:
- Preservation of copyright notices
- Inclusion of license text
- Attribution in derivative works
- No use of trademarks without permission

## Updates

This file should be updated whenever:
1. New direct dependencies are added
2. Major version updates of existing dependencies occur
3. License terms of dependencies change

## Generating SBOM

To generate a Software Bill of Materials (SBOM) for compliance:

```bash
# Using syft (if available)
syft dir:. -o spdx-json > sbom.spdx.json

# Using pip-licenses
pip-licenses --format=json > python-licenses.json
```

## Contact

For questions about third-party licenses or compliance:
- Review the LICENSE file in the repository root
- Check individual dependency repositories for detailed license information
- Consult legal/compliance team for enterprise deployments

---

*Last Updated: 2025-11-13*
*This notice file is maintained as part of the AMPEL360 project's license compliance process.*
