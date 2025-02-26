
"""
Program that makes a dinner guest list and prints out invitations
"""
guest_list = []

def add():
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
    
    return

def replace():
    add_num = 1
    while True:
        replace_times = int(input("How many people do you want to replace:  "))
        if replace_times <= 0:
            print("If you don't want to replace anyone in your list, then let's go back.")
            return
        else:
            for x in range(replace_times):
                guest_list.replace(input(f"Replace"))

# Greet the user
print(f"\nHi user!")
print("Wanting to hold out a dinner date at your house or anywhere?")
print("But don't know how to invite the guests?")
print(f"Well then, you are at the right spot!\n")
print("Welcome to the dinner guest list prgram!")
name = input(f"To begin, what is your name?  ").strip().capitalize()
print(f"Sup {name}! Let's make a good dinner guest list together!\n")

# Ask the user how many guests they want to invite
add()

# Show them the list
print(f"\nHere's your guest list:")
for guests in guest_list:
    print(guests)
print(f"\nThe number of people, you invited-: ")
print(len(guest_list))


# Ask the user if they want to add someone else in the list too
while True:
    choice_add = input("Forgot someone? Do you want to add anyone in the list? [y/n]:  ").strip().lower()
    if choice_add in ['y', 'n']:
        break
    print("Invalid! Enter either [y]es or [n]o.")
    continue

if choice_add == "y":
    add()
    

else:
    break

# Ask the user if they want to replace someone
while True:
    choice_replace = input("Do you want to replace anyone in the list? [y/n]:  ").strip().lower()
    if choice_replace in ['y', 'n']:
        break
    print("Invalid! Enter either [y]es or [n]o.")
    continue

if choice_replace == "y":
    replace()

elif choice_replace == "n": # Final list
    print("Here's your final guest list:")
    print(guests)
    print(f"\nThe number of people, you invited-: ")
    print(len(guest_list))

# Print out the invitations





# Goodbye
print("Thanks for using the program, hope your dinner party goes well! ")