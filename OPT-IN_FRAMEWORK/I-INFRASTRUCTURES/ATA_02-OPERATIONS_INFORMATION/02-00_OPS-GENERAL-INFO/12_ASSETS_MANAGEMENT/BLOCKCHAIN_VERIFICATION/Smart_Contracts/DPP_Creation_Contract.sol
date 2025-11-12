// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title DPPCreationContract
 * @dev Smart contract for creating Digital Product Passports on blockchain
 * @notice This contract handles the creation and initial registration of DPPs
 */

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DPPCreationContract is AccessControl, Pausable, ReentrancyGuard {
    
    // Role definitions
    bytes32 public constant CREATOR_ROLE = keccak256("CREATOR_ROLE");
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
    
    // DPP Structure
    struct DPP {
        string dppId;
        string ipfsHash;
        address owner;
        uint256 timestamp;
        string assetType;
        bool isActive;
        uint256 creationBlock;
    }
    
    // Storage
    mapping(string => DPP) public dppRecords;
    mapping(address => string[]) public ownerDPPs;
    string[] public allDPPIds;
    
    // Events
    event DPPCreated(
        string indexed dppId,
        string ipfsHash,
        address indexed owner,
        string assetType,
        uint256 timestamp
    );
    
    event DPPOwnershipTransferred(
        string indexed dppId,
        address indexed previousOwner,
        address indexed newOwner,
        uint256 timestamp
    );
    
    // Constructor
    constructor() {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(ADMIN_ROLE, msg.sender);
        _grantRole(CREATOR_ROLE, msg.sender);
    }
    
    /**
     * @dev Create a new DPP
     * @param _dppId Unique identifier for the DPP
     * @param _ipfsHash IPFS hash of the DPP document
     * @param _assetType Type of asset (Equipment, Component, Material, Software)
     */
    function createDPP(
        string memory _dppId,
        string memory _ipfsHash,
        string memory _assetType
    ) public onlyRole(CREATOR_ROLE) whenNotPaused nonReentrant {
        require(bytes(_dppId).length > 0, "DPP ID cannot be empty");
        require(bytes(_ipfsHash).length > 0, "IPFS hash cannot be empty");
        require(bytes(dppRecords[_dppId].dppId).length == 0, "DPP already exists");
        
        DPP memory newDPP = DPP({
            dppId: _dppId,
            ipfsHash: _ipfsHash,
            owner: msg.sender,
            timestamp: block.timestamp,
            assetType: _assetType,
            isActive: true,
            creationBlock: block.number
        });
        
        dppRecords[_dppId] = newDPP;
        ownerDPPs[msg.sender].push(_dppId);
        allDPPIds.push(_dppId);
        
        emit DPPCreated(_dppId, _ipfsHash, msg.sender, _assetType, block.timestamp);
    }
    
    /**
     * @dev Transfer ownership of a DPP
     * @param _dppId DPP identifier
     * @param _newOwner New owner address
     */
    function transferOwnership(
        string memory _dppId,
        address _newOwner
    ) public whenNotPaused nonReentrant {
        require(dppRecords[_dppId].owner == msg.sender, "Not the owner");
        require(_newOwner != address(0), "Invalid new owner address");
        require(dppRecords[_dppId].isActive, "DPP is not active");
        
        address previousOwner = dppRecords[_dppId].owner;
        dppRecords[_dppId].owner = _newOwner;
        ownerDPPs[_newOwner].push(_dppId);
        
        emit DPPOwnershipTransferred(_dppId, previousOwner, _newOwner, block.timestamp);
    }
    
    /**
     * @dev Get DPP details
     * @param _dppId DPP identifier
     * @return DPP struct
     */
    function getDPP(string memory _dppId) public view returns (DPP memory) {
        require(bytes(dppRecords[_dppId].dppId).length > 0, "DPP does not exist");
        return dppRecords[_dppId];
    }
    
    /**
     * @dev Get all DPPs owned by an address
     * @param _owner Owner address
     * @return Array of DPP IDs
     */
    function getDPPsByOwner(address _owner) public view returns (string[] memory) {
        return ownerDPPs[_owner];
    }
    
    /**
     * @dev Get total number of DPPs
     * @return Total count
     */
    function getTotalDPPs() public view returns (uint256) {
        return allDPPIds.length;
    }
    
    /**
     * @dev Verify if a DPP exists and is active
     * @param _dppId DPP identifier
     * @return Boolean indicating if DPP exists and is active
     */
    function verifyDPP(string memory _dppId) public view returns (bool) {
        return bytes(dppRecords[_dppId].dppId).length > 0 && dppRecords[_dppId].isActive;
    }
    
    /**
     * @dev Pause contract (emergency use only)
     */
    function pause() public onlyRole(ADMIN_ROLE) {
        _pause();
    }
    
    /**
     * @dev Unpause contract
     */
    function unpause() public onlyRole(ADMIN_ROLE) {
        _unpause();
    }
}
