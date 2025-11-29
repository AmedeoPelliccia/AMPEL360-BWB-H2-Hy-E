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
Envelope Sampler
OFEC-23-95-67-11 - Aircraft Publisher

This module samples envelope analytics data at phase-appropriate rates.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional, Callable
import time
import threading
from collections import deque


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


@dataclass
class EnvelopeSample:
    """Single envelope data sample."""
    timestamp: float
    margins: Dict
    advisory: Dict
    flight_phase: FlightPhase
    validity: str = "VALID"


class EnvelopeSampler:
    """
    Samples envelope analytics data at phase-aware rates.
    
    Acquires margin and advisory data from the N-Axis components
    and buffers samples for the message builder.
    """
    
    # Phase-specific sample rates (Hz)
    PHASE_RATES = {
        FlightPhase.GROUND: 0.1,
        FlightPhase.TAXI: 0.5,
        FlightPhase.TAKEOFF: 10.0,
        FlightPhase.CLIMB: 5.0,
        FlightPhase.CRUISE: 1.0,
        FlightPhase.DESCENT: 5.0,
        FlightPhase.APPROACH: 10.0,
        FlightPhase.LANDING: 10.0
    }
    
    # Maximum sample latency (seconds)
    MAX_LATENCY = 0.05
    
    # Buffer size
    BUFFER_SIZE = 100
    
    def __init__(
        self,
        margin_source: Callable[[], Dict],
        advisory_source: Callable[[], Dict],
        phase_source: Callable[[], FlightPhase]
    ):
        """
        Initialize the envelope sampler.
        
        Args:
            margin_source: Function to get current margins
            advisory_source: Function to get current advisory state
            phase_source: Function to get current flight phase
        """
        self._margin_source = margin_source
        self._advisory_source = advisory_source
        self._phase_source = phase_source
        
        self._buffer: deque = deque(maxlen=self.BUFFER_SIZE)
        self._current_phase = FlightPhase.GROUND
        self._running = False
        self._sample_thread: Optional[threading.Thread] = None
        self._lock = threading.Lock()
    
    def start(self):
        """Start the sampling thread."""
        if self._running:
            return
        
        self._running = True
        self._sample_thread = threading.Thread(target=self._sample_loop, daemon=True)
        self._sample_thread.start()
    
    def stop(self):
        """Stop the sampling thread."""
        self._running = False
        if self._sample_thread:
            self._sample_thread.join(timeout=1.0)
    
    def _sample_loop(self):
        """Main sampling loop."""
        while self._running:
            try:
                # Get current phase and determine rate
                self._current_phase = self._phase_source()
                rate = self.PHASE_RATES.get(self._current_phase, 1.0)
                interval = 1.0 / rate
                
                # Take sample
                sample = self._take_sample()
                
                with self._lock:
                    self._buffer.append(sample)
                
                # Wait for next sample time
                time.sleep(interval)
                
            except Exception as e:
                # Log error but continue sampling
                print(f"Sampling error: {e}")
                time.sleep(0.1)
    
    def _take_sample(self) -> EnvelopeSample:
        """Take a single sample from all sources."""
        timestamp = time.time()
        
        try:
            margins = self._margin_source()
            validity = "VALID"
        except Exception:
            margins = {}
            validity = "INVALID"
        
        try:
            advisory = self._advisory_source()
        except Exception:
            advisory = {"level": "UNKNOWN", "trend": "UNKNOWN"}
        
        return EnvelopeSample(
            timestamp=timestamp,
            margins=margins,
            advisory=advisory,
            flight_phase=self._current_phase,
            validity=validity
        )
    
    def get_sample(self) -> Optional[EnvelopeSample]:
        """
        Get the next sample from the buffer.
        
        Returns:
            EnvelopeSample or None if buffer is empty
        """
        with self._lock:
            if self._buffer:
                return self._buffer.popleft()
            return None
    
    def get_all_samples(self) -> list:
        """
        Get all samples from the buffer.
        
        Returns:
            List of EnvelopeSamples
        """
        with self._lock:
            samples = list(self._buffer)
            self._buffer.clear()
            return samples
    
    def trigger_immediate_sample(self) -> EnvelopeSample:
        """
        Trigger an immediate sample (for event-driven sampling).
        
        Returns:
            The sampled data
        """
        sample = self._take_sample()
        with self._lock:
            self._buffer.append(sample)
        return sample
    
    @property
    def current_rate(self) -> float:
        """Get current sampling rate in Hz."""
        return self.PHASE_RATES.get(self._current_phase, 1.0)
    
    @property
    def buffer_count(self) -> int:
        """Get number of samples in buffer."""
        with self._lock:
            return len(self._buffer)
