# API Client Examples

## Python
```python
import requests
from datetime import datetime, timedelta

# Get authentication token
auth_response = requests.post(
    "https://api.example.com/auth",
    json={"username": "admin", "password": "secure"}
)
token = auth_response.json()["token"]

# Get historical metrics
end = datetime.now()
start = end - timedelta(hours=24)
metrics = requests.get(
    "https://api.example.com/metrics/history",
    headers={"Authorization": f"Bearer {token}"},
    params={"start": start.isoformat(), "end": end.isoformat()}
)
print(metrics.json())
```

## JavaScript
```javascript
const fetch = require('node-fetch');

async function getMetrics() {
  // Authenticate
  const auth = await fetch('https://api.example.com/auth', {
    method: 'POST',
    body: JSON.stringify({username: 'admin', password: 'secure'}),
    headers: {'Content-Type': 'application/json'}
  });
  const {token} = await auth.json();

  // Get current metrics
  const metrics = await fetch('https://api.example.com/metrics', {
    headers: {'Authorization': `Bearer ${token}`}
  });
  return await metrics.json();
}
```

## cURL
```bash
# Get token
TOKEN=$(curl -X POST https://api.example.com/auth \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"secure"}' | jq -r '.token')

# Get alerts
curl -X GET https://api.example.com/alerts \
  -H "Authorization: Bearer $TOKEN"