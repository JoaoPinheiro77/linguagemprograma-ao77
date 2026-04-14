# 9 - Dispositivos de Entrada e Saída

import psutil

particoes = psutil.disk_partitions()

print("=== Dispositivos de Armazenamento ===")

for i, p in enumerate(particoes):
  print(f"{i} - {p.mountpoint}")

escolha = int(input("Escolha uma partição: "))

p = particoes[escolha]
uso = psutil.disk_usage(p.mountpoint)

print("\n === Detalhes ===")
print("Partição:", p.mountpoint)
print("Total:", uso.total / (1024**3), "GB")
print("Usado:", uso.used / (1024**3), "GB")
print("Livre:", uso.free / (1024**3), "GB")