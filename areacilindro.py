# 12) Área do cilindro

raio = float(input("Raio: "))
altura = float(input("Altura: "))

pi = 3.14

area_base = pi * raio**2
area_lateral = 2 * pi * raio * altura

area_total = 2 * area_base + area_lateral

print(f"Área do cilindro: {area_total:}")