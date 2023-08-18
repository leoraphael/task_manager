# =====importing libraries===========
'''This is the section where you will import libraries'''

# Compulsory Task 2:

import datetime
# https://www.w3schools.com/python/python_datetime.asp


def format_current_time():
    '''
    Formats current time in the form DD / Month / YYYYY 

    Parameter:

    Output:
    now : str
    '''

    # now = datetime.now()
    # Very funny / annoying bug :-)
    # https://stackoverflow.com/questions/19480028/attributeerror-datetime-module-has-no-attribute-strptime
    now = datetime.datetime.now()
    format_now = now.strftime("%d %b %Y")

    return format_now


def check_format_time(date_str):
    '''
    Checks if date_str is in the form DD / Month / YYYY

    Parameter:
    date_str : str

    Output:
    Bool 
    '''

    try:
        datetime.datetime.strptime(date_str, "%d %b %Y")
        return True

    except ValueError:
        return False


def user_dict():
    '''
    Reads user.txt and save name and password as a dictionary

    Parameter:

    Output:
    output : dict 
    '''

    output = {}

    with open('user.txt', 'r+', encoding='utf-8') as user:
        for line in user:

            name = line.split(", ")[0]      # Removes comma from the end
            password = line.split()[1]
            output[name] = password

    return (output)


def login(user_name, pw):
    '''
    Returns bool depending if user_name and pw is stored in user_dict()

    Parameter:

    Output:
    Bool
    '''

    user = user_dict()

    if user_name in user.keys() and pw in user.values():
        print("Successful login")
        return True

    elif user_name in user.keys() and pw not in user.values():
        print("Unsuccessful login: invalid password")
        return False

    elif user_name not in user.keys():
        print("Unsuccessful login: invalid user_name")
        return False


def print_tasks(line):
    '''
    Prints the line of string from the tasks.txt in a nice format:
    Name, Title, Description, Due Date, Current Date, Task Completion
    '''
    try:
        name, title, description, due_date, date_assigned, task_completion = line.split(
            ", ")

        print("################################")
        print("Name: ", name)
        print("Title ", title)
        print("Description: ", description)
        print("Due Date: ", due_date)
        print("Date Assigned: ", date_assigned)
        print("Task Completion: ", task_completion)

    except ValueError:
        print("Bad Formatting: Erroneous Comma Usage")


def check_comma_error(str):
    '''
    Checks for commas in the input string
    If there is, then it will cause issue in tm_add()
    '''

    if ", " in str:
        return False

    else:
        return True


def display_error(Errors):

    name_err, format_err, name_comma_err, title_comma_err, desc_comma_err = Errors

    print("\n")
    print("Printing Errors: ")

    if name_err == False:
        print("Error: Entered username is not registered yet")
        print("Please register the user first")
        print("\n")

    if format_err == False:
        print("Error: Date Invalid Format: Must be of form DD/Mon/YYYY ")
        print("\n")

    if name_comma_err == False:
        print("Error: Commas detected in Name")
        print("Please remove the comma")
        print("\n")

    if title_comma_err == False:
        print("Error: Commas detected in Title")
        print("Please remove the comma")
        print("\n")

    if desc_comma_err == False:
        print("Error: Commas detected in Description")
        print("Please remove the comma")
        print("\n")

    print("Finished printing Errors")
    print("\n")


def count(file_name):
    '''
    Counts the number of lines in a file 

    Parameter: 
    file_name : str

    Output:
    count : int 
    '''

    count = 0
    with open(file_name, 'r+', encoding='utf-8') as f:
        for line in f:
            count += 1

    return count


def task_menu(user_name):
    '''
    Goes through various options including:

    Registeration - Registers new user and password and confirms it. 
    Will store the registeration detail if 
    you are the admin, 
    and the registered name is not already contained in user.txt,
    and the password agrees with its confirmation. 

    Adding - Adds task and write it onto tasks.txt if 
    the username already exists in user.txt

    View All - View all tasks 

    View Mine - View the tasks of the user 

    Statistics - View the total number of tasks and users 

    Exit - Exits the task_menu 
    '''

    user = user_dict()
    menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    s - view statistics
    e - exit
    : ''').lower()

    if menu == 'r':

        if user_name == "admin":
            req_name = input("Please enter username to register: ")
            req_pw = input("Please enter password to register: ")
            confirm_pw = input("Please reenter password to confirm: ")

            if req_name in user.keys():
                print("Registeration failed: Username already exists")

            elif req_name not in user.keys() and req_pw == confirm_pw:

                with open('user.txt', 'a') as user:
                    user.write("\n" + req_name + ", " + req_pw)

                print("Password Confirmed")

            else:
                print("Registeration failed: password not confirmed")

        else:
            print("Registeration failed: must be admin")

        print("Ending r")
        print("\n")

    elif menu == 'a':

        name = input(
            "Please enter the username of person the task is assigned to: ")
        title = input("Please enter the title of the task: ")
        description = input("Please enter the description of the task: ")
        current_date = format_current_time()
        task_completion = "No"
        due_date = input("""Please enter the due date for the task:
        Formatted - DD/Mon/YYYY e.g. 13 Aug 2023  """)

        Errors = [name in user.keys(),
                  check_format_time(due_date),
                  check_comma_error(name),
                  check_comma_error(title),
                  check_comma_error(description)
                  ]

        if all(Errors) == True:
            task = [name, title, description, due_date,
                    current_date, task_completion]

            task_line = "\n" + ", ".join(task)  # Task must go to new line

            with open('tasks.txt', 'a') as tasks:
                tasks.write(task_line)

        else:
            display_error(Errors)

        print("Ending a")
        print("\n")

    elif menu == 'va':
        with open('tasks.txt', 'r+', encoding='utf-8') as tasks:
            for line in tasks:
                print_tasks(line)

        print("Ending va")
        print("\n")

    elif menu == 'vm':

        with open('tasks.txt', 'r+', encoding='utf-8') as tasks:
            for line in tasks:
                name = line.split(", ")[0]

                if user_name == name:
                    print_tasks(line)

                else:
                    pass

        print("Ending vm")
        print("\n")

    elif menu == 's':
        task_num = count('tasks.txt')
        user_num = count('user.txt')

        print("Total number of tasks: ", task_num)
        print("Total number of users: ", user_num)

        print("Ending s")
        print("\n")

    elif menu == 'e':
        print('Goodbye!!!')
        print("\n")
        exit()

    else:
        print("You have entered an invalid input. Please try again")
        print("\n")


def task_manager():
    '''
    Gets user_name and pw and checks if you can login
    If logged in successfully, displays all the task_menu 
    '''

    user_name = input("Please give me your login username: ")
    pw = input("Please give me your login password: ")
    login_bool = login(user_name, pw)

    while login_bool == True:
        task_menu(user_name)


#######################################
task_manager()

# NOTE: very easy to add in code. Is this sign of good prior code?
# What is a good way to compare code and update code?
# https://www.textcompare.org/python/
