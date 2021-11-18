import socket
from math import factorial

def soma(number1, number2): 
    return int(number1) + int(number2)

def produto(number1, number2): 
    return int(number1) * int(number2)

def fatorial(number): 
    n = int(number)
    return factorial(n)

serverPort = 5050
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Servidor pronto para receber")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("{} ==> {}".format(clientAddress,message.decode('utf-8')))
    modifiedMessage = message.decode('utf-8').upper()
    split = modifiedMessage.split(' ')
    print(split)

    op = split[0]

    if(op == 'SOMA'):
        result = soma(split[1], split[2])
    elif(op == 'PRODUTO'):
        result = produto(split[1], split[2])
    else:
        result = fatorial(split[1])

    print('result', result)
    msg = str(result)

    serverSocket.sendto(msg.encode('utf-8'), clientAddress)