# AMPEL360 Doc-Meta-Enforcer MCP Server - Integration Guide

This guide explains how to integrate the AMPEL360 Document Meta Enforcer MCP Server with various development environments and AI assistants.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [VS Code with GitHub Copilot](#vs-code-with-github-copilot)
3. [Claude Desktop](#claude-desktop)
4. [Custom MCP Clients](#custom-mcp-clients)
5. [CI/CD Integration](#cicd-integration)
6. [Testing the Integration](#testing-the-integration)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before integrating, ensure you have:

1. **Node.js 18+** installed
2. **Built the MCP server**:
   ```bash
   cd tools/doc-meta-enforcer-mcp
   npm install
   npm run build
   ```
3. **Absolute path** to the built server noted down

---

## VS Code with GitHub Copilot

### Option 1: Workspace Settings (Recommended for per-project use)

1. Create or edit `.vscode/settings.json` in your workspace:

```json
{
  "mcp.servers": {
    "doc-meta-enforcer": {
      "type": "stdio",
      "command": "node",
      "args": [
        "${workspaceFolder}/tools/doc-meta-enforcer-mcp/dist/server.js"
      ],
      "env": {},
      "description": "AMPEL360 Document Control and Hyperlinking Server"
    }
  }
}
```

2. Reload VS Code window (Command Palette → `Developer: Reload Window`)

### Option 2: User Settings (Global use)

1. Open User Settings (JSON):
   - Command Palette (`Ctrl/Cmd+Shift+P`)
   - Type: `Preferences: Open User Settings (JSON)`

2. Add the MCP server configuration:

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

### Copilot Agent Instructions

To make Copilot use the tool automatically for documentation:

1. Create `.github/copilot-instructions.md` in your repository:

```markdown
# GitHub Copilot Instructions for AMPEL360

## Documentation Generation

When creating or heavily editing documentation files (`.md`, `.rst`, `.txt`, `.adoc`):

1. Draft the content first
2. Call the MCP tool `doc_control.enforce` with:
   - `content`: full document text
   - `filePath`: relative path to the file
3. Replace file content with the tool's output

The tool will:
- Add a Document Control block with authorship (AI prompted by Amedeo Pelliccia)
- Convert standards/regulations to hyperlinks (EASA CS-25, FAA FAR 25, DO-178C, etc.)
- Link internal references (ATA chapters, requirements, OPT-IN axes)
```

---

## Claude Desktop

### Configuration

1. Locate Claude Desktop config file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. Add the MCP server:

```json
{
  "mcpServers": {
    "doc-meta-enforcer": {
      "command": "node",
      "args": [
        "/absolute/path/to/AMPEL360-BWB-H2-Hy-E/tools/doc-meta-enforcer-mcp/dist/server.js"
      ],
      "env": {}
    }
  }
}
```

3. Restart Claude Desktop

### Usage in Claude

In your conversation with Claude, you can now ask:

```
Please process this document using the doc_control.enforce tool:

[paste your document content here]
```

Or:

```
Generate a new requirements document about fuel system safety 
and use the doc_control.enforce tool to add proper metadata and hyperlinks.
```

---

## Custom MCP Clients

### Using the MCP TypeScript SDK

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

// Create transport
const transport = new StdioClientTransport({
  command: "node",
  args: [
    "/path/to/AMPEL360-BWB-H2-Hy-E/tools/doc-meta-enforcer-mcp/dist/server.js"
  ],
});

// Create client
const client = new Client(
  {
    name: "my-client",
    version: "1.0.0",
  },
  {
    capabilities: {},
  }
);

// Connect
await client.connect(transport);

// Call the tool
const result = await client.callTool({
  name: "doc_control.enforce",
  arguments: {
    content: "# My Document\n\nThis uses EASA CS-25 standards.",
    filePath: "docs/my-doc.md",
  },
});

console.log(result.content[0].text);

// Close
await client.close();
```

### Using stdio directly (any language)

The MCP server uses JSON-RPC 2.0 over stdio. Example request:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "doc_control.enforce",
    "arguments": {
      "content": "# Document\n\nReferences EASA CS-25.",
      "filePath": "test.md"
    }
  }
}
```

---

## CI/CD Integration

### GitHub Actions

Create `.github/workflows/doc-control-check.yml`:

```yaml
name: Documentation Control Check

on:
  pull_request:
    paths:
      - '**.md'
      - '**.rst'
      - '**.txt'

jobs:
  check-docs:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
      
      - name: Build MCP Server
        run: |
          cd tools/doc-meta-enforcer-mcp
          npm install
          npm run build
      
      - name: Check Documentation Standards
        run: |
          # Example: Check that all markdown files have Document Control blocks
          
          FILES=$(find . -name "*.md" -type f ! -path "./node_modules/*" ! -path "./tools/*")
          
          MISSING=0
          for file in $FILES; do
            if ! grep -q "## Document Control" "$file"; then
              echo "❌ Missing Document Control block: $file"
              MISSING=$((MISSING + 1))
            fi
          done
          
          if [ $MISSING -gt 0 ]; then
            echo ""
            echo "Found $MISSING files without Document Control blocks."
            echo "Please use the doc-meta-enforcer MCP tool on these files."
            exit 1
          fi
          
          echo "✅ All documentation files have Document Control blocks."
```

### Pre-commit Hook

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash

# Check staged markdown files
STAGED_MD=$(git diff --cached --name-only --diff-filter=ACM | grep '\.md$')

if [ -n "$STAGED_MD" ]; then
  echo "Checking documentation standards..."
  
  for file in $STAGED_MD; do
    if ! grep -q "## Document Control" "$file"; then
      echo "⚠️  Warning: $file is missing Document Control block"
      echo "   Consider running the doc-meta-enforcer MCP tool"
    fi
  done
fi
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

---

## Testing the Integration

### 1. Verify MCP Server is Running

```bash
# Start the server manually
cd tools/doc-meta-enforcer-mcp
npm run start:stdio

# The server should start and log: "AMPEL360 Document Meta Enforcer MCP server running on stdio"
# Press Ctrl+C to stop
```

### 2. Test with Sample Document

Create a test file `test-integration.md`:

```markdown
# Test Document

This document references EASA CS-25, DO-178C, and ATA_28-FUEL_SAF_CRYOGENIC_H2.

Requirements:
- RQ-01-02-003
- Compliance with EU AI Act
```

Use the tool (via VS Code Copilot or Claude):

```
Process this document with doc_control.enforce tool
```

Expected output should include:
- Hyperlinked standards
- Hyperlinked internal references
- Document Control block at the end

### 3. Check VS Code Integration

1. Open Command Palette
2. Type: `MCP: List Servers`
3. Verify `doc-meta-enforcer` appears in the list
4. Check status is `Running`

### 4. Test Copilot Integration

In VS Code with Copilot:

1. Open a markdown file
2. Open Copilot Chat
3. Type: `@workspace Use the doc_control.enforce tool to process this file`
4. Copilot should recognize and use the tool

---

## Troubleshooting

### Issue: "MCP server not found"

**Solution:**
- Check the path in your configuration
- Use absolute paths, not relative
- Ensure the server is built (`npm run build`)
- Verify Node.js is in PATH

### Issue: "Tool not available in Copilot"

**Solution:**
- Reload VS Code window
- Check `.vscode/settings.json` syntax
- Verify MCP extension is installed
- Check VS Code output panel for errors

### Issue: "Double-linked references"

This should not happen with the current implementation, but if it does:

**Solution:**
- Update to the latest version of the MCP server
- The server now protects links after each rule application
- Report as a bug if issue persists

### Issue: "Document Control block added multiple times"

The tool is idempotent and should not add multiple blocks.

**Solution:**
- Check if there are multiple manual invocations
- The tool detects existing "## Document Control" headers
- If duplicate blocks exist, remove manually and re-run

### Issue: "Performance is slow"

**Solution:**
- The regex patterns are optimized but complex
- For very large documents (>100KB), processing may take a few seconds
- Consider splitting very large documents
- Ensure Node.js has sufficient memory

### Issue: "Links not working"

Internal link paths are relative and assume the OPT-IN Framework structure.

**Solution:**
- Verify your repository follows the OPT-IN Framework structure
- Check that referenced ATA chapters and requirements exist
- Adjust paths in `src/linkRules.ts` if needed for your structure
- Rebuild after changes: `npm run build`

---

## Advanced Configuration

### Custom Link Rules

Edit `src/linkRules.ts` to add custom patterns:

```typescript
{
  pattern: /(?<!\[)\b(YOUR-PATTERN)\b(?!\]\()/g,
  replacement: "[$1](https://your-url.com)",
  description: "Your custom standard"
}
```

Then rebuild:
```bash
npm run build
```

### Environment-Specific Configuration

You can use environment variables in the MCP server:

```json
{
  "mcp.servers": {
    "doc-meta-enforcer": {
      "type": "stdio",
      "command": "node",
      "args": ["${workspaceFolder}/tools/doc-meta-enforcer-mcp/dist/server.js"],
      "env": {
        "DEBUG": "true",
        "CUSTOM_BASE_PATH": "/custom/path"
      }
    }
  }
}
```

Access in server code via `process.env.DEBUG`, etc.

---

## Support

For issues or questions:

1. Check this integration guide
2. Review the main [README.md](README.md)
3. Open an issue in the AMPEL360-BWB-H2-Hy-E repository
4. Reference the OPT-IN Framework documentation

---

## Version

Integration Guide Version: 1.0.0  
MCP Server Version: 0.1.0  
Last Updated: 2025-11-17
