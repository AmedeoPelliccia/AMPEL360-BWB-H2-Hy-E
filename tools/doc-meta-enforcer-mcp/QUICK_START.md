# Quick Start Guide - AMPEL360 Doc-Meta-Enforcer MCP Server

Get up and running with the Document Meta Enforcer in 5 minutes!

## ⚡ Super Quick Start

### 1. Build the Server

```bash
cd tools/doc-meta-enforcer-mcp
npm install
npm run build
```

### 2. Test It

```bash
node test-full.js
```

You should see `✅ MCP Server is ready for integration!`

### 3. Use It

Choose your environment:

#### With VS Code + GitHub Copilot

Add to `.vscode/settings.json`:

```json
{
  "mcp.servers": {
    "doc-meta-enforcer": {
      "type": "stdio",
      "command": "node",
      "args": ["${workspaceFolder}/tools/doc-meta-enforcer-mcp/dist/server.js"]
    }
  }
}
```

Reload VS Code. Now when you ask Copilot to create documentation, you can say:

> "Create a fuel system safety document and use the doc_control.enforce tool to add proper metadata"

#### With Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "doc-meta-enforcer": {
      "command": "node",
      "args": ["/FULL/PATH/TO/AMPEL360-BWB-H2-Hy-E/tools/doc-meta-enforcer-mcp/dist/server.js"]
    }
  }
}
```

Restart Claude. Then ask:

> "Process this document with doc_control.enforce: [paste your document]"

---

## 🎯 What It Does

### Before

```markdown
# Fuel System Design

Complies with EASA CS-25 requirements.
See ATA_28-FUEL_SAF_CRYOGENIC_H2.
Requirement: RQ-02-01-001
```

### After

```markdown
# Fuel System Design

Complies with [EASA CS-25](https://www.easa.europa.eu/...) requirements.
See [ATA_28-FUEL_SAF_CRYOGENIC_H2](../T-TECHNOLOGY_.../ATA_28-.../README.md).
Requirement: [RQ-02-01-001](../../REQUIREMENTS/RQ-02-01-001/README.md)

---

## Document Control

- **Originator**: _AI prompted by Amedeo Pelliccia_
- **Toolchain**: GitHub Copilot + MCP Doc Control Server
- **Related file**: `fuel-system.md`
- **Status**: `WORKING`
- **Notes**: This document was generated with AI assistance...
```

---

## 🔗 What Gets Linked

### Aviation Standards

- **EASA CS-25** → EASA Large Aircraft Certification
- **FAA FAR 25** → Federal Aviation Regulations
- **ICAO Annex 6/8** → ICAO Standards

### Technical Standards

- **DO-178C**, **DO-254**, **DO-326A** → RTCA Standards
- **ARP4754A**, **ARP4761** → SAE Standards
- **S1000D**, **ATA iSpec 2200** → Documentation Standards

### Regulations

- **EU AI Act** → European AI Regulation
- **GDPR** → Data Protection
- **EASA AI Roadmap** → AI Guidelines

### Internal References

- **RQ-XX-XX-XXX** → Requirements
- **ATA_XX-...** → ATA Chapters
- **O-ORGANIZATION**, **P-PROGRAM**, etc. → OPT-IN Axes

---

## 🛠️ Tool API

### Input

```typescript
{
  content: string;      // Your document text
  filePath?: string;    // Optional: file path for metadata
}
```

### Output

```typescript
{
  content: string;      // Processed document with links and control block
}
```

### Behavior

- ✅ **Idempotent**: Run it multiple times safely
- ✅ **Non-destructive**: Only adds, never removes
- ✅ **Smart**: No double-linking

---

## 📝 Examples

### Example 1: Generate New Doc

**Copilot Prompt:**
```
Create a document about hydrogen fuel safety requirements.
Then use the doc_control.enforce tool to add metadata and hyperlinks.
```

### Example 2: Update Existing Doc

**Copilot Prompt:**
```
Open docs/safety-analysis.md and use doc_control.enforce to ensure it has 
proper document control and hyperlinked standards.
```

### Example 3: Batch Process

**Copilot Prompt:**
```
For each markdown file in docs/, use doc_control.enforce to add 
document control blocks and hyperlink standards.
```

---

## 🐛 Troubleshooting

### Server won't start

```bash
# Check Node version (need 18+)
node --version

# Rebuild
cd tools/doc-meta-enforcer-mcp
rm -rf node_modules dist
npm install
npm run build
```

### Tool not found in Copilot

1. Check `.vscode/settings.json` syntax
2. Reload VS Code window: `Ctrl/Cmd+Shift+P` → `Developer: Reload Window`
3. Check VS Code Output panel for errors

### Links not working

Internal links assume OPT-IN Framework structure:

```
OPT-IN_FRAMEWORK/
├── O-ORGANIZATION/
├── P-PROGRAM/
├── T-TECHNOLOGY_AMEDEOPELLICCIA/
├── I-INFRASTRUCTURES/
└── N-NEURAL_NETWORKS_USERS_TRACEABILITY/
```

If your structure differs, edit `src/linkRules.ts` and rebuild.

---

## 📚 Next Steps

1. ✅ **Built and tested** the server
2. 🔧 **Configured** your IDE
3. 📖 Read [INTEGRATION.md](INTEGRATION.md) for advanced setup
4. 🎨 Customize [src/linkRules.ts](src/linkRules.ts) for your needs
5. 🚀 Start generating documentation!

---

## 🆘 Need Help?

- 📖 Full docs: [README.md](README.md)
- 🔗 Integration: [INTEGRATION.md](INTEGRATION.md)
- 🐛 Issues: [GitHub Issues](https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E/issues)

---

**Built with ❤️ for AMPEL360 by AI prompted by Amedeo Pelliccia**
