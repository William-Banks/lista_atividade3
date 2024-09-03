# Solicitação dos numeros para o usuario
print(20*'=', 'Solicitação de números', 20*'=')
num1 = int(input('Insira um numero: '))
num2 = int(input('Insira um numero: '))
num3 = int(input('Insira um numero: '))
num4 = int(input('Insira um numero: '))
# indentificação dos numeros
lista = [num1,num2,num3,num4]
lista.sort()
# Impressão dos numeros
print(f"O menor número da lista é: {lista[0]}")
print(f"O maior número da lista é: {lista[3]}")
print(63*'=')