# Importando as bibliotecas
import os
import time

# Lendo os IPs e separando por linhas
with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    # Percorrendo o arquivo linha por linha
    for ip in dump:
        print('-'*60)
        os.system(f'ping {ip}')
        time.sleep(3)
        print('-'*60)
        