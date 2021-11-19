import queue
import socket
import threading, queue


def connection(self, data, queue):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.sendto(data.encode('utf-8'), (self.server, self.port))
    modifiedMessage, serverAdress = clientSocket.recvfrom(2048)
    clientSocket.close()
    msg = modifiedMessage.decode('utf-8')
    queue.put(msg)
    return

def startThreads(self, data):
    q = queue.Queue()

    thr = threading.Thread(target=connection, args=(self, data, q))
    thr.start()
    thr.join()
    
    return q.get()

class OperacoesMatematicas:
    def __init__(self, server, port):
        self.server = server
        self.port = port

    def soma(self, number1, number2):
        data = f'soma {number1} {number2}'
        # return connection(self, data)
        return startThreads(self, data)

    def produto(self, number1, number2):
        data = f'produto {number1} {number2}'
        # return connection(self, data)
        return startThreads(self, data)

    def fatorial(self, number):
        data = f'fatorial {number}'
        # return connection(self, data)
        return startThreads(self, data)

