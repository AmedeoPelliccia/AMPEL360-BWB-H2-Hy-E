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
