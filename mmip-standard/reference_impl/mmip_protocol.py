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
MMIP v0.1 — Reference Python API Implementation

A reference implementation skeleton for the Models Memory Inheritance Protocol.
This module provides abstract base classes and type definitions for MMIP compliance.

This implementation is NON-NORMATIVE and serves as a starting point for
developers implementing MMIP-compliant systems.

Reference: spec/mmip-v0.1.md
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional


# --- Enums ---


class CapsuleType(str, Enum):
    """Types of memory capsules as defined in MMIP v0.1 Section 4.1."""

    USER_MESSAGE = "user_message"
    MODEL_MESSAGE = "model_message"
    SUMMARY = "summary"
    ANNOTATION = "annotation"
    UPLOAD = "upload"
    FILE_REF = "file_ref"
    METADATA = "metadata"


class Scope(str, Enum):
    """Scope/lifetime of capsules as defined in MMIP v0.1 Section 4.1."""

    USER_LONG_TERM = "user_long_term"
    SESSION = "session"
    TASK = "task"
    AGENT_LOCAL = "agent_local"


class ExportPolicy(str, Enum):
    """Export policies as defined in MMIP v0.1 Section 5."""

    ALLOW = "allow"
    REDACT = "redact"
    FORBID = "forbid"


class RetentionPolicy(str, Enum):
    """Retention policies as defined in MMIP v0.1 Section 5."""

    EPHEMERAL = "ephemeral"
    SESSION = "session"
    LONG_TERM = "long_term"
    NEVER_PERSIST = "never_persist"


class ProducerType(str, Enum):
    """Types of envelope producers as defined in MMIP v0.1 Section 4.4."""

    MODEL = "model"
    AGENT = "agent"
    TOOL = "tool"
    USER = "user"
    SYSTEM = "system"


class ApplyMode(str, Enum):
    """Modes for applying context packages as defined in MMIP v0.1 Section 7.3."""

    READ_ONLY = "read_only"
    EXTENDABLE = "extendable"
    FORK_INTO_NEW_THREAD = "fork_into_new_thread"


# --- Data Classes ---


@dataclass
class Provenance:
    """Provenance information for capsules and envelopes."""

    timestamp: datetime
    creator_id: Optional[str] = None
    creator_type: Optional[ProducerType] = None
    source_tool: Optional[str] = None
    source_capsule_ids: List[str] = field(default_factory=list)


class LinkType(str, Enum):
    """Types of links between capsules in the DAG."""

    SUMMARIZES = "summarizes"
    DERIVED_FROM = "derived_from"
    REPLIES_TO = "replies_to"
    REFERENCES = "references"


@dataclass
class CapsuleLink:
    """Link between capsules in the DAG."""

    link_type: LinkType
    target_id: str


@dataclass
class Policies:
    """Policy configuration for capsules and envelopes."""

    export: ExportPolicy = ExportPolicy.ALLOW
    visibility: List[str] = field(default_factory=lambda: ["owner_only"])
    retention: RetentionPolicy = RetentionPolicy.SESSION
    redaction_rules: List[str] = field(default_factory=list)


@dataclass
class Metadata:
    """Metadata for capsules."""

    tags: List[str] = field(default_factory=list)
    domain: Optional[str] = None
    token_count: Optional[int] = None
    size_bytes: Optional[int] = None
    embedding_ref: Optional[str] = None


@dataclass
class Capsule:
    """
    Memory Capsule as defined in MMIP v0.1 Section 4.1.

    Atomic unit of memory containing content, metadata, scopes, and policies.
    """

    capsule_id: str
    capsule_type: CapsuleType
    scope: Scope
    content: Dict[str, Any]
    provenance: Provenance
    metadata: Optional[Metadata] = None
    policies: Optional[Policies] = None
    links: List[CapsuleLink] = field(default_factory=list)
    extensions: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Producer:
    """Information about the producer of an envelope."""

    producer_id: str
    role: str
    producer_type: Optional[ProducerType] = None
    name: Optional[str] = None
    version: Optional[str] = None


@dataclass
class Integrity:
    """Integrity verification information."""

    hash_value: Optional[str] = None
    signature: Optional[str] = None
    signed_by: Optional[str] = None
    signed_at: Optional[datetime] = None


@dataclass
class Envelope:
    """
    Memory Envelope as defined in MMIP v0.1 Section 4.4.

    The subset of memory delivered to a model/tool for a single call.
    """

    mmip_version: str
    context_id: str
    producer: Producer
    capsules: List[Capsule]
    thread_id: Optional[str] = None
    policies: Optional[Policies] = None
    links: List[Dict[str, str]] = field(default_factory=list)
    integrity: Optional[Integrity] = None
    extensions: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Thread:
    """
    Memory Thread as defined in MMIP v0.1 Section 4.2.

    A chain or DAG of capsules representing a persistent contextual sequence.
    """

    thread_id: str
    capsules: List[Capsule]
    title: Optional[str] = None
    domain: Optional[str] = None
    participants: List[str] = field(default_factory=list)
    retention: Optional[RetentionPolicy] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ContextPackage:
    """
    Context Package as defined in MMIP v0.1 Section 4.3.

    A named, user-definable bundle of capsules and summaries.
    """

    package_id: str
    owner: str
    name: str
    capsule_refs: List[str]
    description: Optional[str] = None
    policies: Optional[Policies] = None
    summary_capsule: Optional[Capsule] = None
    tags: List[str] = field(default_factory=list)
    provenance: Optional[Provenance] = None


@dataclass
class InheritContextFilters:
    """Filters for the INHERIT_CONTEXT operation."""

    capsule_types: Optional[List[CapsuleType]] = None
    scopes: Optional[List[Scope]] = None
    tags: Optional[List[str]] = None
    since: Optional[datetime] = None
    max_count: Optional[int] = None


@dataclass
class InheritContextRequest:
    """Request for the INHERIT_CONTEXT operation."""

    thread_id: Optional[str] = None
    package_ids: Optional[List[str]] = None
    filters: Optional[InheritContextFilters] = None
    policies: Optional[Policies] = None
    max_tokens: Optional[int] = None
    summarization_profile: Optional[str] = None


# --- Abstract Protocol Interface ---


class MMIPProtocol(ABC):
    """
    Abstract Base Class for MMIP compliance.

    Implementations MUST provide all abstract methods to achieve
    Level 1 compliance. Additional methods are required for
    Level 2 and Level 3 compliance as specified in Section 13.
    """

    # --- Thread Operations (Section 7.1) ---

    @abstractmethod
    def init_thread(self, metadata: Optional[Dict[str, Any]] = None) -> str:
        """
        Create a new thread.

        Args:
            metadata: Optional thread metadata (title, domain, etc.)

        Returns:
            The thread_id of the newly created thread.
        """

    @abstractmethod
    def attach_memory(self, thread_id: str, capsule: Capsule) -> bool:
        """
        Add a capsule to a thread.

        Args:
            thread_id: ID of the thread to attach to.
            capsule: The capsule to attach.

        Returns:
            True if successful, False otherwise.
        """

    @abstractmethod
    def inherit_context(self, request: InheritContextRequest) -> Envelope:
        """
        The core MMIP verb. Retrieve context as an envelope.

        This operation:
        1. Fetches capsules from the specified thread/packages
        2. Applies policy filters (redaction, visibility)
        3. Summarizes if token count exceeds max_tokens
        4. Returns an immutable Memory Envelope

        Args:
            request: The context inheritance request parameters.

        Returns:
            A Memory Envelope ready for model/tool consumption.
        """

    @abstractmethod
    def fork_thread(self, thread_id: str) -> str:
        """
        Create a branch from an existing thread.

        Args:
            thread_id: ID of the thread to fork.

        Returns:
            The thread_id of the new forked thread.
        """

    @abstractmethod
    def merge_threads(self, thread_id_a: str, thread_id_b: str) -> str:
        """
        Combine two threads.

        Args:
            thread_id_a: First thread ID.
            thread_id_b: Second thread ID.

        Returns:
            The thread_id of the merged thread.
        """

    @abstractmethod
    def snapshot_thread(self, thread_id: str) -> str:
        """
        Create a portable Context Package from a thread.

        Args:
            thread_id: ID of the thread to snapshot.

        Returns:
            The package_id of the created package.
        """

    # --- Capsule Operations (Section 7.2) ---

    @abstractmethod
    def list_capsules(
        self, thread_id: str, filters: Optional[InheritContextFilters] = None
    ) -> List[Capsule]:
        """
        List capsules matching criteria.

        Args:
            thread_id: ID of the thread to list from.
            filters: Optional filters to apply.

        Returns:
            List of matching capsules.
        """

    @abstractmethod
    def get_capsule(self, capsule_id: str) -> Optional[Capsule]:
        """
        Retrieve a specific capsule.

        Args:
            capsule_id: ID of the capsule to retrieve.

        Returns:
            The capsule if found, None otherwise.
        """

    @abstractmethod
    def tag_capsules(self, capsule_ids: List[str], tags: List[str]) -> bool:
        """
        Add tags to capsules.

        Args:
            capsule_ids: IDs of capsules to tag.
            tags: Tags to add.

        Returns:
            True if successful, False otherwise.
        """

    @abstractmethod
    def redact_capsule(self, capsule_id: str, rule_set: List[str]) -> Capsule:
        """
        Apply redaction rules to a capsule.

        Args:
            capsule_id: ID of the capsule to redact.
            rule_set: Redaction rules to apply.

        Returns:
            The redacted capsule (or a redaction tombstone).
        """

    @abstractmethod
    def delete_capsule(self, capsule_id: str) -> bool:
        """
        Soft delete a capsule.

        Args:
            capsule_id: ID of the capsule to delete.

        Returns:
            True if successful, False otherwise.
        """

    # --- Context Package Operations (Section 7.3) ---

    @abstractmethod
    def create_context_package(
        self,
        name: str,
        capsule_refs: List[str],
        policies: Optional[Policies] = None,
    ) -> str:
        """
        Create a new context package.

        Args:
            name: Human-readable name for the package.
            capsule_refs: List of capsule IDs to include.
            policies: Optional policies for the package.

        Returns:
            The package_id of the created package.
        """

    @abstractmethod
    def get_context_package(self, package_id: str) -> Optional[ContextPackage]:
        """
        Retrieve a context package.

        Args:
            package_id: ID of the package to retrieve.

        Returns:
            The package if found, None otherwise.
        """

    @abstractmethod
    def list_context_packages(self, owner: str) -> List[ContextPackage]:
        """
        List packages for an owner.

        Args:
            owner: Owner ID to list packages for.

        Returns:
            List of packages owned by the specified owner.
        """

    @abstractmethod
    def export_context_package(
        self, package_id: str, format_type: str = "json"
    ) -> Dict[str, Any]:
        """
        Export a package in the specified format.

        Args:
            package_id: ID of the package to export.
            format_type: Export format (default: "json").

        Returns:
            The exported package data.
        """

    @abstractmethod
    def apply_context_package(
        self,
        session_id: str,
        package_id: str,
        mode: ApplyMode = ApplyMode.READ_ONLY,
    ) -> bool:
        """
        Apply a package to a session.

        Args:
            session_id: ID of the session to apply to.
            package_id: ID of the package to apply.
            mode: Application mode.

        Returns:
            True if successful, False otherwise.
        """

    # --- Envelope Operations (Section 7.4) ---

    @abstractmethod
    def generate_envelope(
        self,
        thread_id: Optional[str] = None,
        package_id: Optional[str] = None,
        filters: Optional[InheritContextFilters] = None,
    ) -> Envelope:
        """
        Generate a memory envelope.

        Args:
            thread_id: Optional thread ID to generate from.
            package_id: Optional package ID to generate from.
            filters: Optional filters to apply.

        Returns:
            The generated envelope.
        """

    @abstractmethod
    def validate_envelope(self, envelope: Envelope) -> bool:
        """
        Validate an envelope against the MMIP schema.

        Args:
            envelope: The envelope to validate.

        Returns:
            True if valid, False otherwise.
        """

    # --- Search Operations (Section 7.5) ---

    @abstractmethod
    def search_memory(
        self,
        query: str,
        filters: Optional[InheritContextFilters] = None,
    ) -> List[Capsule]:
        """
        Search capsules.

        Args:
            query: Search query.
            filters: Optional filters to apply.

        Returns:
            List of matching capsules.
        """

    @abstractmethod
    def search_packages(
        self,
        query: str,
        tags: Optional[List[str]] = None,
    ) -> List[ContextPackage]:
        """
        Search packages.

        Args:
            query: Search query.
            tags: Optional tags to filter by.

        Returns:
            List of matching packages.
        """


# --- Compliance Level Checker ---


def check_compliance_level(implementation: MMIPProtocol) -> int:
    """
    Check the compliance level of an MMIP implementation.

    Returns:
        1 for Level 1 (Basic)
        2 for Level 2 (User-Controlled Memory)
        3 for Level 3 (Full Agentic Interoperability)
    """
    # Level 1: Basic - capsules, threads, envelopes
    level_1_methods = [
        "init_thread",
        "attach_memory",
        "inherit_context",
        "list_capsules",
        "get_capsule",
        "generate_envelope",
        "validate_envelope",
    ]

    # Level 2: User-Controlled - adds packages, export, redaction
    level_2_methods = [
        "create_context_package",
        "get_context_package",
        "list_context_packages",
        "export_context_package",
        "redact_capsule",
        "delete_capsule",
    ]

    # Level 3: Full Agentic - adds inheritance, summarization, lineage
    level_3_methods = [
        "fork_thread",
        "merge_threads",
        "snapshot_thread",
        "apply_context_package",
        "search_memory",
        "search_packages",
        "tag_capsules",
    ]

    has_level_1 = all(
        hasattr(implementation, method) and callable(getattr(implementation, method))
        for method in level_1_methods
    )
    has_level_2 = all(
        hasattr(implementation, method) and callable(getattr(implementation, method))
        for method in level_2_methods
    )
    has_level_3 = all(
        hasattr(implementation, method) and callable(getattr(implementation, method))
        for method in level_3_methods
    )

    if has_level_1 and has_level_2 and has_level_3:
        return 3
    elif has_level_1 and has_level_2:
        return 2
    elif has_level_1:
        return 1
    return 0
