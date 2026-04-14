# 2) Média das idades (50 alunos)

soma = 0

for i in range (50):
  idade = int(input("Digite a idade: "))
  soma += idade

media = soma / 50
print(f"A média das idades é: {media:.2f}")