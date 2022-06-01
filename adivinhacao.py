#cabecalho
print("-"*40)
print(" "*10, "JOGO ADIVINHAÇÃO")
print("\n            Regras do jogo")
print("\nDigite um valor inteiro positivo (1-100)")

print("-"*40)

#numero aleatório
import random as rd
aleatorio= rd.randrange(1,100)
tentativas= 1
dificuldade = int(input("Numero de tentativas:  "))
# input usuário
while tentativas-1 < dificuldade:
  print("Tentativa número:", tentativas)
  chute = int(input("Qual o número?:  "))
  if chute == aleatorio:
    print("Você acertou!!! com", tentativas, "tentativas")
    break
  if chute != aleatorio:
    tentativas+=1
    if chute > aleatorio:
      print("Você errou, digite um número menor")
    elif chute < aleatorio:
      print("Você errou, digite um número maior")
print("="*30)
print( "          Fim de jogo")
print("="*30)

