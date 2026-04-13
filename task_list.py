task_list=["coding","learning","laundry","cleaning"]
print(task_list)
task_list.append("cooking")
task_list.remove("cleaning")
print(task_list)
for i,task in enumerate(task_list):
    print(f"{i}: {task}")
    
