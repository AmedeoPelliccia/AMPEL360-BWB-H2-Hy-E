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
CI (Continuous Integration) Tools

Tools that validate, check, and enforce consistency for all updates
to ensure compatibility with airworthiness documentation requirements.

Includes:
- Structural and documentation CI validators
- PR and commit intelligence tools
- Impact analyzers
"""

__all__ = [
    "geometry_baseline_watchdog",
    "mass_properties_watchdog",
    "ica_impact_analyzer",
    "traceability_matrix_updater",
    "dmc_structure_validator",
    "commit_classifier",
    "auto_tagger",
]
