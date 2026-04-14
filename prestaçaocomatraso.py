# 9) Prestação com atraso

valor = float(input("Valor da prestação: "))
taxa = float(input("Taxa de juros: "))
dias = int(input("Dias de atraso: "))

nova = valor + (valor * taxa * dias) / 100

print(f"Nova prestação: {nova:.2f}")