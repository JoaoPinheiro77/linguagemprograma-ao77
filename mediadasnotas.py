# 7 - Logger de CPU

import psutil
import time
from datetime import datetime

while True:
  uso = psutil.cpu_percent(interval=1)
  agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  with open("cpu_log.txt", "a") as arquivo:
    arquivo.write(f"{agora} - CPU: {uso}%\n")

  time.sleep(5)