# split names from email
from string import digits


def readFiles():
    with open("names.txt", "r") as r:
        names = r.read().splitlines()

    with open("tasks.csv", "r") as r:
        tasks = r.read().splitlines()

    return names, tasks


# splits list into 2D list, grouped into length of elements
def splitList(names):
    maxWordLength = len(max(names, key=len))
    
    lengthSeparatedList = []
    for i in range(1, maxWordLength + 1):
        lengthSeparatedList.append(list(filter(lambda x: len(x) == i, names)))

    # Will check longer less common names first
    lengthSeparatedList.reverse()
    return lengthSeparatedList

def binarySearch(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0

    # shortens prefix so only same number of characters are compared with names in list
    length = len(arr[0])
    string = x[:length].capitalize()
  
    while low <= high: 
  
        mid = (high + low) // 2
        comparison = arr[mid].capitalize()

        if string == comparison:
            return mid, string

        # Check if x is present at mid 
        if comparison < x: 
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif comparison > x: 
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            return mid, string
  
    # If we reach here, then the element was not present 
    return False, False;


def completeTask(task, separatedNames):
    taskSpilt = task.split(",")
    
    email = taskSpilt[0]
    originalFirstName = taskSpilt[1]
    originalLastName = taskSpilt[2]

    # removes numbers from prefix
    remove_digits = str.maketrans('', '', digits)
    prefix = email.split("@")[0].capitalize().translate(remove_digits)

    found = False
    for names in separatedNames:
        # Checks if list isn't empty
        if names:
            found, string = binarySearch(names, prefix)

            if found:
                newFirstName = string
                newLastName = prefix.replace(string, "").capitalize()
                break

    if not found:
        newFirstName = newLastName = prefix

    return str(email + "," + newFirstName + "," + newLastName + "," + taskSpilt[3] + "," + taskSpilt[4] + "," + taskSpilt[5] +
                             "," + taskSpilt[6] + "," + taskSpilt[7] + "," + taskSpilt[8] + "," + taskSpilt[9] + "," + taskSpilt[10] + "," + taskSpilt[11] + "\n")



names, tasks = readFiles()
separatedNames = splitList(names)
final = ""


for task in tasks:
    final += completeTask(task, separatedNames)

with open("form-done.csv", "w") as r:
    r.write(final)
