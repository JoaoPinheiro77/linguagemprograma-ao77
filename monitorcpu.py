# 6 - Monitor de CPU

import psutil

while True:
  total = psutil.cpu_percent(interval=1)
  nucleos = psutil.cpu_percent(interval=1, percpu=True)

  print(f"CPU Totaal: {total}%")

  for i, uso in enumerate(nucleos):
    print(f"Núcleo {i}: {uso}%", end=" | ")

  print("\n")