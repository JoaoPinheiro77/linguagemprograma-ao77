# Alerta de pouco espaço em disco

import psutil

limite = float(input("Defina o limite de espaço livre (%):"))

print("\n=== Partições com pouco espaço ===\n")

print(f"{'Partição':<15} {'Livre (%)':<10} {'Livre (MB)':<12}")

for part in psutil.disk_partitions():
    try:
        uso = psutil.disk_usage(part.mountpoint)

        livre_mb = uso.free / (1024**2)
        livre_percent = 100 - uso.percent

        if livre_percent < limite:
            print(f"{part.mountpoint:<15} {livre_percent:<10.2f} {livre_mb:<12.2f}")

    except PermissionError:
        continue