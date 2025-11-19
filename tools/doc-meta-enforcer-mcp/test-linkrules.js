const { applyLinkRules } = require('./dist/linkRules.js');
const fs = require('fs');

const testDoc = fs.readFileSync('/tmp/test-interface-refs.md', 'utf8');
console.log('=== Original Document ===');
console.log(testDoc);
console.log('\n=== After Applying Link Rules ===');
const result = applyLinkRules(testDoc);
console.log(result);

// Check if our new patterns were applied
const assetPattern = /\[95-00-05-\d{2}-A-\d{3}\]\([^)]+\)/g;
const docPattern = /\[95-00-05-\d{2}-\d{3}\]\([^)]+\)/g;

const assetMatches = result.match(assetPattern);
const docMatches = result.match(docPattern);

console.log('\n=== Test Results ===');
console.log(`Asset references found: ${assetMatches ? assetMatches.length : 0}`);
console.log(`Document references found: ${docMatches ? docMatches.length : 0}`);

if (assetMatches) {
  console.log('\nAsset links:');
  assetMatches.forEach(m => console.log('  ' + m));
}

if (docMatches) {
  console.log('\nDocument links:');
  docMatches.forEach(m => console.log('  ' + m));
}

console.log('\n✅ Link rules test completed successfully!');
