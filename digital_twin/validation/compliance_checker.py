# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Compliance checker for AMPEL360 digital twin.

This module provides regulatory compliance checking capabilities
for aviation standards and software certification.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)


class ComplianceStandard(Enum):
    """Supported compliance standards."""

    DO_178C = "DO-178C"
    DO_254 = "DO-254"
    CS_25 = "CS-25"
    FAR_25 = "FAR-25"
    ARP_4754A = "ARP-4754A"
    ISO_23247 = "ISO-23247"
    EU_AI_ACT = "EU-AI-Act"


@dataclass
class ComplianceRequirement:
    """Single compliance requirement."""

    requirement_id: str
    standard: str
    description: str
    section: str
    category: str
    verification_method: str = "review"  # review, analysis, test, demonstration
    evidence_required: list[str] = field(default_factory=list)


@dataclass
class ComplianceCheck:
    """Result of a compliance check."""

    requirement_id: str
    compliant: bool
    evidence_provided: list[str] = field(default_factory=list)
    findings: str = ""
    verified_by: str = ""
    verified_date: Optional[datetime] = None


@dataclass
class ComplianceResult:
    """Overall compliance assessment result."""

    standard: str
    total_requirements: int
    compliant_count: int
    non_compliant_count: int
    partial_count: int
    compliance_percentage: float
    checks: list[ComplianceCheck] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.utcnow)
    notes: str = ""


class ComplianceChecker:
    """
    Checks compliance against aviation and software standards.

    Provides automated and manual compliance verification against
    standards like DO-178C, CS-25, and others.

    Attributes:
        loaded_standards: List of loaded compliance standards
    """

    def __init__(self) -> None:
        """Initialize the compliance checker."""
        self._requirements: dict[str, list[ComplianceRequirement]] = {}
        self._checks: dict[str, dict[str, ComplianceCheck]] = {}
        self.loaded_standards: list[str] = []

        logger.info("Initialized ComplianceChecker")

    def load_requirements(
        self,
        standard: str,
        requirements: Optional[list[dict[str, Any]]] = None,
    ) -> bool:
        """
        Load compliance requirements for a standard.

        Args:
            standard: Standard identifier (e.g., DO-178C)
            requirements: Optional custom requirements list

        Returns:
            True if requirements were loaded successfully
        """
        if requirements:
            # Load custom requirements
            reqs = [
                ComplianceRequirement(
                    requirement_id=r["id"],
                    standard=standard,
                    description=r.get("description", ""),
                    section=r.get("section", ""),
                    category=r.get("category", ""),
                    verification_method=r.get("verification_method", "review"),
                    evidence_required=r.get("evidence_required", []),
                )
                for r in requirements
            ]
        else:
            # Load default requirements
            reqs = self._get_default_requirements(standard)

        if reqs:
            self._requirements[standard] = reqs
            self._checks[standard] = {}
            self.loaded_standards.append(standard)
            logger.info("Loaded %d requirements for %s", len(reqs), standard)
            return True

        logger.warning("No requirements found for %s", standard)
        return False

    def check(
        self,
        artifact: Any,
        standard: Optional[str] = None,
        categories: Optional[list[str]] = None,
    ) -> ComplianceResult:
        """
        Check artifact compliance against requirements.

        Args:
            artifact: Artifact to check (model, document, code)
            standard: Specific standard to check (None for all loaded)
            categories: Specific categories to check

        Returns:
            ComplianceResult with assessment
        """
        standards_to_check = [standard] if standard else self.loaded_standards

        all_checks: list[ComplianceCheck] = []
        total_reqs = 0
        compliant = 0
        non_compliant = 0
        partial = 0

        for std in standards_to_check:
            if std not in self._requirements:
                continue

            requirements = self._requirements[std]
            if categories:
                requirements = [r for r in requirements if r.category in categories]

            for req in requirements:
                total_reqs += 1
                check = self._check_requirement(artifact, req)
                all_checks.append(check)

                if check.compliant:
                    compliant += 1
                elif check.findings:
                    non_compliant += 1
                else:
                    partial += 1

        compliance_pct = (compliant / max(total_reqs, 1)) * 100

        result = ComplianceResult(
            standard=standard or "Multiple",
            total_requirements=total_reqs,
            compliant_count=compliant,
            non_compliant_count=non_compliant,
            partial_count=partial,
            compliance_percentage=compliance_pct,
            checks=all_checks,
            notes=f"Checked against {len(standards_to_check)} standard(s)",
        )

        logger.info(
            "Compliance check complete: %.1f%% (%d/%d requirements)",
            compliance_pct,
            compliant,
            total_reqs,
        )

        return result

    def record_evidence(
        self,
        standard: str,
        requirement_id: str,
        evidence: list[str],
        findings: str = "",
        verified_by: str = "",
    ) -> bool:
        """
        Record compliance evidence for a requirement.

        Args:
            standard: Standard identifier
            requirement_id: Requirement ID
            evidence: List of evidence documents/artifacts
            findings: Any findings or notes
            verified_by: Verifier name

        Returns:
            True if evidence was recorded
        """
        if standard not in self._checks:
            self._checks[standard] = {}

        check = ComplianceCheck(
            requirement_id=requirement_id,
            compliant=len(findings) == 0,
            evidence_provided=evidence,
            findings=findings,
            verified_by=verified_by,
            verified_date=datetime.utcnow(),
        )

        self._checks[standard][requirement_id] = check
        logger.debug("Recorded evidence for %s/%s", standard, requirement_id)
        return True

    def get_requirements(
        self, standard: str, category: Optional[str] = None
    ) -> list[ComplianceRequirement]:
        """Get requirements for a standard."""
        reqs = self._requirements.get(standard, [])
        if category:
            reqs = [r for r in reqs if r.category == category]
        return reqs

    def get_compliance_status(
        self, standard: str, requirement_id: str
    ) -> Optional[ComplianceCheck]:
        """Get compliance status for a specific requirement."""
        return self._checks.get(standard, {}).get(requirement_id)

    def generate_report(
        self, result: ComplianceResult, format: str = "text"
    ) -> str:
        """
        Generate a compliance report.

        Args:
            result: ComplianceResult to format
            format: Output format (text, markdown, json)

        Returns:
            Formatted report
        """
        if format == "markdown":
            return self._format_markdown(result)
        elif format == "json":
            import json
            return json.dumps(self._result_to_dict(result), indent=2)
        return self._format_text(result)

    def _check_requirement(
        self, artifact: Any, requirement: ComplianceRequirement
    ) -> ComplianceCheck:
        """Check a single requirement against an artifact."""
        # Check if evidence has been recorded
        existing_check = self._checks.get(requirement.standard, {}).get(
            requirement.requirement_id
        )
        if existing_check:
            return existing_check

        # Perform automated check where possible
        evidence: list[str] = []
        findings = ""
        compliant = False

        # Check for standard artifact attributes
        if hasattr(artifact, "documentation"):
            evidence.append("documentation")
        if hasattr(artifact, "test_results"):
            evidence.append("test_results")
        if hasattr(artifact, "review_records"):
            evidence.append("review_records")

        # Simple compliance logic based on evidence
        if requirement.evidence_required:
            missing = set(requirement.evidence_required) - set(evidence)
            if missing:
                findings = f"Missing evidence: {', '.join(missing)}"
            else:
                compliant = True
        else:
            # No specific evidence required, mark as partial
            compliant = len(evidence) > 0

        return ComplianceCheck(
            requirement_id=requirement.requirement_id,
            compliant=compliant,
            evidence_provided=evidence,
            findings=findings,
        )

    def _get_default_requirements(
        self, standard: str
    ) -> list[ComplianceRequirement]:
        """Get default requirements for a standard."""
        defaults: dict[str, list[ComplianceRequirement]] = {
            "DO-178C": [
                ComplianceRequirement(
                    requirement_id="DO178C-SDP-01",
                    standard="DO-178C",
                    description="Software Development Plan documentation",
                    section="4.0",
                    category="planning",
                    verification_method="review",
                    evidence_required=["documentation"],
                ),
                ComplianceRequirement(
                    requirement_id="DO178C-REQ-01",
                    standard="DO-178C",
                    description="Requirements traceability",
                    section="5.0",
                    category="requirements",
                    verification_method="analysis",
                    evidence_required=["traceability_matrix"],
                ),
                ComplianceRequirement(
                    requirement_id="DO178C-TEST-01",
                    standard="DO-178C",
                    description="Test coverage",
                    section="6.0",
                    category="testing",
                    verification_method="test",
                    evidence_required=["test_results", "coverage_report"],
                ),
            ],
            "CS-25": [
                ComplianceRequirement(
                    requirement_id="CS25-1309",
                    standard="CS-25",
                    description="Equipment, systems and installations",
                    section="CS 25.1309",
                    category="systems",
                    verification_method="analysis",
                    evidence_required=["safety_analysis"],
                ),
                ComplianceRequirement(
                    requirement_id="CS25-1302",
                    standard="CS-25",
                    description="Installed systems and equipment",
                    section="CS 25.1302",
                    category="systems",
                    verification_method="test",
                    evidence_required=["test_results"],
                ),
            ],
            "ISO-23247": [
                ComplianceRequirement(
                    requirement_id="ISO23247-4.1",
                    standard="ISO-23247",
                    description="Digital twin framework overview",
                    section="4.1",
                    category="framework",
                    verification_method="review",
                    evidence_required=["documentation"],
                ),
                ComplianceRequirement(
                    requirement_id="ISO23247-5.1",
                    standard="ISO-23247",
                    description="Data collection entity",
                    section="5.1",
                    category="data",
                    verification_method="analysis",
                    evidence_required=["data_flow_documentation"],
                ),
            ],
        }

        return defaults.get(standard, [])

    def _format_text(self, result: ComplianceResult) -> str:
        """Format result as plain text."""
        lines = [
            f"=== Compliance Report: {result.standard} ===",
            f"Timestamp: {result.timestamp.isoformat()}",
            f"Compliance: {result.compliance_percentage:.1f}%",
            f"Total: {result.total_requirements}, "
            f"Compliant: {result.compliant_count}, "
            f"Non-compliant: {result.non_compliant_count}",
            "",
            "Requirements:",
        ]

        for check in result.checks:
            status = "✓" if check.compliant else "✗"
            lines.append(f"  {status} {check.requirement_id}: {check.findings or 'Compliant'}")

        return "\n".join(lines)

    def _format_markdown(self, result: ComplianceResult) -> str:
        """Format result as markdown."""
        lines = [
            f"# Compliance Report: {result.standard}",
            "",
            f"**Generated:** {result.timestamp.isoformat()}",
            f"**Compliance:** {result.compliance_percentage:.1f}%",
            "",
            "## Summary",
            "",
            f"| Metric | Count |",
            f"|--------|-------|",
            f"| Total Requirements | {result.total_requirements} |",
            f"| Compliant | {result.compliant_count} |",
            f"| Non-Compliant | {result.non_compliant_count} |",
            f"| Partial | {result.partial_count} |",
            "",
            "## Requirements",
            "",
            "| ID | Status | Findings |",
            "|----|--------|----------|",
        ]

        for check in result.checks:
            status = "✅" if check.compliant else "❌"
            findings = check.findings or "-"
            lines.append(f"| {check.requirement_id} | {status} | {findings} |")

        return "\n".join(lines)

    def _result_to_dict(self, result: ComplianceResult) -> dict[str, Any]:
        """Convert result to dictionary."""
        return {
            "standard": result.standard,
            "timestamp": result.timestamp.isoformat(),
            "compliance_percentage": result.compliance_percentage,
            "summary": {
                "total": result.total_requirements,
                "compliant": result.compliant_count,
                "non_compliant": result.non_compliant_count,
                "partial": result.partial_count,
            },
            "checks": [
                {
                    "requirement_id": c.requirement_id,
                    "compliant": c.compliant,
                    "evidence": c.evidence_provided,
                    "findings": c.findings,
                }
                for c in result.checks
            ],
        }
