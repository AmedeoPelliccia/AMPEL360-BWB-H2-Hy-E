# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
State tracker for AMPEL360 digital twin synchronization.

This module provides state tracking and delta detection for
identifying changes between synchronization cycles.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional
import copy
import logging

logger = logging.getLogger(__name__)


@dataclass
class StateChange:
    """Represents a state change."""

    field: str
    old_value: Any
    new_value: Any
    timestamp: datetime = field(default_factory=datetime.utcnow)
    change_type: str = "update"  # update, add, remove


@dataclass
class StateSnapshot:
    """Snapshot of state at a point in time."""

    state: dict[str, Any]
    timestamp: datetime = field(default_factory=datetime.utcnow)
    version: int = 0


class StateTracker:
    """
    Tracks state changes and calculates deltas between updates.

    Maintains history of state changes for audit and rollback capabilities.

    Attributes:
        model_id: Identifier of the model being tracked
        max_history: Maximum number of historical snapshots to retain
    """

    def __init__(
        self,
        model_id: str,
        max_history: int = 100,
    ) -> None:
        """
        Initialize the state tracker.

        Args:
            model_id: Identifier for the model
            max_history: Maximum history size
        """
        self.model_id = model_id
        self.max_history = max_history

        self._current_state: dict[str, Any] = {}
        self._history: list[StateSnapshot] = []
        self._pending_changes: list[StateChange] = []
        self._version = 0

        logger.info("Initialized StateTracker for %s", model_id)

    def update(self, new_state: dict[str, Any]) -> list[StateChange]:
        """
        Update state and return detected changes.

        Args:
            new_state: New state data

        Returns:
            List of detected state changes
        """
        changes = self._calculate_delta(self._current_state, new_state)

        if changes:
            # Save current state to history
            self._save_snapshot()

            # Apply new state
            self._current_state = copy.deepcopy(new_state)
            self._version += 1
            self._pending_changes.extend(changes)

            logger.debug(
                "State updated for %s: %d changes, version %d",
                self.model_id,
                len(changes),
                self._version,
            )

        return changes

    def get_current_state(self) -> dict[str, Any]:
        """
        Get the current state.

        Returns:
            Copy of current state
        """
        return copy.deepcopy(self._current_state)

    def get_version(self) -> int:
        """Get current state version."""
        return self._version

    def get_changes_since(self, version: int) -> list[StateChange]:
        """
        Get all changes since a specific version.

        Args:
            version: Version number to compare from

        Returns:
            List of changes since that version
        """
        changes = []
        for i, snapshot in enumerate(self._history):
            if snapshot.version > version:
                # Calculate delta from previous snapshot
                prev_state = self._history[i - 1].state if i > 0 else {}
                changes.extend(self._calculate_delta(prev_state, snapshot.state))
        return changes

    def get_pending_changes(self) -> list[StateChange]:
        """
        Get and clear pending changes.

        Returns:
            List of pending changes
        """
        changes = self._pending_changes.copy()
        self._pending_changes.clear()
        return changes

    def rollback(self, version: int) -> bool:
        """
        Rollback state to a specific version.

        Args:
            version: Target version number

        Returns:
            True if rollback was successful
        """
        for snapshot in reversed(self._history):
            if snapshot.version == version:
                self._current_state = copy.deepcopy(snapshot.state)
                self._version = version
                logger.info("Rolled back %s to version %d", self.model_id, version)
                return True

        logger.warning("Version %d not found in history", version)
        return False

    def get_history(self, limit: int = 10) -> list[dict[str, Any]]:
        """
        Get recent state history.

        Args:
            limit: Maximum number of snapshots to return

        Returns:
            List of historical snapshots
        """
        recent = self._history[-limit:]
        return [
            {
                "version": s.version,
                "timestamp": s.timestamp.isoformat(),
                "state": s.state,
            }
            for s in recent
        ]

    def clear_history(self) -> None:
        """Clear state history."""
        self._history.clear()
        logger.info("Cleared history for %s", self.model_id)

    def _calculate_delta(
        self, old_state: dict[str, Any], new_state: dict[str, Any]
    ) -> list[StateChange]:
        """Calculate differences between two states."""
        changes = []

        # Check for updates and additions
        for key, new_value in new_state.items():
            if key not in old_state:
                changes.append(
                    StateChange(
                        field=key,
                        old_value=None,
                        new_value=new_value,
                        change_type="add",
                    )
                )
            elif old_state[key] != new_value:
                changes.append(
                    StateChange(
                        field=key,
                        old_value=old_state[key],
                        new_value=new_value,
                        change_type="update",
                    )
                )

        # Check for removals
        for key in old_state:
            if key not in new_state:
                changes.append(
                    StateChange(
                        field=key,
                        old_value=old_state[key],
                        new_value=None,
                        change_type="remove",
                    )
                )

        return changes

    def _save_snapshot(self) -> None:
        """Save current state to history."""
        snapshot = StateSnapshot(
            state=copy.deepcopy(self._current_state),
            version=self._version,
        )

        self._history.append(snapshot)

        # Trim history if needed
        if len(self._history) > self.max_history:
            self._history = self._history[-self.max_history :]

    def compare_states(
        self, version_a: int, version_b: int
    ) -> list[StateChange]:
        """
        Compare two historical versions.

        Args:
            version_a: First version
            version_b: Second version

        Returns:
            List of differences
        """
        state_a: dict[str, Any] = {}
        state_b: dict[str, Any] = {}

        for snapshot in self._history:
            if snapshot.version == version_a:
                state_a = snapshot.state
            if snapshot.version == version_b:
                state_b = snapshot.state

        if not state_a and not state_b:
            return []

        return self._calculate_delta(state_a, state_b)

    def has_changed(self, field: str, since_version: Optional[int] = None) -> bool:
        """
        Check if a specific field has changed.

        Args:
            field: Field name to check
            since_version: Version to compare from (default: previous)

        Returns:
            True if field has changed
        """
        if since_version is None:
            since_version = max(0, self._version - 1)

        changes = self.get_changes_since(since_version)
        return any(c.field == field for c in changes)
