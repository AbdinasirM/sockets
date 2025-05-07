import socket
import sys
HOST = "127.0.0.1"
PORT = 65531

def initialize(host, port):    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server is running on {host}:{port}")
    return server_socket


def process_client(server_socket):
    client, address = server_socket.accept()
    print(f"Connected by {address}")
    try:
        while True:
            data = client.recv(1024)
            if not data:
                return "CLient disconnected"
            client.sendall(data)
    except Exception as e:
        return f"Error: {e}"
    
    finally:
        client.close()


if __name__ == "__main__" :
    server_socket = initialize(HOST,PORT)
    process_client(server_socket)