"""
OFEC Authentication
OFEC-60-60-40-10 - Security

This module handles authentication for OFEC communications.
"""

from dataclasses import dataclass
from typing import Dict, Optional
import time
import hashlib
import hmac
import secrets


@dataclass
class AuthToken:
    """Authentication token."""
    token_id: str
    aircraft_id: str
    issued_at: float
    expires_at: float
    permissions: Dict


class OFECAuth:
    """
    Handles authentication for OFEC communications.
    
    Provides token generation, validation, and session management.
    """
    
    # Token lifetime (seconds)
    TOKEN_LIFETIME = 3600  # 1 hour
    
    # Secret key for HMAC (in production, load from secure storage)
    _secret_key: bytes = secrets.token_bytes(32)
    
    def __init__(self, aircraft_id: str):
        """
        Initialize authentication handler.
        
        Args:
            aircraft_id: Aircraft identifier
        """
        self._aircraft_id = aircraft_id
        self._current_token: Optional[AuthToken] = None
    
    def generate_token(self) -> AuthToken:
        """
        Generate a new authentication token.
        
        Returns:
            New authentication token
        """
        current_time = time.time()
        
        token = AuthToken(
            token_id=secrets.token_hex(16),
            aircraft_id=self._aircraft_id,
            issued_at=current_time,
            expires_at=current_time + self.TOKEN_LIFETIME,
            permissions={"publish": True, "read": True}
        )
        
        self._current_token = token
        return token
    
    def validate_token(self, token: AuthToken) -> bool:
        """
        Validate an authentication token.
        
        Args:
            token: Token to validate
            
        Returns:
            True if token is valid
        """
        current_time = time.time()
        
        # Check expiration
        if current_time > token.expires_at:
            return False
        
        # Check aircraft ID matches
        if token.aircraft_id != self._aircraft_id:
            return False
        
        return True
    
    def sign_message(self, message: bytes) -> bytes:
        """
        Sign a message with HMAC.
        
        Args:
            message: Message bytes to sign
            
        Returns:
            HMAC signature
        """
        return hmac.new(
            self._secret_key,
            message,
            hashlib.sha256
        ).digest()
    
    def verify_signature(self, message: bytes, signature: bytes) -> bool:
        """
        Verify a message signature.
        
        Args:
            message: Original message
            signature: Signature to verify
            
        Returns:
            True if signature is valid
        """
        expected = self.sign_message(message)
        return hmac.compare_digest(expected, signature)
    
    def refresh_token(self) -> Optional[AuthToken]:
        """
        Refresh the current token if needed.
        
        Returns:
            New token or current if still valid
        """
        if self._current_token is None:
            return self.generate_token()
        
        # Refresh if less than 5 minutes remaining
        if time.time() > self._current_token.expires_at - 300:
            return self.generate_token()
        
        return self._current_token
    
    @property
    def current_token(self) -> Optional[AuthToken]:
        """Get current authentication token."""
        return self._current_token
    
    @property
    def is_authenticated(self) -> bool:
        """Check if currently authenticated."""
        if self._current_token is None:
            return False
        return self.validate_token(self._current_token)
