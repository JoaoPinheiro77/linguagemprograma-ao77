# 4) Soma das notas >= 5

soma = 0
n = int(input("Quantidade de alunos: "))

for i in range(n):
  nota = float(input("Digite a nota: "))
  if nota >= 5:
    soma += nota

print(f"Soma das notas >= 5: {soma}")