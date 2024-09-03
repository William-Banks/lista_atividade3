# A)
# Criação de lista com os nomes dos meses do ano
print(40*"=", "Meses do Ano", 40*"=","\n")
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
print(meses)

print(40*"-")

# B)
# Verificação da presença do mês de junho na lista
if "Junho" in meses:
    print("\nJunho se escontra na lista\n")
else:
    print("Junho não se encontra na lista")

print(40*"-")

# C)
# Adição do mês de abril na posição 3 e subtituição do mês na posição 6 por dezembro
meses[3] = "Abril"
meses[6] = "Dezembro"

# D)
# Remoção do último elemento da lista e impressão
meses.pop()
print(meses)

print(94*"=")