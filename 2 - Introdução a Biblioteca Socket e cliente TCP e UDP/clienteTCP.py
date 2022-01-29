import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    
    except socket.error as erro:
        print("A conexão falhou!!!")
        print(f"Erro: {erro}")
        sys.exit()
    
    print("Socket criado com sucesso.")


    host_alvo = input("Digite o Host a ser conectado: ")
    porta_alvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print(f"Cliente TCP conectado com Sucesso no Host: {host_alvo} e na porta: {porta_alvo}.")
        s.shutdown(2)
    except socket.error as erro:
        print(f"Não foi possível conectar o Host: {host_alvo} na porta: {porta_alvo}.")
        print(f"Erro: {erro}")
        sys.exit()

if __name__ == "__main__":
    main()