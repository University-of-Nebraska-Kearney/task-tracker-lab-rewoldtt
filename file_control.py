# Create a function called load_tasks that reads tasks from a file
# into a list and then returns the list.
def load_tasks():
  # open file to read tasks
  tasks = []
  try:
    with open("list.txt", 'r') as f:
      file_tasks = f.readline()
      # Turn tasks from separated strings back into a nested list
      tasks = [group.split(", ") for group in file_tasks.split("; ")]
  except FileNotFoundError:
    return []
  return tasks



# Create a function called save_tasks that takes a list of tasks and 
# writes them to a file for long non-volatile storage.
def save_tasks(tasks):
  # turn each task into a string
  tasks_as_string = "; ".join([", ".join(task) for task in tasks])

  # write updated tasks into file
  with open("list.txt", 'w') as f:
    f.write(tasks_as_string)
