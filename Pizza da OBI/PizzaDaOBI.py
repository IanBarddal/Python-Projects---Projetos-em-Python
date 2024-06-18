qtdeAlunos = int(input("Digite a quantidade de alunos: "))
qtde8fatias = int(input("Digite a quantidade de pizzas de 8 fatias: "))
qtde6fatias = int(input("Digite a quantidade de pizzas de 6 fatias: "))

totalfatias = (qtde8fatias * 8) + (qtde6fatias * 6)

if qtdeAlunos > totalfatias:
    print ("Não sobrou pizza para ninguém")
else:
    sobra = totalfatias - qtdeAlunos
    print (f"Sobraram {sobra} fatias")