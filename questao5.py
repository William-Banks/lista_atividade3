print(56*'=')
# Lista com os nomes dos dias da semana
print(20*'-','Dias da semana',20*'-')
lista = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
# Fase de verificação para saber se o dia está na lista
nome = (input('insira um dia da semana: '))
# Impressão mostrando se o dia está ou não na lista
if nome in lista:
    print("O nome está na lista")
else:
    print("O nome não está na lista")
print(56*'=')