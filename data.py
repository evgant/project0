import psutil
from decor import creator


@creator("cpu_times.json")
def cpu_times():
    a = psutil.cpu_times()
    info_cpu = {"User":a[0], "System": a[1], "Idle":a[2], "Interrupt":a[3], "Dpc": a[4]}
    return info_cpu

@creator("cpu_percent.json")
def cpu_procent():
    cpu_perc = psutil.cpu_percent(interval = 1)
    return cpu_perc

@creator("cpu_count.json")
def cpu_count():
    cores = psutil.cpu_count()
    return cores

@creator("freq.json")
def freq():
    frequency = psutil.cpu_freq()[2]
    return frequency

@creator("vm_info.json")
def vm_info():
    data = psutil.virtual_memory()
    info_vm = {"Total Memory":data[0], "Available Memory":data[1], "Used Memory":data[3], "Free Memory":data[4], "Percentage Usage":data[2]}
    return info_vm

@creator("disk_usage.json")
def disk_usage():
    data = psutil.disk_usage('/')
    disk_info = {"Total Disk Memory":data[0], "Used Disk Memory":data[1], "Free Disk Memory":data[2], "Percentage Usage":data[3]}
    return disk_info

@creator("net_info.json")
def net_info():
    data = psutil.net_io_counters()
    net_info = {"Bytes Sent":data[0], "Bytes Received":data[1], "Packets Send":data[2], "Packets Received":data[3], "Errors while Receiving":data[4], "Errors while Sending":data[5], "Incoming packets droppes":data[6], "Outgoing packets dropped":data[7]}
    return net_info