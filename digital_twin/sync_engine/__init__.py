# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Synchronization engine for AMPEL360 digital twin.

This module provides real-time synchronization between the physical aircraft
and its digital twin representation.

Classes:
    SyncManager: Main synchronization manager
    StateTracker: State tracking and delta detection
    ConflictResolver: Conflict resolution strategies
"""

from digital_twin.sync_engine.sync_manager import SyncManager, SyncStatus
from digital_twin.sync_engine.state_tracker import StateTracker, StateChange
from digital_twin.sync_engine.conflict_resolver import ConflictResolver, ConflictType

__all__ = [
    "SyncManager",
    "SyncStatus",
    "StateTracker",
    "StateChange",
    "ConflictResolver",
    "ConflictType",
]
