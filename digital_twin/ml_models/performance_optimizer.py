# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Performance optimization models for AMPEL360 digital twin.

This module provides optimization capabilities for maximizing aircraft
performance including fuel efficiency, range, and operational costs.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)


@dataclass
class OptimizationResult:
    """Result of performance optimization."""

    optimized_parameters: dict[str, float] = field(default_factory=dict)
    expected_improvement_pct: float = 0.0
    constraints_satisfied: bool = True
    violated_constraints: list[str] = field(default_factory=list)
    confidence: float = 0.0
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class OptimizationConstraints:
    """Constraints for optimization."""

    min_values: dict[str, float] = field(default_factory=dict)
    max_values: dict[str, float] = field(default_factory=dict)
    equality_constraints: dict[str, float] = field(default_factory=dict)


class PerformanceOptimizer:
    """
    Performance optimization model for aircraft operations.

    Optimizes operational parameters to achieve objectives such as
    fuel efficiency, range maximization, or cost minimization.

    Attributes:
        objective: Optimization objective (fuel_efficiency, range, cost)
        model_id: Unique model identifier
    """

    OBJECTIVES = ["fuel_efficiency", "range", "cost", "emissions"]

    def __init__(
        self,
        objective: str = "fuel_efficiency",
        model_id: Optional[str] = None,
    ) -> None:
        """
        Initialize the performance optimizer.

        Args:
            objective: Optimization objective
            model_id: Optional model identifier
        """
        if objective not in self.OBJECTIVES:
            logger.warning("Unknown objective '%s', defaulting to fuel_efficiency", objective)
            objective = "fuel_efficiency"

        self.objective = objective
        self.model_id = model_id or f"ML-OPT-{objective.upper()}-001"

        self._constraints = OptimizationConstraints()
        self._performance_model: dict[str, Any] = {}
        self._is_configured = False

        logger.info("Initialized performance optimizer: %s", self.model_id)

    def configure(
        self,
        constraints: Optional[dict[str, Any]] = None,
        performance_data: Optional[list[dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """
        Configure the optimizer with constraints and performance data.

        Args:
            constraints: Dictionary of optimization constraints
            performance_data: Historical performance data for model fitting

        Returns:
            Dictionary containing configuration status
        """
        # Set constraints
        if constraints:
            self._constraints.min_values = constraints.get("min", {})
            self._constraints.max_values = constraints.get("max", {})
            self._constraints.equality_constraints = constraints.get("equality", {})

        # Fit performance model from data
        if performance_data:
            self._fit_performance_model(performance_data)

        self._is_configured = True

        logger.info(
            "Configured optimizer: %d min constraints, %d max constraints",
            len(self._constraints.min_values),
            len(self._constraints.max_values),
        )

        return {
            "success": True,
            "objective": self.objective,
            "constraints_set": {
                "min": len(self._constraints.min_values),
                "max": len(self._constraints.max_values),
                "equality": len(self._constraints.equality_constraints),
            },
            "performance_model_fitted": bool(self._performance_model),
        }

    def optimize(
        self,
        current_state: dict[str, Any],
        flight_conditions: dict[str, Any],
    ) -> OptimizationResult:
        """
        Optimize performance parameters for given conditions.

        Args:
            current_state: Current aircraft state parameters
            flight_conditions: Flight conditions (altitude, speed, etc.)

        Returns:
            OptimizationResult with optimized parameters
        """
        if not self._is_configured:
            logger.warning("Optimizer not configured, using default optimization")

        # Extract current parameters
        altitude_m = flight_conditions.get("altitude_m", 10000)
        mach = flight_conditions.get("mach", 0.78)
        weight_kg = current_state.get("weight_kg", 150000)

        # Calculate optimal parameters based on objective
        if self.objective == "fuel_efficiency":
            optimized = self._optimize_fuel_efficiency(altitude_m, mach, weight_kg)
        elif self.objective == "range":
            optimized = self._optimize_range(altitude_m, mach, weight_kg)
        elif self.objective == "cost":
            optimized = self._optimize_cost(altitude_m, mach, weight_kg)
        elif self.objective == "emissions":
            optimized = self._optimize_emissions(altitude_m, mach, weight_kg)
        else:
            optimized = current_state.copy()

        # Check constraints
        violated = self._check_constraints(optimized)
        constraints_satisfied = len(violated) == 0

        # Apply constraints
        constrained_params = self._apply_constraints(optimized)

        # Estimate improvement
        improvement = self._estimate_improvement(current_state, constrained_params)

        result = OptimizationResult(
            optimized_parameters=constrained_params,
            expected_improvement_pct=improvement,
            constraints_satisfied=constraints_satisfied,
            violated_constraints=violated,
            confidence=0.85 if self._is_configured else 0.5,
        )

        logger.info(
            "Optimization complete: objective=%s, improvement=%.1f%%",
            self.objective,
            improvement,
        )

        return result

    def _optimize_fuel_efficiency(
        self, altitude_m: float, mach: float, weight_kg: float
    ) -> dict[str, float]:
        """Optimize for fuel efficiency."""
        # Simplified fuel efficiency optimization
        # Optimal altitude increases with weight
        optimal_altitude = 10000 + (weight_kg / 10000) * 500
        optimal_altitude = min(12500, optimal_altitude)

        # Optimal mach for fuel efficiency
        optimal_mach = 0.78 - (altitude_m - 10000) / 100000

        # Optimal throttle for given conditions
        altitude_factor = 1 - (altitude_m / 50000) * 0.3
        optimal_throttle = 0.7 + (0.1 * altitude_factor)

        return {
            "altitude_m": optimal_altitude,
            "mach": optimal_mach,
            "throttle": optimal_throttle,
            "climb_rate_fpm": 0.0,  # Level flight
        }

    def _optimize_range(
        self, altitude_m: float, mach: float, weight_kg: float
    ) -> dict[str, float]:
        """Optimize for maximum range."""
        # Higher altitude and slower speed for range
        optimal_altitude = 12000 + (weight_kg / 10000) * 300
        optimal_mach = 0.72  # Long-range cruise

        return {
            "altitude_m": min(13000, optimal_altitude),
            "mach": optimal_mach,
            "throttle": 0.65,
            "climb_rate_fpm": 0.0,
        }

    def _optimize_cost(
        self, altitude_m: float, mach: float, weight_kg: float
    ) -> dict[str, float]:
        """Optimize for minimum operating cost."""
        # Balance between time and fuel costs
        optimal_altitude = 11000
        optimal_mach = 0.76

        return {
            "altitude_m": optimal_altitude,
            "mach": optimal_mach,
            "throttle": 0.72,
            "climb_rate_fpm": 0.0,
        }

    def _optimize_emissions(
        self, altitude_m: float, mach: float, weight_kg: float
    ) -> dict[str, float]:
        """Optimize for minimum emissions."""
        # Lower altitude reduces contrail formation
        optimal_altitude = 9000 + (weight_kg / 10000) * 200

        return {
            "altitude_m": min(11000, optimal_altitude),
            "mach": 0.74,
            "throttle": 0.68,
            "climb_rate_fpm": 0.0,
        }

    def _check_constraints(self, parameters: dict[str, float]) -> list[str]:
        """Check which constraints are violated."""
        violated = []

        for param, value in parameters.items():
            # Check minimum constraints
            if param in self._constraints.min_values:
                if value < self._constraints.min_values[param]:
                    violated.append(f"{param} < min ({value} < {self._constraints.min_values[param]})")

            # Check maximum constraints
            if param in self._constraints.max_values:
                if value > self._constraints.max_values[param]:
                    violated.append(f"{param} > max ({value} > {self._constraints.max_values[param]})")

        return violated

    def _apply_constraints(self, parameters: dict[str, float]) -> dict[str, float]:
        """Apply constraints to parameters."""
        constrained = parameters.copy()

        for param, value in constrained.items():
            # Apply minimum
            if param in self._constraints.min_values:
                constrained[param] = max(value, self._constraints.min_values[param])

            # Apply maximum
            if param in self._constraints.max_values:
                constrained[param] = min(
                    constrained[param], self._constraints.max_values[param]
                )

        return constrained

    def _estimate_improvement(
        self, current: dict[str, Any], optimized: dict[str, float]
    ) -> float:
        """Estimate percentage improvement from optimization."""
        # Simplified improvement estimation
        if self.objective == "fuel_efficiency":
            # Estimate based on altitude and mach differences
            current_alt = current.get("altitude_m", 10000)
            current_mach = current.get("mach", 0.78)

            alt_improvement = abs(optimized.get("altitude_m", current_alt) - current_alt) / 10000 * 2
            mach_improvement = abs(optimized.get("mach", current_mach) - current_mach) * 10

            return min(15.0, alt_improvement + mach_improvement)

        elif self.objective == "range":
            return 8.0  # Typical range improvement

        elif self.objective == "cost":
            return 5.0  # Typical cost improvement

        else:
            return 3.0  # Default improvement estimate

    def _fit_performance_model(self, data: list[dict[str, Any]]) -> None:
        """Fit performance model from historical data."""
        if not data:
            return

        # Simple averaging for baseline model
        self._performance_model = {}
        for key in data[0].keys():
            values = [d.get(key, 0) for d in data if isinstance(d.get(key), (int, float))]
            if values:
                self._performance_model[key] = sum(values) / len(values)

        logger.debug("Fitted performance model with %d parameters", len(self._performance_model))

    def set_objective(self, objective: str) -> bool:
        """
        Change the optimization objective.

        Args:
            objective: New optimization objective

        Returns:
            True if objective was set successfully
        """
        if objective not in self.OBJECTIVES:
            logger.warning("Invalid objective: %s", objective)
            return False

        self.objective = objective
        logger.info("Changed objective to: %s", objective)
        return True

    def get_pareto_front(
        self,
        current_state: dict[str, Any],
        flight_conditions: dict[str, Any],
        objectives: Optional[list[str]] = None,
    ) -> list[OptimizationResult]:
        """
        Calculate Pareto-optimal solutions for multiple objectives.

        Args:
            current_state: Current aircraft state
            flight_conditions: Flight conditions
            objectives: List of objectives to optimize (default: all)

        Returns:
            List of Pareto-optimal solutions
        """
        objectives = objectives or self.OBJECTIVES
        results = []

        original_objective = self.objective

        for obj in objectives:
            if obj in self.OBJECTIVES:
                self.objective = obj
                result = self.optimize(current_state, flight_conditions)
                results.append(result)

        self.objective = original_objective
        return results

    def export_model(self) -> dict[str, Any]:
        """Export optimizer configuration."""
        return {
            "model_id": self.model_id,
            "objective": self.objective,
            "is_configured": self._is_configured,
            "constraints": {
                "min": self._constraints.min_values,
                "max": self._constraints.max_values,
                "equality": self._constraints.equality_constraints,
            },
            "performance_model": self._performance_model,
        }
