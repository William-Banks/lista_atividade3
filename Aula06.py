lista = [1,45,23,12,11,6,8,4,34,19,14]

lista.sort()
lista.sort(reverse=True)
print(f'Lista ordenada {lista}')

lista.remove(12)
lista.pop(5)
del lista[2:5]

nome = 'joão'
lista.append(nome)
print(lista)

#inserção
lista.insert(2, 'oliveira')
print(lista)

#substituição
lista[2] = 'castro'
print(lista)

print('joão' in lista)

if 'joão' not in lista:
    # esse bloco só sera executado quando a condição é  true
    print('sim, o joão esta na lista')
else:
    # esse bloco só sera executado quando a condição é  false
    print('Não, o joão não esta na lista')
