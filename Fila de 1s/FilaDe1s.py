número = int(input("Digite um número qualquer: "))

binário = bin(número)[2:]

print (binário)

if "0" in binário:
    print ("Ana não gosta do número.")
else:
    print ("Ana gosta desse número.")