#Andy Zhu Scripting Assignment 2

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

#Check that all fields have information
#Check that usernames are not numeric


#Remove special characters when making username
#Create username and Check that username is unique
def create_user():
    return 0

EMPID_IND = 0
LNAME_IND = 1
FNAME_IND = 2
OFFICE_IND = 3
PHONE_IND = 4
DEPT_IND = 5
GROUP_IND = 6

users_info = []
not_added = []
added = []

# Gets user info at its raw state
csv = raw_input("Enter the name of the csv : ")
csv = "Lab02_Users.csv"
read_csv(csv, users_info)

#After read, check for records that have a length greater than 7 and see if there is something to remove
for user in users_info:
    if user[7] == '':
        #print(user[7])
        user.pop()
        #print(len(user))
    if len(user) > 7 and '' in user:
        print("Found empty in user: " + ','.join(user))
        user.remove("")
        #print(user)        

print(users_info)

#Check if EMPID even exists

#Check if first name is alphas non-numeric only
for user in users_info:
    #If any of first or last names has a non-alpha in it, chances are that the field is wrong
    if not (user[LNAME_IND].isalpha() and user[FNAME_IND].isalpha()):
        print("There is an error with employee ID %s's name record. User not added" % (user[EMPID_IND]))
        not_added.append(user)
        continue
    #Else create username for user
    else:
        username = user[FNAME_IND][0] + user[LNAME_IND]
        #Check if new username is a dupe
        username_count = sum(x.count(username) for x in added)
        if(username_count > 0):
            username = username + str(username_count)
    #Check for dept and group
    if user[DEPT_IND].strip() == '' or user[GROUP_IND].strip() == '':
        print("There is critical information regarding the Employee %s's department and group missing. User not added" % (user[EMPID_IND]))
        not_added.append(user)
        continue
    #If the info is present, save to the list
    else:
        dept = user[DEPT_IND]
        group = user[GROUP_IND]
    #Check non-critical office and phone info
    if user[OFFICE_IND].strip() == '' or user[PHONE_IND].strip == '' or user[PHONE_IND] == "unlisted":
        print("Employee %s's office and phone numbers are missing. User will be added without this info" % (user[EMPID_IND]))
        office = ''
        phone = ''
    else:
        office = user[OFFICE_IND]
        phone = user[PHONE_IND]
    added.append([username, office, phone, dept, group])

for line in not_added:
    print(line)
print("ADDED:")
for line in added:
    print(line)