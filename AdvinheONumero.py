from random import randint

resposta_certa = randint(0,25)

nome = input("Qual é o seu nome?")

print("Olá {} estou pensando e um número de zero a 20, tente adivinhar!!!".format(nome))

while(True):
    tantativa = int(input("Tentativa:"))

    if tantativa < resposta_certa:
        print("Maior!")

    elif tantativa > resposta_certa:
        print("Menor!")

    if tantativa == resposta_certa:
        print("Fantástico, eu estava pensando no número {}".format(resposta_certa))
        break
