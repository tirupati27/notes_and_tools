import json
with open("database.json", "r") as file:
  task = json.load(file)
while(True):
  with open("database.json", "w") as file:
    json.dump(task, file, indent=4)
  opt=input("\n---Welcome to CLI ToDo App_©Tirupati---\n1. Add Tasks\n2. View Tasks\n3. Mark a task as Done\n4. Remove tasks\n5. Exit\nChoose an option No.: ")
  if(opt=='1'):
    n=int(input("How many tasks, do you want to add: "))
    x=1
    for i in range(1,n+1):
      task.append(input(f"Enter the Task {x}: "))
      print("Task Added Successfully !")
      x=x+1
  elif(opt=='2'):
    if(len(task)==0):
      print("You Don't have any task !")
    else:
      print("--Your_Task_List--")
      n=1
      for i in task:
        print("    ",n,". ",i, sep="")
        n=n+1
  elif(opt=='3'):
    if(len(task)==0):
      print("You Don't have any task !")
    else:
      print("--Your_Task_List--")
      n=1
      for i in task:
        print("    ",n,". ",i, sep="")
        n=n+1
      n=int(input("Enter the task Number to mark as Done!: "))
      task[n-1]=task[n-1]+"   [Done!]"
      print("The task successfully marked as Done!")
  elif(opt=='4'):
    if(len(task)==0):
      print("You Don't have any task !")
    else:
      x=int(input("How many tasks, do you want to remove: "))
      if(len(task)<x):
        print(f"You have only {len(task)} task !")
      else:
        for item in range(1,x+1):
          print("--Your_Task_List--")
          n=1
          for i in task:
            print("    ",n,". ",i, sep="")
            n=n+1
          n=int(input("Enter the task number to remove: "))
          task.pop(n-1)
          print("The task has removed !")
  elif(opt=='5'):
    break
  else:
    print("\ninvalid input\n")
