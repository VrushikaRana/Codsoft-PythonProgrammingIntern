# Command Line Application named as "To Do List Application" in which one can insert,update,delete and track desired the tasks.

print('"TO DO LIST COMMAND LINE APPLICATION"')
print(" 1.Adding or Inserting of the Task \n 2.Deleting or Removing of the task \n 3.Tracking of the desired task \n 4.Updating the task \n 5.To Exit")
choice=int(input("Enter your choice : "))

task_assigned=["Submitting Project","Reviewing Report","Meeting with Boss","Project"]

def add_task():
    add_task1=str(input("Enter the task to be added : "))
    if add_task1 not in task_assigned:
        add_task_to=task_assigned.append(add_task1)
        print("Adding or Inserting of the task is done successfully as shown below : ")
        print(task_assigned) 
    else:
        print("Task to be added is already existing")
            
def delete_task():
    print("List of the tasks : \n ",task_assigned)
    delete_task1=input("Enter the task to be deleted : ")
    if delete_task1 in task_assigned:
        delete_task_to=task_assigned.remove(delete_task1)
        print("Adding or Inserting of the task is done successfully as shown below : ")
        print(task_assigned) 
    else:
        print("Task to be deleted is not existing in the list")


def track_task():
    track_task1=input("Enter the task needed to track : ")
    if track_task1 in task_assigned:
        print("Tracking of the task is done successfully as shown below : ")
        a=task_assigned.index(track_task1)
        print("It's is presented at index ",a) 
    else:
        print("Task to be tracked is not existing in the list")
    
def update_task():
    print("List of the tasks : \n ",task_assigned)
    task1=input("Enter the task which to be updated : ")
    task2=input("Enter the value to be updated : ")
    for i in range(0,len(task_assigned)):
        if task_assigned[i]==task1:
            task_assigned[i]=task2
            print("Updating of the task at desired location is done successfully as shown below: ")
            print(task_assigned)
            
if choice == 1:
    add_task()

elif choice == 2:
    delete_task()
 
elif choice == 3:
    track_task()

elif choice == 4:
    update_task()
    
elif choice == 5:
    print("To Do List Command Line Application is Exiting!!!!")

else:
    print("Invalid Input.....\n You can try again...")
