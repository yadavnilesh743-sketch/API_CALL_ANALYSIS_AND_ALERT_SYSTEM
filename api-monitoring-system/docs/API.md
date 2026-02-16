# API Monitoring System Documentation

## REST API Endpoints

### Health Check
`GET /api/health`
```json
{
  "status": "running", 
  "version": "1.0.0",
  "uptime": "2 days",
  "dependencies": ["postgresql", "redis"]
}
```

### Metrics
`GET /api/metrics`
```json
{
  "avg_response_time": 145,
  "error_rate": 0.03,
  "throughput": 42,
  "endpoints": [
    {
      "name": "auth-service",
      "status": "healthy",
      "last_check": "2023-11-15T14:30:00Z"
    }
  ]
}
```

## Integration Examples

### Python
```python
import requests

response = requests.get("https://api.yourdomain.com/health")
if response.json()["status"] != "running":
    alert_admins()
```

### cURL
```bash
curl -X GET https://api.yourdomain.com/metrics \
  -H "Authorization: Bearer $TOKEN"