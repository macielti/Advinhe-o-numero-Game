#inportando função para gerar numeros aleatorios
from random import randint

#gero um numero aleatorio o guardo
resposta_certa = randint(0,25)

#leio o nome do jogador
nome = input("Qual é o seu nome?")

#limpo a entrada para ter certeza de que não contenha excesso de espaços
nome = nome.strip()

#contatdor de tantaivas
tentativas = 0

print("Olá {} estou pensando e um número de zero a 20, tente adivinhar!!!".format(nome))

while(True):

    #quantidade maxima de tentativas
    if tentativas > 6:
        print("Tentativas Esgotadas!!")
        break

    #leio a tentativa de respota
    tantativa = int(input("Tentativa:"))

    if tantativa < resposta_certa:
        print("Maior!")
        tentativas +=1

    elif tantativa > resposta_certa:
        print("Menor!")
        tentativas +=1

    if tantativa == resposta_certa:
        print("Fantástico, eu estava pensando no número {}".format(resposta_certa))
        break
