# Smart Contract Specification

## Contract: ModelRegistry

### Functions

#### registerModel
```solidity
function registerModel(
    string memory modelId,
    string memory version,
    bytes32 hash,
    string memory metadata
) public
```
Registers a new model on blockchain.

#### getModel
```solidity
function getModel(string memory modelId) 
    public view returns (ModelRecord memory)
```
Retrieves model record.

### Events
- ModelRegistered(modelId, version, timestamp)
- ModelUpdated(modelId, version, timestamp)
