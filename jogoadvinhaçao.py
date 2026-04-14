#Jogo de adivinhação

import random

numero_secreto = random.randint(1, 100)
tentativas = 0
palpite = 0

while palpite != numero_secreto:
  palpite = int(input("Tente adivinhar o número (entre 1 e 100):"))
  tentativas += 1

  if palpite < numero_secreto:
    print("Maior!")
  elif palpite > numero_secreto:
    print("Menor!")
  else: 
    print("Acertou!")
    print(f"Tentativas: {tentativas}")