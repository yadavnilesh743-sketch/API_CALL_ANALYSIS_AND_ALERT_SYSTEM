#!/bin/bash

# Deployment script for API Monitoring System

# Configuration
ENV=${1:-production}
SERVER_IP="your.server.ip"
DEPLOY_USER="deployuser"
APP_DIR="/opt/api-monitoring"
VENV_DIR="$APP_DIR/venv"

echo "=== Deploying API Monitoring System ($ENV) ==="

# 1. Remote server setup
ssh $DEPLOY_USER@$SERVER_IP << EOF
  echo "Creating directory structure..."
  sudo mkdir -p $APP_DIR
  sudo chown -R $DEPLOY_USER:$DEPLOY_USER $APP_DIR

  # 2. Create virtual environment
  echo "Setting up Python virtual environment..."
  python3 -m venv $VENV_DIR
  source $VENV_DIR/bin/activate

  # 3. Install dependencies
  echo "Installing dependencies..."
  pip install -U pip
  pip install -r $APP_DIR/requirements.txt

  # 4. Configure services
  echo "Configuring services..."
  sudo cp $APP_DIR/api-monitor.service /etc/systemd/system/
  
  # Update nginx config with domain
  echo "Setting up domain: $DOMAIN"
  sudo sed -i "s/yourdomain.com/$DOMAIN/g" $APP_DIR/nginx-ssl.conf
  sudo cp $APP_DIR/nginx-ssl.conf /etc/nginx/sites-available/api-monitor
  sudo ln -sf /etc/nginx/sites-available/api-monitor /etc/nginx/sites-enabled

  # 5. Start services
  echo "Starting services..."
  sudo systemctl daemon-reload
  sudo systemctl enable api-monitor
  sudo systemctl restart api-monitor nginx

  echo "Deployment complete!"
EOF