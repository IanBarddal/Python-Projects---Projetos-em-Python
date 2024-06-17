import math

testes = int (input ("Digite o número de testes: "))

teste = 1

while teste <= testes:
    númeroQuestões = int(input("Digite o número de questões: "))
    linhasPergunta = int(input("Digite o número de linhas de pergunta: "))
    linhasResposta = int(input("Digite o número de linhas de resposta: "))
    linhasPágina = int(input("Digite a quantidade de linhas por página: "))

    conta1 = (linhasPágina / (linhasPergunta + linhasResposta)) 
    númeroPáginas = math.ceil(númeroQuestões / conta1)

    if númeroPáginas == 1:
        print (f"O livro terá 1 página")

    print (f"O livro terá {númeroPáginas} páginas")

    teste += 1