#Script 4

import os, subprocess, sys
from geoip import geolite2

def get_ip_from_file(file)
    ip_list = {}
    subprocess.check_output("grep -E -o \"([0-9]{1,3}[\.]){3}[0-9]{1,3}\" script_4_sample.log")


filename = sys.argv[1]
if not os.path.isfile(filename):
    print("File \[%s\] not found. Program will shutdown..." % (filename))
    exit(1)
else:
    print("File exists, program will execute")
    ip_list = get_ip_from_file(filename)