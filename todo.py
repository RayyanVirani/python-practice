#Making a to do list

todo_list = []

def load_tasks():
    i = 1
    with open("todo.txt", "r") as file:
        while True:
            line = file.readline()
            if line == "":
                break
            todo_list.append(line.strip())
            i = i + 1
    
#Load tasks working successfully

def save_tasks():
    with open("todo.txt", "w") as file:
        for i in range(len(todo_list)):
            file.write(todo_list[i] + "\n")

#Save tasks also working successfully

def add_task():
    
    print("Enter the task you want to add" + "\n")
    new_task = str(input("Task: "))
    todo_list.append(new_task)
    print("Task added successfully" + "\n")

def display_tasks():
    if len(todo_list) == 0:
        print("Ah, the to do list is empty lol." + "\n")
    else:
        print("This is your to do list currently" + "\n")
        for j in range(len(todo_list)):
            print(f"{j + 1}. {todo_list[j]}")

def delete_task():

    if len(todo_list) == 0:
        print("Ah, the to do list is empty lol." + "\n")
    else:
        shit = True
        while shit == True:
            print("Type the number of task you want to delete" + "\n")
            display_tasks()
            try:
                user_num = int(input("Your choice: "))
                if 1 <= user_num <= len(todo_list):
                    del todo_list[user_num - 1]
                    print("Task deleted successfully" + "\n")
                    shit = False
                else:
                    print("Invalid Number")
            except ValueError:
                print("Invalid number, enter again")

#The main running of program

load_tasks()
print("This is your to do list." + "\n")
print("The operations performed are add , view , delete , quit" + "\n")
print("Please make sure to type the correct keyword" + "\n")

while True:
    print("What operation would you like to perform?" + "\n")
    print("Type add, view, delete, quit" + "\n")

    user_choice = str(input("Your choice: "))

    if user_choice.lower() == "view":
        display_tasks()
    elif user_choice.lower() == "add":
        add_task()
    elif user_choice.lower() == "delete":
        delete_task()
    elif user_choice.lower() == "quit":
        break
    else:
        print("Invalid operation. Try again" + "\n")
    
save_tasks()