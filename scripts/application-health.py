import requests
import time

application_url = "http://example.com"
timeout_seconds = 5

# Function to check application health
def check_application_health(url):
    try:
        response = requests.get(url, timeout=timeout_seconds)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False

# Check application health
if check_application_health(application_url):
    print("Application is up and running.")
else:
    print("Application is down or not responding.")
