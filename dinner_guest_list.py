
"""
Program that makes a dinner guest list and prints out invitations
"""
guest_list = []

def add(): # Function that adds guests to the list
    add_num = 1
    while True:
        try:
            add_times = int(input("How many people do you want to invite?:  "))
            if add_times <= 0:
                print(f"You need atleast 1 person in your list.\n")
                continue
            break
        except ValueError:
            print(f"Invalid! Enter a number.\n")
            continue   

    for x in range(add_times):
        guest_list.append(input(f"Guest {add_num}:  ").strip().title())
        add_num = add_num + 1

    print(f"\nHere's your guest list:")
    guest_list.sort() # Sorting the list alphabetically
    for guests in guest_list:
        print(guests) # Prints out the guest list

    print(f"\nThe number of people, you invited-: ")
    print(len(guest_list)) # Prints out the number of people in the guest list
    print("")
    return


def remove(): # Function that removes guests from the list
    remove_num = 1

    while True:
        remove_choice = input("[Press X to go back or Y to move forward]:  ").strip().title()
        if remove_choice == "X":
            print("If you don't want to remove anyone from your list, then let's go back.")
            return
        if remove_choice == "Y":
            break

    while True:
        try:
            remove_times = int(input("How many people do you want to remove?:  "))
            if remove_times <= 0:
                print(f"You need atleast 1 person in your list.\n")
                continue
            break
        except ValueError:
            print(f"Invalid! Enter a number.\n")
            continue   

    for x in range(remove_times):
        guest_list.remove(input(f"Guest {remove_num}:  ").strip().title())
        remove_num = remove_num + 1

    print(f"\nHere's your guest list:")
    guest_list.sort() # Sorting the list alphabetically
    for guests in guest_list:
        print(guests) # Prints out the guest list

    print(f"\nThe number of people, you invited-: ")
    print(len(guest_list)) # Prints out the number of people in the guest list
    print("")
    return


def replace(): # Function that replaces a guest in the list
    while True:
        replace_name = input("Who do you want to replace? [Press X to go back]:  ").strip().title()
        if replace_name == "X":
            print("If you don't want to replace anyone in your list, then let's go back.")
            return
        break
        
    replace_name2 = input(f"Replace {replace_name} with:  ").strip().title()
    replace_name == "2"
    guest_list(2) == replace_name2
        
    print(f"\nHere's your guest list:")
    guest_list.sort() # Sorting the list alphabetically
    for guests in guest_list:
        print(guests) # Prints out the guest list

    print(f"\nThe number of people, you invited-: ")
    print(len(guest_list)) # Prints out the number of people in the guest list
    print("")
        
while True:
    # Greet the user
    print(f"\nHi user!")
    print("Wanting to hold out a dinner date at your house or anywhere?")
    print("But don't know how to invite the guests?")
    print(f"Well then, you are at the right spot!\n")
    print("Welcome to the dinner guest list prgram!")
    name = input(f"To begin, what is your name?  ").strip().capitalize()
    print(f"Sup {name}! Let's make a good dinner guest list together!\n")

    # Bring out the add guests function
    add()

    # Ask the user if they want to add someone else in the list 
    while True: # Loop if choice_add is yes
        while True: # Input problem
            choice_add = input("Forgot someone? Do you want to add anyone else in the list? [y/n]:  ").strip().lower()
            if choice_add in ['y', 'n']:
                break
            print(f"Invalid! Enter either [y]es or [n]o.\n")
            continue

        if choice_add == "y":
            add()

        if choice_add == "n":
            break

    # Ask the user if they want to remove anyone from the list
    while True: # Loop if choice_remove is yes
        while True: # Input problem
            choice_remove = input("Do you want to remove anyone else from the list? [y/n]:  ").strip().lower()
            if choice_remove in ['y', 'n']:
                break
            print(f"Invalid! Enter either [y]es or [n]o.\n")
            continue

        if choice_remove == "y":
            remove()

        if choice_remove == "n": # Final list
            print(f"\nHere's your final guest list:")
            guest_list.sort() # Sorting the list alphabetically
            for guests in guest_list:
                print(guests) # Prints out the guest list
            print(f"\nThe number of people, you invited-: ")
            print(len(guest_list)) # Prints out the number of people in the guest list
            print("")
            break

        while True:
            choice = input("Do you want to change anything? [y/n]:  ").strip().title()
            if choice in ['y', 'n']:
                break
            print("Invalid! Enter either [Y]es or [N]o")
            break

        if choice == "Y":
            continue

        if choice == "N":
            break
        break
    break

# Print out the invitations
for x in range(len(guest_list)):
    print(guest_list[0]("Hi, How you doing? It's been a while, wanna get together at my house for a dinner party?"))





# Goodbye
print(f"\nThanks for using the program, hope your dinner party goes well!\n")