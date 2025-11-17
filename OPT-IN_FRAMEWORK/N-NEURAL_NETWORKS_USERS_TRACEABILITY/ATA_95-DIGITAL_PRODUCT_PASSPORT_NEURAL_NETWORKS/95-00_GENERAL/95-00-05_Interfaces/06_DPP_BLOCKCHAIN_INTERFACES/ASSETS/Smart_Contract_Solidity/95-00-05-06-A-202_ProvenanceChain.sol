// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

contract ProvenanceChain {
    struct ProvenanceRecord {
        bytes32 dataHash;
        uint256 timestamp;
        address actor;
    }
    
    ProvenanceRecord[] public records;
    
    function addRecord(bytes32 dataHash) public {
        records.push(ProvenanceRecord(dataHash, block.timestamp, msg.sender));
    }
}
