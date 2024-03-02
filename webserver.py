# Import socket module
from socket import *
import socket
# Prepare server socket
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
print(IP_addres)
serverSocket = socket.socket(AF_INET, SOCK_STREAM)
# Your code starts here
serverSocket.bind((IP_addres, 12000))
#Your code ends here
serverSocket.listen(1)
while True:
    # Establish connection
    print('Server listening...')
    connectionSocket, addr = serverSocket.accept()# Your code starts here # Your code ends here
    try:
        message =connectionSocket.recv(1024) # Your code starts here    # Your code ends here
        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        outputdata = f.read()# Your code starts here # Your code ends here

        # Send one HTTP header line to socket
        a = 'HTTP/1.0 200 OK\r\n'
        b = 'Content-Type: text/html\n\n'
        # Your code starts here
        # Your code ends here
        outputdata = a + b + outputdata
        #Send object to client
        #for i in range(0, len(outputdata)):
        #    print(outputdata[i])
        #    connectionSocket.send(outputdata[i].encode())
        connectionSocket.sendall(outputdata.encode())
        connectionSocket.sendall("\r\n".encode())

        connectionSocket.close()
    except (IOError, IndexError):
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
        connectionSocket.sendall(response.encode())
        # Send 404 message
        # Your code starts here
        connectionSocket.close()
        # Your code ends here

        # Close client socket
        # Your code starts here

        # Your code ends here
    
serverSocket.close()
