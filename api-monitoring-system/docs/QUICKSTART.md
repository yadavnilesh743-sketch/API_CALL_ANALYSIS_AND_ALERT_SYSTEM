# Quick Start Guide

## Development Setup
```bash
# 1. Clone the repository
git clone https://github.com/yourorg/api-monitoring-system.git
cd api-monitoring-system

# 2. Set up Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Configure environment variables
cp .env.example .env
nano .env  # Edit with your configuration

# 4. Start development servers
flask run &  # Backend
python3 -m http.server 8000 -d frontend  # Frontend
```

## First Run
1. Access the dashboard at: http://localhost:8000/dashboard.html
2. Default admin credentials: admin/ChangeMe123 (change immediately)
3. Navigate to Settings → API Endpoints
4. Add your first API endpoint to monitor
5. Configure alert thresholds and notifications

## Key Features
- Real-time API health monitoring
- Performance metrics dashboard
- Custom alert configurations
- Historical data tracking

## Troubleshooting
- Check logs: `tail -f api_monitor.log`
- Reset database: `flask init-db`
- Clear cache: `rm -rf instance/cache/*`