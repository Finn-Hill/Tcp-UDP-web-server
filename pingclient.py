# UDP Client
import timeit

# How Python makes it easy to make sockets
from socket import *

# serverName here works as the IP address
# serverPort is on what port we will open up our connection
serverName = '134.10.75.119'
serverPort = 12000
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
# This gets Python to create our socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Ask user for some input, lowercase just because the server will make uppercase
message = input('Input a sentence in lowercase:')
# Use socket to send message, note the use of encode() and the address
times = []
returned = 0
for i in range(10):
    start = timeit.timeit()
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    # Receiving follows similar format, 2048 is buffer size for input
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    end = timeit.timeit()
    if modifiedMessage.decode() == '':
        print("*")
    else:
        print(modifiedMessage.decode())
        returned += 1
        print(f"RTT {end-start}")
    times.append(end-start)
z = 0
for x in times:
    z = z +x

print(f"Average time: {z/10}")
print(f"Percent returned: {returned/10}")
clientSocket.close()


