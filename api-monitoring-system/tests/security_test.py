import requests
import pytest

BASE_URL = "http://localhost:5000"

def test_sql_injection_protection():
    # Test for SQL injection vulnerability
    malicious_input = "1' OR '1'='1"
    response = requests.get(
        f"{BASE_URL}/api/metrics/history",
        params={"hours": malicious_input}
    )
    assert response.status_code == 400  # Should reject malformed input

def test_xss_protection():
    # Test for XSS vulnerability
    malicious_input = "<script>alert('xss')</script>"
    response = requests.post(
        f"{BASE_URL}/api/test/alert",
        json={"api_name": malicious_input}
    )
    assert response.status_code == 400  # Should reject malformed input

def test_auth_required_endpoints():
    # Test authentication requirements
    protected_endpoints = [
        "/api/metrics/history",
        "/api/test/alert"
    ]
    for endpoint in protected_endpoints:
        response = requests.get(f"{BASE_URL}{endpoint}")
        assert response.status_code in [400, 401, 403]
