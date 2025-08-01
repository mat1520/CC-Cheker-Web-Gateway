# Security Utilities - Demo Version
"""
DEMO FILE - Security and Encryption Functions

Full version security features:
- AES encryption for sensitive data
- Secure hashing algorithms
- API key generation
- Rate limiting implementation
- CSRF protection
- SQL injection prevention
- XSS protection
- Secure session management
- PCI DSS compliance tools
- Audit logging

Contact @mat1520 for enterprise security implementation.
"""

import hashlib
import secrets
from datetime import datetime

class Encryption:
    """Encryption utilities - Demo version"""
    
    @staticmethod
    def encrypt_card_data(card_data, key=None):
        """
        DEMO - Card data encryption
        Full version uses AES-256 encryption
        """
        return f"demo_encrypted_{hash(card_data)}"
    
    @staticmethod
    def decrypt_card_data(encrypted_data, key=None):
        """
        DEMO - Card data decryption
        Full version decrypts with proper key management
        """
        return "demo_decrypted_data"
    
    @staticmethod
    def hash_sensitive_data(data):
        """Secure hashing - Demo version"""
        return hashlib.sha256(str(data).encode()).hexdigest()

class APIKeyManager:
    """API key management - Demo version"""
    
    @staticmethod
    def generate_api_key():
        """Generate secure API key - Demo version"""
        return f"demo_api_key_{secrets.token_hex(16)}"
    
    @staticmethod
    def validate_api_key(api_key):
        """Validate API key - Demo version"""
        return api_key.startswith("demo_api_key_")

class RateLimiter:
    """Rate limiting - Demo version"""
    
    def __init__(self):
        self.demo_mode = True
    
    def check_rate_limit(self, identifier, limit=100):
        """Check if rate limit exceeded - Demo version"""
        return {
            "allowed": True,
            "remaining": limit - 1,
            "demo_note": "Full version has Redis-based rate limiting"
        }
