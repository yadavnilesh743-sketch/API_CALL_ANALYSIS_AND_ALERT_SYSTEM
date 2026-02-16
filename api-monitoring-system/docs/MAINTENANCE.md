# System Maintenance Guide

## Backup Procedures
```bash
# Database backup (daily)
pg_dump -U monitor -h localhost api_monitor | gzip > /backups/api_monitor_$(date +%F).sql.gz

# Configuration backup (weekly)
tar czvf /backups/config_$(date +%F).tar.gz \
  .env.production \
  gunicorn_config.py \
  nginx*.conf \
  logging.conf
```

## Common Issues

### High Resource Usage
```bash
# Check top processes
top -o %CPU

# Analyze Gunicorn workers
sudo journalctl -u api-monitor -n 100 -f
```

### Certificate Renewal
```bash
# Test renewal
sudo certbot renew --dry-run

# Manual renewal
sudo certbot renew --force-renewal
sudo systemctl reload nginx
```

## Upgrade Checklist
1. Notify users of maintenance window
2. Backup database and configurations
3. Stop services: `sudo systemctl stop api-monitor`
4. Update code: `git pull origin main`
5. Update dependencies: `pip install -U -r requirements.txt`
6. Run migrations if needed
7. Restart services
8. Verify system health