# Configuration Management - Demo Version
"""
DEMO FILE - Application Configuration

Full version configuration includes:
- Database connection strings
- Gateway API credentials
- Security settings
- Rate limiting rules
- Logging configuration
- Environment variables
- Feature flags
- Performance settings
- Monitoring setup
- Backup configurations

Contact @mat1520 for production configuration.
"""

import os
from datetime import timedelta

class Config:
    """Base configuration - Demo version"""
    
    # Demo settings
    SECRET_KEY = "demo_secret_key_change_in_production"
    DEBUG = True
    DEMO_MODE = True
    
    # Database (Demo)
    DATABASE_URL = "sqlite:///demo.db"
    
    # API Settings (Demo)
    API_RATE_LIMIT = "100 per hour"
    API_VERSION = "v1"
    
    # Security (Demo)
    JWT_SECRET_KEY = "demo_jwt_secret"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    
    # Gateway Configs (Demo placeholders)
    STRIPE_API_KEY = "demo_stripe_key"
    PAYPAL_CLIENT_ID = "demo_paypal_id"
    SQUARE_ACCESS_TOKEN = "demo_square_token"
    
    # Telegram (Demo)
    TELEGRAM_BOT_TOKEN = "demo_bot_token"
    TELEGRAM_WEBHOOK_URL = "https://demo.example.com/webhook"
    
    # Logging (Demo)
    LOG_LEVEL = "DEBUG"
    LOG_FILE = "demo.log"
    
    @staticmethod
    def get_demo_config():
        return {
            "status": "demo_configuration",
            "message": "Demo configuration loaded",
            "note": "Full version has production-ready configuration",
            "contact": "@mat1520 for production setup"
        }

class ProductionConfig(Config):
    """Production configuration - Demo placeholder"""
    
    DEBUG = False
    DEMO_MODE = False
    
    # In full version, these would be loaded from environment variables
    # DATABASE_URL = os.environ.get('DATABASE_URL')
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # etc.

class DevelopmentConfig(Config):
    """Development configuration - Demo placeholder"""
    
    DEBUG = True
    DEMO_MODE = True
