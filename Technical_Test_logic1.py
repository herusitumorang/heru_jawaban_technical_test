#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install psutil')

import psutil
import time

def cek_status_cpu(cpu_usage):
    if cpu_usage > 90:
        return "Critical"
    elif cpu_usage >= 80:
        return "Warning"
    else:
        return "Normal"

# Simulasi monitoring loop
cpu = psutil.cpu_percent(interval=1)
status = cek_status_cpu(cpu)

print(f"Penggunaan CPU: {cpu}%")
print(f"Status Alert: {status}")

while True:
    cpu = psutil.cpu_percent(interval=1)
    status = cek_status_cpu(cpu)
    print(f"[{time.strftime('%H:%M:%S')}] CPU: {cpu}% → {status}")
    time.sleep(5)


# In[ ]:




