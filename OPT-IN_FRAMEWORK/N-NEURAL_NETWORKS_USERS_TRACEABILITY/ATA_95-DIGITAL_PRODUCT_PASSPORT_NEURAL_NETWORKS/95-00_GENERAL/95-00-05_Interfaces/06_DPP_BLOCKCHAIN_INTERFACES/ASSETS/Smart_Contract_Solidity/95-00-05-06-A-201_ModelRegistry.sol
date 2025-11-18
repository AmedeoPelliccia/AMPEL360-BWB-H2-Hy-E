// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

contract ModelRegistry {
    struct Model {
        string modelId;
        bytes32 weightsHash;
        uint256 timestamp;
        address deployer;
    }
    
    mapping(string => Model) public models;
    
    function registerModel(string memory modelId, bytes32 weightsHash) public {
        models[modelId] = Model(modelId, weightsHash, block.timestamp, msg.sender);
    }
}
