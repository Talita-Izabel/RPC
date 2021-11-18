import socket

def connection(self, data):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.sendto(data.encode('utf-8'), (self.server, self.port))
    modifiedMessage, serverAdress = clientSocket.recvfrom(2048)
    clientSocket.close()
    return modifiedMessage.decode('utf-8')

class OperacoesMatematicas:
    def __init__(self, server, port):
        self.server = server
        self.port = port

    def soma(self, number1, number2):
        data = f'soma {number1} {number2}'
        return connection(self, data)

    def produto(self, number1, number2):
        data = f'produto {number1} {number2}'
        return connection(self, data)

    def fatorial(self, number):
        data = f'fatorial {number}'
        return connection(self, data)

