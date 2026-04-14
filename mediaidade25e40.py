# 10) Média idades entre 25 e 40

soma = 0
contador = 0
n = int(input("Quantidade de alunos: "))

for i in range(n):
  idade = int(input("Digite a idade: "))
  if idade > 25 and idade < 40:
    soma += idade
    contador += 1

if contador > 0:
  media = soma / contador
  print(f"Média: {media:.2f}")
else:
  print("Nenhum aluno nessa faixa")