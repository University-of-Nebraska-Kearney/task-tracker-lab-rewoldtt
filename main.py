# Import library of functions
import file_control

def main():
  # Get tasks from file
  tasks = load_tasks()

  # Create loop for menu
  while True:
    print("---Task Tracker Menu---")
    print("1. Display tasks",
         "\n2. Add tasks",
         "\n3. Mark task as complete",
         "\n4. Save and exit")

    # Get user choice
    choice = input()

    # Navigate user based on choice
    if choice == "1":
      display_tasks(tasks)
    elif choice == "2":
      add_tasks(tasks)
    elif choice == "3":
      complete(tasks)
    elif choice == "4":
      save_tasks(tasks)
      print("Thank you for using Task Tracker.")
      break
    else:
      print("That is not a valid option.")



# Create a function called display_tasks that takes a list of taks and
# displays every task in the list.





# Create a function called add_task that takes a list of tasks, prompts
# the user for another task, and then appends the new tasks to the 
# end of the list.





# Create a function called complete that takes a lists of tasks,
# displays them to the user, and then lets the user choose one
# to mark as complete. It will then update the status of the 
# task in the list and return the updated list.



if __name__ == "__main__":
  main()
