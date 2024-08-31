def task():
      tasks=[]
      print("---Welcome to the task manager app ----")
      number_of_task=int(input("enter number of task "))

      for i in range(1,number_of_task+1):
            task_name=input(f"enter the task name {i}")
            tasks.append(task_name)
            i=i+1
      print("todays taks are ",tasks)

      while True:
            operations=int(input("Enter 1 for add \nEnter 2 for update\nEnter 3 for Delete\nEnter 4 for view\nEnter 5 for exit\n"))
            if operations==1:
                  add=input("enter a new task ")
                  tasks.append(add)
                  print(f"tasks {add} has been added")
            
            elif operations==2:
                  update=input("enter the the task that you want to update ")
                  if update in tasks:
                        up=input("enter new value : ")
                        index=tasks.index(update)
                        tasks[index]=up
                        print(f"updated taks {update} to {up}")
            elif operations==3:
                  delete=input("enter the delete task : ")
                  if delete in tasks:
                        index=tasks.index(delete)
                        del tasks[index]
                        print(f"task {delete} has been deleted ")
            
            elif operations==4:
                  print("your taks are \n",tasks)
            elif operations==5:
                  break;





task()