quantidadeCaixas = int(input("Digite a quantidade de caixas: "))

prêmio = 100
números = []

for x in range (quantidadeCaixas):
    número = int(input("Digite um número: "))
    prêmio += número
    números.append(prêmio)
    números.append(100)
    
    if prêmio < 100:
        maior = max(números)

print (números)

print (maior)