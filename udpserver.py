import socket
import threading

HOST = "0.0.0.0"
PORT = 65433

def handle_packet(data, addr, s):
    msg = data.decode()
    print(f"Received from {addr}: {msg}")
    if msg == "PING":
        s.sendto(b"PONG", addr)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"UDP server listening on {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(1024)
        # Handle each packet in a new thread
        threading.Thread(target=handle_packet, args=(data, addr, s), daemon=True).start()
