import requests
import time
from locust import HttpUser, task, between

class APIMonitorUser(HttpUser):
    wait_time = between(1, 3)
    
   
        
    @task(3)
    def get_history(self):
        self.client.get("/api/metrics/history?hours=24")
        
    @task(2)
    def test_alert(self):
        self.client.post("/api/test/alert", json={"error_rate": 0.12})

def run_load_test():
    import subprocess
    subprocess.run(["locust", "-f", "load_test.py", "--headless", 
                   "--users", "100", "--spawn-rate", "10", "--run-time", "1m"])