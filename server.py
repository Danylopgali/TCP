# server.py
import socket
import os

HOST = os.environ.get("TCP_SERVER_HOST", "0.0.0.0")
PORT = int(os.environ.get("TCP_SERVER_PORT", "5000"))

def start_server():
    print("[INFO] Starting TCP server...")
    print(f"[INFO] Host: {HOST}, Port: {PORT}")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[READY] Server is listening on {HOST}:{PORT}\n")

    while True:
        conn, addr = server_socket.accept()
        print(f"[NEW CONNECTION] Client connected from {addr}")

        while True:
            data = conn.recv(1024).decode()

            if not data:
                print(f"[INFO] Connection with {addr} closed by client.")
                conn.close()
                break

            print(f"[RECEIVED] {addr} sent: {data}")

            if data.strip().upper() == "DESCONEXION":
                print(f"[DISCONNECT] Client {addr} requested disconnection.")
                conn.close()
                print(f"[INFO] Connection with {addr} has been closed.\n")
                break
            else:
                response = data.upper()
                print(f"[RESPONDING] Sending to {addr}: {response}")
                conn.send(response.encode())

if __name__ == "__main__":
    start_server()
