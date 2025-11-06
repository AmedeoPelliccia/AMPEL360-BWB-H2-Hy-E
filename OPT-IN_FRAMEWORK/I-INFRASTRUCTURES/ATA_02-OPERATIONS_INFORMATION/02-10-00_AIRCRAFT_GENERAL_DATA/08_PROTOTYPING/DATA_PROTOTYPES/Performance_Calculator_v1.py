#!/usr/bin/env python3
"""
AMPEL360 BWB Performance Calculator v1.0
ATA 02-10-00 Aircraft General Data - Prototyping Tool

Calculates key performance parameters: takeoff distance, landing distance, 
cruise performance, range, and fuel consumption for AMPEL360 BWB aircraft.

Author: AMPEL360 Engineering Team
Date: 2025-11-05
Version: 1.0 (Prototype)
"""

import math
from typing import Dict, Tuple


class PerformanceCalculator:
    """
    Performance Calculator for AMPEL360 BWB Aircraft
    
    Based on preliminary aerodynamic and propulsion data from wind tunnel
    and CFD analysis.
    """
    
    def __init__(self):
        """Initialize with AMPEL360 BWB aircraft parameters"""
        
        # Aircraft geometry
        self.wing_area = 750.0  # m²
        self.wingspan = 64.0    # m
        self.aspect_ratio = 5.46
        
        # Weight parameters (kg)
        self.mtow = 95000
        self.mlw = 82000
        self.oew = 42000
        
        # Aerodynamic parameters (from wind tunnel Model_Test_Results.csv)
        self.cl_max_takeoff = 1.70  # With flaps
        self.cl_max_landing = 1.90  # With flaps + slats
        self.cl_cruise = 0.48       # Cruise lift coefficient
        self.cd0_clean = 0.0145     # Zero-lift drag coefficient (clean)
        self.cd0_takeoff = 0.0280   # With flaps extended
        self.cd0_landing = 0.0380   # With flaps + gear extended
        self.oswald_e = 0.89        # Oswald efficiency factor
        self.ld_max = 21.4          # Maximum L/D ratio (from tests)
        
        # Propulsion (H2 fuel cells + electric motors)
        self.max_thrust = 250000    # N (total, sea level static)
        self.cruise_thrust = 80000  # N (cruise power)
        self.h2_energy_density = 33.3  # kWh/kg (LHV)
        self.fuel_cell_efficiency = 0.60  # 60% electrical efficiency
        self.propeller_efficiency = 0.85  # Electric motor + propeller
        
        # Performance speeds (knots TAS)
        self.v_stall_clean = 140  # kt
        self.v_cruise = 470       # kt (M 0.72 at FL350)
        self.v_approach = 140     # kt
        
        # Constants
        self.g = 9.81             # m/s²
        self.rho_sl = 1.225       # kg/m³ (sea level)
        self.kt_to_ms = 0.5144    # Knots to m/s conversion
        
    def calculate_stall_speed(self, weight_kg: float, altitude_m: float, 
                              config: str = 'clean') -> float:
        """
        Calculate stall speed (TAS)
        
        Args:
            weight_kg: Aircraft weight
            altitude_m: Altitude (m)
            config: 'clean', 'takeoff', or 'landing'
        
        Returns:
            Stall speed (knots TAS)
        """
        # Air density at altitude (ISA model, simplified)
        rho = self.rho_sl * math.exp(-altitude_m / 8500)
        
        # CL_max based on configuration
        cl_max = {
            'clean': 1.20,
            'takeoff': self.cl_max_takeoff,
            'landing': self.cl_max_landing
        }[config]
        
        # Stall speed formula: V_stall = sqrt(2*W/(rho*S*CL_max))
        v_stall_ms = math.sqrt((2 * weight_kg * self.g) / 
                               (rho * self.wing_area * cl_max))
        
        return v_stall_ms / self.kt_to_ms  # Convert to knots
    
    def calculate_takeoff_distance(self, weight_kg: float, altitude_m: float,
                                   temperature_c: float, headwind_kt: float = 0) -> Dict:
        """
        Calculate takeoff distance (balanced field length)
        
        Args:
            weight_kg: Takeoff weight
            altitude_m: Field elevation
            temperature_c: Temperature (°C)
            headwind_kt: Headwind component (positive = headwind)
        
        Returns:
            Dictionary with takeoff performance data
        """
        # Density altitude correction
        rho = self.rho_sl * math.exp(-altitude_m / 8500)
        temp_isa = 15 - 0.0065 * altitude_m
        temp_ratio = (temperature_c + 273.15) / (temp_isa + 273.15)
        rho_corrected = rho / temp_ratio
        
        # Stall speed in takeoff configuration
        v_stall = self.calculate_stall_speed(weight_kg, altitude_m, 'takeoff')
        
        # V1, VR, V2 speeds (simplified, regulatory minimums)
        v1 = v_stall * 1.05  # Decision speed
        vr = v_stall * 1.10  # Rotation speed
        v2 = v_stall * 1.20  # Takeoff safety speed
        
        # Effective takeoff speed (accounting for headwind)
        vr_eff = vr - headwind_kt
        vr_ms = vr_eff * self.kt_to_ms
        
        # Drag during ground roll
        cl_ground = 0.3  # Approximate, before rotation
        cd_ground = self.cd0_takeoff + (cl_ground**2) / (math.pi * self.aspect_ratio * self.oswald_e)
        drag = 0.5 * rho_corrected * (vr_ms**2) * self.wing_area * cd_ground
        
        # Rolling resistance
        mu_rolling = 0.02  # Typical for paved runway
        rolling_resistance = mu_rolling * weight_kg * self.g
        
        # Net accelerating force
        thrust_available = self.max_thrust * (rho_corrected / self.rho_sl)  # Thrust lapse
        accel_force = thrust_available - drag - rolling_resistance
        acceleration = accel_force / weight_kg
        
        # Ground roll distance (simplified: constant acceleration)
        # s = v² / (2*a)
        ground_roll = (vr_ms**2) / (2 * acceleration)
        
        # Airborne distance to clear 35 ft (10.7 m) obstacle
        # Simplified: assume 10° climb gradient
        airborne_distance = 10.7 / math.tan(math.radians(10))
        
        # Total takeoff distance (balanced field length)
        total_distance = ground_roll + airborne_distance
        
        results = {
            'v1_kt': v1,
            'vr_kt': vr,
            'v2_kt': v2,
            'ground_roll_m': ground_roll,
            'airborne_distance_m': airborne_distance,
            'total_distance_m': total_distance,
            'total_distance_ft': total_distance * 3.28084,
        }
        
        return results
    
    def calculate_landing_distance(self, weight_kg: float, altitude_m: float,
                                   temperature_c: float, headwind_kt: float = 0) -> Dict:
        """
        Calculate landing distance (from 50 ft obstacle)
        
        Args:
            weight_kg: Landing weight
            altitude_m: Field elevation
            temperature_c: Temperature (°C)
            headwind_kt: Headwind component
        
        Returns:
            Dictionary with landing performance data
        """
        # Density altitude correction
        rho = self.rho_sl * math.exp(-altitude_m / 8500)
        temp_isa = 15 - 0.0065 * altitude_m
        temp_ratio = (temperature_c + 273.15) / (temp_isa + 273.15)
        rho_corrected = rho / temp_ratio
        
        # Approach speed (1.3 × V_stall_landing)
        v_stall_ldg = self.calculate_stall_speed(weight_kg, altitude_m, 'landing')
        v_app = v_stall_ldg * 1.3
        v_ref = v_stall_ldg * 1.23  # Reference landing speed
        
        # Effective speeds (accounting for headwind)
        v_app_eff = v_app - headwind_kt
        v_app_ms = v_app_eff * self.kt_to_ms
        
        # Airborne distance (50 ft = 15.24 m obstacle to touchdown)
        # Assume 3° glide slope
        airborne_distance = 15.24 / math.tan(math.radians(3))
        
        # Flare distance (additional distance during flare)
        flare_distance = 150  # m (typical for this aircraft size)
        
        # Ground roll distance with braking
        # Drag with spoilers/air brakes deployed
        cd_landing = self.cd0_landing * 1.5  # Spoilers increase drag
        drag_avg = 0.5 * rho_corrected * ((v_app_ms/2)**2) * self.wing_area * cd_landing
        
        # Braking force
        mu_braking = 0.40  # Dry runway, wheel brakes
        braking_force = mu_braking * weight_kg * self.g
        
        # Deceleration
        decel_force = drag_avg + braking_force
        deceleration = decel_force / weight_kg
        
        # Ground roll: s = v² / (2*a)
        ground_roll = (v_app_ms**2) / (2 * deceleration)
        
        # Total landing distance
        total_distance = airborne_distance + flare_distance + ground_roll
        
        results = {
            'v_approach_kt': v_app,
            'v_ref_kt': v_ref,
            'airborne_distance_m': airborne_distance,
            'flare_distance_m': flare_distance,
            'ground_roll_m': ground_roll,
            'total_distance_m': total_distance,
            'total_distance_ft': total_distance * 3.28084,
        }
        
        return results
    
    def calculate_cruise_performance(self, weight_kg: float, altitude_m: float,
                                    speed_kt: float = None) -> Dict:
        """
        Calculate cruise performance
        
        Args:
            weight_kg: Cruise weight
            altitude_m: Cruise altitude
            speed_kt: Cruise speed (if None, use design cruise)
        
        Returns:
            Dictionary with cruise performance data
        """
        if speed_kt is None:
            speed_kt = self.v_cruise
        
        speed_ms = speed_kt * self.kt_to_ms
        
        # Air density at altitude
        rho = self.rho_sl * math.exp(-altitude_m / 8500)
        
        # Required lift coefficient for steady cruise
        cl_cruise = (2 * weight_kg * self.g) / (rho * (speed_ms**2) * self.wing_area)
        
        # Drag coefficient (induced drag from lift)
        cd_induced = (cl_cruise**2) / (math.pi * self.aspect_ratio * self.oswald_e)
        cd_total = self.cd0_clean + cd_induced
        
        # L/D ratio
        ld_ratio = cl_cruise / cd_total
        
        # Drag force
        drag = 0.5 * rho * (speed_ms**2) * self.wing_area * cd_total
        
        # Required thrust (equals drag in steady cruise)
        thrust_required = drag
        
        # Power required (Watts)
        power_required = thrust_required * speed_ms
        
        # Fuel consumption (H2)
        # Power = Fuel_rate * H2_energy_density * FC_efficiency * Prop_efficiency
        fuel_rate_kg_s = power_required / (self.h2_energy_density * 1000 * 3600 * 
                                           self.fuel_cell_efficiency * self.propeller_efficiency)
        fuel_rate_kg_h = fuel_rate_kg_s * 3600
        
        # Specific range (nm/kg)
        specific_range = speed_kt / fuel_rate_kg_h
        
        results = {
            'altitude_m': altitude_m,
            'altitude_ft': altitude_m * 3.28084,
            'speed_kt': speed_kt,
            'cl_cruise': cl_cruise,
            'cd_cruise': cd_total,
            'ld_ratio': ld_ratio,
            'thrust_required_n': thrust_required,
            'power_required_kw': power_required / 1000,
            'fuel_flow_kg_h': fuel_rate_kg_h,
            'specific_range_nm_kg': specific_range,
        }
        
        return results
    
    def calculate_range(self, fuel_kg: float, payload_kg: float, 
                       cruise_altitude_m: float = 11000) -> Dict:
        """
        Calculate aircraft range (Breguet range equation)
        
        Args:
            fuel_kg: Available fuel
            payload_kg: Payload (passengers + cargo)
            cruise_altitude_m: Cruise altitude
        
        Returns:
            Dictionary with range calculation
        """
        # Initial cruise weight (OEW + payload + fuel)
        initial_weight = self.oew + payload_kg + fuel_kg
        
        # Final cruise weight (OEW + payload, fuel burned)
        final_weight = self.oew + payload_kg
        
        # Average cruise weight
        avg_weight = (initial_weight + final_weight) / 2
        
        # Cruise performance at average weight
        cruise_perf = self.calculate_cruise_performance(avg_weight, cruise_altitude_m)
        
        # Range using Breguet equation (simplified)
        # Range = (V/SFC) * L/D * ln(W_initial/W_final)
        # where SFC = specific fuel consumption
        
        # Average specific range
        avg_specific_range = cruise_perf['specific_range_nm_kg']
        
        # Range = fuel * specific_range
        range_nm = fuel_kg * avg_specific_range
        
        # Flight time
        flight_time_h = range_nm / self.v_cruise
        
        results = {
            'range_nm': range_nm,
            'range_km': range_nm * 1.852,
            'flight_time_h': flight_time_h,
            'initial_weight_kg': initial_weight,
            'final_weight_kg': final_weight,
            'avg_fuel_flow_kg_h': cruise_perf['fuel_flow_kg_h'],
            'avg_ld_ratio': cruise_perf['ld_ratio'],
        }
        
        return results


def example_calculations():
    """Run example performance calculations"""
    
    calc = PerformanceCalculator()
    
    print("\n" + "#"*70)
    print("# EXAMPLE PERFORMANCE CALCULATIONS")
    print("#"*70)
    
    # Scenario 1: Takeoff performance
    print("\n### TAKEOFF PERFORMANCE ###")
    print("MTOW: 95,000 kg | Airport: Sea level, ISA, no wind")
    to_perf = calc.calculate_takeoff_distance(
        weight_kg=95000,
        altitude_m=0,
        temperature_c=15,
        headwind_kt=0
    )
    print(f"\n  Decision Speed (V1):      {to_perf['v1_kt']:.0f} kt")
    print(f"  Rotation Speed (VR):      {to_perf['vr_kt']:.0f} kt")
    print(f"  Takeoff Safety Speed (V2): {to_perf['v2_kt']:.0f} kt")
    print(f"  Ground Roll:              {to_perf['ground_roll_m']:.0f} m ({to_perf['ground_roll_m']*3.28:.0f} ft)")
    print(f"  Total Takeoff Distance:   {to_perf['total_distance_m']:.0f} m ({to_perf['total_distance_ft']:.0f} ft)")
    
    # Scenario 2: Landing performance
    print("\n### LANDING PERFORMANCE ###")
    print("MLW: 82,000 kg | Airport: Sea level, ISA, no wind")
    ldg_perf = calc.calculate_landing_distance(
        weight_kg=82000,
        altitude_m=0,
        temperature_c=15,
        headwind_kt=0
    )
    print(f"\n  Approach Speed (V_app):   {ldg_perf['v_approach_kt']:.0f} kt")
    print(f"  Reference Speed (V_ref):  {ldg_perf['v_ref_kt']:.0f} kt")
    print(f"  Ground Roll:              {ldg_perf['ground_roll_m']:.0f} m ({ldg_perf['ground_roll_m']*3.28:.0f} ft)")
    print(f"  Total Landing Distance:   {ldg_perf['total_distance_m']:.0f} m ({ldg_perf['total_distance_ft']:.0f} ft)")
    
    # Scenario 3: Cruise performance
    print("\n### CRUISE PERFORMANCE ###")
    print("Weight: 85,000 kg | Altitude: FL350 (35,000 ft) | Speed: M 0.72")
    cruise_perf = calc.calculate_cruise_performance(
        weight_kg=85000,
        altitude_m=10670,  # 35,000 ft
        speed_kt=470
    )
    print(f"\n  Cruise Altitude:          {cruise_perf['altitude_ft']:.0f} ft")
    print(f"  Cruise Speed:             {cruise_perf['speed_kt']:.0f} kt")
    print(f"  Lift Coefficient:         {cruise_perf['cl_cruise']:.3f}")
    print(f"  L/D Ratio:                {cruise_perf['ld_ratio']:.1f}")
    print(f"  Thrust Required:          {cruise_perf['thrust_required_n']:.0f} N")
    print(f"  Fuel Flow:                {cruise_perf['fuel_flow_kg_h']:.0f} kg/h")
    print(f"  Specific Range:           {cruise_perf['specific_range_nm_kg']:.2f} nm/kg")
    
    # Scenario 4: Range calculation
    print("\n### RANGE CALCULATION ###")
    print("Fuel: 12,000 kg | Payload: 24,000 kg (220 pax + 3000 kg cargo)")
    range_calc = calc.calculate_range(
        fuel_kg=12000,
        payload_kg=24000,
        cruise_altitude_m=10670
    )
    print(f"\n  Maximum Range:            {range_calc['range_nm']:.0f} nm ({range_calc['range_km']:.0f} km)")
    print(f"  Flight Time:              {range_calc['flight_time_h']:.1f} hours")
    print(f"  Initial Cruise Weight:    {range_calc['initial_weight_kg']:.0f} kg")
    print(f"  Final Cruise Weight:      {range_calc['final_weight_kg']:.0f} kg")
    print(f"  Average Fuel Flow:        {range_calc['avg_fuel_flow_kg_h']:.0f} kg/h")
    print(f"  Average L/D:              {range_calc['avg_ld_ratio']:.1f}")


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   AMPEL360 BWB Performance Calculator v1.0                          ║
║   ATA 02-10-00 Aircraft General Data                                ║
║                                                                      ║
║   Prototype Tool - For Engineering Analysis Only                    ║
║   Not Certified for Flight Operations                               ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    example_calculations()
    
    print("\n" + "="*70)
    print("NOTE: This is a prototype tool using preliminary data.")
    print("Production version will include:")
    print("  - Certified performance database")
    print("  - All regulatory corrections (runway slope, contamination, etc.)")
    print("  - Integration with flight planning systems")
    print("  - Real-time weather data")
    print("="*70 + "\n")
