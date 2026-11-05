"""Retry dengan tenacity: coba akses URL beberapa kali sebelum menyerah."""
import requests
from tenacity import RetryError, retry, retry_if_exception_type, stop_after_attempt, wait_fixed

URL = "http://localhost:44777"


@retry(
    stop=stop_after_attempt(5),          # maksimal 5 percobaan
    wait=wait_fixed(1),                  # jeda 1 detik antar percobaan
    retry=retry_if_exception_type(requests.exceptions.ConnectionError),
)
def access_url():
    print(f"Attempting to access {URL}...")
    response = requests.get(URL, timeout=3)
    response.raise_for_status()
    print(f"Successfully accessed {URL}")


if __name__ == "__main__":
    try:
        access_url()
    except RetryError as e:
        print(f"Failed to access URL after multiple retries: {e}")
