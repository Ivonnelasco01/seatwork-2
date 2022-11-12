#dictionary
info = {
    "Full Name":"Ivonne Glynn P. Lasco",
    "Age":"20",
    "Address":"Luzon Avenue",
    "Contact Number":"09123456789",
    "Hobby":"Programming",
    "Course":"BS Comp. Eng.",
}
#MENU
def menu():
    print("======== MENU ========")
    print("1. Add an info")
    print("2. Display the info")
    print("3. Search an item")
    print("4. Exit")
    print("======================")
menu()
while True:
    #input
    select = input("What do you want to do? >> ")
#1. Add an info
    if select == "1":
        #display dictionary
        print()
        print("== Here is the info ==")
        for key, value in info.items():
            print(key, ":",value)
        print()
        #What do you want to add?
        add = input("What do you want to add? ")
        input_add = input("Fill up your info: " +add+ " >> ")
        #add to dictionary
        info[add] = input_add
        print()
        print("Your info has been added.")
        menu()
#2. Display info
    if select == "2":
        print()
        print("== Info has been displayed ==")
        print("       Here is the info      ")
        for key, value in info.items():
            print(key, ":",value)
        print()
        menu()
#3. Search an item
    if select == "3":
        search = input("What do you want to search? ")
    #display the record
        if search in info:
            print()
            print("== There is existing one ==")
            print(search,": ",info.get(search))
            menu()
    #not exist
        if search not in info:
            print()
            print("There is not existing one, search another!")
            print()
            menu()
#4. Exit
    if select == "4":
        exit = input("Are you sure you want to exit? y/n ")
        if exit == "y":
            break
        if exit == "n":
            print()
            menu()
