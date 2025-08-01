# Docker Configuration - Demo Version
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create logs directory
RUN mkdir -p logs

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=api/index.py
ENV FLASK_ENV=production
ENV DEMO_MODE=true

# Add demo startup message
RUN echo '#!/bin/bash\necho "🚀 Starting CC Checker Demo Version"\necho "📧 Contact @mat1520 for full version"\necho "🔗 Telegram: https://t.me/mat1520"\necho "💻 GitHub: https://github.com/mat1520"\necho ""\npython api/index.py' > start.sh && chmod +x start.sh

# Run the demo application
CMD ["./start.sh"]

# Note: This is a demo Dockerfile
# Full version includes:
# - Multi-stage builds for optimization
# - Security hardening
# - Production-grade configurations
# - Health checks
# - Monitoring setup
# - Proper secret management
# Contact @mat1520 for production Docker setup
