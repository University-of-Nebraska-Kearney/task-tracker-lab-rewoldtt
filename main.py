# Import library of functions
import file_control

def main():
  # assign tasks as load_tasks function
  tasks = file_control.load_tasks()
  save_tasks = file_control.save_tasks(tasks)

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
      add_task(tasks)
    elif choice == "3":
      complete(tasks)
    elif choice == "4":
      save_tasks(tasks)
      print("Thank you for using Task Tracker.")
      break
    else:
      print("That is not a valid option.")



# Create a function called display_tasks that takes a list of tasks and
# displays every task in the list.
# Takes tasks as a parameter
def display_tasks(tasks):
  # Display tasks as a list, however if empty let user know
  if tasks == []:
    print("You do not have any current tasks.")
  else:
    print(tasks)

def add_task(tasks):
  # Create title for task
  title = input("What task would you like to add to your to-do list? ")
  # Create description for task
  description = input("Enter the description of the task" )
  # Create date for task
  date = input("What is the due date of the task?")
  # Create variable for if complete task or not
  complete = 'incompleted'
  # Make new task into a list with variables
  new_task = [title, description, date, complete]
  # Add new task onto tasks list
  tasks.append(new_task)
  # Return updated list
  return tasks

def complete(tasks):
  # Enter a loop until user is done marking tasks as completed
  while True:
  # Display tasks as nested list
    print(tasks)
  # Ask user which task in the nested list they would like to mark as completed
    choice = input("Which task number would you like to mark as completed? (enter 'done' to exit): ")
  # If user chooses to exit, break loop
    if choice == "done":
      print("Returning to menu...")
      break
    # Change chosen task to completed by changing 3rd index of task list to 'completed'
    # Validate user input as number
    if choice.isdigit():
      # Subtract user's choice by one for index
      index = int(choice) - 1
      # Validate that user's choice is an available task 
      if 0 <= index <= len(tasks):
        # Change to completed
        tasks[index][3] = "completed"
      # Reprompt user if not an available task number
      else:
        print("This is not a valid task number. Try again. ")
    # Reprompt user if not a digit
    else:
      print("Please enter the number of the task. ")
  # Return tasks list
  return tasks

if __name__ == "__main__":
  main()
