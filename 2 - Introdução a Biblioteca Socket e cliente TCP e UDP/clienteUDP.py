import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor show de bola?'

try:
    print(f'Cliente: {mensagem}')
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f'Cliente: {dados}')
finally:
    print('Cliente: Fechando a Conexão')
    s.close()