# 8- Informações do processador

import psutil
import platform

print("=== CPU ===")

print("Modelo:", platform.processor())
print("Núcleos físicos:", psutil.cpu_count(logical=False))
print("Núcleos lógicos:", psutil.cpu_count(logical=True))

freq = psutil.cpu_freq()
print(f"Frequência atual: {freq.current:.2f} MHz")

# número de série (geralmente não disponível)
print("Número de série: Não disponível neste sistema")