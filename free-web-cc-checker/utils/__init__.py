# Utility Functions - Demo Version
"""
DEMO FILE - Helper Functions and Utilities

Full version includes:
- Card number validation
- Luhn algorithm verification
- BIN lookup functions
- Data encryption/decryption
- Rate limiting helpers
- Logging utilities
- Error handling
- Security functions
- Performance monitoring
- Data export functions

Contact @mat1520 for complete utility library.
"""

import re
from datetime import datetime

class CCValidator:
    """Credit Card Validation Utilities - Demo Version"""
    
    @staticmethod
    def validate_card_number(card_number):
        """
        DEMO METHOD - Card number validation
        Full version includes complete Luhn algorithm validation
        """
        if not card_number or len(card_number) < 13:
            return False
        return True  # Demo always returns True
    
    @staticmethod
    def get_card_brand(card_number):
        """
        DEMO METHOD - Card brand detection
        Full version has comprehensive brand detection
        """
        if card_number.startswith('4'):
            return "VISA_DEMO"
        elif card_number.startswith('5'):
            return "MASTERCARD_DEMO"
        elif card_number.startswith('3'):
            return "AMEX_DEMO"
        return "UNKNOWN_DEMO"
    
    @staticmethod
    def format_card_number(card_number):
        """Format card number for display"""
        if len(card_number) >= 8:
            return card_number[:4] + '****' + card_number[-4:]
        return "****"

class SecurityUtils:
    """Security utilities - Demo version"""
    
    @staticmethod
    def hash_card_data(card_data):
        """Demo hash function"""
        return f"demo_hash_{hash(card_data)}"
    
    @staticmethod
    def encrypt_sensitive_data(data):
        """Demo encryption"""
        return f"demo_encrypted_{data}"

class ExportUtils:
    """Data export utilities - Demo version"""
    
    @staticmethod
    def export_to_csv(data):
        """Demo CSV export"""
        return "demo_csv_data"
    
    @staticmethod
    def export_to_json(data):
        """Demo JSON export"""
        return {"demo": "json_data"}
