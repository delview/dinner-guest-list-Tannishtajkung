
"""
Program that makes a dinner guest list and prints out invitations
"""
guest_list = []

def add(): # Function that adds guests to the list
    add_num = 1
    while True:
        try:
            add_times = int(input(f"\nHow many people do you want to invite?:  "))
            if add_times <= 0:
                print("You need atleast 1 person in your list.")
                continue
            break
        except ValueError:
            print("Invalid! Enter a number.")
            continue   

    for x in range(add_times):
        while True:
            guest_add = input(f"\nAdd guest {add_num}:  ").strip().title()
            if guest_add in guest_list: # Checks if input is in the list
                print("Guest already in the list.")
                continue
            elif not guest_add: # Checks if input is empty
                print("Please enter a valid name.")
                continue
            else:
                guest_list.append(guest_add)
                add_num = add_num + 1
                break

    print(f"\nHere's your guest list:")
    guest_list.sort() # Sorting the list alphabetically
    for guests in guest_list:
        print(guests) # Prints out the guest list

    print(f"\nThe number of people, you invited-: ")
    print(len(guest_list)) # Prints out the number of people in the guest list
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
            remove_times = int(input(f"\nHow many people do you want to remove?:  "))
            if remove_times <= 0:
                print("You need atleast 1 person in your list.")
                continue
            break
        except ValueError:
            print("Invalid! Enter a number.")
            continue   

    for x in range(remove_times):
        while True:
            guest_remove = input(f"\nRemove guest {remove_num}:  ").strip().title()
            if guest_remove in guest_list: # Checks if input is in the list
                guest_list.remove(guest_remove)
                remove_num = remove_num + 1
                break
            else:
                print(f"{guest_remove} is not in the list.")
                continue


    print(f"\nHere's your guest list:")
    guest_list.sort() # Sorting the list alphabetically
    for guests in guest_list:
        print(guests) # Prints out the guest list

    print(f"\nThe number of people, you invited-: ")
    print(len(guest_list)) # Prints out the number of people in the guest list
    return
        
# Greet the user
print(f"\nHi user!")
print("Wanting to hold out a dinner date at your house or anywhere?")
print("But don't know how to invite the guests?")
print(f"Well then, you are at the right spot!\n")
print("Welcome to the dinner guest list prgram!")
while True:
    name = input(f"To begin, what is your name?  ").strip().capitalize()
    if not name: # Checks if input is empty
        print("You can't have 'no name', that's weird! Please enter a valid name.")
        continue
    else:
        print(f"Sup {name}! Let's make a good dinner guest list together!")
        break

while True: # Loop if choice is yes
    # Bring out the add guests function
    add()

    # Ask the user if they want to add someone else in the list 
    while True: # Loop if choice_add is yes
        while True: # Input problem
            choice_add = input(f"\nForgot someone? Do you want to add anyone else in the list? [y/n]:  ").strip().lower()
            if choice_add in ['y', 'n']:
                break
            print("Invalid! Enter either [y]es or [n]o.")
            continue

        if choice_add == "y":
            add()

        if choice_add == "n":
            break

    # Ask the user if they want to remove anyone from the list
    while True: # Loop if choice_remove is yes
        while True: # Input problem
            choice_remove = input(f"\nDo you want to remove anyone else from the list? [y/n]:  ").strip().lower()
            if choice_remove in ['y', 'n']:
                break
            print("Invalid! Enter either [y]es or [n]o.")
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
            break

    while True:
        choice = input(f"\nDo you want to change anything? [y/n]:  ").strip().lower()
        if choice in ['y', 'n']:
            break
        print("Invalid! Enter either [y]es or [n]o")
        continue

    if choice == "y":
        continue

    if choice == "n":
        break
    break

 # Print out the invitations
print(f"Here are your invitation messages-:\n")
invitation = [
    "\nHey {}, how's it going? I am hosting a dinner party at my place tomorrow and you are invited!",
    "\nHii {}, it's been a while. Let's catch up tomorrow over a wonderful dinner party at my place!",
    "\nDear {}, I hope you're doing well. You are invited to a dinner party at my place tomorrow!",
    "\nSup {}, dinner party at my place tomorrow, no excuses, you better show up!",
    "\nYo {}, I'm throwing a dinner party at my place tommorow, would love if you were there too.",
    "\nHello {}, free tommorow? I'm throwing a dinner party and you are invited!" ,
]

for i, guests in enumerate(guest_list):
    message = invitation[i % len(invitation)] # Will loop through the invitations if there are more than 6 guests in the list
    print(message.format(guests))

# Goodbye
print("")
print(f"\nThanks for using the program, hope your dinner party goes well!\n")