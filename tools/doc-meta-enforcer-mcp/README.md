# AMPEL360 Document Meta Enforcer MCP Server

A Model Context Protocol (MCP) server that enforces document control blocks and automatically hyperlinks standards, regulations, and internal references in AMPEL360 documentation.

## Features

### 1. Document Control Block Enforcement

Automatically adds or preserves a standardized Document Control section at the end of documents with:

- **Authorship**: "AI prompted by Amedeo Pelliccia"
- **Toolchain**: GitHub Copilot + MCP Doc Control Server
- **Status**: Working draft status
- **Notes**: Review requirements and approval workflow

### 2. Automatic Hyperlinking

Converts plain text references into hyperlinks for:

#### Aviation Standards & Regulations
- **EASA CS-25** → EASA Certification Specifications
- **FAA FAR 25** / **FAA 14 CFR Part 25** → Federal Aviation Regulations
- **ICAO Annex 6/8** → ICAO International Standards

#### AI & Data Regulations
- **EU AI Act** → European AI Regulation
- **EASA AI Roadmap** → EASA AI Development
- **GDPR** → Data Protection Regulation

#### Technical Standards
- **S1000D** → Technical Publications Standard
- **ATA iSpec 2200** → Aviation Industry Standards
- **ARP4754A**, **ARP4761** → SAE Aerospace Standards
- **DO-178C**, **DO-254**, **DO-326A** → RTCA Standards
- **ED-202A** → EUROCAE Standards

#### ISO Standards
- **ISO 15926**, **ISO 9001**, **ISO 14001**

#### Internal References
- **RQ-XX-XX-XXX** → Requirement documents
- **ATA_XX-DESCRIPTION** → ATA chapter references
- **O-ORGANIZATION**, **P-PROGRAM**, etc. → OPT-IN Framework axes

## Installation

### Prerequisites

- Node.js 18.0.0 or higher
- npm or yarn

### Setup

1. Navigate to the MCP server directory:

```bash
cd tools/doc-meta-enforcer-mcp
```

2. Install dependencies:

```bash
npm install
```

3. Build the server:

```bash
npm run build
```

## Usage

### Standalone Mode (for testing)

Run the server in stdio mode:

```bash
npm run start:stdio
```

### With GitHub Copilot / VS Code

#### Method 1: VS Code Settings

Add to your VS Code settings (`.vscode/settings.json` or user settings):

```json
{
  "mcp.servers": {
    "doc-meta-enforcer": {
      "type": "stdio",
      "command": "node",
      "args": [
        "/absolute/path/to/AMPEL360-BWB-H2-Hy-E/tools/doc-meta-enforcer-mcp/dist/server.js"
      ],
      "env": {}
    }
  }
}
```

#### Method 2: Claude Desktop / MCP Client Configuration

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "doc-meta-enforcer": {
      "command": "node",
      "args": [
        "/absolute/path/to/AMPEL360-BWB-H2-Hy-E/tools/doc-meta-enforcer-mcp/dist/server.js"
      ]
    }
  }
}
```

### Copilot Agent Instructions

To make GitHub Copilot use this tool by default, add these instructions to your Copilot agent configuration:

```text
For any new or heavily edited documentation file (.md, .rst, .txt, .adoc):

1. After drafting the content, call the MCP tool `doc_control.enforce` with:
   - content: the full document text
   - filePath: the relative path of the file

2. Replace the file content with the tool's output

3. The tool will:
   - Add a Document Control block if missing (authorship: AI prompted by Amedeo Pelliccia)
   - Convert standards/regulations to hyperlinks (EASA CS-25, FAA FAR 25, etc.)
   - Link internal references (ATA chapters, requirements, OPT-IN axes)
```

## Tool API

### `doc_control.enforce`

Processes a document to enforce standards and hyperlinks.

**Input:**
```typescript
{
  content: string;      // Required: document text to process
  filePath?: string;    // Optional: file path for metadata
}
```

**Output:**
```typescript
{
  content: [
    {
      type: "text",
      text: string      // Processed document with control block and hyperlinks
    }
  ]
}
```

**Behavior:**
- **Idempotent**: Running multiple times produces the same result
- **Non-destructive**: Only adds content, doesn't remove existing text
- **Smart linking**: Avoids double-linking already hyperlinked text

## Examples

### Before

```markdown
# Fuel System Design

This system complies with EASA CS-25 and FAA FAR 25 requirements.
See also ATA_28-FUEL_SAF_CRYOGENIC_H2 for details.

References:
- Requirement RQ-02-01-001
- DO-178C software development
- EU AI Act compliance
```

### After

```markdown
# Fuel System Design

This system complies with [EASA CS-25](https://www.easa.europa.eu/...) and 
[FAA FAR 25](https://www.ecfr.gov/...) requirements.
See also [ATA_28-FUEL_SAF_CRYOGENIC_H2](../T-TECHNOLOGY_.../README.md) for details.

References:
- Requirement [RQ-02-01-001](../../REQUIREMENTS/RQ-02-01-001/README.md)
- [DO-178C](https://www.rtca.org/...) software development
- [EU AI Act](https://eur-lex.europa.eu/...) compliance

---

## Document Control

- **Originator**: _AI prompted by Amedeo Pelliccia_
- **Toolchain**: GitHub Copilot + MCP Doc Control Server
- **Related file**: `fuel-system.md`
- **Status**: `WORKING`
- **Notes**: This document was generated with AI assistance and must be reviewed and
  approved by a designated human checker/approver before being used as an
  official baseline. All changes should follow the AMPEL360 Documentation Standard
  and OPT-IN Framework guidelines.
```

## Development

### Watch Mode

For development with auto-rebuild:

```bash
npm run dev
```

### Adding New Link Rules

Edit `src/linkRules.ts` and add new patterns:

```typescript
{
  pattern: /\b(YOUR-PATTERN)\b(?!\])/g,
  replacement: "[$1](https://your-url.com)",
  description: "Description of the standard"
}
```

Then rebuild:

```bash
npm run build
```

## CI/CD Integration

You can add a GitHub Action to automatically check and enforce document control:

```yaml
name: Document Control Check

on:
  pull_request:
    paths:
      - '**.md'
      - '**.rst'

jobs:
  check-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
      
      - name: Build MCP Server
        run: |
          cd tools/doc-meta-enforcer-mcp
          npm install
          npm run build
      
      - name: Check Documentation
        run: |
          # Add script to verify all docs have Document Control blocks
          # and proper hyperlinks
          node tools/doc-meta-enforcer-mcp/scripts/check-docs.js
```

## Architecture

```
doc-meta-enforcer-mcp/
├── src/
│   ├── server.ts          # MCP server implementation
│   └── linkRules.ts       # Regex patterns for hyperlinking
├── dist/                  # Compiled JavaScript (generated)
├── config/                # Optional configuration files
├── package.json           # Node.js dependencies
├── tsconfig.json          # TypeScript configuration
└── README.md             # This file
```

## License

Apache-2.0 - See LICENSE file in repository root

## Contributing

When adding new link rules:

1. Test the regex pattern thoroughly
2. Use negative lookahead `(?!\])` to avoid double-linking
3. Add descriptive comments
4. Update this README with examples

## Support

For issues or questions:
- Open an issue in the AMPEL360-BWB-H2-Hy-E repository
- Reference the OPT-IN Framework documentation
- Contact: Amedeo Pelliccia

## Version History

- **0.1.0** (2025-11-17): Initial implementation
  - Document Control block enforcement
  - Comprehensive link rules for aviation standards
  - MCP server with stdio transport
  - VS Code / Copilot integration
