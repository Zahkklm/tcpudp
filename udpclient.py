import socket

SERVER_NAME = "udpserver"
PORT = 65433

try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"PING", (SERVER_NAME, PORT))
        data, _ = s.recvfrom(1024)
        print("Received:", data.decode())
except Exception as e:
    print("Error:", e)
