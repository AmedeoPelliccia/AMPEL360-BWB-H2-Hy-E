// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

contract AccessControl {
    mapping(address => bool) public authorizedUsers;
    
    function grantAccess(address user) public {
        authorizedUsers[user] = true;
    }
    
    function revokeAccess(address user) public {
        authorizedUsers[user] = false;
    }
}
