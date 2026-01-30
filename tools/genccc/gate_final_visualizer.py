#!/usr/bin/env python3
# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# SPDX-License-Identifier: Apache-2.0

"""
Final Gate — Comprehensive Chain State Visualization

Generates comprehensive images/graphs from chain state showing:
- Metadata coherence status across artifacts
- Cross-reference validation results
- Evolution proposals and recommendations
- Overall health metrics

Outputs SVG and Markdown reports for human review.

Usage:
    python tools/genccc/gate_final_visualizer.py \
        --chain .genccc/chain_state.json \
        --output .genccc/comprehensive_report.md \
        --graph .genccc/chain_visualization.svg

Exit codes:
    0: Success
    1: Failed to generate visualization
"""

import argparse
import json
import logging
import pathlib
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ============================================================================
# DATA ANALYSIS
# ============================================================================

def analyze_chain_state(chain_state: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze chain state and compute statistics."""
    artifacts = chain_state.get("artifacts", [])
    
    total_artifacts = len(artifacts)
    
    # Gate 0 statistics
    gate0_stats = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "skipped": 0,
        "errors": 0,
        "warnings": 0,
    }
    
    # Gate 1 statistics
    gate1_stats = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "skipped": 0,
        "errors": 0,
        "warnings": 0,
        "total_links": 0,
        "total_refs": 0,
    }
    
    # Artifact classifications
    healthy_artifacts = []
    warning_artifacts = []
    error_artifacts = []
    
    for artifact in artifacts:
        path = artifact.get("path", "")
        
        # Gate 0 analysis
        gate0 = artifact.get("gate0_metadata", {})
        if gate0:
            gate0_stats["total"] += 1
            status = gate0.get("status", "")
            
            if status == "passed":
                gate0_stats["passed"] += 1
            elif status == "failed":
                gate0_stats["failed"] += 1
            elif status == "skipped":
                gate0_stats["skipped"] += 1
            elif status == "passed_with_warnings":
                gate0_stats["passed"] += 1
                gate0_stats["warnings"] += gate0.get("warning_count", 0)
            
            gate0_stats["errors"] += gate0.get("error_count", 0)
            gate0_stats["warnings"] += gate0.get("warning_count", 0)
        
        # Gate 1 analysis
        gate1 = artifact.get("gate1_xref", {})
        if gate1:
            gate1_stats["total"] += 1
            status = gate1.get("status", "")
            
            if status == "passed":
                gate1_stats["passed"] += 1
            elif status == "failed":
                gate1_stats["failed"] += 1
            elif status == "skipped":
                gate1_stats["skipped"] += 1
            elif status == "passed_with_warnings":
                gate1_stats["passed"] += 1
            
            gate1_stats["errors"] += gate1.get("error_count", 0)
            gate1_stats["warnings"] += gate1.get("warning_count", 0)
            gate1_stats["total_links"] += gate1.get("links_found", 0)
            gate1_stats["total_refs"] += gate1.get("references_found", 0)
        
        # Classify artifact health
        has_errors = (
            gate0.get("error_count", 0) > 0 or
            gate1.get("error_count", 0) > 0
        )
        has_warnings = (
            gate0.get("warning_count", 0) > 0 or
            gate1.get("warning_count", 0) > 0
        )
        
        if has_errors:
            error_artifacts.append(path)
        elif has_warnings:
            warning_artifacts.append(path)
        else:
            healthy_artifacts.append(path)
    
    return {
        "total_artifacts": total_artifacts,
        "gate0": gate0_stats,
        "gate1": gate1_stats,
        "healthy_artifacts": healthy_artifacts,
        "warning_artifacts": warning_artifacts,
        "error_artifacts": error_artifacts,
    }


# ============================================================================
# EVOLUTION PROPOSALS
# ============================================================================

def generate_evolution_proposals(analysis: Dict[str, Any]) -> List[str]:
    """Generate evolution proposals based on analysis."""
    proposals = []
    
    gate0 = analysis["gate0"]
    gate1 = analysis["gate1"]
    
    # Metadata proposals
    if gate0["errors"] > 0:
        proposals.append(
            f"🔴 **CRITICAL**: Fix {gate0['errors']} metadata errors across "
            f"{gate0['failed']} artifacts"
        )
    
    if gate0["warnings"] > 10:
        proposals.append(
            f"⚠️ **Recommend**: Address {gate0['warnings']} metadata warnings "
            f"to improve documentation quality"
        )
    
    if gate0["skipped"] > 0:
        proposals.append(
            f"💡 **Suggestion**: Add metadata to {gate0['skipped']} artifacts "
            f"for better traceability"
        )
    
    # Cross-reference proposals
    if gate1["errors"] > 0:
        proposals.append(
            f"🔴 **CRITICAL**: Fix {gate1['errors']} broken cross-references "
            f"across {gate1['failed']} artifacts"
        )
    
    if gate1["warnings"] > 5:
        proposals.append(
            f"⚠️ **Recommend**: Review {gate1['warnings']} cross-reference warnings"
        )
    
    # Positive feedback
    if len(analysis["healthy_artifacts"]) > len(analysis["error_artifacts"]):
        proposals.append(
            f"✅ **Good**: {len(analysis['healthy_artifacts'])} artifacts "
            f"are healthy and well-structured"
        )
    
    # General recommendations
    if gate1["total_links"] > 0:
        avg_links = gate1["total_links"] / max(gate1["total"], 1)
        if avg_links < 2:
            proposals.append(
                f"💡 **Suggestion**: Increase cross-referencing between documents "
                f"(avg: {avg_links:.1f} links per document)"
            )
    
    return proposals


# ============================================================================
# SVG VISUALIZATION
# ============================================================================

def generate_svg_visualization(analysis: Dict[str, Any]) -> str:
    """Generate SVG visualization of chain state."""
    gate0 = analysis["gate0"]
    gate1 = analysis["gate1"]
    
    # SVG dimensions
    width = 800
    height = 600
    margin = 50
    
    # Calculate percentages with bounds checking
    total = analysis["total_artifacts"]
    if total == 0:
        healthy_pct = warning_pct = error_pct = 0
    else:
        healthy_pct = (len(analysis["healthy_artifacts"]) / total) * 100
        warning_pct = (len(analysis["warning_artifacts"]) / total) * 100
        error_pct = (len(analysis["error_artifacts"]) / total) * 100
    
    # Bar widths (max 600px total to fit within chart area)
    max_bar_width = 600
    healthy_width = (healthy_pct / 100) * max_bar_width
    warning_width = (warning_pct / 100) * max_bar_width
    error_width = (error_pct / 100) * max_bar_width
    
    svg_lines = [
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
        '  <!-- Title -->',
        f'  <text x="{width/2}" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#333">',
        '    Gate Chain Validation Status',
        '  </text>',
        '',
        '  <!-- Gate 0 Summary -->',
        f'  <g transform="translate({margin}, 80)">',
        '    <text x="0" y="0" font-size="16" font-weight="bold" fill="#333">Gate 0: Metadata Coherence</text>',
        f'    <rect x="0" y="10" width="300" height="80" fill="#f0f0f0" stroke="#ccc" rx="5"/>',
        f'    <text x="10" y="30" font-size="14" fill="#333">Total: {gate0["total"]}</text>',
        f'    <text x="10" y="50" font-size="14" fill="#28a745">✓ Passed: {gate0["passed"]}</text>',
        f'    <text x="10" y="70" font-size="14" fill="#dc3545">✗ Failed: {gate0["failed"]}</text>',
        f'    <text x="150" y="30" font-size="14" fill="#dc3545">Errors: {gate0["errors"]}</text>',
        f'    <text x="150" y="50" font-size="14" fill="#ffc107">Warnings: {gate0["warnings"]}</text>',
        f'    <text x="150" y="70" font-size="14" fill="#6c757d">Skipped: {gate0["skipped"]}</text>',
        '  </g>',
        '',
        '  <!-- Gate 1 Summary -->',
        f'  <g transform="translate({width - margin - 300}, 80)">',
        '    <text x="0" y="0" font-size="16" font-weight="bold" fill="#333">Gate 1: Cross-References</text>',
        f'    <rect x="0" y="10" width="300" height="80" fill="#f0f0f0" stroke="#ccc" rx="5"/>',
        f'    <text x="10" y="30" font-size="14" fill="#333">Total: {gate1["total"]}</text>',
        f'    <text x="10" y="50" font-size="14" fill="#28a745">✓ Passed: {gate1["passed"]}</text>',
        f'    <text x="10" y="70" font-size="14" fill="#dc3545">✗ Failed: {gate1["failed"]}</text>',
        f'    <text x="150" y="30" font-size="14" fill="#dc3545">Errors: {gate1["errors"]}</text>',
        f'    <text x="150" y="50" font-size="14" fill="#6c757d">Links: {gate1["total_links"]}</text>',
        f'    <text x="150" y="70" font-size="14" fill="#6c757d">Refs: {gate1["total_refs"]}</text>',
        '  </g>',
        '',
        '  <!-- Overall Health Bar Chart -->',
        f'  <g transform="translate({margin}, 220)">',
        '    <text x="0" y="0" font-size="16" font-weight="bold" fill="#333">Artifact Health Distribution</text>',
        '',
        f'    <!-- Healthy bar -->',
        f'    <rect x="0" y="20" width="{healthy_width}" height="40" fill="#28a745"/>',
        f'    <text x="5" y="45" font-size="14" fill="white" font-weight="bold">{healthy_pct:.1f}% Healthy</text>',
        '',
        f'    <!-- Warning bar -->',
        f'    <rect x="{healthy_width}" y="20" width="{warning_width}" height="40" fill="#ffc107"/>',
        f'    <text x="{healthy_width + 5}" y="45" font-size="14" fill="#333" font-weight="bold">{warning_pct:.1f}% Warnings</text>',
        '',
        f'    <!-- Error bar -->',
        f'    <rect x="{healthy_width + warning_width}" y="20" width="{error_width}" height="40" fill="#dc3545"/>',
        f'    <text x="{healthy_width + warning_width + 5}" y="45" font-size="14" fill="white" font-weight="bold">{error_pct:.1f}% Errors</text>',
        '',
        f'    <!-- Counts -->',
        f'    <text x="0" y="80" font-size="12" fill="#333">Healthy: {len(analysis["healthy_artifacts"])}</text>',
        f'    <text x="150" y="80" font-size="12" fill="#333">Warnings: {len(analysis["warning_artifacts"])}</text>',
        f'    <text x="300" y="80" font-size="12" fill="#333">Errors: {len(analysis["error_artifacts"])}</text>',
        '  </g>',
        '',
        '  <!-- Legend -->',
        f'  <g transform="translate({margin}, {height - margin - 60})">',
        '    <text x="0" y="0" font-size="12" fill="#666">Legend:</text>',
        '    <circle cx="10" cy="20" r="5" fill="#28a745"/>',
        '    <text x="20" y="24" font-size="11" fill="#666">No issues</text>',
        '    <circle cx="100" cy="20" r="5" fill="#ffc107"/>',
        '    <text x="110" y="24" font-size="11" fill="#666">Warnings only</text>',
        '    <circle cx="220" cy="20" r="5" fill="#dc3545"/>',
        '    <text x="230" y="24" font-size="11" fill="#666">Has errors</text>',
        '  </g>',
        '',
        '  <!-- Timestamp -->',
        f'  <text x="{width - margin}" y="{height - 10}" text-anchor="end" font-size="10" fill="#999">',
        f'    Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
        '  </text>',
        '',
        '</svg>',
    ]
    
    return '\n'.join(svg_lines)


# ============================================================================
# MARKDOWN REPORT
# ============================================================================

def generate_markdown_report(
    analysis: Dict[str, Any],
    proposals: List[str]
) -> str:
    """Generate comprehensive Markdown report."""
    gate0 = analysis["gate0"]
    gate1 = analysis["gate1"]
    
    lines = [
        "# Comprehensive Gate Chain Validation Report",
        "",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
        f"- **Total Artifacts Analyzed**: {analysis['total_artifacts']}",
        f"- **Healthy Artifacts**: {len(analysis['healthy_artifacts'])} "
        f"({len(analysis['healthy_artifacts'])/max(analysis['total_artifacts'], 1)*100:.1f}%)",
        f"- **Artifacts with Warnings**: {len(analysis['warning_artifacts'])} "
        f"({len(analysis['warning_artifacts'])/max(analysis['total_artifacts'], 1)*100:.1f}%)",
        f"- **Artifacts with Errors**: {len(analysis['error_artifacts'])} "
        f"({len(analysis['error_artifacts'])/max(analysis['total_artifacts'], 1)*100:.1f}%)",
        "",
        "---",
        "",
        "## Gate 0 — Metadata Coherence Screen",
        "",
        "### Statistics",
        "",
        f"- **Total Screened**: {gate0['total']}",
        f"- **Passed**: {gate0['passed']} ✅",
        f"- **Failed**: {gate0['failed']} ❌",
        f"- **Skipped (No Metadata)**: {gate0['skipped']} ⊝",
        f"- **Total Errors**: {gate0['errors']}",
        f"- **Total Warnings**: {gate0['warnings']}",
        "",
        "### Key Findings",
        "",
    ]
    
    if gate0['errors'] > 0:
        lines.append(f"⚠️ **{gate0['errors']} metadata errors** require immediate attention.")
        lines.append("")
    
    if gate0['warnings'] > 0:
        lines.append(f"ℹ️ **{gate0['warnings']} metadata warnings** should be reviewed.")
        lines.append("")
    
    if gate0['failed'] == 0:
        lines.append("✅ All artifacts with metadata passed coherence checks!")
        lines.append("")
    
    lines.extend([
        "---",
        "",
        "## Gate 1 — Cross-Reference Validation",
        "",
        "### Statistics",
        "",
        f"- **Total Validated**: {gate1['total']}",
        f"- **Passed**: {gate1['passed']} ✅",
        f"- **Failed**: {gate1['failed']} ❌",
        f"- **Skipped (No References)**: {gate1['skipped']} ⊝",
        f"- **Total Errors**: {gate1['errors']}",
        f"- **Total Warnings**: {gate1['warnings']}",
        f"- **Links Found**: {gate1['total_links']}",
        f"- **Document References**: {gate1['total_refs']}",
        "",
        "### Key Findings",
        "",
    ])
    
    if gate1['errors'] > 0:
        lines.append(f"⚠️ **{gate1['errors']} broken references** require fixing.")
        lines.append("")
    
    if gate1['total_links'] > 0:
        avg_links = gate1['total_links'] / max(gate1['total'], 1)
        lines.append(f"📊 Average links per document: **{avg_links:.1f}**")
        lines.append("")
    
    if gate1['failed'] == 0 and gate1['total'] > 0:
        lines.append("✅ All cross-references are valid!")
        lines.append("")
    
    lines.extend([
        "---",
        "",
        "## Evolution Proposals & Recommendations",
        "",
    ])
    
    if proposals:
        for proposal in proposals:
            lines.append(f"- {proposal}")
        lines.append("")
    else:
        lines.append("✅ No specific proposals — documentation is in good health!")
        lines.append("")
    
    # Artifact lists (limited)
    lines.extend([
        "---",
        "",
        "## Artifact Details",
        "",
    ])
    
    if analysis['error_artifacts']:
        lines.append("### ❌ Artifacts with Errors")
        lines.append("")
        for artifact in analysis['error_artifacts'][:20]:
            lines.append(f"- `{artifact}`")
        if len(analysis['error_artifacts']) > 20:
            lines.append(f"- ... and {len(analysis['error_artifacts']) - 20} more")
        lines.append("")
    
    if analysis['warning_artifacts']:
        lines.append("### ⚠️ Artifacts with Warnings")
        lines.append("")
        for artifact in analysis['warning_artifacts'][:20]:
            lines.append(f"- `{artifact}`")
        if len(analysis['warning_artifacts']) > 20:
            lines.append(f"- ... and {len(analysis['warning_artifacts']) - 20} more")
        lines.append("")
    
    lines.extend([
        "---",
        "",
        "## Next Steps",
        "",
        "1. **Address Critical Errors**: Fix all errors flagged in Gate 0 and Gate 1",
        "2. **Review Warnings**: Evaluate warnings and determine if action is needed",
        "3. **Improve Coverage**: Add metadata and cross-references where missing",
        "4. **Monitor Trends**: Track these metrics over time to measure improvement",
        "",
        "---",
        "",
        "*This report was automatically generated by the GenCCC Gate Chain system.*",
    ])
    
    return '\n'.join(lines)


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Final Gate — Comprehensive Chain State Visualization"
    )
    parser.add_argument(
        "--chain",
        type=pathlib.Path,
        default=pathlib.Path(".genccc/chain_state.json"),
        help="Path to chain state JSON file"
    )
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=pathlib.Path(".genccc/comprehensive_report.md"),
        help="Output Markdown report path"
    )
    parser.add_argument(
        "--graph",
        type=pathlib.Path,
        default=pathlib.Path(".genccc/chain_visualization.svg"),
        help="Output SVG graph path"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Load chain state
    if not args.chain.exists():
        logger.error(f"Chain state file not found: {args.chain}")
        sys.exit(1)
    
    try:
        with open(args.chain, "r", encoding="utf-8") as f:
            chain_state = json.load(f)
    except Exception as e:
        logger.error(f"Failed to load chain state: {e}")
        sys.exit(1)
    
    # Analyze chain state
    logger.info("Analyzing chain state...")
    analysis = analyze_chain_state(chain_state)
    
    # Generate proposals
    logger.info("Generating evolution proposals...")
    proposals = generate_evolution_proposals(analysis)
    
    # Generate outputs
    logger.info("Generating SVG visualization...")
    svg_content = generate_svg_visualization(analysis)
    
    logger.info("Generating Markdown report...")
    markdown_content = generate_markdown_report(analysis, proposals)
    
    # Write outputs
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.graph.parent.mkdir(parents=True, exist_ok=True)
    
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    logger.info(f"Wrote report: {args.output}")
    
    with open(args.graph, "w", encoding="utf-8") as f:
        f.write(svg_content)
    logger.info(f"Wrote graph: {args.graph}")
    
    # Print summary
    print(f"\n{'=' * 60}")
    print("Final Gate — Comprehensive Visualization Generated")
    print(f"{'=' * 60}")
    print(f"Total Artifacts: {analysis['total_artifacts']}")
    print(f"Healthy: {len(analysis['healthy_artifacts'])}")
    print(f"Warnings: {len(analysis['warning_artifacts'])}")
    print(f"Errors: {len(analysis['error_artifacts'])}")
    print(f"\nOutputs:")
    print(f"  Report: {args.output}")
    print(f"  Graph:  {args.graph}")
    print(f"\nProposals: {len(proposals)}")
    
    sys.exit(0)


if __name__ == "__main__":
    main()
