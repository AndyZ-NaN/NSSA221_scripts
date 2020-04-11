#Andy Zhu Script 4

import os, subprocess, sys
from geolite2 import geolite2

'''
Greps ip addresses from the log file and sets them as dictionary values for which the keys are their occurences. Removes ip keys with a value less than or equal to 10.
'''
def get_ip_from_file(file):
    ip_dict = {}
    temp_ip_dict = {}
    ips = subprocess.check_output('grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" script_4_sample.log', shell=True)
    ips = ips.decode("utf-8")
    ip_array = ips.split("\n")
    #Removes empty ips at end of the array
    while '' in ip_array:
        ip_array.remove('')
    #Aggregates ips that are the same and counts how many are each
    for ip in ip_array:
        if ip not in temp_ip_dict.keys():
             temp_ip_dict[ip]=1
        else:
             temp_ip_dict[ip]=temp_ip_dict.get(ip)+1
    #Remove ips that have less than 11 counts
    for ip in temp_ip_dict:
        if temp_ip_dict[ip] > 10:
            ip_dict[ip] = temp_ip_dict.get(ip)

    return(ip_dict)

'''
Uses the maxminddb-geolite2 library to get GeoIP2 databases to search up locations
'''
def geolocate(ip_dict):
    reader = geolite2.reader()
    for ip in ip_dict:
        country = reader.get(ip).get('country').get('names').get('en')
        ip_dict[ip] = [ip_dict.get(ip), country]
    geolite2.close()

# MAIN #
filename = sys.argv[1]
if os.path.isfile(filename):
    print("File exists, program will execute")
    ip_list = get_ip_from_file(filename)
    geolocate(ip_list)

    file_obj = open("script_4_out.csv", "a")
    file_obj.write("Count,IP,Location\n")
    for ip in ip_list:
        print("IP '%s' from %s failed password %s times" % (ip, ip_list[ip][1], ip_list[ip][0]))
        #Output to .csv
        file_obj.write("%s,%s,%s\n" % (ip_list[ip][0], ip, ip_list[ip][1]))
    print("Output dumped to 'script_4_out.csv'. Program complete.")

else:

    print("File \"%s\" not found. Program will shutdown..." % (filename))
    exit(1)
