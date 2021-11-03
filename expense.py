from PyInquirer import prompt
import PyInquirer as inquirer
from csv import writer
from user import user_list, user_list_without_input

filename = "expense_report.csv"



#Adding data to expense csv
def csv_add(data):
    to_add = []
    with open(filename, "a+", newline='') as file:
        csv_writer = writer(file)
        for (key, val) in data.items():
            to_add.append(val)
        # Writing new expense in file
        csv_writer.writerow(to_add)
    return True

def new_expense(*args):
    #Updating the questions with new users
    expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"Select a spender: ",
        "choices": user_list()
    },
    ]
    infos = prompt(expense_questions)
    while (True):
        #Doing the add for the splitted bill
        answer = input("Did you split the amount of the bill? yes/no: ") 
        if answer == "yes":
            users = [{
                "type":"checkbox",
                "name": "refund",
                "message":"Select users that needs to make a refund :",
                "choices": user_list_without_input(infos.get('spender')),
            },
            ]
            refund_users = prompt(users)
            print(refund_users)
            infos['refund'] = refund_users.get('refund')
            infos['no_refund'] = []
            print(infos)
            break
        if answer == "no":
            infos['refund'] = []
            infos['no_refund'] = []
            break
    isAdded = csv_add(infos)
    if (isAdded):
        print("New Expense Added")
    else:
        print("the Expense action failed!")
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    return True


