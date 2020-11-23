# split names from email
from string import digits


def readFiles():
    with open("names.txt", "r") as r:
        names = r.read().splitlines()

    with open("tasks.csv", "r") as r:
        tasks = r.read().splitlines()

    return names, tasks


def binarySearch(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
        # shortens prefix so only same number of characters are compared with names list
        string = x[:len(arr[mid])].capitalize()
        comparison = arr[mid].capitalize()

        # Check if x is present at mid 
        if comparison < string: 
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif comparison > string: 
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            return mid, string
  
    # If we reach here, then the element was not present 
    return False, False;


def completeTask(task, names):
    taskSpilt = task.split(",")
    
    email = taskSpilt[0]
    originalFirstName = taskSpilt[1]
    originalLastName = taskSpilt[2]

    # removes numbers from prefix
    remove_digits = str.maketrans('', '', digits)
    prefix = email.split("@")[0].capitalize().translate(remove_digits)

    found, string = binarySearch(names, prefix)

    if found:
        newFirstName = string
        newLastName = prefix.replace(string, "").capitalize()

    if not found:
        newFirstName = newLastName = prefix

    return str(email + "," + newFirstName + "," + newLastName + "," + taskSpilt[3] + "," + taskSpilt[4] + "," + taskSpilt[5] +
                             "," + taskSpilt[6] + "," + taskSpilt[7] + "," + taskSpilt[8] + "," + taskSpilt[9] + "," + taskSpilt[10] + "," + taskSpilt[11] + "\n")



names, tasks = readFiles()
final = ""

for task in tasks:
    final += completeTask(task, names)

with open("form-done.csv", "w") as r:
    r.write(final)
