#!/bin/bash

# Demo Setup Script
echo "🚀 Setting up CC Checker Demo Environment"
echo "=========================================="

# Check Python version
echo "📋 Checking Python version..."
python3 --version

# Create virtual environment
echo "🐍 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing demo dependencies..."
pip install -r requirements.txt

# Create demo database
echo "🗄️ Setting up demo database..."
python -c "
from api.index import app
with app.app_context():
    print('Demo database initialized')
"

# Create demo directories
echo "📁 Creating demo directories..."
mkdir -p logs
mkdir -p data
mkdir -p uploads

# Set permissions
echo "🔐 Setting demo permissions..."
chmod +x scripts/*.sh

# Create demo data
echo "📊 Creating demo data..."
python -c "
import json
demo_data = {
    'initialized': True,
    'version': '2.0.0-demo',
    'contact': '@mat1520'
}
with open('data/demo_config.json', 'w') as f:
    json.dump(demo_data, f, indent=2)
"

echo ""
echo "✅ Demo environment setup complete!"
echo ""
echo "🎯 To start the demo:"
echo "   ./scripts/start_demo.sh"
echo ""
echo "📧 For the full version contact @mat1520"
echo "🔗 Telegram: https://t.me/mat1520"
