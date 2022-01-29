import random, string

def gerador_senha():

    while 1:
        print('='*20)
        tamanho = int(input('Digite o tamanho de senha que você deseja: '))

        chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+,.:;/?'

        r = random.SystemRandom()

        print('='*tamanho)
        print(''.join(r.choice(chars) for i in range(tamanho)))
        print('='*tamanho)
        continua = input('===Deseja continuar?=== ')
        if continua in 'naoNao':
            break

gerador_senha()