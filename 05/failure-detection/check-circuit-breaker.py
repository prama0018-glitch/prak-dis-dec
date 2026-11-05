"""Circuit breaker dengan pybreaker: closed -> open -> half-open -> closed."""
import time

import pybreaker
import requests

URL = "http://localhost:44777"

# Setelah 3 kegagalan beruntun, sirkuit OPEN selama 10 detik.
breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=10)


@breaker
def access_url():
    print(f"Attempting to access {URL}...")
    response = requests.get(URL, timeout=3)
    response.raise_for_status()
    print(f"Successfully accessed {URL}")


if __name__ == "__main__":
    for i in range(1, 8):
        print(f"--- Percobaan {i} | state: {breaker.current_state}")
        try:
            access_url()
        except pybreaker.CircuitBreakerError:
            print("Circuit OPEN: permintaan ditolak langsung tanpa menghubungi server")
        except requests.exceptions.RequestException as e:
            print(f"Gagal: {type(e).__name__}")
        time.sleep(2)
