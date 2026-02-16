# API Monitoring System Deployment Guide

## Prerequisites
- Ubuntu 20.04+ server
- Python 3.8+
- PostgreSQL 12+
- Nginx
- Certbot (for Let's Encrypt)

## Installation Steps

1. **Server Setup**:
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx postgresql certbot
```

2. **Application Deployment**:
```bash
# Clone repository
git clone https://your-repo-url /opt/api-monitoring

# Set up virtual environment
python3 -m venv /opt/api-monitoring/venv
source /opt/api-monitoring/venv/bin/activate
pip install -r requirements.txt

# Configure production settings
cp .env.production .env
nano .env  # Edit configuration
```

3. **Database Setup**:
```bash
sudo -u postgres psql
CREATE DATABASE api_monitor;
CREATE USER monitor_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE api_monitor TO monitor_user;
```

4. **Service Configuration**:
```bash
# Copy service file
sudo cp api-monitor.service /etc/systemd/system/

# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable api-monitor
sudo systemctl start api-monitor
```

5. **Nginx Setup**:
```bash
sudo cp nginx-ssl.conf /etc/nginx/sites-available/api-monitor
sudo ln -s /etc/nginx/sites-available/api-monitor /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

6. **SSL Certificate**:
```bash
sudo certbot --nginx -d yourdomain.com
```

## Verification
- Access dashboard at: https://yourdomain.com
- Check service status: `sudo systemctl status api-monitor`
- View logs: `journalctl -u api-monitor -f`