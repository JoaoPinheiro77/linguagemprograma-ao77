# 8) Soma das idades > 25

soma = 0
n = int(input("Quantidade de alunos: "))

for i in range (n):
  idade = int(input("Digite a idade: "))
  if idade > 25:
    soma += idade

print(f"Soma das idades > 25: {soma}")