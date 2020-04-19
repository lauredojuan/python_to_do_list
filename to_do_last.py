to_do = []


def add_one_task(title):
    new_list = to_do + [title]
    return new_list


def delete_task(element_to_delete):
    if element_to_delete in to_do:
        to_do.remove(element_to_delete)
        print(element_to_delete +" deleted from the list.")
    else:
        print(
            element_to_delete +
            " is not in this To-Do list, you can type print to see all tasks currently stored in this list."
        )
    return to_do

stop = False
while stop == False:

    inputAction = input("what do you want to do?")

    if inputAction == "stop":
        stop = True

    elif inputAction[0:3] == "add":
        if inputAction[3:4] != " ":
          print("error: leave one space after command 'add'")
        elif inputAction[4:] == "":
          print("please enter task to add to de the list")
        elif inputAction[4:] == " ":
          print("'"+inputAction[4:]+"'"+" added to the list.")
          to_do = add_one_task(inputAction[4:])

    elif inputAction[0:3] == "del":
        if inputAction[3:4] != " ":
          print("error: leave one space after command 'del'")
        elif inputAction[4:] == "":
            print("please enter task to add to de the list")
       
    elif inputAction[0:5] == "print":
        print("printed: " + inputAction[6:])
    else:
        print("Unknown command, accepted commands are: del, add, print, stop.")