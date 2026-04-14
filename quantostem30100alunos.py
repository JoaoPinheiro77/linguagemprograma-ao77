# 3) Quantos têm 30 anos (100 alunos)

contador = 0

for i in range(100):
  idade = int(input("Digite a idade: "))
  if idade == 30:
    contador += 1

print(f"Quantidade de alunos com 30 anos: {contador}")