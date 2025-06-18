from random import randint
from time import sleep

print('Estou pensando em um número entre 0 e 5. Tente adivinhar!')

numero = randint(0, 5)
escolha = int(input('Em que número eu pensei? '))

print('Processando...')
sleep(1)

if escolha == numero:
    print(f'Parabéns, você acertou! Eu pensei no número {numero}.')
    
else:
    print(f'Que pena, você errou! Eu pensei no número {numero} e não no {escolha}.')
