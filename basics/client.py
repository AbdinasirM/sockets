import socket
import pickle
# socket.SOCK_STREAM : Is for TCP
# socket.AF_INET: Is for IPV4

#what is buffer?
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#coonecting to the server
s.connect((socket.gethostname(), 2342))

#accept the message from the server

while True:
    full_message = b''
    new_message = True
    
    while True:
        message = s.recv(16)
        if new_message:
            print(f'new message length {message[:HEADERSIZE]}')
            message_length = int(message[:HEADERSIZE])
            new_message = False

#        full_message += message.decode("utf-8")
        full_message += message
        if len(full_message) - HEADERSIZE == message_length:
            print("Full message recieved")
            print(full_message[HEADERSIZE:])

            d = pickle.loads(full_message[HEADERSIZE:])
            print(d)
            new_message = True
            full_message = b''

print(full_message)


 