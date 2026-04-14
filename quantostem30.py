# 9) Quantos têm 30 anos (turma qualquer)

contador = 0
n = int(input("Quantidade de alunos: "))

for i in range(n):
  idade = int(input("Digite a idade: "))
  if idade == 30:
    contador += 1

print(f"Quantidade de alunos com 30 anos: {contador}")