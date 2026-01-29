# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Data validator for AMPEL360 digital twin.

This module provides data validation capabilities for ensuring
data integrity and consistency.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Optional
import logging
import re

logger = logging.getLogger(__name__)


class RuleType(Enum):
    """Types of validation rules."""

    RANGE = "range"
    TYPE = "type"
    PATTERN = "pattern"
    REQUIRED = "required"
    CUSTOM = "custom"
    ENUM = "enum"


@dataclass
class ValidationRule:
    """Validation rule definition."""

    field: str
    rule_type: RuleType
    parameters: dict[str, Any] = field(default_factory=dict)
    error_message: str = ""
    severity: str = "error"  # error, warning


@dataclass
class ValidationError:
    """Validation error detail."""

    field: str
    rule_type: str
    message: str
    severity: str
    value: Any = None


@dataclass
class DataValidationResult:
    """Result of data validation."""

    is_valid: bool
    errors: list[ValidationError] = field(default_factory=list)
    warnings: list[ValidationError] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.utcnow)


class DataValidator:
    """
    Validates data integrity and consistency.

    Provides rule-based validation for sensor data, model inputs,
    and other data sources.

    Attributes:
        strict_mode: If True, warnings are treated as errors
    """

    def __init__(self, strict_mode: bool = False) -> None:
        """
        Initialize the data validator.

        Args:
            strict_mode: Treat warnings as errors
        """
        self.strict_mode = strict_mode
        self._rules: list[ValidationRule] = []
        self._custom_validators: dict[str, Callable] = {}

        logger.info("Initialized DataValidator (strict=%s)", strict_mode)

    def add_rule(
        self,
        field: str,
        constraints: dict[str, Any],
        error_message: Optional[str] = None,
        severity: str = "error",
    ) -> None:
        """
        Add a validation rule.

        Args:
            field: Field name to validate
            constraints: Constraint parameters (min, max, type, pattern, etc.)
            error_message: Custom error message
            severity: Rule severity (error, warning)
        """
        # Determine rule type from constraints
        if "min" in constraints or "max" in constraints:
            rule_type = RuleType.RANGE
        elif "type" in constraints:
            rule_type = RuleType.TYPE
        elif "pattern" in constraints:
            rule_type = RuleType.PATTERN
        elif "required" in constraints:
            rule_type = RuleType.REQUIRED
        elif "values" in constraints:
            rule_type = RuleType.ENUM
        elif "validator" in constraints:
            rule_type = RuleType.CUSTOM
            if isinstance(constraints["validator"], Callable):
                self._custom_validators[field] = constraints["validator"]
        else:
            rule_type = RuleType.REQUIRED

        rule = ValidationRule(
            field=field,
            rule_type=rule_type,
            parameters=constraints,
            error_message=error_message or f"Validation failed for {field}",
            severity=severity,
        )

        self._rules.append(rule)
        logger.debug("Added rule for %s: %s", field, rule_type.value)

    def remove_rule(self, field: str) -> bool:
        """Remove all rules for a field."""
        initial_count = len(self._rules)
        self._rules = [r for r in self._rules if r.field != field]
        return len(self._rules) < initial_count

    def validate(self, data: dict[str, Any]) -> DataValidationResult:
        """
        Validate data against all rules.

        Args:
            data: Dictionary of data to validate

        Returns:
            DataValidationResult with errors and warnings
        """
        errors: list[ValidationError] = []
        warnings: list[ValidationError] = []

        for rule in self._rules:
            error = self._apply_rule(rule, data)
            if error:
                if error.severity == "warning" and not self.strict_mode:
                    warnings.append(error)
                else:
                    errors.append(error)

        is_valid = len(errors) == 0

        result = DataValidationResult(
            is_valid=is_valid,
            errors=errors,
            warnings=warnings,
        )

        if not is_valid:
            logger.warning("Validation failed: %d errors, %d warnings", len(errors), len(warnings))

        return result

    def validate_field(self, field: str, value: Any) -> list[ValidationError]:
        """
        Validate a single field value.

        Args:
            field: Field name
            value: Value to validate

        Returns:
            List of validation errors
        """
        data = {field: value}
        result = self.validate(data)
        return result.errors + result.warnings

    def get_rules(self, field: Optional[str] = None) -> list[ValidationRule]:
        """Get validation rules, optionally filtered by field."""
        if field:
            return [r for r in self._rules if r.field == field]
        return self._rules.copy()

    def clear_rules(self) -> None:
        """Clear all validation rules."""
        self._rules.clear()
        self._custom_validators.clear()

    def _apply_rule(
        self, rule: ValidationRule, data: dict[str, Any]
    ) -> Optional[ValidationError]:
        """Apply a single validation rule."""
        field = rule.field
        value = data.get(field)

        # Check required
        if rule.rule_type == RuleType.REQUIRED:
            if value is None:
                return ValidationError(
                    field=field,
                    rule_type="required",
                    message=rule.error_message or f"{field} is required",
                    severity=rule.severity,
                    value=value,
                )
            return None

        # Skip validation if field not present (unless required)
        if value is None:
            if rule.parameters.get("required", False):
                return ValidationError(
                    field=field,
                    rule_type="required",
                    message=f"{field} is required",
                    severity=rule.severity,
                    value=value,
                )
            return None

        # Apply rule based on type
        if rule.rule_type == RuleType.RANGE:
            return self._validate_range(field, value, rule)
        elif rule.rule_type == RuleType.TYPE:
            return self._validate_type(field, value, rule)
        elif rule.rule_type == RuleType.PATTERN:
            return self._validate_pattern(field, value, rule)
        elif rule.rule_type == RuleType.ENUM:
            return self._validate_enum(field, value, rule)
        elif rule.rule_type == RuleType.CUSTOM:
            return self._validate_custom(field, value, rule)

        return None

    def _validate_range(
        self, field: str, value: Any, rule: ValidationRule
    ) -> Optional[ValidationError]:
        """Validate numeric range."""
        try:
            num_value = float(value)
        except (ValueError, TypeError):
            return ValidationError(
                field=field,
                rule_type="range",
                message=f"{field} must be a number",
                severity=rule.severity,
                value=value,
            )

        min_val = rule.parameters.get("min")
        max_val = rule.parameters.get("max")

        if min_val is not None and num_value < min_val:
            return ValidationError(
                field=field,
                rule_type="range",
                message=rule.error_message or f"{field} must be >= {min_val}",
                severity=rule.severity,
                value=value,
            )

        if max_val is not None and num_value > max_val:
            return ValidationError(
                field=field,
                rule_type="range",
                message=rule.error_message or f"{field} must be <= {max_val}",
                severity=rule.severity,
                value=value,
            )

        return None

    def _validate_type(
        self, field: str, value: Any, rule: ValidationRule
    ) -> Optional[ValidationError]:
        """Validate data type."""
        expected_type = rule.parameters.get("type")

        type_map = {
            "string": str,
            "str": str,
            "int": int,
            "integer": int,
            "float": float,
            "number": (int, float),
            "bool": bool,
            "boolean": bool,
            "list": list,
            "array": list,
            "dict": dict,
            "object": dict,
        }

        if expected_type in type_map:
            expected = type_map[expected_type]
            if not isinstance(value, expected):
                return ValidationError(
                    field=field,
                    rule_type="type",
                    message=rule.error_message or f"{field} must be of type {expected_type}",
                    severity=rule.severity,
                    value=value,
                )

        return None

    def _validate_pattern(
        self, field: str, value: Any, rule: ValidationRule
    ) -> Optional[ValidationError]:
        """Validate string pattern."""
        pattern = rule.parameters.get("pattern", "")

        if not isinstance(value, str):
            return ValidationError(
                field=field,
                rule_type="pattern",
                message=f"{field} must be a string",
                severity=rule.severity,
                value=value,
            )

        if not re.match(pattern, value):
            return ValidationError(
                field=field,
                rule_type="pattern",
                message=rule.error_message or f"{field} does not match pattern {pattern}",
                severity=rule.severity,
                value=value,
            )

        return None

    def _validate_enum(
        self, field: str, value: Any, rule: ValidationRule
    ) -> Optional[ValidationError]:
        """Validate value is in allowed set."""
        allowed_values = rule.parameters.get("values", [])

        if value not in allowed_values:
            return ValidationError(
                field=field,
                rule_type="enum",
                message=rule.error_message or f"{field} must be one of {allowed_values}",
                severity=rule.severity,
                value=value,
            )

        return None

    def _validate_custom(
        self, field: str, value: Any, rule: ValidationRule
    ) -> Optional[ValidationError]:
        """Validate using custom validator function."""
        validator = self._custom_validators.get(field)

        if validator:
            try:
                is_valid = validator(value)
                if not is_valid:
                    return ValidationError(
                        field=field,
                        rule_type="custom",
                        message=rule.error_message or f"{field} failed custom validation",
                        severity=rule.severity,
                        value=value,
                    )
            except Exception as e:
                return ValidationError(
                    field=field,
                    rule_type="custom",
                    message=f"Custom validator error: {e}",
                    severity=rule.severity,
                    value=value,
                )

        return None
