from rpc import OperacoesMatematicas

RPC_SERVER = "192.168.2.108"
RPC_PORT = 5050

op = OperacoesMatematicas(RPC_SERVER, RPC_PORT)

soma = op.soma(2, 3)
produto = op.produto(4, 6)
fatorial = op.fatorial(5)

print('Soma: ', soma) # Exibe 5
print('Produto: ', produto)
print('Fatorial: ', fatorial)