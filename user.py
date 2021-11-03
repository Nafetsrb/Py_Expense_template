from PyInquirer import prompt
from csv import writer
from csv import reader

filename = 'users.csv'
user_questions = [    
    {
        "type":"input",
        "name":"name",
        "message":"Enter a unique username: ",
    },
]

#returns the list of users 
def user_list():
    users = []
    with open(filename, "r") as file:
        my_reader = reader(file, delimiter=',')
        for row in my_reader:
            users.append(row[0])
    return users

def user_list_without_input(user):
    users = []
    with open(filename, "r") as file:
        my_reader = reader(file, delimiter=',')
        for row in my_reader:
            if (user != row[0]):
                users.append({'name':row[0]})
    return users
            

# Adding a new user only if it does not exist
def csv_add(data):
    to_add = []
    with open(filename, "r") as file:
        my_reader = reader(file, delimiter=',')
        for row in my_reader:
            for (key, value) in data.items():
                if (value in row):
                    print("Username is not unique! Try again")
                    return False
    with open(filename, "a+", newline='') as file:
        csv_writer = writer(file)
        for (key, val) in data.items():
            to_add.append(val)
        # Writing new expense in file
        csv_writer.writerow(to_add)
    return True
    

def add_user():
    isAdded = False
    # Try to add a user while th ename is not unique
    while (not isAdded):
        infos = prompt(user_questions)
        isAdded = csv_add(infos)
    print("User added successfully!")
    # This function should create a new user, asking for its name
    return True