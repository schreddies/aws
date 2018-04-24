#!/usr/bin/env python

#Author: Artur Balsam
#Date: 2018 May
#Scope: General scanning script for penetration tests
#Usage: python nmap_py_1.py <ip_addr>/<netmask> <file_name_without_file_extension>, for example: "python nmap_py_1.py 192.168.1.0/24 list_of_scanned_hosts"

import sys
from datetime import datetime
from colorama import Fore
try:
    import nmap
except:
    sys.exit(Fore.RED + "[ERROR]" + Fore.RESET + "python-nmap library is required")

#starting clock for statistic
startTime = datetime.now()

#args validator
if len(sys.argv) != 3:
    sys.exit("Insert ip, mask and file name for scanning")

addr, mask = str(sys.argv[1]).split("/")
fname = str(sys.argv[2])

#scanner magic
scanner = nmap.PortScanner()

#scan: 
#-PE: ICMP echo;
#-PS: TCP SYN on 22, 80, 139, 443, 335, 3389;
#-sn: Ping Scan - disable port scan;
#-n: Never do DNS resolution.
scanner.scan(hosts='{0}/{1}'.format(addr,mask), arguments='-PE -PS22,80,139,443,445,3389 -sn -n')

#printing and saving to file 
hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
for host, state in hosts_list:
    print('{0}'.format(host))
    with open('{0}.txt'.format(fname), 'a') as file:
    	#file.write('\n')
    	file.write('{0}'.format(host)) 
        file.write('\n')

#closing file
file.close()

#time printing for comparison with nmap scan can be removed
print(Fore.BLUE + "[TIME]:" + Fore.RESET)
print(datetime.now()- startTime)

#system exit
sys.exit(0)
