import data
import show


def main():
    cpu_info = data.cpu_times()
    show.cpu_info(cpu_info)
    cpu_perc = data.cpu_procent()
    show.cpu_percent(cpu_perc)
    cores = data.cpu_count()
    show.cpu_counter(cores)
    frequency = data.freq()
    show.cpu_freq(frequency)
    info_vm = data.vm_info()
    show.vm_info(info_vm)
    disk_info = data.disk_usage()
    show.disk_usage(disk_info)
    info_net = data.net_info()
    show.net_inf(info_net)
    
    
main()
