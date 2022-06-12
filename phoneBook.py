def search(persons):
    name = input("name: ")
    if name in persons:
        for value in persons[name]:
            print(f"{value}")
    else:
        print("No information regarding this person")
        
def add(persons):
    name = input("name:")
    name = name
    phoneNumber = input("number:")
    if name not in persons:
        persons[name] =[]
        persons[name].append(phoneNumber)
        print(persons[name])
        print("New person and phone number have been added!")
    elif name in persons:
        persons[name].append(phoneNumber)
        print(f"The phone number has been updated for {name}")

def delete(persons):
    name = input("name: ")
    if name in persons:
        del persons[name]
        print("Deleted")
    else:
        print("No such person found in the phone book!!")

def entireList(persons):
    for key, value in persons.items():
        print(f"Name: {key} Phone number: {value}")

def main():
    persons = {}
    print("Welcome!\nPlease follow the instructions below for utilising this phone book." )
    while True:
        cmd = input("Enter a command using one of the integers 1-5:\n 1.Search person, 2.Add person, 3.Delete person, 4.Whole list, 5.Quit program: ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            delete(persons)
        if cmd == "4":
            entireList(persons)
        if cmd == "5":
            break

        
    print("Program has ended")
    print("Thank you for using!")
    persons.clear()

main()

