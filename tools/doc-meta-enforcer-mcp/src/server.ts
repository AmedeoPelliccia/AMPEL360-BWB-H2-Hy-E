/*
 * Copyright 2025 AMPEL360 Project Contributors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#!/usr/bin/env node

/**
 * AMPEL360 Document Meta Enforcer MCP Server
 * 
 * This MCP server provides a tool for enforcing document control blocks
 * and automatically hyperlinking standards, regulations, and internal
 * references in AMPEL360 documentation.
 * 
 * Author: AI prompted by Amedeo Pelliccia
 * License: Apache-2.0
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  Tool,
} from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";
import { applyLinkRules } from "./linkRules.js";

/**
 * Document Control block template
 */
const DOCUMENT_CONTROL_TEMPLATE = `---

## Document Control

- **Originator**: _AI prompted by Amedeo Pelliccia_
- **Toolchain**: GitHub Copilot + MCP Doc Control Server
- **Related file**: \`{{filePath}}\`
- **Status**: \`WORKING\`
- **Notes**: This document was generated with AI assistance and must be reviewed and
  approved by a designated human checker/approver before being used as an
  official baseline. All changes should follow the AMPEL360 Documentation Standard
  and OPT-IN Framework guidelines.
`;

/**
 * Check if document already has a Document Control block
 */
function hasDocumentControlBlock(content: string): boolean {
  // Look for various forms of the Document Control header
  return /^#{2,3}\s+Document\s+Control/im.test(content);
}

/**
 * Append or update Document Control block in document
 */
function enforceDocumentControlBlock(content: string, filePath: string = "<unknown>"): string {
  if (hasDocumentControlBlock(content)) {
    // Block already exists - leave it as-is (idempotent)
    return content;
  }

  // Prepare the block with the file path
  const block = DOCUMENT_CONTROL_TEMPLATE.replace("{{filePath}}", filePath);

  // Ensure content ends with proper whitespace
  const trimmed = content.trimEnd();
  
  // Add the block at the end
  return `${trimmed}\n\n${block}\n`;
}

/**
 * Main MCP Server
 */
class DocumentMetaEnforcerServer {
  private server: Server;

  constructor() {
    this.server = new Server(
      {
        name: "doc-meta-enforcer",
        version: "0.1.0",
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.setupHandlers();
  }

  private setupHandlers() {
    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [
          {
            name: "doc_control.enforce",
            description:
              "Enforces document control block with authorship (AI prompted by Amedeo Pelliccia) " +
              "and converts known standards, regulations, and internal references into hyperlinks. " +
              "Supports: EASA CS-25, FAA FAR 25, ICAO Annex, EU AI Act, S1000D, ATA iSpec 2200, " +
              "DO-178C, ARP4754A, ISO standards, internal ATA chapter references, and requirement IDs.",
            inputSchema: {
              type: "object",
              properties: {
                content: {
                  type: "string",
                  description: "The document content to process",
                },
                filePath: {
                  type: "string",
                  description: "Optional file path for documentation purposes",
                },
              },
              required: ["content"],
            },
          } as Tool,
        ],
      };
    });

    // Handle tool calls
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      if (request.params.name !== "doc_control.enforce") {
        throw new Error(`Unknown tool: ${request.params.name}`);
      }

      const args = request.params.arguments as {
        content: string;
        filePath?: string;
      };

      if (!args.content) {
        throw new Error("Missing required argument: content");
      }

      try {
        // Step 1: Enforce document control block
        let processed = enforceDocumentControlBlock(
          args.content,
          args.filePath || "<unknown>"
        );

        // Step 2: Apply hyperlink rules
        processed = applyLinkRules(processed);

        return {
          content: [
            {
              type: "text",
              text: processed,
            },
          ],
        };
      } catch (error) {
        const errorMessage = error instanceof Error ? error.message : String(error);
        return {
          content: [
            {
              type: "text",
              text: `Error processing document: ${errorMessage}`,
            },
          ],
          isError: true,
        };
      }
    });
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    
    // Log to stderr so it doesn't interfere with stdio protocol
    console.error("AMPEL360 Document Meta Enforcer MCP server running on stdio");
  }
}

// Main entry point
const server = new DocumentMetaEnforcerServer();
server.run().catch((error) => {
  console.error("Fatal error running server:", error);
  process.exit(1);
});
