import socket
import time
import pickle
# socket.SOCK_STREAM : Is for TCP
# socket.AF_INET: Is for IPV4



# what is a header and fixed length?
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding the socket into hostname
s.bind((socket.gethostname(), 2342))

# what is a socket?
# why use bytes

#listening for clients to connect
#the #5 is for how many clients we are accepting at the same to connect to the server
s.listen(5)


while True:
    #accept everyone
    clientsocket, address = s.accept() 
    #address saves the client ip 
    #clientsocket saves the client socket object
    print(f"Connection from {address} has been established!")
    
    #send information to the client
    # clientsocket.send(bytes("", "utf-8")) 
    #header
    #message = "Welcome to the server"
    
    d = {1:"Hey", 2:"There"}
    message = pickle.dumps(d)

    message = bytes(f'{len(message) :< {HEADERSIZE}}', "utf-8") + message
    clientsocket.send(bytes(message))
    
    # clientsocket.close()


    
    # while True:
    #     time.sleep(3)
    #     message = f"The time is! {time.time()}"
    #     message = f'{len(message) :< {HEADERSIZE}}' + message
    #     clientsocket.send(bytes(message, "utf-8"))
