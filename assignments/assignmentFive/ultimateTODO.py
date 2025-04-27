# Riley Ahlrichs            4-16-2025
# Assignment 5: Use a provided python file and update the different functions marked with TODO in order to create my UltimateTODO list. 
# This will help me keep track of everyday tasks as well as organize the different tasks as I am working through them by tracking
# whether they are in progress or have been completed. I can also save lists, create new ones as needed, move items to new lists
# and delete items from lists as they have been finished. 
import sys
import pickle

def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print("The Ultimate TODO List!")
    print()

    print("By: Riley Ahlrichs")
    print("[COM S 127 Section 1]")
    print()

def initList():
    """Create a Dictionary of Lists - this is the primary data structure for the script.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def checkIfListEmpty(todoList):
    """This function checks if there are any entries in the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean: If there is at least one item in the data structure, return False - it is not empty. Otherwise return True.
    """
    if (len(todoList["backlog"]) > 0 or 
        len(todoList["todo"]) > 0 or
        len(todoList["in_progress"]) > 0 or
        len(todoList["in_review"]) > 0 or
        len(todoList["done"]) > 0):
        return False
    return True

def saveList(todoList):
    """Allows the user to save their data to a binary file.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    """Allows the user to load their data from a binary file.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList):
    """This function iterates through all the keys in the dictionary, and checks each list to see if a key is present.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, String, Integer: This function returns True/ False depending on whether the item was found, the String of the keyName, and the index in the list where the item was found.
    """
    # Keep these default values if the item is not found in any of the lists in the dictionary
    itemFound = False
    keyName = ""
    index = -1

    for key, items in todoList.items():
        # Iterate through each item in the dictionary associated with the current key
        if item in items:
            itemFound = True
            keyName = key
            index = items.index(item)
            break  # Exit the loop once the item is found
    return itemFound, keyName, index

def addItem(item, toList, todoList):
    """This function allows the user to add an item to a specific list in the todoList data structure.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    # Check if the item already exists using checkItem
    itemFound, keyName, index = checkItem(item, todoList)
    
    if itemFound:
        # If found, print an error message
        print(f"Error: '{item}' already exists in the list '{keyName}' at index {index}.")
    else:
        # If not found, add the item to the correct list in the specified 'toList'
        if toList in todoList:
            todoList[toList].append(item)
        else:
            # If the list doesn't exist, optionally create it
            print(f"Warning: '{toList}' not found in todoList. Creating new list.")
            todoList[toList] = [item]
    return todoList

def deleteItem(item, todoList):
    """This function allows the user to delete an item in the todoList data structure.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, Dictionary of Lists: This function returns True/ False depending on whether the item was found, and the modified Dictionary of Lists data structure.
    """
    # Check if the item already exists using checkItem
    itemFound, keyName, index = checkItem(item, todoList)

    if itemFound:
        # Remove the item from the appropriate list if found
        todoList[keyName].pop(index)
    else:
        # Print error message if item not found
        print(f"Error: '{item}' not found in any list.")
    return itemFound, todoList

def moveItem(item, toList, todoList):
    """This function allows the user to move an item from one List in the Dictionary of Lists to another.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    # Try to delete the item first
    itemFound, todoList = deleteItem(item, todoList)

    if itemFound:
        # If it was found and deleted, add it to the new list
        todoList = addItem(item, toList, todoList)
    return todoList

def printTODOList(todoList):
    """This function prints out the contents of the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return None: After printing out the contents of the Dictionary of Lists data structure, we are explicitly returning 'None.'
    """
    for key, items in todoList.items():
        print(f"{key}: {items}")
    return None

def runApplication(todoList):
    """This function provides the primary funcionality for the application. It allows the user to add items to the data structure, move items,
    delete items, save the data structure to a binary file, and return to the main menu.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":
            item = input(str("Enter an item to add to the backlog: "))
            todoList = addItem(item, "backlog", todoList)
            printTODOList(todoList)
        elif choice == "m":
            if not checkIfListEmpty(todoList):
                item = input(str("Enter the item you want to move: "))
                itemFound, _, _ = checkItem(item, todoList)

                while not itemFound:
                    print(f"Error: '{item}' not found.")
                    item = input(str("Please enter a valid item to move: "))
                    itemFound, _, _ = checkItem(item, todoList)

                toList = input("Enter the category to move the item to: ")
                while toList not in todoList:
                    print(f"Error: '{toList}' is not a valid category.")
                    toList = input("Enter a valid category to move the item to: ")

                todoList = moveItem(item, toList, todoList)
            else:
                print("No items to move!")

            printTODOList(todoList)
        elif choice == "d":
            if not checkIfListEmpty(todoList):
                item = input(str("Enter the item you want to delete: "))
                _, todoList = deleteItem(item, todoList)
            else:
                print("No items to delete!")

            printTODOList(todoList)
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    """This is the main() function for the program. It contains all of the initial choices the user can make. These choices include:
    - Starting a new Dictionary of Lists.
    - Loading a previously saved Dictionary of Lists.
    - Quitting the script altogether.
    """
    taskOver = False

    printTitleMaterial()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()