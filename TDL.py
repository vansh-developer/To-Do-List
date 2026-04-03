def to_do_list():
    # Intro 
    print("Welcome to To-Do list!\n")

    # Creating a empty list to store tasks
    tasks = []

    # Creating a infinite loop till the user chooses to exit.
    while True:

        # Features of the To-Do-list
        print("1. Add task")
        print("2. View task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")

        # Exception Handling if user chooses anything else than (1-5)
        try:
            user = int(input("\nChoose option (1-5): "))
        except ValueError:
            print("Error: Please choose (1-5).\n")
            continue
        
        # 1. Add task section
        if(user == 1):
            task = input("\nEnter the task: ") # Asking user 
            tasks.append({"task": task, "done" : False}) # When user first adds a task it is obviously not completed yet. So done starts as False by default.
        
        # 2. View Task section
        elif(user == 2):
            if len(tasks) == 0:
                print("No task found. Add a task first.")
            else:
                for i, task in enumerate(tasks, 1): # enumerate(iterable, start) ,  task = item and i = index 
                    if task["done"] == True:
                        status = "✅"
                    else:
                        status = " "
                    print(f"\n{i}. [{status}] {task['task']}") 
        
        # 3. Mark Task Complete Section
        elif(user == 3):
            if(len(tasks) == 0):
                print("No tasks to mark complete.") 
            else: 
                num = int(input("\nEnter task number to mark complete: "))
                if(num < 1 or (num > len(tasks))):
                    print("Invalid task number.")
                    continue
                tasks[num - 1]["done"] = True

        # 4. Delete Task Section
        elif(user == 4):
            if len(tasks) == 0:
                print("No task to delete. Add task first.")
            else:
                delete = int(input("\nEnter task number which you want to delete it: "))
                if delete < 1 or delete > len(tasks):
                    print("Invalid task number.")
                else:
                    tasks.pop(delete - 1)

        # 5. Exit Section
        elif(user == 5):
            print("\nThank You!")
            break

        else:
            print("Please choose between 1 and 5.")
        
to_do_list()
