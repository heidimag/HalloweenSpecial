import time

# Introduction
print("Welcome to the Haunted House!")
print("You find yourself in a dark room with two doors. One leads to safety, the other... to a terrifying fate.")
time.sleep(1)
print("Choose wisely!")

# Main game loop
while True:
    choice = input("\nDo you go through the LEFT door or the RIGHT door? (type 'left' or 'right'):").lower()
    
    if choice == "left":
        print("You enter a room filled with bats! They swarm around you, screeching!")
        time.sleep(1)
        print("You quickly retreat back to the first room.")
        
    elif choice == "right":
        print("You enter a silent room. In the middle of the room is a spooky ghost!")
        time.sleep(1)
        
        # Second choice
        action = input("Do you RUN or TALK to the ghost? (type 'run' or 'talk'): ").lower()
        
        if action == "run":
            print("You run back to the first room, heart pounding!")
        elif action == "talk":
            print("The ghost says 'BOO!' and disappears. You've made a friend!")
            time.sleep(1)
            print("Congratulations! You made it out of the Haunted House safely.")
            break
        else:
            print("Invalid choice! The ghost vanishes, leaving you confused.")
            
    else:
        print("Invalid choice! Please type 'left' or 'right'.")