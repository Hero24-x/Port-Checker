```python
import socket

host = input("Enter Host/IP: ")

ports = [21, 22, 25, 53, 80, 110, 143, 443, 445, 3306]

print(f"\nScanning {host}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    if result == 0:
        print(f"[OPEN]   Port {port}")
    else:
        print(f"[CLOSED] Port {port}")

    sock.close()

print("\nScan Complete.")
```
