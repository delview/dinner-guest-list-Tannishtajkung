
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




# Ask the user if they want to replace someone



# Final list



# Print out the invitations





# Goodbye