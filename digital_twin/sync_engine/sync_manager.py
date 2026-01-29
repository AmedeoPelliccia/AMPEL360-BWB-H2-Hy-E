# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Synchronization manager for AMPEL360 digital twin.

This module provides the main synchronization manager that coordinates
real-time updates between physical sensors and digital twin models.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Optional
import logging
import threading
import time

logger = logging.getLogger(__name__)


class SyncStatus(Enum):
    """Synchronization status enumeration."""

    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    PAUSED = "paused"
    ERROR = "error"


@dataclass
class SyncMetrics:
    """Metrics for synchronization performance."""

    updates_total: int = 0
    updates_successful: int = 0
    updates_failed: int = 0
    conflicts_resolved: int = 0
    average_latency_ms: float = 0.0
    last_sync_time: Optional[datetime] = None


class SyncManager:
    """
    Manager for real-time synchronization between physical and digital twin.

    Coordinates state updates across multiple models, handles conflict
    resolution, and maintains synchronization metrics.

    Attributes:
        update_interval_ms: Interval between sync updates in milliseconds
        conflict_strategy: Strategy for resolving conflicts
        status: Current synchronization status
    """

    def __init__(
        self,
        update_interval_ms: int = 1000,
        conflict_strategy: str = "last_write_wins",
        max_queue_size: int = 1000,
    ) -> None:
        """
        Initialize the sync manager.

        Args:
            update_interval_ms: Update interval in milliseconds
            conflict_strategy: Conflict resolution strategy
            max_queue_size: Maximum pending update queue size
        """
        self.update_interval_ms = update_interval_ms
        self.conflict_strategy = conflict_strategy
        self.max_queue_size = max_queue_size
        self.status = SyncStatus.STOPPED

        self._models: dict[str, Any] = {}
        self._state_trackers: dict[str, Any] = {}
        self._update_queue: list[dict[str, Any]] = []
        self._metrics = SyncMetrics()
        self._callbacks: dict[str, list[Callable]] = {
            "on_update": [],
            "on_conflict": [],
            "on_error": [],
        }

        self._sync_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self._lock = threading.Lock()

        logger.info(
            "Initialized SyncManager: interval=%dms, strategy=%s",
            update_interval_ms,
            conflict_strategy,
        )

    def register_model(self, model_id: str, model: Any) -> bool:
        """
        Register a model for synchronization.

        Args:
            model_id: Identifier for the model
            model: Model instance to register

        Returns:
            True if registration was successful
        """
        with self._lock:
            if model_id in self._models:
                logger.warning("Model already registered: %s", model_id)
                return False

            self._models[model_id] = model
            logger.info("Registered model: %s", model_id)
            return True

    def unregister_model(self, model_id: str) -> bool:
        """
        Unregister a model from synchronization.

        Args:
            model_id: Identifier of the model to unregister

        Returns:
            True if unregistration was successful
        """
        with self._lock:
            if model_id not in self._models:
                logger.warning("Model not found: %s", model_id)
                return False

            del self._models[model_id]
            if model_id in self._state_trackers:
                del self._state_trackers[model_id]

            logger.info("Unregistered model: %s", model_id)
            return True

    def start(self) -> bool:
        """
        Start the synchronization engine.

        Returns:
            True if started successfully
        """
        if self.status == SyncStatus.RUNNING:
            logger.warning("Sync manager already running")
            return False

        self.status = SyncStatus.STARTING
        self._stop_event.clear()

        self._sync_thread = threading.Thread(target=self._sync_loop, daemon=True)
        self._sync_thread.start()

        self.status = SyncStatus.RUNNING
        logger.info("Sync manager started")
        return True

    def stop(self) -> bool:
        """
        Stop the synchronization engine.

        Returns:
            True if stopped successfully
        """
        if self.status == SyncStatus.STOPPED:
            return True

        self._stop_event.set()

        if self._sync_thread and self._sync_thread.is_alive():
            self._sync_thread.join(timeout=5.0)

        self.status = SyncStatus.STOPPED
        logger.info("Sync manager stopped")
        return True

    def pause(self) -> bool:
        """Pause synchronization."""
        if self.status == SyncStatus.RUNNING:
            self.status = SyncStatus.PAUSED
            logger.info("Sync manager paused")
            return True
        return False

    def resume(self) -> bool:
        """Resume synchronization."""
        if self.status == SyncStatus.PAUSED:
            self.status = SyncStatus.RUNNING
            logger.info("Sync manager resumed")
            return True
        return False

    def push_state(self, model_id: str, state_data: dict[str, Any]) -> bool:
        """
        Push a state update for a model.

        Args:
            model_id: Target model identifier
            state_data: State data to push

        Returns:
            True if update was queued successfully
        """
        if model_id not in self._models:
            logger.warning("Model not found: %s", model_id)
            return False

        with self._lock:
            if len(self._update_queue) >= self.max_queue_size:
                logger.warning("Update queue full, dropping oldest update")
                self._update_queue.pop(0)

            self._update_queue.append(
                {
                    "model_id": model_id,
                    "state_data": state_data,
                    "timestamp": datetime.utcnow(),
                }
            )

        return True

    def get_state(self, model_id: str) -> Optional[dict[str, Any]]:
        """
        Get current state of a model.

        Args:
            model_id: Model identifier

        Returns:
            Current state or None if model not found
        """
        if model_id not in self._models:
            return None

        model = self._models[model_id]
        if hasattr(model, "get_state"):
            return model.get_state().__dict__
        elif hasattr(model, "to_dict"):
            return model.to_dict()
        return None

    def get_metrics(self) -> dict[str, Any]:
        """
        Get synchronization metrics.

        Returns:
            Dictionary containing metrics
        """
        return {
            "updates_total": self._metrics.updates_total,
            "updates_successful": self._metrics.updates_successful,
            "updates_failed": self._metrics.updates_failed,
            "success_rate": (
                self._metrics.updates_successful / max(self._metrics.updates_total, 1)
            ),
            "conflicts_resolved": self._metrics.conflicts_resolved,
            "average_latency_ms": self._metrics.average_latency_ms,
            "last_sync_time": (
                self._metrics.last_sync_time.isoformat()
                if self._metrics.last_sync_time
                else None
            ),
            "queue_size": len(self._update_queue),
            "registered_models": list(self._models.keys()),
            "status": self.status.value,
        }

    def add_callback(self, event: str, callback: Callable) -> bool:
        """
        Add a callback for sync events.

        Args:
            event: Event name (on_update, on_conflict, on_error)
            callback: Callback function

        Returns:
            True if callback was added
        """
        if event not in self._callbacks:
            logger.warning("Unknown event: %s", event)
            return False

        self._callbacks[event].append(callback)
        return True

    def _sync_loop(self) -> None:
        """Main synchronization loop."""
        while not self._stop_event.is_set():
            if self.status == SyncStatus.RUNNING:
                self._process_updates()

            time.sleep(self.update_interval_ms / 1000.0)

    def _process_updates(self) -> None:
        """Process pending updates from the queue."""
        with self._lock:
            updates = self._update_queue.copy()
            self._update_queue.clear()

        for update in updates:
            self._apply_update(update)

    def _apply_update(self, update: dict[str, Any]) -> None:
        """Apply a single update to a model."""
        model_id = update["model_id"]
        state_data = update["state_data"]
        timestamp = update["timestamp"]

        start_time = time.time()
        self._metrics.updates_total += 1

        try:
            model = self._models.get(model_id)
            if not model:
                raise ValueError(f"Model not found: {model_id}")

            # Apply update
            if hasattr(model, "update"):
                success = model.update(state_data)
            else:
                logger.warning("Model %s has no update method", model_id)
                success = False

            latency_ms = (time.time() - start_time) * 1000

            if success:
                self._metrics.updates_successful += 1
                self._update_latency(latency_ms)
                self._metrics.last_sync_time = datetime.utcnow()

                # Trigger callbacks
                for callback in self._callbacks["on_update"]:
                    try:
                        callback(model_id, state_data)
                    except Exception as e:
                        logger.error("Callback error: %s", e)

            else:
                self._metrics.updates_failed += 1
                logger.warning("Update failed for model: %s", model_id)

        except Exception as e:
            self._metrics.updates_failed += 1
            self.status = SyncStatus.ERROR
            logger.error("Error applying update to %s: %s", model_id, e)

            # Trigger error callbacks
            for callback in self._callbacks["on_error"]:
                try:
                    callback(model_id, str(e))
                except Exception as cb_err:
                    logger.error("Error callback error: %s", cb_err)

    def _update_latency(self, latency_ms: float) -> None:
        """Update average latency metric."""
        n = self._metrics.updates_successful
        old_avg = self._metrics.average_latency_ms
        self._metrics.average_latency_ms = old_avg + (latency_ms - old_avg) / n

    def force_sync(self, model_id: Optional[str] = None) -> bool:
        """
        Force immediate synchronization.

        Args:
            model_id: Specific model to sync, or None for all

        Returns:
            True if sync was triggered
        """
        if model_id:
            if model_id in self._models:
                model = self._models[model_id]
                if hasattr(model, "validate"):
                    model.validate()
                return True
            return False

        # Sync all models
        for mid in self._models:
            model = self._models[mid]
            if hasattr(model, "validate"):
                model.validate()

        return True
