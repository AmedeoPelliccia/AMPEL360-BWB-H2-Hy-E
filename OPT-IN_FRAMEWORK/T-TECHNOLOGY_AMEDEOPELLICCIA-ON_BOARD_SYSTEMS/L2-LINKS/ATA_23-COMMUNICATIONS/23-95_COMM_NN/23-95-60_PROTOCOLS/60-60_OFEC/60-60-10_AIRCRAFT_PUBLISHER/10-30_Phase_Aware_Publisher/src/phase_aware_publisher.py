"""
Phase-Aware Publisher
OFEC-60-60-10-30 - Aircraft Publisher

This module publishes OFEC messages with phase-aware rate control.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional, Callable
import time
import threading
import queue


class FlightPhase(Enum):
    """Flight phase enumeration."""
    GROUND = 0
    TAXI = 1
    TAKEOFF = 2
    CLIMB = 3
    CRUISE = 4
    DESCENT = 5
    APPROACH = 6
    LANDING = 7


class PublishPriority(Enum):
    """Publishing priority levels."""
    LOW = 0
    MEDIUM = 1
    HIGH = 2


@dataclass
class PublishConfig:
    """Phase-specific publishing configuration."""
    rate_hz: float
    priority: PublishPriority
    preemptible: bool


class PhaseAwarePublisher:
    """
    Publishes OFEC messages with phase-aware rate control.
    
    Adjusts publishing rate and priority based on flight phase,
    and handles connection management and retry logic.
    """
    
    # Phase configurations
    PHASE_CONFIGS = {
        FlightPhase.GROUND: PublishConfig(0.1, PublishPriority.LOW, True),
        FlightPhase.TAXI: PublishConfig(0.5, PublishPriority.LOW, True),
        FlightPhase.TAKEOFF: PublishConfig(10.0, PublishPriority.HIGH, False),
        FlightPhase.CLIMB: PublishConfig(5.0, PublishPriority.MEDIUM, True),
        FlightPhase.CRUISE: PublishConfig(1.0, PublishPriority.LOW, True),
        FlightPhase.DESCENT: PublishConfig(5.0, PublishPriority.MEDIUM, True),
        FlightPhase.APPROACH: PublishConfig(10.0, PublishPriority.HIGH, False),
        FlightPhase.LANDING: PublishConfig(10.0, PublishPriority.HIGH, False)
    }
    
    # Retry configuration
    RETRY_DELAYS = [1.0, 2.0, 4.0, 8.0, 16.0, 30.0]  # Exponential backoff
    MAX_QUEUE_SIZE = 1000
    
    def __init__(
        self,
        send_func: Callable[[bytes], bool],
        aircraft_id: str
    ):
        """
        Initialize the phase-aware publisher.
        
        Args:
            send_func: Function to send encoded message (returns True on success)
            aircraft_id: Aircraft identifier
        """
        self._send_func = send_func
        self._aircraft_id = aircraft_id
        
        self._current_phase = FlightPhase.GROUND
        self._message_queue: queue.Queue = queue.Queue(maxsize=self.MAX_QUEUE_SIZE)
        self._retry_queue: queue.Queue = queue.Queue()
        
        self._running = False
        self._publish_thread: Optional[threading.Thread] = None
        self._retry_thread: Optional[threading.Thread] = None
        
        self._stats = {
            "sent": 0,
            "failed": 0,
            "retried": 0,
            "dropped": 0
        }
    
    def start(self):
        """Start the publisher threads."""
        if self._running:
            return
        
        self._running = True
        
        self._publish_thread = threading.Thread(
            target=self._publish_loop, daemon=True
        )
        self._retry_thread = threading.Thread(
            target=self._retry_loop, daemon=True
        )
        
        self._publish_thread.start()
        self._retry_thread.start()
    
    def stop(self):
        """Stop the publisher threads."""
        self._running = False
        
        if self._publish_thread:
            self._publish_thread.join(timeout=2.0)
        if self._retry_thread:
            self._retry_thread.join(timeout=2.0)
    
    def set_phase(self, phase: FlightPhase) -> None:
        """Update the current flight phase."""
        self._current_phase = phase
    
    def publish(self, message_bytes: bytes) -> bool:
        """
        Queue a message for publishing.
        
        Args:
            message_bytes: CBOR-encoded message
            
        Returns:
            True if queued successfully
        """
        try:
            self._message_queue.put_nowait(message_bytes)
            return True
        except queue.Full:
            self._stats["dropped"] += 1
            return False
    
    def _publish_loop(self):
        """Main publishing loop."""
        while self._running:
            try:
                config = self.PHASE_CONFIGS.get(
                    self._current_phase,
                    PublishConfig(1.0, PublishPriority.LOW, True)
                )
                interval = 1.0 / config.rate_hz
                
                # Get message from queue
                try:
                    message = self._message_queue.get(timeout=interval)
                except queue.Empty:
                    continue
                
                # Attempt to send
                success = self._send_func(message)
                
                if success:
                    self._stats["sent"] += 1
                else:
                    self._stats["failed"] += 1
                    # Queue for retry if not preemptible
                    if not config.preemptible:
                        self._retry_queue.put((message, 0, time.time()))
                
            except Exception as e:
                print(f"Publishing error: {e}")
                time.sleep(0.1)
    
    def _retry_loop(self):
        """Retry loop for failed messages."""
        while self._running:
            try:
                # Get message to retry
                try:
                    message, retry_count, first_attempt = self._retry_queue.get(timeout=1.0)
                except queue.Empty:
                    continue
                
                # Check if we should give up
                if retry_count >= len(self.RETRY_DELAYS):
                    self._stats["dropped"] += 1
                    continue
                
                # Wait for retry delay
                delay = self.RETRY_DELAYS[retry_count]
                time.sleep(delay)
                
                # Attempt to send
                success = self._send_func(message)
                
                if success:
                    self._stats["retried"] += 1
                    self._stats["sent"] += 1
                else:
                    # Re-queue with incremented retry count
                    self._retry_queue.put((message, retry_count + 1, first_attempt))
                
            except Exception as e:
                print(f"Retry error: {e}")
    
    @property
    def current_config(self) -> PublishConfig:
        """Get current phase configuration."""
        return self.PHASE_CONFIGS.get(
            self._current_phase,
            PublishConfig(1.0, PublishPriority.LOW, True)
        )
    
    @property
    def stats(self) -> Dict:
        """Get publishing statistics."""
        return self._stats.copy()
    
    @property
    def queue_depth(self) -> int:
        """Get current queue depth."""
        return self._message_queue.qsize()
