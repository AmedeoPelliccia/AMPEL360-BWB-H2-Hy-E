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

#!/usr/bin/env python3
"""
Load Shedding Logic Module
AMPEL360 BWB-H2-Hy-E Aircraft - ATA 02-80-02

This is a SKELETON implementation demonstrating load shedding decision rules.
DO NOT use actual aircraft values or proprietary algorithms.

Purpose: Illustrate the structure and logic flow for automated load shedding
         based on available power and system priorities.

Compliance: CS-25.1309 (Equipment, Systems, and Installations)
            DO-178C (Software Considerations - appropriate DAL required)

Author: AI (GitHub Copilot), prompted by Amedeo Pelliccia
Status: DRAFT - Template only, not flight-certified
Repository: AMPEL360-BWB-H2-Hy-E
Last Update: 2025-11-21
"""

from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime


class Priority(Enum):
    """Load priority classification per energy management strategy"""
    CRITICAL = 1      # Flight-critical, never auto-shed
    ESSENTIAL = 2     # Safety-related, shed only in multi-failure
    OPERATIONAL = 3   # Non-essential, auto-shed when constrained
    COMFORT = 4       # Comfort/convenience, first to shed


class LoadStatus(Enum):
    """Current status of electrical load"""
    POWERED = "powered"
    SHED = "shed"
    STANDBY = "standby"


@dataclass
class Load:
    """Represents an electrical load on the aircraft"""
    load_id: str
    name: str
    priority: Priority
    power_kw: float
    status: LoadStatus
    bus_id: str
    shed_delay_sec: float = 0.0  # Delay before shedding (for graceful shutdown)


@dataclass
class PowerStatus:
    """Current power system status"""
    total_available_kw: float
    total_load_kw: float
    reserve_margin_kw: float
    reserve_margin_percent: float
    timestamp: datetime


class LoadSheddingController:
    """
    Load shedding controller implementing priority-based power management.
    
    This is a simplified skeleton for demonstration. Real implementation
    would require:
    - Integration with aircraft data bus (ARINC 429/664)
    - Redundant processing for safety-critical functions
    - Extensive testing and certification per DO-178C
    - Hardware interlocks and safety monitoring
    """
    
    # Load shedding thresholds (percentage of total available power)
    THRESHOLD_SHED_PRIORITY_4 = 90.0  # Shed comfort loads
    THRESHOLD_SHED_PRIORITY_3 = 75.0  # Shed operational loads
    THRESHOLD_ALERT_PRIORITY_2 = 60.0  # Alert crew, prepare to shed essential
    THRESHOLD_EMERGENCY = 50.0        # Emergency procedures
    
    def __init__(self, loads: List[Load], max_available_power_kw: float):
        """
        Initialize load shedding controller.
        
        Args:
            loads: List of all aircraft electrical loads
            max_available_power_kw: Maximum available power from all sources
        """
        self.loads = loads
        self.max_available_power_kw = max_available_power_kw
        self.shed_history: List[Dict] = []
        
    def calculate_power_status(self) -> PowerStatus:
        """Calculate current power system status"""
        total_load = sum(
            load.power_kw for load in self.loads 
            if load.status == LoadStatus.POWERED
        )
        reserve = self.max_available_power_kw - total_load
        reserve_pct = (reserve / self.max_available_power_kw) * 100
        
        return PowerStatus(
            total_available_kw=self.max_available_power_kw,
            total_load_kw=total_load,
            reserve_margin_kw=reserve,
            reserve_margin_percent=reserve_pct,
            timestamp=datetime.now()
        )
    
    def evaluate_shedding_required(self, power_status: PowerStatus) -> Optional[Priority]:
        """
        Determine if load shedding is required and which priority level.
        
        Args:
            power_status: Current power system status
            
        Returns:
            Priority level to shed, or None if no shedding required
        """
        utilization_pct = (power_status.total_load_kw / power_status.total_available_kw) * 100
        
        if utilization_pct > self.THRESHOLD_SHED_PRIORITY_4:
            return Priority.COMFORT
        elif utilization_pct > self.THRESHOLD_SHED_PRIORITY_3:
            return Priority.OPERATIONAL
        elif utilization_pct > self.THRESHOLD_ALERT_PRIORITY_2:
            # Don't auto-shed Priority 2, but alert crew
            self._generate_crew_alert("POWER MARGIN LOW - PREPARE FOR ESSENTIAL LOAD SHED")
            return None
        elif utilization_pct > self.THRESHOLD_EMERGENCY:
            # Emergency situation - crew-initiated procedures
            self._generate_crew_alert("EMERGENCY POWER CONDITION - CREW ACTION REQUIRED")
            return None
        
        return None
    
    def shed_loads(self, priority_to_shed: Priority) -> List[Load]:
        """
        Shed loads at specified priority level.
        
        Args:
            priority_to_shed: Priority level of loads to shed
            
        Returns:
            List of loads that were shed
        """
        shed_loads = []
        
        for load in self.loads:
            if load.priority == priority_to_shed and load.status == LoadStatus.POWERED:
                # In real implementation, would command actual load disconnect
                # through aircraft data bus with appropriate interlocks
                if self._safe_to_shed(load):
                    load.status = LoadStatus.SHED
                    shed_loads.append(load)
                    self._log_shed_event(load, "AUTO_SHED")
        
        return shed_loads
    
    def restore_loads(self, priority_to_restore: Priority) -> List[Load]:
        """
        Restore previously shed loads when power available.
        
        Args:
            priority_to_restore: Priority level of loads to restore
            
        Returns:
            List of loads that were restored
        """
        restored_loads = []
        power_status = self.calculate_power_status()
        
        for load in self.loads:
            if (load.priority == priority_to_restore and 
                load.status == LoadStatus.SHED):
                
                # Check if sufficient margin to restore this load
                if power_status.reserve_margin_kw >= (load.power_kw + 5.0):  # 5kW buffer
                    load.status = LoadStatus.POWERED
                    restored_loads.append(load)
                    power_status.total_load_kw += load.power_kw
                    power_status.reserve_margin_kw -= load.power_kw
                    self._log_shed_event(load, "AUTO_RESTORE")
        
        return restored_loads
    
    def _safe_to_shed(self, load: Load) -> bool:
        """
        Determine if it's safe to shed a specific load.
        
        Real implementation would check:
        - No active operations requiring this load
        - Graceful shutdown sequence completed
        - Crew override not active
        - No maintenance mode preventing shed
        """
        # Simplified check - Priority 1 never auto-shed
        if load.priority == Priority.CRITICAL:
            return False
        
        # Priority 2 only shed with crew authorization
        if load.priority == Priority.ESSENTIAL:
            return False  # Would check crew authorization in real system
        
        return True
    
    def _generate_crew_alert(self, message: str):
        """
        Generate alert to flight crew.
        
        In real implementation, would interface with ECAM/EICAS
        or equivalent crew alerting system.
        """
        alert = {
            "timestamp": datetime.now().isoformat(),
            "severity": "CAUTION",
            "message": message,
            "system": "ELECTRICAL_POWER"
        }
        # Placeholder - would send to crew alerting system
        print(f"CREW ALERT: {alert}")
    
    def _log_shed_event(self, load: Load, action: str):
        """Log load shed/restore event for maintenance and analysis"""
        event = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "load_id": load.load_id,
            "load_name": load.name,
            "priority": load.priority.name,
            "power_kw": load.power_kw
        }
        self.shed_history.append(event)
        # Would also log to Central Maintenance Computer (CMC)
    
    def run_cycle(self):
        """
        Execute one cycle of load shedding logic.
        
        In real implementation, this would be called periodically
        (e.g., 10 Hz) by the power management computer.
        """
        power_status = self.calculate_power_status()
        
        # Check if shedding required
        priority_to_shed = self.evaluate_shedding_required(power_status)
        if priority_to_shed:
            shed_loads = self.shed_loads(priority_to_shed)
            if shed_loads:
                print(f"Shed {len(shed_loads)} loads at priority {priority_to_shed.name}")
        
        # Check if loads can be restored (in reverse priority order)
        if power_status.reserve_margin_percent > 25.0:  # Ample margin
            for priority in [Priority.OPERATIONAL, Priority.COMFORT]:
                restored = self.restore_loads(priority)
                if restored:
                    print(f"Restored {len(restored)} loads at priority {priority.name}")


# Example usage (for demonstration only - not actual aircraft configuration)
if __name__ == "__main__":
    # Define example loads (NOT REAL AIRCRAFT DATA)
    example_loads = [
        Load("FC_01", "Flight Controls", Priority.CRITICAL, 20.0, LoadStatus.POWERED, "AC_BUS_1"),
        Load("PFD_01", "Primary Flight Display", Priority.CRITICAL, 5.0, LoadStatus.POWERED, "DC_ESS"),
        Load("WX_RADAR", "Weather Radar", Priority.ESSENTIAL, 3.0, LoadStatus.POWERED, "AC_BUS_2"),
        Load("IFE_01", "In-Flight Entertainment", Priority.OPERATIONAL, 12.0, LoadStatus.POWERED, "AC_BUS_3"),
        Load("GALLEY_01", "Galley Equipment", Priority.OPERATIONAL, 10.0, LoadStatus.POWERED, "AC_BUS_3"),
        Load("SEAT_PWR", "Passenger Seat Power", Priority.COMFORT, 5.0, LoadStatus.POWERED, "AC_BUS_4"),
    ]
    
    # Create controller with 100 kW max available power (example value)
    controller = LoadSheddingController(example_loads, max_available_power_kw=100.0)
    
    # Simulate normal operation
    print("=== Initial Power Status ===")
    status = controller.calculate_power_status()
    print(f"Total Load: {status.total_load_kw:.1f} kW")
    print(f"Reserve: {status.reserve_margin_kw:.1f} kW ({status.reserve_margin_percent:.1f}%)")
    
    # Simulate power reduction (e.g., generator failure)
    print("\n=== Simulating Generator Failure - Reducing Available Power ===")
    controller.max_available_power_kw = 60.0
    controller.run_cycle()
    
    status = controller.calculate_power_status()
    print(f"\nNew Total Load: {status.total_load_kw:.1f} kW")
    print(f"New Reserve: {status.reserve_margin_kw:.1f} kW ({status.reserve_margin_percent:.1f}%)")
    
    print("\n=== Load Shed History ===")
    for event in controller.shed_history:
        print(f"{event['timestamp']}: {event['action']} - {event['load_name']} ({event['power_kw']} kW)")
