# 1)Soma das idades (30 alunos)

soma = 0

for i in range (30):
  idade = int(input("Digite a idade: "))
  soma += idade

print (f"Soma das idade: {soma}")