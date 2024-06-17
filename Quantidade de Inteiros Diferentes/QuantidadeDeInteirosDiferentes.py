quantidade = int (input ("Digite a quantidade de números a inserir: "))

lista = set()

for x in range (quantidade):
    números = int(input("Digite os números: "))
    lista.add(números)
        
print (", ".join(map(str, lista)))
print (f"{len(lista)} números foram exibidos")
