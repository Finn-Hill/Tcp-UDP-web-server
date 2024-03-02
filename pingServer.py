# UDP Ping Server
# Using random to simulate packet loss
import random
# Import socket module
from socket import *
import socket

# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
serverSocket = socket.socket(AF_INET, SOCK_DGRAM)
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
# Assign IP address and port number to socket
serverSocket.bind((IP_addres, 12000))

while True:
    # Receive client packet and arrival address
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message
    message = message.decode().upper()
    # Error simulator goes here
    # Your code starts here
    x = random.randint(0,100)
    y = random.randint(0,100)
    if x>y:
    # Your code ends here
    # If no error, server responds
        serverSocket.sendto(message.encode(), address)
    serverSocket.sendto((''.encode()),address)

