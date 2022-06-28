import platform
import psutil

#need to install
#pip install psutil


#systeminfo
pcname = platform.node()
print("[*] Computer Network name:",pcname )

machinetype = platform.machine()
print("[*] Machine Type:",machinetype) 

processortype = platform.processor()
print("[*] Processor Type:",processortype)

platformtype = platform.platform()
print("[*] Platform Type :",platformtype)

opersys = platform.system()
print("[*] Operating System :",opersys)

opersysreal = platform.release()
print("[*] OperationgStstem release :",opersysreal)

opersysver = platform.version
print("[*] Operationg System Version :",opersysver)

#CPU usage
physicalcore = psutil.cpu_count(logical=False)
print("[*] Number of Physical Core :",physicalcore)

logicore = psutil.cpu_count(logical=True)
print("[*] Number of Logical Core :",logicore)

currentcpu = psutil.cpu_freq().current
print("[*] Current CPU frequemcy :",currentcpu)

maxcpu = psutil.cpu_freq().max
print("[*] Max CPU frequemcy :",maxcpu)

mincpu = psutil.cpu_freq().min
print("[*] Min CPU frequemcy :",mincpu)

cpuuti = psutil.cpu_percent(interval=1)
print("[*] Current CPU utilization :",cpuuti)

per_cpu = psutil.cpu_percent(interval=1, percpu = True)
print("[*] Current Per-CPU utilization :",per_cpu)

#ram

ramins = (round(psutil.virtual_memory().total/1000000000, 2))
print("[*] Total Ram Installed :",ramins)

availram = (round(psutil.virtual_memory().available/1000000000, 2))
print("[*] Available RAM :",availram)

useram = (round(psutil.virtual_memory().used/1000000000, 2))
print("[*] Used Ram :",useram)

ramuse = (psutil.virtual_memory().percent)
print("[*] Ram usage in Percent:",ramuse)








