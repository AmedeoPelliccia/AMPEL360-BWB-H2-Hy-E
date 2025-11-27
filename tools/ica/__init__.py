# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python3

"""
ICA (Instructions for Continued Airworthiness) Enabling Toolchain

This package provides tools for continuous airworthiness compliance in the
AMPEL360-BWB-H2-Hy-E aircraft program. The toolchain enables:

1. CGen (Content-Generation) - Automated documentation synthesis
2. CI (Continuous Integration) - Validation and compliance checking
3. CD (Continuous Deployment) - Publishing to IETP/DPP/MRO portals
4. Pipelines - Telemetry ingestion and ICA mapping
5. Governance - Airworthiness rules and workflow enforcement
6. Agents - Autonomous documentation and support agents

Part of the CAOS (Computer Aided Operations and Services) ecosystem.
"""

__version__ = "1.0.0"
__author__ = "AMPEL360 Project Contributors"

from pathlib import Path

# Package root
ICA_ROOT = Path(__file__).resolve().parent

# Repository root (tools/ica -> repo root)
REPO_ROOT = ICA_ROOT.parents[1]

# Key paths
OPT_IN_FRAMEWORK = REPO_ROOT / "OPT-IN_FRAMEWORK"
CAOS_DIR = REPO_ROOT / "CAOS"
CD_DIR = REPO_ROOT / "cd"
REPORTS_DIR = CD_DIR / "reports"


def ensure_directories():
    """Ensure required directories exist."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (CD_DIR / "publications").mkdir(parents=True, exist_ok=True)
    (CD_DIR / "baselines").mkdir(parents=True, exist_ok=True)
