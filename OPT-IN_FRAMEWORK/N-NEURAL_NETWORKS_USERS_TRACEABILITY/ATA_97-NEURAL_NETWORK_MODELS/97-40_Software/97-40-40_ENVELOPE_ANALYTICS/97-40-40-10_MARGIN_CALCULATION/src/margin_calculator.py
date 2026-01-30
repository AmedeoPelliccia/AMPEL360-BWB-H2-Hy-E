"""
Margin Calculator Module
OFEC-97-40-40-10 - Envelope Analytics

This module provides the main MarginCalculator class that coordinates
all margin calculations for the flight envelope.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional
import time

from .alpha_margin import calculate_alpha_margin
from .speed_margin import calculate_speed_margins
from .load_factor_margin import calculate_load_factor_margin
from .altitude_margin import calculate_altitude_margin
from .bank_angle_margin import calculate_bank_margin


class AdvisoryLevel(Enum):
    """Advisory level enumeration."""
    NORMAL = 0
    CAUTION = 1
    WARNING = 2
    CRITICAL = 3


@dataclass
class Configuration:
    """Aircraft configuration state."""
    flap_deg: float = 0.0
    slat_deg: float = 0.0
    gear_down: bool = False
    speedbrake_pct: float = 0.0
    weight_kg: float = 70000.0
    cg_pct_mac: float = 25.0


@dataclass
class FlightState:
    """Current flight state parameters."""
    aoa_deg: float = 0.0
    cas_kts: float = 250.0
    mach: float = 0.0
    altitude_ft: float = 0.0
    load_factor_g: float = 1.0
    bank_angle_deg: float = 0.0
    oat_celsius: float = 15.0
    timestamp: float = 0.0


@dataclass
class EnvelopeMargins:
    """Complete envelope margin state."""
    alpha: Dict
    speed: Dict
    load_factor: Dict
    altitude: Dict
    bank_angle: Dict
    timestamp: float
    advisory_level: AdvisoryLevel


class MarginCalculator:
    """
    Main margin calculator class.
    
    Coordinates calculation of all envelope margins and determines
    overall advisory level.
    """
    
    # Advisory thresholds (percentage)
    NORMAL_THRESHOLD = 50.0
    CAUTION_THRESHOLD = 25.0
    WARNING_THRESHOLD = 10.0
    
    def __init__(self, config: Optional[Configuration] = None):
        """
        Initialize the margin calculator.
        
        Args:
            config: Initial aircraft configuration
        """
        self.config = config or Configuration()
        self._last_margins: Optional[EnvelopeMargins] = None
    
    def update_configuration(self, config: Configuration) -> None:
        """Update aircraft configuration."""
        self.config = config
    
    def calculate_all_margins(self, state: FlightState) -> EnvelopeMargins:
        """
        Calculate all envelope margins for current flight state.
        
        Args:
            state: Current flight state parameters
            
        Returns:
            Complete envelope margins including advisory level
        """
        # Calculate individual margins
        alpha_margin = calculate_alpha_margin(
            current_aoa=state.aoa_deg,
            config=self.config,
            mach=state.mach,
            altitude=state.altitude_ft
        )
        
        speed_margin = calculate_speed_margins(
            cas=state.cas_kts,
            config=self.config,
            altitude=state.altitude_ft,
            weight=self.config.weight_kg
        )
        
        load_margin = calculate_load_factor_margin(
            current_g=state.load_factor_g,
            config=self.config
        )
        
        alt_margin = calculate_altitude_margin(
            current_alt=state.altitude_ft,
            weight=self.config.weight_kg,
            oat=state.oat_celsius
        )
        
        bank_margin = calculate_bank_margin(
            current_bank=state.bank_angle_deg,
            config=self.config
        )
        
        # Determine overall advisory level
        advisory = self._determine_advisory_level(
            alpha_margin, speed_margin, load_margin, alt_margin, bank_margin
        )
        
        margins = EnvelopeMargins(
            alpha=alpha_margin,
            speed=speed_margin,
            load_factor=load_margin,
            altitude=alt_margin,
            bank_angle=bank_margin,
            timestamp=state.timestamp or time.time(),
            advisory_level=advisory
        )
        
        self._last_margins = margins
        return margins
    
    def _determine_advisory_level(
        self,
        alpha: Dict,
        speed: Dict,
        load: Dict,
        altitude: Dict,
        bank: Dict
    ) -> AdvisoryLevel:
        """
        Determine overall advisory level from individual margins.
        
        Uses the most critical (lowest) margin to set the level.
        """
        # Collect all margin percentages
        margin_pcts = [
            alpha.get("margin_pct", 100),
            speed.get("margin_low_pct", 100),
            speed.get("margin_high_pct", 100),
            load.get("margin_positive_pct", 100),
            load.get("margin_negative_pct", 100),
            altitude.get("margin_pct", 100),
            bank.get("margin_pct", 100)
        ]
        
        # Find minimum margin
        min_margin = min(margin_pcts)
        
        # Determine advisory level
        if min_margin < 0:
            return AdvisoryLevel.CRITICAL
        elif min_margin < self.WARNING_THRESHOLD:
            return AdvisoryLevel.WARNING
        elif min_margin < self.CAUTION_THRESHOLD:
            return AdvisoryLevel.CAUTION
        else:
            return AdvisoryLevel.NORMAL
    
    @property
    def last_margins(self) -> Optional[EnvelopeMargins]:
        """Get last calculated margins."""
        return self._last_margins
