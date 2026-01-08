import platform
import psutil
from datetime import datetime

def system_info():
    print("Systeminformationen")
    print("-------------------")
    print(f"Betriebssystem: {platform.system()} {platform.release()}")
    print(f"Hostname: {platform.node()}")
    print(f"Zeitpunkt: {datetime.now()}")
    print()

def cpu_info():
    print("CPU")
    print("---")
    print(f"Auslastung: {psutil.cpu_percent(interval=1)} %")
    print()

def memory_info():
    print("Arbeitsspeicher")
    print("---------------")
    mem = psutil.virtual_memory()
    print(f"Gesamt: {round(mem.total / (1024**3), 2)} GB")
    print(f"Belegt: {round(mem.used / (1024**3), 2)} GB")
    print(f"Frei: {round(mem.available / (1024**3), 2)} GB")
    print()

def disk_info():
    print("Festplatten")
    print("-----------")
    for disk in psutil.disk_partitions():
        usage = psutil.disk_usage(disk.mountpoint)
        print(f"{disk.device} ({disk.mountpoint}) - {round(usage.percent)} % genutzt")

if __name__ == "__main__":
    system_info()
    cpu_info()
    memory_info()
    disk_info()
