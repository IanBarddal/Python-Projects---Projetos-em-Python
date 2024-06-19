data = input("Digite a data (AA/BB/CCCC): ")

if data[0:2] >= "13":
    print ("Padrão EUROPEU!")
elif data[3:5] >= "13":
    print ("Padrão AMERICANO!")
else:
    print ("Não é possível saber!")