#dictionary
info = {
    "Full Name: ":"Ivonne Glynn P. Lasco",
    "Age: ":"20",
    "Address: ":"Luzon Avenue",
    "Contact Number: ":"09123456789",
    "Hobby: ":"Programming",
    "Course: ":"BS Comp. Eng.",
}
#MENU
print("=========MENU=========")
print("1. Add an info")
print("2. Search an item")
print("3. Exit")
print("======================")
#input
select = input("What do you want to do? >> ")
#1. Add an info
if select == "1":
    #display dictionary
    print()
    for key, value in info.items():
        print(key, value)
    print()
    #What do you want to add?
    add = input("What do you want to add? ")
    #add to dictionary
#2. Search an item
    #display the record
#3. Exit