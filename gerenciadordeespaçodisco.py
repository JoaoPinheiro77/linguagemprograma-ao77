#Gerenciador de espaço em disco (todas as partições)

import psutil

print(" === Espaço em disco ===\n")

# Cabeçalho da tabela
print(f"{'Partição' : <15} {'Total (MB)':<12} {'Usado (MB)':<12} {'Livre (MB)':<12} {'Uso (%)':<8}")

for part in psutil.disk_partitions():
  try:
    uso = psutil.disk_usage(part.mountpoint)

    total = uso.total / (1024 ** 2)
    usado = uso.used / (1024 ** 2)
    livre = uso.free / (1024 ** 2)
    porcentagem = uso.percent

    print(f"{part.mountpoint:<15} {total:<12.2f} {usado:<12.2f} {livre:<12.2f} {porcentagem:<8.2f}")

  except PermissionError:
    # ignora partições sem permissão
    continue