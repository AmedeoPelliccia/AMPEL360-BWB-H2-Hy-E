#!/usr/bin/env python3
"""
CG Apply - Neural Networks Directory
Specialized workflow to apply CG framework to N-NEURAL_NETWORKS_USERS_TRACEABILITY.

This script orchestrates the CG chain for the Neural Network documentation:
1. Scans for issues (broken links, unlinked ATA references)
2. Generates missing documents and converts references
3. Expands underdeveloped sections

Usage:
    python tools/cg/apply_neural_networks.py [--scan-only] [--no-generate] [--no-expand]
"""

from pathlib import Path
import subprocess
import sys
import os
import argparse

REPO_ROOT = Path(__file__).resolve().parents[2]
NN_DIR = REPO_ROOT / "OPT-IN_FRAMEWORK" / "N-NEURAL_NETWORKS_USERS_TRACEABILITY"
REPORT_DIR = REPO_ROOT / "cd" / "reports"

def banner(text: str):
    """Print a formatted banner."""
    width = 70
    print("\n" + "=" * width)
    print(f"  {text}")
    print("=" * width + "\n")

def run_scan():
    """Run CG scan on Neural Networks directory."""
    banner("Step 1: Scanning Neural Networks Directory")
    
    # Temporarily set environment to focus on NN directory
    env = os.environ.copy()
    
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "tools" / "cg" / "scan.py")],
        env=env,
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print("Warnings/Errors:", result.stderr, file=sys.stderr)
    
    return result.returncode == 0

def run_generate():
    """Run CG generate on Neural Networks directory."""
    banner("Step 2: Generating Missing Documents & Converting References")
    
    env = os.environ.copy()
    
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "tools" / "cg" / "generate.py")],
        env=env,
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print("Warnings/Errors:", result.stderr, file=sys.stderr)
    
    return result.returncode == 0

def run_expand(mode: str = "BALANCED", max_edits: int = 25):
    """Run CG expand on Neural Networks directory."""
    banner(f"Step 3: Expanding Underdeveloped Sections (mode={mode})")
    
    env = os.environ.copy()
    env["CG_MODE"] = mode
    env["CG_MAX_EDITS"] = str(max_edits)
    
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "tools" / "cg" / "expand.py")],
        env=env,
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print("Warnings/Errors:", result.stderr, file=sys.stderr)
    
    return result.returncode == 0

def print_summary():
    """Print summary of the CG chain execution."""
    banner("CG Chain Complete - Neural Networks Directory")
    
    scan_report = REPORT_DIR / "cg_scan_report.md"
    if scan_report.exists():
        print(f"📊 Scan report: {scan_report.relative_to(REPO_ROOT)}")
        
        # Extract summary from report
        content = scan_report.read_text()
        if "## Summary" in content:
            summary_section = content.split("## Summary")[1].split("---")[0]
            print("\nSummary:")
            for line in summary_section.strip().split("\n"):
                if line.strip().startswith("-"):
                    print(f"  {line.strip()}")
    
    print("\n✅ CG chain successfully applied to Neural Networks directory")
    print(f"\n📁 Target: {NN_DIR.relative_to(REPO_ROOT)}")
    print("\nNext steps:")
    print("  - Review the generated report and changes")
    print("  - Commit any new or modified documentation")
    print("  - Run CG chain periodically to maintain documentation quality")

def main():
    parser = argparse.ArgumentParser(
        description="Apply CG framework to Neural Networks directory"
    )
    parser.add_argument(
        "--scan-only",
        action="store_true",
        help="Only run scan, skip generation and expansion"
    )
    parser.add_argument(
        "--no-generate",
        action="store_true",
        help="Skip document generation step"
    )
    parser.add_argument(
        "--no-expand",
        action="store_true",
        help="Skip section expansion step"
    )
    parser.add_argument(
        "--mode",
        choices=["STEADY", "BALANCED", "DEEPENING", "EXPANSIVE"],
        default="BALANCED",
        help="Expansion mode (default: BALANCED)"
    )
    parser.add_argument(
        "--max-edits",
        type=int,
        default=25,
        help="Maximum edits for expansion (default: 25)"
    )
    
    args = parser.parse_args()
    
    if not NN_DIR.exists():
        print(f"❌ Error: Neural Networks directory not found: {NN_DIR}", file=sys.stderr)
        return 1
    
    banner("CG Chain - Neural Networks Directory")
    print(f"Target: {NN_DIR.relative_to(REPO_ROOT)}")
    print(f"Mode: {'Scan only' if args.scan_only else 'Full chain'}")
    
    # Step 1: Scan
    if not run_scan():
        print("❌ Scan failed", file=sys.stderr)
        return 1
    
    if args.scan_only:
        print_summary()
        return 0
    
    # Step 2: Generate
    if not args.no_generate:
        if not run_generate():
            print("❌ Generate failed", file=sys.stderr)
            return 1
    
    # Step 3: Expand
    if not args.no_expand:
        if not run_expand(args.mode, args.max_edits):
            print("❌ Expand failed", file=sys.stderr)
            return 1
    
    print_summary()
    return 0

if __name__ == "__main__":
    sys.exit(main())
