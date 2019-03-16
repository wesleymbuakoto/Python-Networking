from socket import *

while True:
    serverName = 'localhost'
    serverPort = 5000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    sentence = input("Input a lowercase sentence: ")
    if sentence == "Quit":
        break
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())
