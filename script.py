tList = []

def displayMenu():
    print( "\n--- Task Manager Menu ---" )
    print("1. View tasks");print("2. Add a task")
    print("3. Mark task as complete"); print("4. Delete a task")
    print( "5. Exit" )

def vwTsk():
  if len(tList) == 0:
        print("\nNo tasks found.")
        return
  print("\n--- Your Tasks ---")
  i = 0
  while i < len(tList):
     if tList[i]['c'] == True:
        s = "[X]"
     else:
         s = "[ ]"
     print(str(i + 1) + ". " + s + " " + tList[i]['n'])
     i = i + 1

def add_tsk():
   name = input("\nEnter the new task: ")
   if name == "":
      print("Task name cannot be empty.")
   else:
      tList.append({"n": name, "c": False})
      print("Task added.")

def MkCmp():
    vwTsk()
    if len(tList) > 0:
        try:
           num = input("\nEnter task number: ")
           num = int(num)
           if num >= 1 and num <= len(tList):
              tList[num - 1]['c'] = True
              print("Task marked as complete.")
           else:
              print("Invalid task number.")
        except:
           print("Please enter a valid number.")

def del_t():
  vwTsk()
  if len(tList) > 0:
     try:
        x = int(input("\nEnter task number to delete: "))
        if x >= 1 and x <= len(tList):
           print("Task '" + tList[x - 1]['n'] + "' deleted.")
           tList.pop(x - 1)
        else: print("Invalid task number.")
     except: print("Please enter a valid number.")

def run():
 print("Welcome to the Task Manager!")
 while True:
  displayMenu()
  c = input("\nChoose an option (1-5): ")
  if c == '1': vwTsk()
  if c == '2': add_tsk()
  if c == '3': MkCmp()
  if c == '4': del_t()
  if c == '5':
     print("\nExiting Task Manager. Goodbye!")
     break
  if c not in ['1','2','3','4','5']:
      print("\nInvalid choice.")

run()