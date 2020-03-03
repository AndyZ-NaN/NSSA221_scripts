#Andy Zhu Scripting Assignment 2

def read_csv(file_item, record_list):
    # Reads lines of data from a csv file and appends them to a list
    f = open(file_item, 'r')

    # Header is saved in a separate variable
    headers = f.readline()
    identify_headers()
    line = f.readline()
    while line:
        record = line.strip().split(',')
        record_list.append(record)
        line = f.readline()
    f.close()

#Check that all fields have information
#Check that usernames are not numeric


#Remove special characters when making username
#Create username and Check that username is unique3
def create_user():
#Create password


#Do a useradd

users_info = []
csv = raw_input("Enter the name of the csv : ")
read_csv(Lab02_Users.csv












'''
def identify_headers(header_line):
    header_line = header_line.lower()
    header_items = header_line.strip().split('
    for index in range(0,len(header_items)):

    
# MAIN
header_dict = {'employeeid':null, 'lastname': null, 'firstname': null, 'office': null, 'phone': null, 'department':null, 'group':null}
'''