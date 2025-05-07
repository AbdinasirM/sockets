import socket

HOST = "127.0.0.1"
PORT = 65531

def initialize():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client_socket;

def connect(client_socket, host, port):
    client_socket.connect((host, port))

def send_data(client_socket):
    data = client_socket.send(b"Hello")

def recieve_data(client_socket):
    result = client_socket.recv(1024)



if __name__ == "__main__":
    client_socket = initialize()
    connect(client_socket, HOST, PORT)
    send_data(client_socket)
    recieve_data(client_socket)
    client_socket.close()