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

# Gets user info at its raw state
users_info = []
csv = raw_input("Enter the name of the csv : ")
csv = "Lab02_Users.csv"
read_csv(csv, users_info)

#After read, check for records that have a length greater than 7 and see if there is something to remove
print(users_info)
for user in users_info:
    if user[7] == '':
        #print(user[7])
        user.pop()
        #print(len(user))
    if len(user) > 7 and '' in user:
        print("Found empty in user: " + ','.join(user))
        user.remove("")
        #print(user)