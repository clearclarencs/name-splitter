#split names from email
from string import digits

with open("names.txt","r") as r:
    names = r.read().splitlines()
    names.reverse()

with open("tasks.csv","r") as r:
    tasks = r.read().splitlines()

finishedTasks = []

for task in tasks:
    tasksplt = task.split(",")
    email = tasksplt[0]
    ogfname = tasksplt[1]
    oglname = tasksplt[2]
    remove_digits = str.maketrans('', '', digits) # to remove  numbers from prefix
    prefix = email.split("@")[0].capitalize().translate(remove_digits)
    worked = False
    for name in names:
        if name in prefix:
            worked = True
            fname = name
            lname = prefix.replace(name,"").capitalize()
            break
    if not worked:
        fname = lname = prefix
    finishedTasks.append(str(email+","+fname+","+lname+","+tasksplt[3]+","+tasksplt[4]+","+tasksplt[5]+","+tasksplt[6]+","+tasksplt[7]+","+tasksplt[8]+","+tasksplt[9]+","+tasksplt[10]+","+tasksplt[11]+"\n"))

final = ""
for task in finishedTasks:
    final += task
with open("form-done.csv","w") as r:
    r.write(final)
