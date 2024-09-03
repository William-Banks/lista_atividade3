notas = []
print(30*'-', 'BOLETIM ESCOLAR' ,30*'-')
print('')

#Declaração dos elementos
numero_usuario1 = int(input('Digite um numero: '))
notas.append(numero_usuario1)
print('')

numero_usuario2 = int(input('Digite um numero: '))
notas.append(numero_usuario2)
print('')

numero_usuario3 = int(input('Digite um numero: '))
notas.append(numero_usuario3)
print('')

numero_usuario4 = int(input('Digite um numero: '))
notas.append(numero_usuario4)
print('')

numero_usuario5 = int(input('Digite um numero: '))
notas.append(numero_usuario5)
print('')

# Len conta a quantidade de elementos dentro da lista
quantidade_notas = len(notas)

# sum ira somar todos os elementos da lista
soma = sum(notas)

#Declaração das somas e divisão das notas
media = soma / quantidade_notas

print(f'As notas são: {notas}')
print(f'A quantidade de notas: {quantidade_notas}')
print(f'A soma de todas as notas: {soma}')
print(f'A media é: {media}')

'''
    #TODO: Situação
    Aprovado >= 7
    Recuperção >= 5 
    Reprovado
'''

#Declaração da media dos elementos
if media >= 7:
    print(f'Aprovado com media {media}')

elif media >= 5:
    print(f'Recuperação com media {media}')

else:
    print(f'Reprovado com media {media} ')
   