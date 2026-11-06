import os
import platform
import time

import psutil

print("HostPulse 啟動成功！")
print("操作系統：", platform.system())
print("處理器架構：", platform.machine())
print("邏輯處理器數量：", os.cpu_count())
hostname = platform.node()
short_hostname = hostname.removesuffix(".local")
print("主機名稱：", short_hostname)
memory = psutil.virtual_memory()
print("內存總量 (GiB)：", round(memory.total / (1024 ** 3), 2))
print("內存使用率：", memory.percent, "%")
disk = psutil.disk_usage("/")
print("硬盤容量(GiB)：", round(disk.total / (1024 ** 3), 2))
print("硬盤使用率：", disk.percent, "%")
cpu_usage = psutil.cpu_percent(interval=1)
print("CPU 使用率：", cpu_usage, "%")
uptime_seconds = time.time() - psutil.boot_time()
print("距離上次開機（小時）：", round(uptime_seconds / 3600, 1))