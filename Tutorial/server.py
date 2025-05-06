import socket

HOST = "127.0.0.1"
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

client, address = server_socket.accept()
print(f"Connected by {address}")

try:
    while True:
        data = client.recv(1024)
        if not data:
            print("Client disconnected.")
            break
        client.sendall(data)
finally:
    client.close()
    server_socket.close()
