#TO DO LIST

todo = []
def add_one_task(title):
    new_list = todo + [title]
    #print(todo)
    #print(" - " + title)
    return new_list

def delete_task(element_to_delete):
    if element_to_delete in todo: 
        todo.remove(element_to_delete)
    else:
        print(element_to_delete + " is not in this To-Do list")
    return todo
#todo = delete_task("task1")
#print(todo)

stop = False
while stop == False:
    inputAction = input("what do you want to do?")
    #print(inputAction[0:2])
    if inputAction == "stop":
        stop = True
    elif inputAction[0:3] == "add":
        todo = add_one_task(inputAction[4:])
    elif inputAction[0:3] == "del":
        todo = delete_task(inputAction[4:])
    elif inputAction == "print":
        print(todo)
    

# save to a file todos.csv




#def print_list():

#def save_todos():
#def load_todos():