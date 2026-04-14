#Monitor de tráfego de rede

import psutil
import time
import os

while True:
  net1 = psutil.net_io_counters()
  time.sleep (1)
  net2 = psutil.net_io_counters()

  download = (net2.bytes_recv - net1.bytes_recv) / 1024
  upload = (net2.bytes_sent - net1.bytes_sent) / 1024

  os.system('cls' if os.name == 'nt' else 'clear')

  print(f"Download: {download:.2f} KB/s | Upload: {upload:.2f} KB/s")