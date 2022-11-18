#dictionary
info = {}
#MENU
def menu():
    print("======== MENU ========")
    print("1. Add an info")
    print("2. Display the info")
    print("3. Search an item")
    print("4. Exit")
    print("======================")
menu()
def answer():
    print("==== Add an info ====")
    print("5. Full Name")
    print("6. Age")
    print("7. Address")
    print("8. Contact Number")
    print("9. Hobby")
    print("10. Course")
    print("11. Back to menu")
while True:
    #input
    select = input("What do you want to do? >> ")
#1. Add an info
    if select == "1":
        print()
        answer()
        #What do you want to add?
        add = input("What do you want to add? select from (5-10) ")
        if add == "5":
            fullname = input("What is your full name? ")
            info["Full name"] = fullname 
            print("Your info has been added")
            back = input("Do you want to add more? y/n ")
            if back == "y":
                print()
                answer()
                add = input("What do you want to add? select from (5-10) ")
            if back == "n":
                print()
                menu()
        if add == "6":
            age = input("What is your age? ")
            info["Age"] = age
            print("Your info has been added")
            back = input("Do you want to add more? y/n ")
            if back == "y":
                print()
                answer()
                add = input("What do you want to add? select from (5-10) ")
            if back == "n":
                print()
                menu()
        if add == "7":
            address = input("What is your address? ")
            print("Your info has been added")
            info["Address"] = address
            back = input("Do you want to add more? y/n ")
            if back == "y":
                print()
                answer()
                add = input("What do you want to add? select from (5-10) ")
            if back == "n":
                print()
                menu()
        if add == "8":
            contact = input("What is your contact number? ")
            info["Contact Number"] = contact
            print("Your info has been added")
            back = input("Do you want to add more? y/n ")
            if back == "y":
                print()
                answer()
                add = input("What do you want to add? select from (5-10) ")
            if back == "n":
                print()
                menu()
        if add == "9":
            hobby = input("What is your hobby? ")
            info["Hobby"] = hobby
            print("Your info has been added")
            back = input("Do you want to add more? y/n ")
            if back == "y":
                print()
                answer()
                add = input("What do you want to add? select from (5-10) ")
            if back == "n":
                print()
                menu()
        if add == "10":
            course = input("What is your course? ")
            info["Course"] = course
            print("Your info has been added")
            back = input("Do you want to add more? y/n ")
            if back == "y":
                print()
                answer()
                add = input("What do you want to add? select from (5-10) ")
            if back == "n":
                print()
                menu()
        if add == "11":
            print()
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
