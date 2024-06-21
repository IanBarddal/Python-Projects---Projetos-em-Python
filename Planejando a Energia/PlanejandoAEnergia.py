testes = int(input("Digite a quantidade de testes: "))

for x in range (testes):
    ano1 = int(input("Digite o primeiro ano: "))
    consumoAno1 = int(input("Digite o consumo desse ano: "))
    ano2 = int(input("Digite o segundo ano: "))
    consumoAno2 = int(input("Digite o consumo desse ano: "))

    diferençaAnos = ano2 - ano1

    consumo = (consumoAno2 - consumoAno1) / (diferençaAnos)

    print (f"A taxa de crescimento do consumo foi de {consumo:.2f} GWh por ano.")