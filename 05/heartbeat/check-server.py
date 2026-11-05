"""Heartbeat sederhana: cek apakah server TCP di host:port masih merespons.

Pemakaian: python check-server.py <host> <port>
Contoh   : python check-server.py localhost 44777
"""
import socket
import sys


def check_server(host: str, port: int, timeout: float = 3.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Pemakaian: python check-server.py <host> <port>")
        sys.exit(2)

    host, port = sys.argv[1], int(sys.argv[2])
    if check_server(host, port):
        print("Server up")
    else:
        print("Server down")
        sys.exit(1)
