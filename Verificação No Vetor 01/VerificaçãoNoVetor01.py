quantidadeNúmeros = int(input("Qual a quantidade de números? "))

lista = []

for x in range (quantidadeNúmeros):
    números = int(input("Digite os números: "))
    lista.append(números)

quantidadeConsultas = int(input("Qual a quantidade de consultas? "))

for x in range (quantidadeConsultas):
    consultas = int(input("Digite o número a consultar: "))

    if consultas in lista:
        print ("Sim, está na lista.")
    else:
        print ("Não, não está na lista.")