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

"""
MMIP v0.1 — Reference Implementation Package

This package provides the reference implementation for the
Models Memory Inheritance Protocol (MMIP) v0.1.
"""

from .mmip_protocol import (
    # Enums
    ApplyMode,
    CapsuleType,
    ExportPolicy,
    LinkType,
    ProducerType,
    RetentionPolicy,
    Scope,
    # Data classes
    Capsule,
    CapsuleLink,
    ContextPackage,
    Envelope,
    InheritContextFilters,
    InheritContextRequest,
    Integrity,
    Metadata,
    Policies,
    Producer,
    Provenance,
    Thread,
    # Protocol
    MMIPProtocol,
    # Utilities
    check_compliance_level,
)

__version__ = "0.1"
__all__ = [
    # Enums
    "CapsuleType",
    "Scope",
    "ExportPolicy",
    "RetentionPolicy",
    "ProducerType",
    "ApplyMode",
    "LinkType",
    # Data classes
    "Provenance",
    "CapsuleLink",
    "Policies",
    "Metadata",
    "Capsule",
    "Producer",
    "Integrity",
    "Envelope",
    "Thread",
    "ContextPackage",
    "InheritContextFilters",
    "InheritContextRequest",
    # Protocol
    "MMIPProtocol",
    # Utilities
    "check_compliance_level",
]
