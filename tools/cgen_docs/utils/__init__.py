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
#
# SPDX-License-Identifier: Apache-2.0

"""CGen Docs utilities package."""

from .context import load_context_snippets, load_global_context
from .ai import run_deepen_evolve_prompt, AIResponse
from .diff import (
    write_sidecar,
    apply_changes,
    create_backup,
    compute_diff_summary,
    utc_now,
    BackupManager,
    DiffEngine,
    SidecarWriter,
    DocumentWriter,
    CGenWriter,
)
from .metadata import update_wave_log

__all__ = [
    "load_context_snippets",
    "load_global_context",
    "run_deepen_evolve_prompt",
    "AIResponse",
    "write_sidecar",
    "apply_changes",
    "create_backup",
    "compute_diff_summary",
    "utc_now",
    "BackupManager",
    "DiffEngine",
    "SidecarWriter",
    "DocumentWriter",
    "CGenWriter",
    "update_wave_log",
]
