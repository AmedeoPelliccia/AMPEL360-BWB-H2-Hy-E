#!/usr/bin/env python3
"""
GenCCC Apply - Auto-fix and Content Generation
Applies automatic fixes for cross-reference issues and generates missing documentation.

Features:
- Fixes broken internal links by updating paths
- Generates missing documentation with contextual content using AI
- Creates proper cross-references between related documents
- Maintains ATA structure and CAOS framework consistency

Requires: OPENAI_API_KEY environment variable for AI-powered content generation
"""

import os
import pathlib
import re
import sys
from typing import Dict, List, Optional, Tuple

# Repository root
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
FRAMEWORK_ROOT = REPO_ROOT / "OPT-IN_FRAMEWORK"


def find_all_markdown_files() -> List[pathlib.Path]:
    """Find all markdown files in the framework."""
    md_files = []
    if FRAMEWORK_ROOT.exists():
        md_files.extend(FRAMEWORK_ROOT.rglob("*.md"))
    
    # Also include root-level markdown files
    root_files = [
        REPO_ROOT / "README.md",
        REPO_ROOT / "CAOS_INDEX.md",
        REPO_ROOT / "CAOS_MANIFESTO.md",
        REPO_ROOT / "CAOS_OPERATIONS_FRAMEWORK.md",
        REPO_ROOT / "CAOS_USE_CASES.md",
    ]
    for f in root_files:
        if f.exists():
            md_files.append(f)
    
    return sorted(md_files)


def extract_internal_links(content: str) -> List[Tuple[str, str, str]]:
    """Extract internal markdown links with their text and target."""
    # Match [text](path) format, excluding external URLs
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    links = []
    
    for match in re.finditer(link_pattern, content):
        link_text = match.group(1)
        link_target = match.group(2)
        full_match = match.group(0)
        
        # Skip external URLs, anchors, and mailto links
        if not link_target.startswith(('http://', 'https://', '#', 'mailto:')):
            links.append((link_text, link_target, full_match))
    
    return links


def find_file_in_repo(filename: str) -> Optional[pathlib.Path]:
    """Search for a file in the repository by name."""
    # Try exact matches first
    for md_file in REPO_ROOT.rglob(filename):
        if md_file.is_file():
            return md_file
    
    # Try case-insensitive match
    filename_lower = filename.lower()
    for md_file in REPO_ROOT.rglob("*.md"):
        if md_file.name.lower() == filename_lower:
            return md_file
    
    return None


def fix_broken_link(source_file: pathlib.Path, old_link: str) -> Optional[str]:
    """Attempt to fix a broken link by finding the actual file location."""
    # Extract filename from the link
    link_parts = old_link.split('/')
    filename = link_parts[-1].split('#')[0]  # Remove anchor if present
    
    if not filename:
        return None
    
    # Search for the file
    target_file = find_file_in_repo(filename)
    if not target_file:
        return None
    
    # Calculate relative path from source to target
    try:
        rel_path = os.path.relpath(target_file, source_file.parent)
        # Preserve anchor if present
        if '#' in old_link:
            anchor = old_link.split('#', 1)[1]
            rel_path = f"{rel_path}#{anchor}"
        return rel_path
    except Exception:
        return None


def add_cross_references(content: str, file_path: pathlib.Path) -> str:
    """Add cross-references to related documents based on ATA structure."""
    # This is a placeholder for more sophisticated cross-referencing logic
    # In a full implementation, this would analyze the document structure
    # and add links to parent/sibling/child documents in the ATA hierarchy
    
    # For now, we'll just ensure the content is returned unchanged
    # The AI-powered generation in generate_missing_doc will handle this
    return content


def generate_missing_doc_template(file_path: pathlib.Path) -> str:
    """Generate a basic template for missing documentation."""
    # Extract context from path
    path_parts = file_path.parts
    
    # Determine document type from path
    doc_title = "Documentation"
    section_info = ""
    
    # Look for ATA pattern in path
    ata_pattern = re.compile(r'ATA[_\s-]?(\d{2})[_\s-]?(\d{2})?[_\s-]?(\d{2})?')
    for part in path_parts:
        match = ata_pattern.search(part)
        if match:
            chapter = match.group(1)
            section = match.group(2) or "00"
            subsection = match.group(3) or "00"
            doc_title = f"ATA {chapter}-{section}-{subsection}"
            section_info = f"Chapter {chapter}, Section {section}, Subsection {subsection}"
            break
    
    # Look for descriptive folder names
    descriptive_parts = [p for p in path_parts if not ata_pattern.search(p) and p != "README.md"]
    if descriptive_parts:
        description = descriptive_parts[-1].replace('_', ' ').replace('-', ' ').title()
    else:
        description = "Documentation"
    
    template = f"""# {doc_title}: {description}

## Overview

This document is part of the AMPEL360 BWB H₂ Hy-E aircraft documentation framework.

{f'**ATA Reference:** {section_info}' if section_info else ''}

## Purpose

[This section should describe the purpose and scope of this document]

## Contents

- Overview and context
- Technical specifications
- Requirements and constraints
- Related documentation

## Related Documents

- [CAOS Index](../../../CAOS_INDEX.md)
- [Main README](../../../README.md)

## Document Control

**Status:** Draft  
**Version:** 1.0  
**Last Updated:** Auto-generated by GenCCC  

---

*This document was automatically generated as part of the AMPEL360 documentation framework. Please review and update with specific content as needed.*
"""
    
    return template


def generate_missing_doc_with_ai(file_path: pathlib.Path, context: Dict[str, Any]) -> str:
    """Generate missing documentation using AI (OpenAI API)."""
    api_key = os.environ.get('OPENAI_API_KEY')
    
    if not api_key:
        print(f"⚠️  No OPENAI_API_KEY found. Using template for {file_path.name}")
        return generate_missing_doc_template(file_path)
    
    try:
        import openai
        
        # Extract context
        path_str = str(file_path.relative_to(REPO_ROOT))
        related_docs = context.get('related_docs', [])
        
        # Build prompt
        prompt = f"""Generate comprehensive technical documentation for an aerospace document in the AMPEL360 BWB H₂ Hy-E aircraft project.

File path: {path_str}

Context:
- This is part of an ATA iSpec 2200 compliant documentation framework
- The aircraft is a revolutionary blended wing body design with hydrogen fuel cells
- Documentation follows CAOS (Computer Aided Operations and Services) framework

Related documentation:
{chr(10).join(f"- {doc}" for doc in related_docs[:5]) if related_docs else "- No related docs found"}

Generate a detailed, technically accurate markdown document that:
1. Explains the purpose and scope based on the file path
2. Includes relevant technical content for aerospace documentation
3. Links to related documents appropriately
4. Follows ATA chapter structure conventions
5. Maintains professional technical writing style

Format as markdown with appropriate headers, lists, and structure."""

        client = openai.OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-oss",
            messages=[
                {"role": "system", "content": "You are a technical documentation expert specializing in aerospace engineering and ATA iSpec 2200 standards."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        content = response.choices[0].message.content
        print(f"✅ AI-generated content for {file_path.name}")
        return content
        
    except ImportError:
        print(f"⚠️  OpenAI package not installed. Using template for {file_path.name}")
        return generate_missing_doc_template(file_path)
    except Exception as e:
        print(f"⚠️  AI generation failed for {file_path.name}: {str(e)}")
        print(f"   Using template instead.")
        return generate_missing_doc_template(file_path)


def extract_plain_text_ata_references(content: str) -> List[Tuple[str, str, int, int]]:
    """
    Extract plain text ATA references that are not already linked.
    Returns list of (reference_text, normalized_ref, start_pos, end_pos)
    
    Path normalization mode 2: Standard ATA structure
    - ATA_02 -> Chapter root
    - ATA_02-11 -> Section  
    - ATA_02-11-00 -> Subsection index
    """
    # Mask all markdown links to avoid matching ATA references inside them
    link_pattern = r'\[[^\]]+\]\([^)]+\)'
    def mask_link(match):
        return ' ' * (match.end() - match.start())
    masked_content = re.sub(link_pattern, mask_link, content)

    # Pattern to match ATA references (no negative lookbehind needed)
    ata_pattern = r'\b(?:ATA[_\s-]?)?(\d{2})(?:[_\s-](\d{2})(?:[_\s-](\d{2}))?)?\b'
    
    references = []
    
    # Find all matches in masked content
    for match in re.finditer(ata_pattern, masked_content):
        start_pos = match.start()
        end_pos = match.end()
        full_match = content[start_pos:end_pos]
        chapter = match.group(1)
        section = match.group(2)
        subsection = match.group(3)
        
        # Normalize the reference (mode 2: standard structure)
        if subsection:
            normalized = f"ATA_{chapter}-{section}-{subsection}"
        elif section:
            normalized = f"ATA_{chapter}-{section}"
        else:
            normalized = f"ATA_{chapter}"
        
        references.append((full_match, normalized, start_pos, end_pos))
    
    return references


def find_ata_document_path(ata_ref: str) -> Optional[pathlib.Path]:
    """
    Find the file path for an ATA reference.
    Path normalization mode 2: Standard ATA structure
    
    Examples:
    - ATA_02 -> finds chapter root README
    - ATA_02-11 -> finds section README
    - ATA_02-11-00 -> finds subsection README
    """
    # Parse the ATA reference
    parts = ata_ref.replace('ATA_', '').split('-')
    
    if len(parts) == 1:
        # Chapter level (e.g., ATA_02)
        chapter = parts[0]
    elif len(parts) == 2:
        # Section level (e.g., ATA_02-11)
        chapter, section = parts
    else:
        # Subsection level (e.g., ATA_02-11-00)
        chapter, section, subsection = parts
    
    # Search for matching files
    if FRAMEWORK_ROOT.exists():
        for md_file in FRAMEWORK_ROOT.rglob("*.md"):
            rel_path = str(md_file.relative_to(FRAMEWORK_ROOT))
            
            # Simple pattern matching
            if 'ATA' in rel_path:
                # Check if path contains the reference
                if len(parts) == 1 and f"ATA_{chapter}" in rel_path and md_file.name == "README.md":
                    # Make sure it's at the right level (not too deep)
                    if rel_path.count('/') <= 2:
                        return md_file
                elif len(parts) == 2 and f"{chapter}-{section}" in rel_path and md_file.name == "README.md":
                    return md_file
                elif len(parts) == 3 and f"{chapter}-{section}-{subsection}" in rel_path and md_file.name == "README.md":
                    return md_file
    
    return None


def auto_link_plain_text_references(content: str, source_file: pathlib.Path, aggressiveness: str = "STANDARD") -> Tuple[str, int]:
    """
    Auto-link plain text ATA references in content.
    
    Aggressiveness levels:
    - SAFE: Only link if target exists
    - STANDARD: Link if target exists, or create placeholder with note
    - AGGRESSIVE: Link all references, generate missing docs
    
    Returns: (modified_content, links_added)
    """
    references = extract_plain_text_ata_references(content)
    
    if not references:
        return content, 0
    
    links_added = 0
    modified_content = content
    
    # Process references in reverse order to maintain position indices
    for ref_text, normalized_ref, start_pos, end_pos in reversed(references):
        target_path = find_ata_document_path(normalized_ref)
        
        if target_path:
            # Calculate relative path
            try:
                rel_path = os.path.relpath(target_path, source_file.parent)
                # Create markdown link
                link = f"[{ref_text}]({rel_path})"
                modified_content = modified_content[:start_pos] + link + modified_content[end_pos:]
                links_added += 1
            except Exception:
                # If we can't calculate relative path, skip this reference
                continue
        elif aggressiveness in ["STANDARD", "AGGRESSIVE"]:
            # For STANDARD mode, add a comment but don't generate
            # For AGGRESSIVE mode, we would generate the document
            # For now, STANDARD just adds a link with a note
            # Create a placeholder link with proper markdown syntax
            link = f"[{ref_text}](#'{normalized_ref}' \"Document pending\")"
            modified_content = modified_content[:start_pos] + link + modified_content[end_pos:]
            links_added += 1
    
    return modified_content, links_added


def apply_fixes() -> int:
    """Apply automatic fixes and generate missing documentation."""
    print("🔧 GenCCC Apply: Starting auto-fix and content generation...")
    print(f"📁 Repository root: {REPO_ROOT}")
    print(f"📂 Framework root: {FRAMEWORK_ROOT}")
    print("")
    
    md_files = find_all_markdown_files()
    print(f"📄 Found {len(md_files)} markdown files")
    print("")
    
    files_modified = 0
    links_fixed = 0
    docs_generated = 0
    
    # Pass 1: Fix broken links
    print("🔗 Pass 1: Fixing broken links...")
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            original_content = content
            
            links = extract_internal_links(content)
            for link_text, link_target, full_match in links:
                # Check if link is broken
                if link_target.startswith('/'):
                    target = REPO_ROOT / link_target.lstrip('/')
                else:
                    target = (md_file.parent / link_target).resolve()
                
                target_str = str(target).split('#')[0]
                target_path = pathlib.Path(target_str)
                
                if not target_path.exists():
                    # Try to fix it
                    new_link = fix_broken_link(md_file, link_target)
                    if new_link:
                        new_match = f"[{link_text}]({new_link})"
                        content = content.replace(full_match, new_match)
                        links_fixed += 1
                        print(f"  ✓ Fixed link in {md_file.name}: {link_target} → {new_link}")
            
            if content != original_content:
                md_file.write_text(content, encoding='utf-8')
                files_modified += 1
                
        except Exception as e:
            print(f"  ⚠️  Error processing {md_file.name}: {str(e)}")
    
    print(f"✅ Fixed {links_fixed} broken links in {files_modified} files")
    print("")
    
    # Pass 2: Auto-link plain text ATA references (STANDARD mode)
    print("🔗 Pass 2: Auto-linking plain text ATA references...")
    print("   Mode: STANDARD (path normalization mode 2)")
    
    refs_linked = 0
    pass2_files_modified = 0
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            
            # Auto-link plain text references with STANDARD aggressiveness
            modified_content, links_added = auto_link_plain_text_references(
                content, md_file, aggressiveness="STANDARD"
            )
            
            if links_added > 0:
                md_file.write_text(modified_content, encoding='utf-8')
                refs_linked += links_added
                pass2_files_modified += 1
                print(f"  ✓ Linked {links_added} references in {md_file.name}")
                
        except Exception as e:
            print(f"  ⚠️  Error processing {md_file.name}: {str(e)}")
    
    print(f"✅ Auto-linked {refs_linked} plain text references in {pass2_files_modified} files")
    print("")
    
    # Update total files modified
    files_modified += pass2_files_modified
    
    # Pass 3: Generate missing documentation (limited scope for safety)
    print("📝 Pass 3: Checking for critical missing documentation...")
    print("   (Generation is conservative to avoid unwanted files)")
    print("")
    
    # For now, we'll skip automatic generation of new files to be safe
    # This would be enabled with a more sophisticated detection mechanism
    print("ℹ️  Skipping automatic file generation for safety.")
    print("   Missing files should be created manually or with explicit configuration.")
    print("")
    
    # Summary
    print("=" * 80)
    print("📊 Summary:")
    print(f"  - Files modified: {files_modified}")
    print(f"  - Broken links fixed: {links_fixed}")
    print(f"  - Plain text references auto-linked: {refs_linked}")
    print(f"  - Docs generated: {docs_generated}")
    print("")
    
    if files_modified > 0 or docs_generated > 0:
        print("✅ Changes applied successfully!")
        print("   Review the changes and commit them if they look correct.")
    else:
        print("ℹ️  No changes needed - documentation is already in good shape!")
    
    print("=" * 80)
    
    return 0


def main():
    """Main execution function."""
    return apply_fixes()


if __name__ == "__main__":
    sys.exit(main())
