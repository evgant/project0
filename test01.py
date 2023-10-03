import psutil

a = psutil.cpu_times()
a = dict(a._asdict())


def show_cpu_info(d):
        for el in d:
            print(el + " : " + str(round(d[el])) + " s.")
            
          
print ("        CPU TIMES")
show_cpu_info(a)











"""b = psutil.virtual_memory()
b = dict(b._asdict())
c = psutil.disk_usage('/')
c = dict(c._asdict())
e = psutil.net_io_counters()
e = dict(e._asdict())"""

"""temp_cpu_info = "CPU INFO"
for i in range(len(a)):
    temp_cpu_info += str(i) + " : " + str(round(a[i])) + "s."""

"""def show_vm_info(d):
    print ("     Virtual Memory Info")
    for el in d:
        print(el)
    """
"""def show_disk_info():
    c = dict(c._asdict())
    for el in"""

"""b = list(dict.keys(a))

c = dict(c._asdict())
d = psutil.cpu_count()
e = psutil.cpu_stats()
f = psutil.cpu_freq()
g = psutil.getloadavg()"""