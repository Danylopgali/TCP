# client.py
import socket
import sys
import os

HOST = os.environ.get("TCP_CLIENT_SERVER_HOST", "127.0.0.1")
PORT = int(os.environ.get("TCP_CLIENT_SERVER_PORT", "6000"))

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print(f"[CLIENT] Connected to {HOST}:{PORT}")
    except ConnectionRefusedError:
        print(f"[ERROR] Could not connect to server at {HOST}:{PORT}")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        sys.exit(1)

    try:
        while True:
            message = input("Enter a message ('DESCONEXION' to exit): ")

            if message == "DESCONEXION":
                client_socket.send(message.encode())
                print("[CLIENT] Disconnected from the server.")
                client_socket.close()
                print("Connection terminated.")
                break
            elif message.lower() == "desconexion":
                print("[INFO] To disconnect, type 'DESCONEXION' in uppercase exactly.")
                continue

            client_socket.send(message.encode())

            response = client_socket.recv(1024).decode()
            print(f"[SERVER RESPONSE]: {response}")
    except KeyboardInterrupt:
        print("\n[CLIENT] Interrupted by user. Closing connection.")
        client_socket.close()
        print("Connection terminated.")
    except Exception as e:
        print(f"[ERROR] Communication error: {e}")
        client_socket.close()
        print("Connection terminated.")

if __name__ == "__main__":
    start_client()
