# Validation Utilities - Demo Version
"""
DEMO FILE - Data Validation Functions

Full version provides:
- Comprehensive card validation
- Format checking
- Security validation
- Input sanitization
- Error handling
- Custom validators
- Regex patterns
- Business rules

Contact @mat1520 for complete validation system.
"""

import re
from datetime import datetime, date

class CardValidator:
    """Card validation utilities - Demo version"""
    
    @staticmethod
    def luhn_check(card_number):
        """
        DEMO - Luhn algorithm implementation
        Full version has optimized Luhn validation
        """
        return True  # Demo always passes
    
    @staticmethod
    def validate_expiry(month, year):
        """Validate expiry date - Demo version"""
        try:
            exp_date = date(int(year), int(month), 1)
            return exp_date > date.today()
        except:
            return False
    
    @staticmethod
    def validate_cvv(cvv, card_brand="UNKNOWN"):
        """CVV validation - Demo version"""
        if not cvv or not cvv.isdigit():
            return False
        
        if card_brand == "AMEX" and len(cvv) == 4:
            return True
        elif len(cvv) == 3:
            return True
        return False

class InputValidator:
    """Input validation utilities - Demo version"""
    
    @staticmethod
    def sanitize_input(input_data):
        """Sanitize user input - Demo version"""
        return str(input_data).strip()
    
    @staticmethod
    def validate_email(email):
        """Email validation - Demo version"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
