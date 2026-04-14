# 5) Soma das notas (Turma qualquer)

soma = 0
n = int(input("Quantidade de alunos: "))

for i in range(n):
  nota = float(input("Digite a nota: "))
  soma += nota

print(f"Soma das notas: {soma:.2f}")