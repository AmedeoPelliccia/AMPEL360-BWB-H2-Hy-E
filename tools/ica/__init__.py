#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2025 AMPEL360 Project Contributors

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
