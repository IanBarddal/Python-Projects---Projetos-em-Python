alunos = int (input ("Digite o número de alunos na sala: "))

naSala = set() # Utiliza-se 'set()' para criar listas onde não pode haver repetição

for x in range (1, alunos+1):
    aluno = int(input("Digite o número do aluno"))
    naSala.add(aluno)

print(len(naSala))