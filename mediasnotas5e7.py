# 11) Média notas 5 e 7

soma = 0
contador = 0
n = int(input("Quantidade de alunos: "))

for i in range(n):
  nota = float(input("Digite a nota: "))
  if nota > 5 and nota < 7:
    soma += nota
    contador += 1

if contador > 0:
  media = soma / contador
  print(f"Média: {media:.2f}")
else:
  print("Nenhuma nota nesse intervalo")