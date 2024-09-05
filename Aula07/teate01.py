from time import sleep
x = int(input('Digite o numero de segundos da contagem regressiva:  '))
import os

for i in range(x, -1, -1):
    os.system('cls')
    print(f'contando {i}...')

    sleep(1)
    

print('Fim da contagem')
