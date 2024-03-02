from socket import *
import re 



# Create socket for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
ipid = input("IP")
socket = int(input("socket"))
path = input("path")
ip = ipid+ ":"
ip = ip + socket
# Connect via our socket and port number to the IP
clientSocket.connect((ipid, socket))
# Ask user for a sentence to echo
# Send user input sentence
clientSocket.send((f"GET {path} HTTP/1.1\r\nHost:"+ ip +"\r\n\r\n").encode())
modifiedSentence = clientSocket.recv(1024).decode()
#I looked up this regex on SO
modifiedSentence = re.compile(r'<[^>]+>').sub('', modifiedSentence)
print(modifiedSentence)
