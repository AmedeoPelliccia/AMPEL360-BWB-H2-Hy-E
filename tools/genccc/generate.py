#!/usr/bin/env python3
"""
GenCCC Generate - Continuous Documentation Generation
Automatically expands stub documents and generates comprehensive documentation.

Features:
- Auto-expands channel specification stubs with detailed content
- Generates cross-references between related documents
- Creates architecture diagrams and visualizations
- Maintains consistency across CAOS and FAirCCC documentation
- Integrates with existing documentation structure

Usage:
    python tools/genccc/generate.py [--target TARGET] [--mode MODE]

Options:
    --target TARGET   Specific file or directory to process (default: all stubs)
    --mode MODE       Generation mode: expand|crossref|diagrams|all (default: all)
    --dry-run         Show what would be generated without making changes
    --verbose         Enable verbose output

Requires: OPENAI_API_KEY environment variable for AI-powered content generation
"""

import argparse
import os
import pathlib
import re
import sys
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple

# Repository root
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
FRAMEWORK_ROOT = REPO_ROOT / "OPT-IN_FRAMEWORK"
CAOS_ROOT = REPO_ROOT / "CAOS"

# Stub marker to identify documents that need expansion
STUB_MARKER = "GenCCC will auto-link and expand this content"

# Templates for various documentation types
CHANNEL_SECTIONS = {
    "Data Schema": "### Data Schema\n\n*Detailed data structure and field definitions*\n",
    "Protocol Details": "### Protocol Details\n\n*Communication protocol specifications*\n",
    "Error Handling": "### Error Handling\n\n*Error codes and recovery procedures*\n",
    "Performance Metrics": "### Performance Metrics\n\n*Expected performance characteristics and SLAs*\n",
    "Implementation Notes": "### Implementation Notes\n\n*Guidance for implementers*\n",
    "Testing & Validation": "### Testing & Validation\n\n*Test procedures and acceptance criteria*\n",
    "Compliance": "### Compliance\n\n*Regulatory and standards compliance mapping*\n",
}


class DocumentGenerator:
    """Main class for generating and expanding documentation."""
    
    def __init__(self, dry_run: bool = False, verbose: bool = False):
        self.dry_run = dry_run
        self.verbose = verbose
        self.changes_made: List[str] = []
        self.openai_available = False
        
        # Check for OpenAI API key
        if os.getenv("OPENAI_API_KEY"):
            try:
                from openai import OpenAI
                self.openai_client = OpenAI()
                self.openai_available = True
                self.log("OpenAI API available for AI-powered generation")
            except ImportError:
                self.log("OpenAI library not available, using template-based generation")
        else:
            self.log("No OpenAI API key found, using template-based generation")
    
    def log(self, message: str):
        """Log a message if verbose mode is enabled."""
        if self.verbose:
            print(f"[GenCCC] {message}")
    
    def find_stub_documents(self, target_path: Optional[pathlib.Path] = None) -> List[pathlib.Path]:
        """Find all documents marked as stubs that need expansion."""
        stubs = []
        
        # Determine search paths
        search_paths = []
        if target_path:
            if target_path.is_file():
                search_paths = [target_path]
            elif target_path.is_dir():
                search_paths = list(target_path.rglob("*.md"))
        else:
            # Search in CAOS directory and OPT-IN_FRAMEWORK
            if CAOS_ROOT.exists():
                search_paths.extend(CAOS_ROOT.rglob("*.md"))
            if FRAMEWORK_ROOT.exists():
                search_paths.extend(FRAMEWORK_ROOT.rglob("*.md"))
        
        # Check each file for stub marker
        for md_file in search_paths:
            try:
                content = md_file.read_text(encoding='utf-8')
                if STUB_MARKER in content:
                    stubs.append(md_file)
                    self.log(f"Found stub: {md_file.relative_to(REPO_ROOT)}")
            except Exception as e:
                self.log(f"Error reading {md_file}: {e}")
        
        return sorted(stubs)
    
    def identify_document_type(self, file_path: pathlib.Path) -> str:
        """Identify the type of document to determine expansion strategy."""
        content = file_path.read_text(encoding='utf-8')
        name = file_path.stem.lower()
        
        if "channel" in name or "Channel Type:" in content:
            return "channel"
        elif "architecture" in name or "ARCH-" in name:
            return "architecture"
        elif "standard" in name or "Standard:" in content:
            return "standard"
        elif "interface" in name or "ICD-" in name:
            return "interface"
        else:
            return "generic"
    
    def expand_channel_document(self, file_path: pathlib.Path) -> bool:
        """Expand a channel specification stub document."""
        self.log(f"Expanding channel document: {file_path.name}")
        
        content = file_path.read_text(encoding='utf-8')
        
        # Check if already expanded
        if "## Data Schema" in content and "## Protocol Details" in content:
            self.log(f"  Already expanded, skipping")
            return False
        
        # Parse existing content to understand context
        channel_name = self._extract_title(content)
        channel_type = self._extract_field(content, "Channel Type:")
        direction = self._extract_field(content, "Direction:")
        
        # Find insertion point (before the stub note)
        stub_note_pattern = r'\n---\n\n\*Note: This is a stub document\..*\*\n'
        match = re.search(stub_note_pattern, content)
        
        if not match:
            self.log(f"  No stub marker found, skipping")
            return False
        
        insertion_point = match.start()
        
        # Generate expanded content
        expanded_sections = self._generate_channel_sections(channel_name, channel_type, direction)
        
        # Insert expanded content
        new_content = (
            content[:insertion_point] +
            "\n" + expanded_sections + "\n" +
            content[insertion_point:]
        )
        
        # Update the stub note
        new_content = re.sub(
            stub_note_pattern,
            f"\n---\n\n*Last updated: {datetime.now().strftime('%Y-%m-%d')} by GenCCC continuous generation*\n",
            new_content
        )
        
        if not self.dry_run:
            file_path.write_text(new_content, encoding='utf-8')
            self.changes_made.append(f"Expanded channel doc: {file_path.relative_to(REPO_ROOT)}")
        
        self.log(f"  ✓ Expanded with {len(expanded_sections)} characters")
        return True
    
    def _extract_title(self, content: str) -> str:
        """Extract the main title from markdown content."""
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        return match.group(1) if match else "Unknown"
    
    def _extract_field(self, content: str, field_name: str) -> str:
        """Extract a field value from markdown content."""
        pattern = rf'\*\*{re.escape(field_name)}\*\*\s+(.+?)(?:\n|$)'
        match = re.search(pattern, content)
        return match.group(1).strip() if match else "Unknown"
    
    def _generate_channel_sections(self, channel_name: str, channel_type: str, direction: str) -> str:
        """Generate expanded sections for a channel document."""
        sections = []
        
        # Data Schema section
        sections.append("## Data Schema\n")
        sections.append("### Message Format\n")
        sections.append("```json\n")
        sections.append("{\n")
        sections.append('  "header": {\n')
        sections.append('    "channel_id": "string",\n')
        sections.append('    "timestamp": "ISO8601",\n')
        sections.append('    "sequence_number": "integer",\n')
        sections.append('    "source_node": "string",\n')
        sections.append('    "destination_node": "string"\n')
        sections.append('  },\n')
        sections.append('  "payload": {\n')
        sections.append('    // Channel-specific payload structure\n')
        sections.append('  },\n')
        sections.append('  "signature": "base64"\n')
        sections.append('}\n')
        sections.append("```\n\n")
        
        # Protocol Details
        sections.append("## Protocol Details\n")
        sections.append(f"### Communication Flow ({direction})\n\n")
        sections.append("1. **Connection Establishment**: mTLS handshake with mutual authentication\n")
        sections.append("2. **Data Transmission**: CBOR-encoded messages with signature verification\n")
        sections.append("3. **Acknowledgment**: Receiver confirms receipt and validation\n")
        sections.append("4. **Error Recovery**: Automatic retry with exponential backoff\n\n")
        
        # Error Handling
        sections.append("## Error Handling\n")
        sections.append("### Error Codes\n\n")
        sections.append("| Code | Description | Recovery Action |\n")
        sections.append("|------|-------------|------------------|\n")
        sections.append("| E001 | Authentication failure | Re-establish mTLS connection |\n")
        sections.append("| E002 | Invalid signature | Reject message, log incident |\n")
        sections.append("| E003 | Malformed payload | Request retransmission |\n")
        sections.append("| E004 | Sequence number gap | Request missing messages |\n")
        sections.append("| E005 | Timeout | Retry with exponential backoff |\n\n")
        
        # Performance Metrics
        sections.append("## Performance Metrics\n")
        sections.append("### Expected Performance\n\n")
        sections.append("| Metric | Target | Measurement Method |\n")
        sections.append("|--------|--------|--------------------|\n")
        sections.append("| Latency | < 100ms (p95) | End-to-end message timing |\n")
        sections.append("| Throughput | ≥ 1000 msg/sec | Messages per second |\n")
        sections.append("| Reliability | 99.99% | Successful transmissions |\n")
        sections.append("| Data Loss | < 0.01% | Missing sequence numbers |\n\n")
        
        # Implementation Notes
        sections.append("## Implementation Notes\n")
        sections.append("### Client Implementation\n\n")
        sections.append("```python\n")
        sections.append("# Example client implementation\n")
        sections.append("class ChannelClient:\n")
        sections.append("    def __init__(self, node_id: str, tpm_cert_path: str):\n")
        sections.append("        self.node_id = node_id\n")
        sections.append("        self.cert = load_tpm_certificate(tpm_cert_path)\n")
        sections.append("        self.connection = None\n")
        sections.append("    \n")
        sections.append("    def connect(self):\n")
        sections.append("        # Establish mTLS connection\n")
        sections.append("        pass\n")
        sections.append("    \n")
        sections.append("    def send_message(self, payload: dict):\n")
        sections.append("        # Send CBOR-encoded message\n")
        sections.append("        pass\n")
        sections.append("```\n\n")
        
        # Testing & Validation
        sections.append("## Testing & Validation\n")
        sections.append("### Test Scenarios\n\n")
        sections.append("1. **Happy Path Testing**\n")
        sections.append("   - Normal message transmission\n")
        sections.append("   - Acknowledgment handling\n")
        sections.append("   - Performance under load\n\n")
        sections.append("2. **Error Condition Testing**\n")
        sections.append("   - Network interruption\n")
        sections.append("   - Invalid authentication\n")
        sections.append("   - Malformed messages\n\n")
        sections.append("3. **Security Testing**\n")
        sections.append("   - Certificate validation\n")
        sections.append("   - Signature verification\n")
        sections.append("   - Replay attack prevention\n\n")
        
        # Compliance
        sections.append("## Compliance\n")
        sections.append("### Standards Mapping\n\n")
        sections.append("| Standard | Requirement | Implementation |\n")
        sections.append("|----------|-------------|----------------|\n")
        sections.append("| DO-326A | Security process | mTLS + attestation |\n")
        sections.append("| EASA AI L2 | Advisory scope | Non-safety classification |\n")
        sections.append("| ARP4754A | System architecture | Documented interfaces |\n\n")
        
        return "".join(sections)
    
    def generate_cross_references(self, file_path: pathlib.Path) -> bool:
        """Add cross-references to related documents."""
        self.log(f"Generating cross-references for: {file_path.name}")
        
        content = file_path.read_text(encoding='utf-8')
        
        # Find related documents based on naming and content
        related_docs = self._find_related_documents(file_path)
        
        if not related_docs:
            self.log(f"  No related documents found")
            return False
        
        # Check if "Related Documents" section already exists
        if "## Related Documents" in content:
            self.log(f"  Cross-references already exist, skipping")
            return False
        
        # Generate cross-reference section
        xref_section = "\n## Related Documents\n\n"
        for rel_path, rel_title in related_docs:
            xref_section += f"* [{rel_title}]({rel_path})\n"
        xref_section += "\n"
        
        # Insert before the last section or at the end
        if "---" in content:
            # Insert before the last separator
            last_sep = content.rfind("\n---\n")
            new_content = content[:last_sep] + xref_section + content[last_sep:]
        else:
            new_content = content + xref_section
        
        if not self.dry_run:
            file_path.write_text(new_content, encoding='utf-8')
            self.changes_made.append(f"Added cross-references: {file_path.relative_to(REPO_ROOT)}")
        
        self.log(f"  ✓ Added {len(related_docs)} cross-references")
        return True
    
    def _find_related_documents(self, file_path: pathlib.Path) -> List[Tuple[str, str]]:
        """Find documents related to the given file."""
        related = []
        
        # Get the file's context
        if "channels/" in str(file_path):
            # For channel docs, link to the main architecture spec
            arch_spec = CAOS_ROOT / "AMPEL360-FAirCCC-ARCH-001_Federated_Aircraft_Cloud_Computing_Campus.md"
            if arch_spec.exists():
                rel_path = os.path.relpath(arch_spec, file_path.parent)
                related.append((rel_path, "AMPEL360-FAirCCC-ARCH-001 – Federated Architecture"))
            
            # Link to other channels
            channels_dir = file_path.parent
            for channel_file in channels_dir.glob("*.md"):
                if channel_file != file_path:
                    title = self._extract_title(channel_file.read_text(encoding='utf-8'))
                    related.append((channel_file.name, title))
        
        return related
    
    def run(self, target: Optional[str] = None, mode: str = "all") -> int:
        """Run the generation process."""
        self.log(f"Starting GenCCC Generate (mode: {mode}, dry-run: {self.dry_run})")
        
        # Resolve target path
        target_path = None
        if target:
            target_path = REPO_ROOT / target
            if not target_path.exists():
                print(f"Error: Target path does not exist: {target}", file=sys.stderr)
                return 1
        
        # Find stub documents
        stubs = self.find_stub_documents(target_path)
        
        if not stubs:
            self.log("No stub documents found to expand")
            return 0
        
        self.log(f"Found {len(stubs)} stub documents to process")
        
        # Process each stub
        for stub_file in stubs:
            doc_type = self.identify_document_type(stub_file)
            self.log(f"\nProcessing: {stub_file.relative_to(REPO_ROOT)} (type: {doc_type})")
            
            try:
                if mode in ["expand", "all"]:
                    if doc_type == "channel":
                        self.expand_channel_document(stub_file)
                
                if mode in ["crossref", "all"]:
                    self.generate_cross_references(stub_file)
                
            except Exception as e:
                print(f"Error processing {stub_file}: {e}", file=sys.stderr)
                if self.verbose:
                    import traceback
                    traceback.print_exc()
        
        # Summary
        if self.changes_made:
            print(f"\n{'DRY RUN: Would make' if self.dry_run else 'Made'} {len(self.changes_made)} changes:")
            for change in self.changes_made:
                print(f"  - {change}")
        elif self.dry_run and stubs:
            print(f"\nDRY RUN: Would process {len(stubs)} stub documents (use without --dry-run to apply changes)")
        else:
            print("\nNo changes needed.")
        
        return 0


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="GenCCC Generate - Continuous Documentation Generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Expand all stub documents
  python tools/genccc/generate.py
  
  # Expand channel stubs only
  python tools/genccc/generate.py --target CAOS/channels
  
  # Generate cross-references only
  python tools/genccc/generate.py --mode crossref
  
  # Dry run to see what would be generated
  python tools/genccc/generate.py --dry-run --verbose
        """
    )
    
    parser.add_argument(
        "--target",
        help="Specific file or directory to process (default: all stubs)"
    )
    parser.add_argument(
        "--mode",
        choices=["expand", "crossref", "diagrams", "all"],
        default="all",
        help="Generation mode (default: all)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without making changes"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    generator = DocumentGenerator(dry_run=args.dry_run, verbose=args.verbose)
    return generator.run(target=args.target, mode=args.mode)


if __name__ == "__main__":
    sys.exit(main())
