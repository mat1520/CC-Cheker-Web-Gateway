#!/bin/bash

# Demo Start Script
echo "🚀 Starting CC Checker Demo Application"
echo "======================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Running setup..."
    ./scripts/setup_demo.sh
fi

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source venv/bin/activate

# Start demo message
echo ""
echo "🎯 CC CHECKER TERMINAL - DEMO VERSION"
echo "======================================"
echo "📧 Contact: @mat1520"
echo "🔗 Telegram: https://t.me/mat1520"
echo "💻 GitHub: https://github.com/mat1520"
echo ""
echo "🚨 DEMO LIMITATIONS:"
echo "   - Simulated results only"
echo "   - No real gateway connections"
echo "   - Limited functionality"
echo ""
echo "💰 FULL VERSION FEATURES:"
echo "   - 50+ Live Payment Gateways"
echo "   - Real-time Card Verification"
echo "   - Mass Processing"
echo "   - Telegram Bot Integration"
echo "   - Advanced Analytics"
echo "   - Enterprise Security"
echo ""

# Start web server for static files
echo "🌐 Starting demo web server on port 8000..."
echo "📱 Open: http://localhost:8000"
echo ""
echo "⏹️  Press Ctrl+C to stop the demo"
echo ""

# Start simple HTTP server
python3 -m http.server 8000
