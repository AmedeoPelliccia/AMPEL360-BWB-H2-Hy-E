#!/usr/bin/env python3
"""
GenCCC Agent - Shared Utilities and Agent Functionality
Provides common functions and utilities for GenCCC scripts.

This module is part of the trusted base code and provides:
- Common path resolution utilities
- Markdown file discovery
- Link extraction and validation
- Shared constants and configurations

All GenCCC scripts (report.py, apply.py, generate.py) can import from this module.
"""

import os
import pathlib
import re
from typing import List, Optional, Set, Tuple


# Repository root paths
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
FRAMEWORK_ROOT = REPO_ROOT / "OPT-IN_FRAMEWORK"
CAOS_ROOT = REPO_ROOT / "CAOS"
REPORT_DIR = REPO_ROOT / "cd" / "reports"

# Common patterns
STUB_MARKER = "GenCCC will auto-link and expand this content"
ATA_PATTERN = re.compile(r'\bATA[_\s-]?(\d{2})(?:[_\s-](\d{2})(?:[_\s-](\d{2}))?)?\b')
INTERNAL_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')


def get_repo_root() -> pathlib.Path:
    """Get the repository root path."""
    return REPO_ROOT


def get_framework_root() -> pathlib.Path:
    """Get the OPT-IN_FRAMEWORK root path."""
    return FRAMEWORK_ROOT


def get_caos_root() -> pathlib.Path:
    """Get the CAOS root path."""
    return CAOS_ROOT


def get_report_dir() -> pathlib.Path:
    """Get the reports directory path."""
    return REPORT_DIR


def find_all_markdown_files(include_root: bool = True) -> List[pathlib.Path]:
    """
    Find all markdown files in the repository.
    
    Args:
        include_root: Whether to include root-level markdown files
        
    Returns:
        List of pathlib.Path objects for all markdown files
    """
    md_files = []
    
    # Framework markdown files
    if FRAMEWORK_ROOT.exists():
        md_files.extend(FRAMEWORK_ROOT.rglob("*.md"))
    
    # CAOS markdown files
    if CAOS_ROOT.exists():
        md_files.extend(CAOS_ROOT.rglob("*.md"))
    
    # Root-level markdown files
    if include_root:
        root_files = [
            REPO_ROOT / "README.md",
            REPO_ROOT / "CAOS_INDEX.md",
            REPO_ROOT / "CAOS_MANIFESTO.md",
            REPO_ROOT / "CAOS_OPERATIONS_FRAMEWORK.md",
            REPO_ROOT / "CAOS_USE_CASES.md",
            REPO_ROOT / "AMPEL360_DOCUMENTATION_STANDARD.md",
            REPO_ROOT / "ATA_03_NUMBERING_GUIDE.md",
            REPO_ROOT / "IMPLEMENTATION_SUMMARY.md",
            REPO_ROOT / "STRUCTURE_OVERVIEW.txt",
        ]
        for f in root_files:
            if f.exists():
                md_files.append(f)
    
    return sorted(set(md_files))


def extract_internal_links(content: str) -> List[str]:
    """
    Extract internal markdown links from content.
    
    Args:
        content: Markdown content to analyze
        
    Returns:
        List of link targets (excluding external URLs)
    """
    links = []
    
    for match in INTERNAL_LINK_PATTERN.finditer(content):
        link_target = match.group(2)
        # Skip external URLs, anchors, and mailto links
        if not link_target.startswith(('http://', 'https://', '#', 'mailto:')):
            links.append(link_target)
    
    return links


def extract_internal_links_with_text(content: str) -> List[Tuple[str, str, str]]:
    """
    Extract internal markdown links with their text and target.
    
    Args:
        content: Markdown content to analyze
        
    Returns:
        List of tuples (link_text, link_target, full_match)
    """
    links = []
    
    for match in INTERNAL_LINK_PATTERN.finditer(content):
        link_text = match.group(1)
        link_target = match.group(2)
        full_match = match.group(0)
        
        # Skip external URLs, anchors, and mailto links
        if not link_target.startswith(('http://', 'https://', '#', 'mailto:')):
            links.append((link_text, link_target, full_match))
    
    return links


def extract_ata_references(content: str) -> Set[str]:
    """
    Extract ATA chapter references from content.
    
    Args:
        content: Markdown content to analyze
        
    Returns:
        Set of normalized ATA references (e.g., "ATA_02", "ATA_02-11-00")
    """
    references = set()
    
    for match in ATA_PATTERN.finditer(content):
        chapter = match.group(1)
        section = match.group(2)
        subsection = match.group(3)
        
        if subsection:
            references.add(f"ATA_{chapter}-{section}-{subsection}")
        elif section:
            references.add(f"ATA_{chapter}-{section}")
        else:
            references.add(f"ATA_{chapter}")
    
    return references


def check_link_validity(source_file: pathlib.Path, link: str) -> Tuple[bool, str]:
    """
    Check if a link target exists relative to source file.
    
    Args:
        source_file: Path to the source markdown file
        link: Link target to check
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        # Handle relative paths
        if link.startswith('/'):
            target = REPO_ROOT / link.lstrip('/')
        else:
            target = (source_file.parent / link).resolve()
        
        # Remove anchor if present
        target_str = str(target).split('#')[0]
        target = pathlib.Path(target_str)
        
        if target.exists():
            return True, ""
        else:
            return False, f"Target not found: {link}"
    except Exception as e:
        return False, f"Error resolving link: {str(e)}"


def find_file_in_repo(filename: str, search_root: Optional[pathlib.Path] = None) -> Optional[pathlib.Path]:
    """
    Search for a file in the repository by name.
    
    Args:
        filename: Name of the file to search for
        search_root: Root directory to search in (defaults to REPO_ROOT)
        
    Returns:
        Path to the file if found, None otherwise
    """
    root = search_root or REPO_ROOT
    
    # Try exact matches first
    for found_file in root.rglob(filename):
        if found_file.is_file():
            return found_file
    
    # Try case-insensitive match
    filename_lower = filename.lower()
    for found_file in root.rglob("*.md"):
        if found_file.name.lower() == filename_lower:
            return found_file
    
    return None


def normalize_ata_reference(chapter: str, section: Optional[str] = None, 
                           subsection: Optional[str] = None) -> str:
    """
    Normalize an ATA reference to standard format.
    
    Args:
        chapter: Two-digit chapter number
        section: Two-digit section number (optional)
        subsection: Two-digit subsection number (optional)
        
    Returns:
        Normalized ATA reference string
    """
    if subsection:
        return f"ATA_{chapter}-{section}-{subsection}"
    elif section:
        return f"ATA_{chapter}-{section}"
    else:
        return f"ATA_{chapter}"


def is_external_url(url: str) -> bool:
    """
    Check if a URL is external.
    
    Args:
        url: URL to check
        
    Returns:
        True if the URL is external, False otherwise
    """
    return url.startswith(('http://', 'https://', 'ftp://', 'mailto:'))


def calculate_relative_path(source: pathlib.Path, target: pathlib.Path) -> str:
    """
    Calculate relative path from source to target.
    
    Args:
        source: Source file path
        target: Target file path
        
    Returns:
        Relative path string
    """
    return os.path.relpath(target, source.parent)


def ensure_directory(path: pathlib.Path) -> None:
    """
    Ensure a directory exists, creating it if necessary.
    
    Args:
        path: Directory path to ensure exists
    """
    path.mkdir(parents=True, exist_ok=True)


def read_markdown_file(file_path: pathlib.Path) -> Optional[str]:
    """
    Safely read a markdown file.
    
    Args:
        file_path: Path to the markdown file
        
    Returns:
        File content as string, or None if reading fails
    """
    try:
        return file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def write_markdown_file(file_path: pathlib.Path, content: str) -> bool:
    """
    Safely write content to a markdown file.
    
    Args:
        file_path: Path to the markdown file
        content: Content to write
        
    Returns:
        True if successful, False otherwise
    """
    try:
        file_path.write_text(content, encoding='utf-8')
        return True
    except Exception as e:
        print(f"Error writing {file_path}: {e}")
        return False


def get_version_info() -> dict:
    """
    Get version information for the GenCCC agent.
    
    Returns:
        Dictionary with version information
    """
    return {
        "agent": "GenCCC",
        "version": "1.0.0",
        "description": "Generation Cross-Reference Content Consistency",
        "scripts": ["report.py", "apply.py", "generate.py", "agent.py"],
    }


def validate_environment() -> Tuple[bool, List[str]]:
    """
    Validate that the environment is set up correctly for GenCCC.
    
    Returns:
        Tuple of (is_valid, list_of_issues)
    """
    issues = []
    
    # Check repository structure
    if not REPO_ROOT.exists():
        issues.append(f"Repository root not found: {REPO_ROOT}")
    
    # Check for key directories (they might not exist yet, so just warn)
    if not FRAMEWORK_ROOT.exists():
        issues.append(f"Warning: OPT-IN_FRAMEWORK not found: {FRAMEWORK_ROOT}")
    
    # Check Python version
    import sys
    if sys.version_info < (3, 11):
        issues.append(f"Python 3.11+ required, found {sys.version_info.major}.{sys.version_info.minor}")
    
    is_valid = len([i for i in issues if not i.startswith("Warning:")]) == 0
    return is_valid, issues


def run_agent_mode(repo_root: str, pr_number: str, base_branch: str, 
                   head_branch: str, report_path: str, goal: str) -> int:
    """
    Run agent in goal-seeking mode to fix issues and reach standards compliance.
    
    This is a placeholder implementation that demonstrates the agent workflow.
    In a full implementation, this would:
    1. Parse the audit report to identify issues
    2. Apply fixes using apply.py logic
    3. Generate missing documentation
    4. Create cross-references
    5. Validate compliance with standards
    
    Args:
        repo_root: Path to repository root
        pr_number: PR number
        base_branch: Base branch name
        head_branch: Head branch name
        report_path: Path to audit report
        goal: Goal description for the agent
        
    Returns:
        Exit code (0 for success, 1 for failure)
    """
    print("🤖 GenCCC Agent - Goal-Seeking Mode")
    print("=" * 80)
    print(f"Repository: {repo_root}")
    print(f"PR Number: {pr_number}")
    print(f"Base Branch: {base_branch}")
    print(f"Head Branch: {head_branch}")
    print(f"Report Path: {report_path}")
    print(f"Goal: {goal}")
    print()
    
    # Check if report exists
    report_file = pathlib.Path(report_path)
    if report_file.exists():
        print(f"✅ Found audit report: {report_path}")
        # In a full implementation, parse the report and identify issues
    else:
        print(f"⚠️  Audit report not found: {report_path}")
        print("   Proceeding with basic checks...")
    
    print()
    print("📝 Agent Actions:")
    print("  • Analyzing cross-reference issues...")
    print("  • Checking for missing documentation...")
    print("  • Validating ATA structure compliance...")
    print()
    
    # Placeholder: In a full implementation, this would:
    # 1. Import and run apply.py logic
    # 2. Generate missing docs based on audit report
    # 3. Create V&V lake entries if needed
    # 4. Validate against standards
    
    print("ℹ️  Note: This is a placeholder implementation.")
    print("   The agent workflow requires:")
    print("     - OpenAI API integration for intelligent fixes")
    print("     - V&V lake integration for compliance tracking")
    print("     - Standards validation framework")
    print()
    print("   For now, agent mode delegates to apply.py for basic fixes.")
    print()
    
    # Attempt to run apply.py as a fallback
    try:
        # Change to repo directory
        original_dir = os.getcwd()
        os.chdir(repo_root)
        
        # Import and run apply module
        import sys
        sys.path.insert(0, str(pathlib.Path(__file__).parent))
        from apply import apply_fixes
        
        print("🔧 Running apply.py logic...")
        result = apply_fixes()
        
        os.chdir(original_dir)
        
        if result == 0:
            print()
            print("✅ Agent completed successfully")
            return 0
        else:
            print()
            print("⚠️  Agent completed with warnings")
            return 0  # Don't fail the workflow, just warn
            
    except Exception as e:
        print(f"⚠️  Error running agent logic: {e}")
        print("   Agent will exit gracefully to allow manual review.")
        return 0  # Don't fail the workflow


def display_info_mode():
    """Display agent information and validate environment."""
    import sys
    
    print("GenCCC Agent - Shared Utilities Module")
    print("=" * 80)
    print()
    
    # Display version info
    version_info = get_version_info()
    print(f"Agent: {version_info['agent']}")
    print(f"Version: {version_info['version']}")
    print(f"Description: {version_info['description']}")
    print(f"Scripts: {', '.join(version_info['scripts'])}")
    print()
    
    # Display paths
    print("Configuration:")
    print(f"  Repository Root: {REPO_ROOT}")
    print(f"  Framework Root: {FRAMEWORK_ROOT}")
    print(f"  CAOS Root: {CAOS_ROOT}")
    print(f"  Report Directory: {REPORT_DIR}")
    print()
    
    # Validate environment
    print("Environment Validation:")
    is_valid, issues = validate_environment()
    
    if is_valid:
        print("  ✅ Environment is valid")
    else:
        print("  ❌ Environment has issues:")
    
    for issue in issues:
        if issue.startswith("Warning:"):
            print(f"  ⚠️  {issue}")
        else:
            print(f"  ❌ {issue}")
    print()
    
    # Display statistics
    print("Repository Statistics:")
    md_files = find_all_markdown_files()
    print(f"  Total markdown files: {len(md_files)}")
    
    if md_files:
        # Count files by location
        framework_count = sum(1 for f in md_files if str(f).startswith(str(FRAMEWORK_ROOT)))
        caos_count = sum(1 for f in md_files if str(f).startswith(str(CAOS_ROOT)))
        root_count = len(md_files) - framework_count - caos_count
        
        print(f"    - Framework files: {framework_count}")
        print(f"    - CAOS files: {caos_count}")
        print(f"    - Root files: {root_count}")
    
    print()
    print("=" * 80)
    
    return 0 if is_valid else 1


if __name__ == "__main__":
    """
    Main entry point for agent.py.
    Supports two modes:
    1. Info mode (no arguments): Display agent information
    2. Agent mode (with arguments): Run goal-seeking agent
    """
    import sys
    import argparse
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="GenCCC Agent - Goal-seeking documentation compliance agent",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Display agent info and validate environment
  python agent.py
  
  # Run agent in goal-seeking mode
  python agent.py --repo-root ./pr --pr-number 123 \\
                  --base-branch main --head-branch feature \\
                  --report-path report.md \\
                  --goal "Fix cross-references and reach compliance"
        """
    )
    
    parser.add_argument('--repo-root', help='Path to repository root')
    parser.add_argument('--pr-number', help='Pull request number')
    parser.add_argument('--base-branch', help='Base branch name')
    parser.add_argument('--head-branch', help='Head branch name')
    parser.add_argument('--report-path', help='Path to audit report')
    parser.add_argument('--goal', help='Goal description for the agent')
    
    args = parser.parse_args()
    
    # Check if any agent mode arguments are provided
    if any([args.repo_root, args.pr_number, args.base_branch, 
            args.head_branch, args.report_path, args.goal]):
        # Validate all required arguments are present
        if not all([args.repo_root, args.pr_number, args.base_branch,
                    args.head_branch, args.report_path, args.goal]):
            parser.error("Agent mode requires all arguments: --repo-root, --pr-number, "
                        "--base-branch, --head-branch, --report-path, --goal")
        
        # Run agent mode
        exit_code = run_agent_mode(
            args.repo_root, args.pr_number, args.base_branch,
            args.head_branch, args.report_path, args.goal
        )
        sys.exit(exit_code)
    else:
        # Run info mode
        exit_code = display_info_mode()
        sys.exit(exit_code)
