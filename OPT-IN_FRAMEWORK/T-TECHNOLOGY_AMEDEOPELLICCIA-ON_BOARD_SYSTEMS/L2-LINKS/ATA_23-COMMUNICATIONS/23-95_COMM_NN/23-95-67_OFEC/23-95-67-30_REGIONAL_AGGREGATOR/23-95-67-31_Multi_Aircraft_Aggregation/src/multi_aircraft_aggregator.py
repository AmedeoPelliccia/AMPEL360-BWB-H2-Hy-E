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
Multi-Aircraft Aggregator
OFEC-23-95-67-31 - Regional Aggregator

This module aggregates envelope data from multiple aircraft.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from collections import defaultdict
import time
import statistics


@dataclass
class AircraftSummary:
    """Summary of single aircraft state."""
    aircraft_id: str
    last_update: float
    flight_phase: str
    advisory_level: str
    min_margin_pct: float
    margin_trend: str


@dataclass
class RegionalSummary:
    """Regional fleet summary."""
    region_id: str
    timestamp: float
    aircraft_count: int
    aircraft_summaries: List[AircraftSummary]
    statistics: Dict


class MultiAircraftAggregator:
    """
    Aggregates envelope data from multiple aircraft.
    
    Maintains state for all aircraft in a region and provides
    aggregated views of fleet envelope status.
    """
    
    # Aircraft considered stale after this time (seconds)
    STALE_THRESHOLD = 60.0
    
    def __init__(self, region_id: str):
        """
        Initialize the aggregator.
        
        Args:
            region_id: Regional identifier
        """
        self._region_id = region_id
        self._aircraft_state: Dict[str, Dict] = {}
        self._last_update: Dict[str, float] = {}
    
    def update(self, aircraft_id: str, message: Dict) -> None:
        """
        Update state for an aircraft.
        
        Args:
            aircraft_id: Aircraft identifier
            message: Latest envelope message
        """
        self._aircraft_state[aircraft_id] = message
        self._last_update[aircraft_id] = time.time()
    
    def get_aircraft_summary(self, aircraft_id: str) -> Optional[AircraftSummary]:
        """
        Get summary for a single aircraft.
        
        Args:
            aircraft_id: Aircraft identifier
            
        Returns:
            Aircraft summary or None if not found
        """
        if aircraft_id not in self._aircraft_state:
            return None
        
        state = self._aircraft_state[aircraft_id]
        margins = state.get("margins", {})
        
        # Calculate minimum margin
        margin_values = []
        for margin_type in ["alpha", "speed", "load_factor", "altitude", "bank_angle"]:
            margin_data = margins.get(margin_type, {})
            margin_pct = margin_data.get("margin_pct")
            if margin_pct is not None:
                margin_values.append(margin_pct)
        
        min_margin = min(margin_values) if margin_values else 100.0
        
        return AircraftSummary(
            aircraft_id=aircraft_id,
            last_update=self._last_update.get(aircraft_id, 0),
            flight_phase=state.get("flight_phase", "UNKNOWN"),
            advisory_level=state.get("advisory", {}).get("level", "UNKNOWN"),
            min_margin_pct=min_margin,
            margin_trend=state.get("advisory", {}).get("trend", "UNKNOWN")
        )
    
    def get_regional_summary(self) -> RegionalSummary:
        """
        Get summary for entire region.
        
        Returns:
            Regional summary with all aircraft
        """
        current_time = time.time()
        
        # Filter active aircraft
        active_aircraft = [
            aid for aid, last_time in self._last_update.items()
            if current_time - last_time < self.STALE_THRESHOLD
        ]
        
        # Generate summaries
        summaries = []
        for aircraft_id in active_aircraft:
            summary = self.get_aircraft_summary(aircraft_id)
            if summary:
                summaries.append(summary)
        
        # Calculate statistics
        stats = self._calculate_statistics(summaries)
        
        return RegionalSummary(
            region_id=self._region_id,
            timestamp=current_time,
            aircraft_count=len(summaries),
            aircraft_summaries=summaries,
            statistics=stats
        )
    
    def _calculate_statistics(
        self, 
        summaries: List[AircraftSummary]
    ) -> Dict:
        """Calculate regional statistics."""
        if not summaries:
            return {"message": "No active aircraft"}
        
        # Margin statistics
        margins = [s.min_margin_pct for s in summaries]
        
        # Advisory level counts
        level_counts = defaultdict(int)
        for s in summaries:
            level_counts[s.advisory_level] += 1
        
        # Phase distribution
        phase_counts = defaultdict(int)
        for s in summaries:
            phase_counts[s.flight_phase] += 1
        
        return {
            "margin_min": min(margins),
            "margin_max": max(margins),
            "margin_mean": statistics.mean(margins),
            "margin_std": statistics.stdev(margins) if len(margins) > 1 else 0,
            "advisory_distribution": dict(level_counts),
            "phase_distribution": dict(phase_counts)
        }
    
    @property
    def aircraft_count(self) -> int:
        """Get number of tracked aircraft."""
        return len(self._aircraft_state)
    
    @property
    def active_count(self) -> int:
        """Get number of active (non-stale) aircraft."""
        current_time = time.time()
        return sum(
            1 for last_time in self._last_update.values()
            if current_time - last_time < self.STALE_THRESHOLD
        )
