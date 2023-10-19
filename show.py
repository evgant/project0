def cpu_info(info_cpu):
    print('////////////////////////////////////////')
    print("CPU TIMES")
    for el in info_cpu:
        print(f'{el:16}' + " : " + str(f'{info_cpu[el]:0.0f}') + "s.")
    
        

def cpu_percent(cpu_perc):
    print('////////////////////////////////////////')
    print(f'CPU Utilization : {str(cpu_perc)} %')
    
def cpu_counter(cores):
    print('////////////////////////////////////////')
    print(f'Logical CPU\'s in system: {cores}')
    
def cpu_freq(frequency):
    print('////////////////////////////////////////')
    print(f'CPU Frequency: {str(frequency)} MHz.')
    
def vm_info(info_vm):
    print('////////////////////////////////////////')
    print("VIRTUAL MEMORY INFO")
    for el in info_vm:
        if el != "Percentage Usage":
            print(f'{el:16}' + " : " + str(round(info_vm[el]/1000000000, 2)) + " Gb")
        else:
            print(f'{el:16}' + " : " + str(info_vm[el]) + " %")
        
def disk_usage(disk_info):
    print('////////////////////////////////////////')
    print("DISK USAGE INFO")
    for el in disk_info:
        if el != "Percentage Usage":
            print(f'{el:17}' + " : " + str(round(disk_info[el]/1000000000, 2)) + " Gb")
        else:
            print(f'{el:17}' + " : " + str(disk_info[el]) + " %")
    
def net_inf(info_net):
    print('////////////////////////////////////////')
    print("NETWORK INFORMATION")
    for el in info_net:
        print(f'{el:25}' + " : " + str(info_net[el]))