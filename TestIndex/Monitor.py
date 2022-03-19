# -*- coding:utf-8 -*-

# 导入psutil
import psutil
import time

'''
    cpu性能监控脚本
'''
print(" Cpu使用率  内存使用率   C盘使用率")
delay = 3
while True:
    # 监控cpu数量
    # print(psutil.cpu_count())
    time.sleep(delay)
    # 监控cpu百分比
    print(str(psutil.cpu_percent()) + "%     " + str(psutil.virtual_memory().percent) + "%    " + \
          str(psutil.disk_usage("C:\\").percent) + "%   " )
    # 监控虚拟内存
    # print(psutil.virtual_memory().percent)
    # print(psutil.disk_usage("C:").percent)
    # print(psutil.disk_usage("D:").percent)
    # print(psutil.disk_usage("E:").percent)

