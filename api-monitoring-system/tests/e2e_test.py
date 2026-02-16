import unittest
import requests
from datetime import datetime, timedelta

class TestAPIMonitoringSystem(unittest.TestCase):
    BASE_URL = "http://localhost:5000"
    
    def test_metrics_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/api/metrics")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('response_time', data)
        self.assertIn('error_rate', data)
        
    def test_historical_metrics(self):
        params = {'hours': 24}
        response = requests.get(f"{self.BASE_URL}/api/metrics/history", params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(isinstance(data, list))
        if len(data) > 0:
            self.assertIn('timestamp', data[0])
            self.assertIn('response_time', data[0])
            
    def test_alert_thresholds(self):
        # Simulate high error rate
        test_data = {'error_rate': 0.15}
        response = requests.post(f"{self.BASE_URL}/api/test/alert", json=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['alert_triggered'])

if __name__ == '__main__':
    unittest.main()