números = []

quantidade = int(input("Digite a quantidade de números a dizer: "))

for x in range (1, quantidade+1):
    número = int (input("Digite os números: "))
    if número != 0:
        números.append(número)
    if número == 0:
        números.pop(-1)
    print (números)

print(sum(números))