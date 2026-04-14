# 13) Número Primo

n = int(input("Digite um número: "))
primo = True

if n <= 1:
  primo = False
else:
  for i in range(2, n):
    if n % i == 0:
      primo = False
      break

if primo:
  print("É primo")
else:
  print("Não é primo")