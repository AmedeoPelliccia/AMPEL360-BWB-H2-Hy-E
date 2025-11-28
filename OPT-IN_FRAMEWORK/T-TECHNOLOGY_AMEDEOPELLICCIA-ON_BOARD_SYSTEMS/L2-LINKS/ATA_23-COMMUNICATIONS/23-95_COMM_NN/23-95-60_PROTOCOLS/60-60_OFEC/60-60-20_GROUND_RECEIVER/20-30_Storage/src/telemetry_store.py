"""
Telemetry Store
OFEC-60-60-20-30 - Ground Receiver

This module handles storage of validated OFEC telemetry data.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Iterator
from collections import defaultdict
import time
import threading


@dataclass
class TelemetryRecord:
    """Single telemetry record."""
    envelope_id: str
    aircraft_id: str
    timestamp: float
    flight_phase: str
    margins: Dict
    advisory: Dict
    received_at: float


class TelemetryStore:
    """
    Stores validated OFEC telemetry data.
    
    Provides in-memory storage with time-based retention
    and query capabilities.
    """
    
    # Default retention period (seconds)
    DEFAULT_RETENTION_SEC = 86400 * 7  # 7 days
    
    def __init__(self, retention_sec: int = DEFAULT_RETENTION_SEC):
        """
        Initialize the telemetry store.
        
        Args:
            retention_sec: Data retention period in seconds
        """
        self._retention_sec = retention_sec
        self._records: Dict[str, List[TelemetryRecord]] = defaultdict(list)
        self._record_count = 0
        self._lock = threading.Lock()
    
    def store(self, message: Dict) -> str:
        """
        Store a validated message.
        
        Args:
            message: Validated message dictionary
            
        Returns:
            Record ID
        """
        record = TelemetryRecord(
            envelope_id=message["envelope_id"],
            aircraft_id=message["aircraft_id"],
            timestamp=self._parse_timestamp(message["timestamp"]),
            flight_phase=message["flight_phase"],
            margins=message["margins"],
            advisory=message["advisory"],
            received_at=time.time()
        )
        
        with self._lock:
            self._records[record.aircraft_id].append(record)
            self._record_count += 1
        
        return record.envelope_id
    
    def _parse_timestamp(self, timestamp: str) -> float:
        """Parse ISO 8601 timestamp to epoch."""
        from datetime import datetime
        try:
            dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            return dt.timestamp()
        except Exception:
            return time.time()
    
    def query_by_aircraft(
        self,
        aircraft_id: str,
        start_time: Optional[float] = None,
        end_time: Optional[float] = None,
        limit: int = 1000
    ) -> List[TelemetryRecord]:
        """
        Query records for an aircraft.
        
        Args:
            aircraft_id: Aircraft identifier
            start_time: Start of time range (epoch)
            end_time: End of time range (epoch)
            limit: Maximum records to return
            
        Returns:
            List of matching records
        """
        with self._lock:
            records = self._records.get(aircraft_id, [])
        
        # Filter by time range
        if start_time is not None:
            records = [r for r in records if r.timestamp >= start_time]
        if end_time is not None:
            records = [r for r in records if r.timestamp <= end_time]
        
        # Apply limit
        return records[-limit:]
    
    def get_latest(self, aircraft_id: str) -> Optional[TelemetryRecord]:
        """
        Get latest record for an aircraft.
        
        Args:
            aircraft_id: Aircraft identifier
            
        Returns:
            Latest record or None
        """
        with self._lock:
            records = self._records.get(aircraft_id, [])
            return records[-1] if records else None
    
    def get_all_aircraft(self) -> List[str]:
        """Get list of all aircraft with data."""
        with self._lock:
            return list(self._records.keys())
    
    def cleanup_old_records(self) -> int:
        """
        Remove records older than retention period.
        
        Returns:
            Number of records removed
        """
        cutoff = time.time() - self._retention_sec
        removed = 0
        
        with self._lock:
            for aircraft_id in list(self._records.keys()):
                records = self._records[aircraft_id]
                original_count = len(records)
                
                # Filter out old records
                self._records[aircraft_id] = [
                    r for r in records if r.received_at > cutoff
                ]
                
                removed += original_count - len(self._records[aircraft_id])
                self._record_count -= (original_count - len(self._records[aircraft_id]))
        
        return removed
    
    @property
    def record_count(self) -> int:
        """Get total record count."""
        return self._record_count
    
    @property
    def aircraft_count(self) -> int:
        """Get number of aircraft with data."""
        with self._lock:
            return len(self._records)
