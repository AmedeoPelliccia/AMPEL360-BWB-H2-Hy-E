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
CD (Continuous Deployment) Tools

Tools that deploy documentation and data to the places where CAOS uses them:
MRO UI, cockpit viewers, IETP, Ops dashboards, DPP endpoints.

Includes:
- Deployment targets (IETP, MRO API, DPP)
- Distribution and versioning tools
"""

__all__ = [
    "ietp_bundle_generator",
    "mro_api_publisher",
    "dpp_publisher",
    "ops_dashboard_sync",
    "doc_release_bundler",
    "airworthiness_release_exporter",
    "multi_format_exporter",
]
