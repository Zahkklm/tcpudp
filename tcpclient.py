import socket

SERVER_NAME = "tcpserver"
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_NAME, PORT))
        s.sendall(b"PING")
        data = s.recv(1024)
        print("Received:", data.decode())
except Exception as e:
    print("Error:", e)
