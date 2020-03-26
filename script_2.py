# Andy Zhu Scripting Assignment 2

from re import sub
import os

#Header indexes
EMPID_IND = 0
LNAME_IND = 1
FNAME_IND = 2
OFFICE_IND = 3
PHONE_IND = 4
DEPT_IND = 5
GROUP_IND = 6

def read_csv(file_item, record_list):
    # Reads lines of data from a csv file and appends them to a list
    f = open(file_item, 'r')

    headers = f.readline()
    line = f.readline()
    while line:
        record = line.strip().split(',')
        record_list.append(record)
        line = f.readline()
    f.close()
    
def has_numbers(input_str):
    return any(char.isdigit() for char in input_str)

# Formats the first/last name strings so that they can be used to create a username
def format_name(name):
    return sub('[^A-Za-z0-9]+', '', name).lower()

def shift_cells(record_list):
    for user in record_list:
        if user[7] == '':
            # print(user[7])
            user.pop()
            # print(len(user))
        if len(user) > 7 and '' in user:
            user.remove("")
            
def filter_entries(record_list, new_users):
    usernames = []
    for user in record_list:
        # New dictionary for user listing
        listing = {}
        listing["EmployeeID"] = user[EMPID_IND]
        # If any of first or last names has a non-alpha in it, chances are that the field is wrong
        if has_numbers(user[LNAME_IND]) or has_numbers(user[FNAME_IND]):
            print("CRITICAL ERROR: Employee ID %s's name record missing information. User will NOT be added" % (user[EMPID_IND]))
            # not_added.append(user)
            continue
        # Else create username for user
        else:
            listing["fullname"] = user[FNAME_IND] + " " + user[LNAME_IND]
            username = format_name(user[FNAME_IND])[0] + format_name(user[LNAME_IND])
            # Ensure no duplicate usernames
            username_count = sum(x.count(username) for x in usernames)
            if(username_count > 0):
                username = username + str(username_count)
            listing["username"] = username
            usernames.append(username)
        # Check for dept and group
        if user[DEPT_IND].strip() == '' or user[GROUP_IND].strip() == '':
            print("CRITICAL ERROR: Employee %s's department and group missing. User will NOT be added" % (user[EMPID_IND]))
            # not_added.append(user)
            continue
        # If the info is present, save to the list
        else:
            listing["department"] = user[DEPT_IND]
            listing["group"] = user[GROUP_IND]
        # Check non-critical office and phone info
        if user[OFFICE_IND].strip() == '':
            print("Employee %s's office number is missing. User will be added without this info" % (user[EMPID_IND]))
            user[OFFICE_IND] = ''
        listing["office"] = user[OFFICE_IND]
        if user[PHONE_IND].strip == "" or user[PHONE_IND] == "unlisted":
            print("Employee %s's phone number is missing. User will be added without this info" % (user[EMPID_IND]))
            user[PHONE_IND] = ''
        listing["phone"] = user[PHONE_IND]
        new_users.append(listing)
        
def create_pass(username):
    return username[::-1]

#==================================================#
#                       MAIN                       #                    
#==================================================#

users_info = []
users_to_be_added = []

# Gets user info at its raw state
csv = input("Enter the name of the csv : ")
# lol
csv = "Lab02_Users.csv"
read_csv(csv, users_info)

# After read, check for records that have a length greater than 7 and see if there is something to remove
shift_cells(users_info)
filter_entries(users_info, users_to_be_added)

# List out all users to be added to the system
for user in users_to_be_added:
    print(user)
    temp_pass = create_pass(user["username"])
    
    os.system("groupadd -f %s" % (user["group"]))
    if not os.path.exists("/home/%s" % (user["department"])):
        os.system("mkdir /home/%s" % (user["department"]))
    os.system("useradd -m -d /home/%s/%s -s /bin/bash -g %s -c \"%s\" %s" % (user["department"], user["username"], user["group"], user["fullname"], user["username"]))
    os.system("echo \"%s\" | passwd --stdin %s" % (temp_pass, user["username"]))
    os.system("passwd -e %s" % (user["username"]))
