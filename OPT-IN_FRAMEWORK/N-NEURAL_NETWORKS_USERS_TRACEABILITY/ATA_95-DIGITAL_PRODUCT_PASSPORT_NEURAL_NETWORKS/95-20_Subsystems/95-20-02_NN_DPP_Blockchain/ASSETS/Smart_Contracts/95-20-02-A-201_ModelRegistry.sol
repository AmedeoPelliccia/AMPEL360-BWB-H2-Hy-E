// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title ModelRegistry
 * @dev Smart contract for AMPEL360 Neural Network Model Registry
 * @notice Part of 95-20-02 NN DPP Blockchain subsystem
 * 
 * Document ID: 95-20-02-A-201
 * Version: 1.0
 * Date: 2025-11-17
 * Criticality: DAL-B
 * 
 * Purpose: Immutable registry for neural network models with provenance tracking
 * 
 * Compliance:
 * - DO-178C Level B
 * - EASA MOC SC-AI
 * - EU Digital Product Passport Regulation
 */

contract ModelRegistry {
    
    // ==================== Data Structures ====================
    
    /**
     * @dev Model metadata structure
     */
    struct Model {
        string modelId;           // e.g., "95-20-27-A-201"
        string modelName;         // e.g., "Aero_PINN"
        string version;           // Semantic version e.g., "2.1.0"
        string subsystemId;       // e.g., "95-20-27"
        string parentATA;         // e.g., "ATA 27"
        string dal;               // e.g., "DAL-A"
        ModelStatus status;       // Current status
        address registrar;        // Address that registered the model
        uint256 registrationTime; // Unix timestamp
        string artifactHash;      // IPFS hash of model artifact
        string trainingDataHash;  // IPFS hash of training data manifest
        string validationHash;    // IPFS hash of validation evidence
    }
    
    /**
     * @dev Model lifecycle status
     */
    enum ModelStatus {
        Registered,    // Initial registration
        Validated,     // V&V completed
        Deployed,      // Deployed to aircraft
        Active,        // Currently in use
        Deprecated,    // Superseded by newer version
        Retired        // Removed from service
    }
    
    /**
     * @dev Deployment record
     */
    struct Deployment {
        string modelId;
        string aircraftTailNumber;
        string eisVersion;        // e.g., "v2.0" from 95-00-11
        uint256 deploymentTime;
        address deployer;
    }
    
    /**
     * @dev Validation record
     */
    struct Validation {
        string modelId;
        string validationType;    // e.g., "ground_test", "flight_test"
        bool passed;
        uint256 validationTime;
        string evidenceHash;      // IPFS hash of evidence
        address validator;
    }
    
    // ==================== State Variables ====================
    
    /// @dev Mapping from model ID to Model struct
    mapping(string => Model) public models;
    
    /// @dev Array of all model IDs for enumeration
    string[] public modelIds;
    
    /// @dev Mapping from model ID to array of deployments
    mapping(string => Deployment[]) public deployments;
    
    /// @dev Mapping from model ID to array of validations
    mapping(string => Validation[]) public validations;
    
    /// @dev Mapping of authorized registrars (development team addresses)
    mapping(address => bool) public authorizedRegistrars;
    
    /// @dev Mapping of authorized validators (certification authority addresses)
    mapping(address => bool) public authorizedValidators;
    
    /// @dev Contract owner
    address public owner;
    
    // ==================== Events ====================
    
    event ModelRegistered(
        string indexed modelId,
        string modelName,
        string version,
        string subsystemId,
        address registrar,
        uint256 timestamp
    );
    
    event ModelStatusChanged(
        string indexed modelId,
        ModelStatus oldStatus,
        ModelStatus newStatus,
        uint256 timestamp
    );
    
    event ModelDeployed(
        string indexed modelId,
        string aircraftTailNumber,
        string eisVersion,
        address deployer,
        uint256 timestamp
    );
    
    event ModelValidated(
        string indexed modelId,
        string validationType,
        bool passed,
        address validator,
        uint256 timestamp
    );
    
    event RegistrarAuthorized(address indexed registrar, uint256 timestamp);
    event RegistrarRevoked(address indexed registrar, uint256 timestamp);
    event ValidatorAuthorized(address indexed validator, uint256 timestamp);
    event ValidatorRevoked(address indexed validator, uint256 timestamp);
    
    // ==================== Modifiers ====================
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    modifier onlyAuthorizedRegistrar() {
        require(
            authorizedRegistrars[msg.sender],
            "Only authorized registrars can call this function"
        );
        _;
    }
    
    modifier onlyAuthorizedValidator() {
        require(
            authorizedValidators[msg.sender],
            "Only authorized validators can call this function"
        );
        _;
    }
    
    modifier modelExists(string memory modelId) {
        require(
            bytes(models[modelId].modelId).length > 0,
            "Model does not exist"
        );
        _;
    }
    
    // ==================== Constructor ====================
    
    constructor() {
        owner = msg.sender;
        authorizedRegistrars[msg.sender] = true;
        authorizedValidators[msg.sender] = true;
    }
    
    // ==================== Admin Functions ====================
    
    /**
     * @dev Authorize a registrar address
     * @param registrar Address to authorize
     */
    function authorizeRegistrar(address registrar) external onlyOwner {
        authorizedRegistrars[registrar] = true;
        emit RegistrarAuthorized(registrar, block.timestamp);
    }
    
    /**
     * @dev Revoke a registrar address
     * @param registrar Address to revoke
     */
    function revokeRegistrar(address registrar) external onlyOwner {
        authorizedRegistrars[registrar] = false;
        emit RegistrarRevoked(registrar, block.timestamp);
    }
    
    /**
     * @dev Authorize a validator address
     * @param validator Address to authorize
     */
    function authorizeValidator(address validator) external onlyOwner {
        authorizedValidators[validator] = true;
        emit ValidatorAuthorized(validator, block.timestamp);
    }
    
    /**
     * @dev Revoke a validator address
     * @param validator Address to revoke
     */
    function revokeValidator(address validator) external onlyOwner {
        authorizedValidators[validator] = false;
        emit ValidatorRevoked(validator, block.timestamp);
    }
    
    // ==================== Core Functions ====================
    
    /**
     * @dev Register a new model
     * @param modelId Unique model identifier (e.g., "95-20-27-A-201")
     * @param modelName Human-readable model name
     * @param version Semantic version
     * @param subsystemId Subsystem ID (e.g., "95-20-27")
     * @param parentATA Parent ATA chapter
     * @param dal Design Assurance Level
     * @param artifactHash IPFS hash of model artifact
     * @param trainingDataHash IPFS hash of training data manifest
     */
    function registerModel(
        string memory modelId,
        string memory modelName,
        string memory version,
        string memory subsystemId,
        string memory parentATA,
        string memory dal,
        string memory artifactHash,
        string memory trainingDataHash
    ) external onlyAuthorizedRegistrar {
        require(
            bytes(models[modelId].modelId).length == 0,
            "Model already registered"
        );
        
        models[modelId] = Model({
            modelId: modelId,
            modelName: modelName,
            version: version,
            subsystemId: subsystemId,
            parentATA: parentATA,
            dal: dal,
            status: ModelStatus.Registered,
            registrar: msg.sender,
            registrationTime: block.timestamp,
            artifactHash: artifactHash,
            trainingDataHash: trainingDataHash,
            validationHash: ""
        });
        
        modelIds.push(modelId);
        
        emit ModelRegistered(
            modelId,
            modelName,
            version,
            subsystemId,
            msg.sender,
            block.timestamp
        );
    }
    
    /**
     * @dev Update model status
     * @param modelId Model identifier
     * @param newStatus New status
     */
    function updateModelStatus(
        string memory modelId,
        ModelStatus newStatus
    ) external onlyAuthorizedRegistrar modelExists(modelId) {
        ModelStatus oldStatus = models[modelId].status;
        models[modelId].status = newStatus;
        
        emit ModelStatusChanged(modelId, oldStatus, newStatus, block.timestamp);
    }
    
    /**
     * @dev Record model validation
     * @param modelId Model identifier
     * @param validationType Type of validation
     * @param passed Whether validation passed
     * @param evidenceHash IPFS hash of validation evidence
     */
    function recordValidation(
        string memory modelId,
        string memory validationType,
        bool passed,
        string memory evidenceHash
    ) external onlyAuthorizedValidator modelExists(modelId) {
        validations[modelId].push(Validation({
            modelId: modelId,
            validationType: validationType,
            passed: passed,
            validationTime: block.timestamp,
            evidenceHash: evidenceHash,
            validator: msg.sender
        }));
        
        // Update model validation hash if first validation
        if (bytes(models[modelId].validationHash).length == 0) {
            models[modelId].validationHash = evidenceHash;
        }
        
        emit ModelValidated(
            modelId,
            validationType,
            passed,
            msg.sender,
            block.timestamp
        );
    }
    
    /**
     * @dev Record model deployment
     * @param modelId Model identifier
     * @param aircraftTailNumber Aircraft tail number
     * @param eisVersion EIS version (from 95-00-11)
     */
    function recordDeployment(
        string memory modelId,
        string memory aircraftTailNumber,
        string memory eisVersion
    ) external onlyAuthorizedRegistrar modelExists(modelId) {
        deployments[modelId].push(Deployment({
            modelId: modelId,
            aircraftTailNumber: aircraftTailNumber,
            eisVersion: eisVersion,
            deploymentTime: block.timestamp,
            deployer: msg.sender
        }));
        
        emit ModelDeployed(
            modelId,
            aircraftTailNumber,
            eisVersion,
            msg.sender,
            block.timestamp
        );
    }
    
    // ==================== Query Functions ====================
    
    /**
     * @dev Get model details
     * @param modelId Model identifier
     * @return Model struct
     */
    function getModel(string memory modelId)
        external
        view
        modelExists(modelId)
        returns (Model memory)
    {
        return models[modelId];
    }
    
    /**
     * @dev Get all model IDs
     * @return Array of model IDs
     */
    function getAllModelIds() external view returns (string[] memory) {
        return modelIds;
    }
    
    /**
     * @dev Get deployment count for a model
     * @param modelId Model identifier
     * @return Number of deployments
     */
    function getDeploymentCount(string memory modelId)
        external
        view
        modelExists(modelId)
        returns (uint256)
    {
        return deployments[modelId].length;
    }
    
    /**
     * @dev Get specific deployment
     * @param modelId Model identifier
     * @param index Deployment index
     * @return Deployment struct
     */
    function getDeployment(string memory modelId, uint256 index)
        external
        view
        modelExists(modelId)
        returns (Deployment memory)
    {
        require(index < deployments[modelId].length, "Invalid deployment index");
        return deployments[modelId][index];
    }
    
    /**
     * @dev Get validation count for a model
     * @param modelId Model identifier
     * @return Number of validations
     */
    function getValidationCount(string memory modelId)
        external
        view
        modelExists(modelId)
        returns (uint256)
    {
        return validations[modelId].length;
    }
    
    /**
     * @dev Get specific validation
     * @param modelId Model identifier
     * @param index Validation index
     * @return Validation struct
     */
    function getValidation(string memory modelId, uint256 index)
        external
        view
        modelExists(modelId)
        returns (Validation memory)
    {
        require(index < validations[modelId].length, "Invalid validation index");
        return validations[modelId][index];
    }
    
    /**
     * @dev Check if all validations passed for a model
     * @param modelId Model identifier
     * @return True if all validations passed
     */
    function allValidationsPassed(string memory modelId)
        external
        view
        modelExists(modelId)
        returns (bool)
    {
        uint256 count = validations[modelId].length;
        if (count == 0) return false;
        
        for (uint256 i = 0; i < count; i++) {
            if (!validations[modelId][i].passed) {
                return false;
            }
        }
        return true;
    }
}
