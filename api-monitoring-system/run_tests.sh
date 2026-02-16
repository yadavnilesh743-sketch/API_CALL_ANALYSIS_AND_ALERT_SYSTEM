#!/bin/bash

# Install test dependencies
pip install -r requirements.txt

# Start the API server in background
python backend/main.py &
SERVER_PID=$!
sleep 3  # Wait for server to start

# Run unit tests
echo "=== Running unit tests ==="
pytest tests/e2e_test.py -v

# Run security tests
echo "=== Running security tests ==="
pytest tests/security_test.py -v

# Run load tests
echo "=== Running load tests ==="
locust -f tests/load_test.py --headless --users 100 --spawn-rate 10 --run-time 1m

# Clean up
kill $SERVER_PID
echo "=== All tests completed ==="