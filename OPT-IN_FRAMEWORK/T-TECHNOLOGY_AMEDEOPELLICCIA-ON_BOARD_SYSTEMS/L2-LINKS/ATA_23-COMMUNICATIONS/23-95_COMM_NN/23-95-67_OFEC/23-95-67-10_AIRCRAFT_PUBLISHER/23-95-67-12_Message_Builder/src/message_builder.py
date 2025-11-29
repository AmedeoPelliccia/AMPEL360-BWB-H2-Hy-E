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
Message Builder
OFEC-23-95-67-12 - Aircraft Publisher

This module constructs OFEC messages from envelope samples.
"""

from dataclasses import dataclass
from typing import Dict, Optional
import uuid
import time


@dataclass
class OFECMessage:
    """OFEC protocol message."""
    envelope_id: str
    aircraft_id: str
    timestamp: str
    flight_phase: str
    margins: Dict
    h2_specific: Dict
    advisory: Dict
    metadata: Dict


class MessageBuilder:
    """
    Builds OFEC messages from envelope samples.
    
    Converts internal data structures to the OFEC message format
    for transmission to ground stations.
    """
    
    SCHEMA_VERSION = "1.0.0"
    
    def __init__(self, aircraft_id: str):
        """
        Initialize the message builder.
        
        Args:
            aircraft_id: Aircraft serial number (MSN)
        """
        self.aircraft_id = aircraft_id
        self._message_count = 0
    
    def build_envelope_state(
        self,
        margins: Dict,
        advisory: Dict,
        flight_phase: str,
        h2_specific: Optional[Dict] = None,
        sample_rate_hz: float = 1.0
    ) -> OFECMessage:
        """
        Build a complete envelope state message.
        
        Args:
            margins: All margin values
            advisory: Advisory state
            flight_phase: Current flight phase
            h2_specific: H2-specific constraints (optional)
            sample_rate_hz: Current sample rate
            
        Returns:
            OFECMessage ready for encoding
        """
        self._message_count += 1
        
        return OFECMessage(
            envelope_id=str(uuid.uuid4()),
            aircraft_id=self.aircraft_id,
            timestamp=self._format_timestamp(time.time()),
            flight_phase=flight_phase,
            margins=self._format_margins(margins),
            h2_specific=h2_specific or {},
            advisory=self._format_advisory(advisory),
            metadata={
                "sample_rate_hz": sample_rate_hz,
                "encoding": "CBOR",
                "schema_version": self.SCHEMA_VERSION,
                "sequence": self._message_count
            }
        )
    
    def _format_timestamp(self, timestamp: float) -> str:
        """Format timestamp as ISO 8601."""
        from datetime import datetime, timezone
        dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        return dt.isoformat(timespec='milliseconds')
    
    def _format_margins(self, margins: Dict) -> Dict:
        """Format margins for message."""
        return {
            "alpha": margins.get("alpha", {}),
            "speed": margins.get("speed", {}),
            "load_factor": margins.get("load_factor", {}),
            "altitude": margins.get("altitude", {}),
            "bank_angle": margins.get("bank_angle", {})
        }
    
    def _format_advisory(self, advisory: Dict) -> Dict:
        """Format advisory state for message."""
        return {
            "level": advisory.get("level", "NORMAL"),
            "active_advisories": advisory.get("active_advisories", []),
            "trend": advisory.get("trend", "STABLE")
        }
    
    def to_dict(self, message: OFECMessage) -> Dict:
        """
        Convert message to dictionary for encoding.
        
        Args:
            message: OFECMessage to convert
            
        Returns:
            Dictionary representation
        """
        return {
            "envelope_id": message.envelope_id,
            "aircraft_id": message.aircraft_id,
            "timestamp": message.timestamp,
            "flight_phase": message.flight_phase,
            "margins": message.margins,
            "h2_specific": message.h2_specific,
            "advisory": message.advisory,
            "metadata": message.metadata
        }
    
    @property
    def message_count(self) -> int:
        """Get total messages built."""
        return self._message_count
