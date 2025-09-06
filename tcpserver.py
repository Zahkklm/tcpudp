import socket
import threading

HOST = "0.0.0.0"
PORT = 65432

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode()
        print(f"Received: {msg} from {addr}")
        if msg == "PING":
            conn.sendall(b"PONG")
    conn.close()
    print(f"Connection closed {addr}")

# TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"TCP server listening on {HOST}:{PORT}")
    
    while True:
        conn, addr = s.accept()
        # Handle each client in a new thread
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
