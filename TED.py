#Elabore um Jogo de Adivinhação, no qual o usuário deverá acertar o número escolhido pelo programa, entre 1 e 100. Regras:
#O programa deverá avisar quando o palpite estiver acima ou abaixo da resposta correta;
#Quando o usuário acertar a resposta, o programa deve informar quantas tentativas o usuário usou para alcançar o número correto.

from random import randint

print("")
numero_secreto = randint(1, 100)

print("BEM VINDO AO JOGO DA ADIVINHAÇÃO!\n")
print("Digite um número escolhido entre 1 e 100!")
print("Lembrando! Digite números e não letras!\n")
print("O número de tentativas são ilimitadas! Boa sorte!")

acertou = False
tentativa = 0

while not acertou:
    tentativa += 1
    tentativa = int(input("Digite um número: "))
    print("")

    if tentativa == numero_secreto:
        acertou = True
        print("Parabéns você acertou!\n")

    else:
        if tentativa < numero_secreto:
            print("O número que você digitou é menor que o número escolhido! Tente novamente!")
        elif tentativa > numero_secreto:
            print("O número que você digitou é maior que o número escolhido! Tente novamente!")

    if tentativa > 100:
        print("Você digitou um número maior que 100!")
        print("Lembrando! O número escolhido é entre 1 e 100!")

print("Foram feitas {} tentativas.".format(tentativa))
print("Obrigado por jogar!")
