
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
    for guests in guest_list:
        print(guests) # Prints out the guest list

    print(f"\nThe number of people, you invited-: ")
    print(len(guest_list)) # Prints out the number of people in the guest list
    print("")
    return


def remove(): # Function that removes guests from the list
    remove_num = 1
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
    for guests in guest_list:
        print(guests) # Prints out the guest list

    print(f"\nThe number of people, you invited-: ")
    print(len(guest_list)) # Prints out the number of people in the guest list
    print("")
    return


def replace(): # Function that replaces a guest in the list
    replace_num = 1
    while True:
        try:
            replace_times = int(input("How many people do you want to replace:  "))
            if replace_times <= 0:
                print("If you don't want to replace anyone in your list, then let's go back.")
                return
            break
        except ValueError:
            print(f"Invalid! Enter a number\n")
            continue
        
    for x in range(replace_times):
        guest_list.replace(input(f"Replace {replace_num}:").strip().title())
        replace_num = replace_num + 1
        
    print(f"\nHere's your guest list:")
    for guests in guest_list:
        print(guests) # Prints out the guest list

    print(f"\nThe number of people, you invited-: ")
    print(len(guest_list)) # Prints out the number of people in the guest list
    print("")
        

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
        choice_remove = input("Forgot someone? Do you want to add anyone else in the list? [y/n]:  ").strip().lower()
        if choice_remove in ['y', 'n']:
            break
        print(f"Invalid! Enter either [y]es or [n]o.\n")
        continue

    if choice_remove == "y":
        remove()

    if choice_remove == "n":
        break
    
# Ask the user if they want to replace someone from the list
while True: # Loop if choice_replace is yes
    while True: # Input problem
        choice_replace = input("Do you want to replace anyone in the list? [y/n]:  ").strip().lower()
        if choice_replace in ['y', 'n']:
            break
        print(f"Invalid! Enter either [y]es or [n]o.\n")
        continue

    if choice_replace == "y":
        replace()

    elif choice_replace == "n": # Final list
        print(f"\nHere's your final guest list:")
        for guests in guest_list:
            print(guests)
        print(f"\nThe number of people, you invited-: ")
        print(len(guest_list))
        print("")
        break

# Print out the invitations





# Goodbye
print(f"Thanks for using the program, hope your dinner party goes well!\n")