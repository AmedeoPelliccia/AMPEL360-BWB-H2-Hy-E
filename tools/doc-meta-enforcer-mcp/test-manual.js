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

/**
 * Manual test script for the MCP server
 * This simulates what an MCP client would send
 */

const fs = require('fs');
const path = require('path');

// Import the functions directly for testing
const { enforceDocumentControlBlock, applyLinkRules } = require('./dist/linkRules.js');

// Read test document
const testDoc = fs.readFileSync('/tmp/test-doc.md', 'utf-8');

console.log('=== ORIGINAL DOCUMENT ===');
console.log(testDoc);
console.log('\n');

// Apply link rules (this is a workaround since we can't easily import the private functions)
// Instead, let's read the built JavaScript and test the patterns

console.log('=== TESTING LINK RULES ===');
const linkRulesModule = require('./dist/linkRules.js');
const processed = linkRulesModule.applyLinkRules(testDoc);

console.log(processed);
console.log('\n');

console.log('=== SUCCESS ===');
console.log('Link rules applied successfully!');
console.log('Check that standards like "EASA CS-25", "DO-178C", etc. are now hyperlinks.');
