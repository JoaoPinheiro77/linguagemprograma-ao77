#Lista de números: Maior, Menor e Média

num = int(input("Quantos números você deseja inserir?"))

#Validação
while num <= 0:
  num = int(input("Digite um número maior que 0:"))

numeros = []

for i in range(num):
  valor = float(input(f"Digite o {i+1}º número:"))
  numeros.append(valor)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média dos números: {media:.2f}")