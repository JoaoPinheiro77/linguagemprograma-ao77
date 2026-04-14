# 10 - Painel Completo (RAM + CPU + Disco + Rede)

import psutil
import time
import os

while True:
  #RAM
  ram = psutil.virtual_memory()
  ram_usada = ram.used / (1024**2)

  #CPU
  cpu = psutil.cpu_percent(interval=1)

  #Disco (partição principal)
  disco = psutil.disk_usage('/')
  disco_livre = disco.free / (1024**3)

  #Rede
  net1 = psutil.net_io_counters()
  time.sleep(1)
  net2 = psutil.net_io_counters()

  download = (net2.bytes_recv - net1.bytes_recv) / 1024
  upload = (net2.bytes_sent - net1.bytes_sent) / 1024

  os.system('cls' if os.name == 'nt' else 'clear')

  print ("=== Monitor Do Sistema ===\n")

  print(f"RAM: {ram.percent}% ({ram_usada:.2f} MB)")
  print(f"CPU: {cpu}%")
  print(f"Disco Livre: {disco_livre:.2f} GB")
  print(f"Download: {download:.2f} KB/s | Upload: {upload:.2f} KB/s")

  time.sleep(2)
