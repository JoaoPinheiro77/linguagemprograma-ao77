#Monitor simples de RAM

import psutil
import time
import os

while True:
  memoria = psutil.virtual_memory()

  total = memoria.total / (1024 ** 2) #MB
  usado = memoria.used / (1024 ** 2) #MB
  livre = memoria.available / (1024 ** 2) #MB
  porcentagem_livre = memoria.available / memoria.total * 100

  os.system('cls' if os.name == 'nt' else 'clear') #Limpa a tela

  print("=== Monitor de RAM ===")
  print(f"Total: {total:.2f} MB")
  print(f"Usado: {usado:.2f} MB")
  print(f"Livre: {livre:.2f} MB ({porcentagem_livre:.2f}%)")

  time.sleep(2)