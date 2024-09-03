# A)
# Criação e impressão da lista inicial
lista = [5,8,2,9,1]
print(lista)

# B)
# Ordenação da lista em ordem crescente e impressão
lista.sort()
print(lista)

# Ordenação da lista em ordem descrescente e impressão
lista.sort(reverse=True)
print(lista)

# C)
# Adição do número 7 ao final da lista
lista.append(7)
print(lista)

# Adição do número 3 na posição 2
lista.insert(2, 3)
print(lista)

# D)
# Substituição do item de índice 1 por 10 e remoção do número 9
lista[1] = 10
lista.remove(9)
print(lista)

# E)
# Remoção dos items de índice 2 até 4
del lista[2:4]
print(lista)