# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Conflict resolver for AMPEL360 digital twin synchronization.

This module provides conflict resolution strategies for handling
concurrent updates to the digital twin.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Optional
import logging

logger = logging.getLogger(__name__)


class ConflictType(Enum):
    """Types of synchronization conflicts."""

    VALUE_MISMATCH = "value_mismatch"
    CONCURRENT_UPDATE = "concurrent_update"
    VERSION_CONFLICT = "version_conflict"
    TYPE_MISMATCH = "type_mismatch"
    CONSTRAINT_VIOLATION = "constraint_violation"


@dataclass
class Conflict:
    """Represents a synchronization conflict."""

    conflict_type: ConflictType
    field: str
    source_value: Any
    target_value: Any
    source_timestamp: datetime
    target_timestamp: datetime
    resolved: bool = False
    resolution: Optional[Any] = None
    resolution_strategy: str = ""


@dataclass
class ResolutionResult:
    """Result of conflict resolution."""

    resolved: bool
    final_value: Any
    strategy_used: str
    conflicts_resolved: int
    manual_review_required: bool = False
    notes: str = ""


class ConflictResolver:
    """
    Resolves conflicts during digital twin synchronization.

    Supports multiple resolution strategies including automatic
    and manual resolution workflows.

    Attributes:
        default_strategy: Default conflict resolution strategy
    """

    STRATEGIES = [
        "last_write_wins",
        "first_write_wins",
        "source_wins",
        "target_wins",
        "merge",
        "manual",
        "custom",
    ]

    def __init__(
        self,
        default_strategy: str = "last_write_wins",
        custom_resolver: Optional[Callable] = None,
    ) -> None:
        """
        Initialize the conflict resolver.

        Args:
            default_strategy: Default resolution strategy
            custom_resolver: Optional custom resolution function
        """
        if default_strategy not in self.STRATEGIES:
            logger.warning(
                "Unknown strategy '%s', defaulting to last_write_wins",
                default_strategy,
            )
            default_strategy = "last_write_wins"

        self.default_strategy = default_strategy
        self._custom_resolver = custom_resolver
        self._pending_conflicts: list[Conflict] = []
        self._resolved_conflicts: list[Conflict] = []
        self._field_strategies: dict[str, str] = {}

        logger.info("Initialized ConflictResolver with strategy: %s", default_strategy)

    def detect_conflict(
        self,
        field: str,
        source_value: Any,
        target_value: Any,
        source_timestamp: datetime,
        target_timestamp: datetime,
    ) -> Optional[Conflict]:
        """
        Detect if there is a conflict between values.

        Args:
            field: Field name
            source_value: Value from source
            target_value: Value from target
            source_timestamp: Source update timestamp
            target_timestamp: Target update timestamp

        Returns:
            Conflict object if conflict detected, None otherwise
        """
        if source_value == target_value:
            return None

        # Determine conflict type
        if type(source_value) != type(target_value):
            conflict_type = ConflictType.TYPE_MISMATCH
        elif abs((source_timestamp - target_timestamp).total_seconds()) < 1.0:
            conflict_type = ConflictType.CONCURRENT_UPDATE
        else:
            conflict_type = ConflictType.VALUE_MISMATCH

        conflict = Conflict(
            conflict_type=conflict_type,
            field=field,
            source_value=source_value,
            target_value=target_value,
            source_timestamp=source_timestamp,
            target_timestamp=target_timestamp,
        )

        self._pending_conflicts.append(conflict)
        logger.debug("Conflict detected: %s (%s)", field, conflict_type.value)

        return conflict

    def resolve(
        self,
        conflict: Conflict,
        strategy: Optional[str] = None,
    ) -> ResolutionResult:
        """
        Resolve a single conflict.

        Args:
            conflict: Conflict to resolve
            strategy: Strategy to use (defaults to default_strategy)

        Returns:
            ResolutionResult with resolved value
        """
        strategy = strategy or self._get_strategy_for_field(conflict.field)

        if strategy == "last_write_wins":
            final_value = self._last_write_wins(conflict)
        elif strategy == "first_write_wins":
            final_value = self._first_write_wins(conflict)
        elif strategy == "source_wins":
            final_value = conflict.source_value
        elif strategy == "target_wins":
            final_value = conflict.target_value
        elif strategy == "merge":
            final_value = self._merge_values(conflict)
        elif strategy == "custom" and self._custom_resolver:
            final_value = self._custom_resolver(conflict)
        elif strategy == "manual":
            return ResolutionResult(
                resolved=False,
                final_value=None,
                strategy_used="manual",
                conflicts_resolved=0,
                manual_review_required=True,
                notes="Manual review required",
            )
        else:
            final_value = self._last_write_wins(conflict)
            strategy = "last_write_wins"

        conflict.resolved = True
        conflict.resolution = final_value
        conflict.resolution_strategy = strategy

        self._pending_conflicts.remove(conflict)
        self._resolved_conflicts.append(conflict)

        logger.debug(
            "Resolved conflict for %s using %s: %s",
            conflict.field,
            strategy,
            final_value,
        )

        return ResolutionResult(
            resolved=True,
            final_value=final_value,
            strategy_used=strategy,
            conflicts_resolved=1,
        )

    def resolve_all(
        self, strategy: Optional[str] = None
    ) -> list[ResolutionResult]:
        """
        Resolve all pending conflicts.

        Args:
            strategy: Strategy to use for all conflicts

        Returns:
            List of resolution results
        """
        results = []
        # Create copy since resolve() modifies the list
        conflicts = self._pending_conflicts.copy()

        for conflict in conflicts:
            result = self.resolve(conflict, strategy)
            results.append(result)

        return results

    def set_field_strategy(self, field: str, strategy: str) -> bool:
        """
        Set specific strategy for a field.

        Args:
            field: Field name
            strategy: Strategy to use

        Returns:
            True if strategy was set
        """
        if strategy not in self.STRATEGIES:
            logger.warning("Invalid strategy: %s", strategy)
            return False

        self._field_strategies[field] = strategy
        logger.info("Set strategy for %s: %s", field, strategy)
        return True

    def get_pending_conflicts(self) -> list[Conflict]:
        """Get list of pending (unresolved) conflicts."""
        return self._pending_conflicts.copy()

    def get_resolved_conflicts(self) -> list[Conflict]:
        """Get list of resolved conflicts."""
        return self._resolved_conflicts.copy()

    def clear_resolved(self) -> None:
        """Clear resolved conflicts history."""
        self._resolved_conflicts.clear()

    def get_statistics(self) -> dict[str, Any]:
        """
        Get conflict resolution statistics.

        Returns:
            Dictionary of statistics
        """
        total_resolved = len(self._resolved_conflicts)
        strategies_used: dict[str, int] = {}

        for conflict in self._resolved_conflicts:
            strategy = conflict.resolution_strategy
            strategies_used[strategy] = strategies_used.get(strategy, 0) + 1

        return {
            "pending_conflicts": len(self._pending_conflicts),
            "total_resolved": total_resolved,
            "strategies_used": strategies_used,
            "default_strategy": self.default_strategy,
            "field_strategies": self._field_strategies.copy(),
        }

    def _get_strategy_for_field(self, field: str) -> str:
        """Get the appropriate strategy for a field."""
        return self._field_strategies.get(field, self.default_strategy)

    def _last_write_wins(self, conflict: Conflict) -> Any:
        """Resolve using last write wins strategy."""
        if conflict.source_timestamp > conflict.target_timestamp:
            return conflict.source_value
        return conflict.target_value

    def _first_write_wins(self, conflict: Conflict) -> Any:
        """Resolve using first write wins strategy."""
        if conflict.source_timestamp < conflict.target_timestamp:
            return conflict.source_value
        return conflict.target_value

    def _merge_values(self, conflict: Conflict) -> Any:
        """
        Attempt to merge conflicting values.

        Works best for dictionaries and lists.
        """
        source = conflict.source_value
        target = conflict.target_value

        # Merge dictionaries
        if isinstance(source, dict) and isinstance(target, dict):
            merged = target.copy()
            merged.update(source)  # Source wins for overlapping keys
            return merged

        # Merge lists
        if isinstance(source, list) and isinstance(target, list):
            # Return union of both lists
            return list(set(source + target))

        # Cannot merge, fall back to last write wins
        return self._last_write_wins(conflict)

    def set_custom_resolver(self, resolver: Callable) -> None:
        """
        Set a custom resolution function.

        Args:
            resolver: Function that takes a Conflict and returns resolved value
        """
        self._custom_resolver = resolver
        logger.info("Custom resolver set")
