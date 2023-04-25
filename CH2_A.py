from os import system, name
import time
import sys
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/64)

print("DISCLAIMER: It is recommended that you do not resize the terminal at any point within gameplay.\n\
If you wish to adjust the window size, do so now. Thank you.\n")
time.sleep(2)
input("Press ENTER to begin.")
def clear():
    if name == 'nt':
        _ = system('cls')
clear()

print("\033[0;31m\
░█████╗░██╗░░██╗░█████╗░██████╗░████████╗███████╗██████╗░  ██████╗░██╗\n\
██╔══██╗██║░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ╚════██╗╚═╝\n\
██║░░╚═╝███████║███████║██████╔╝░░░██║░░░█████╗░░██████╔╝  ░░███╔═╝░░░\n\
██║░░██╗██╔══██║██╔══██║██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗  ██╔══╝░░░░░\n\
╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░███████╗██║░░██║  ███████╗██╗\n\
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚══════╝╚═╝\n\
\n\
░█████╗░██████╗░██████╗░██╗░░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗\n\
██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║\n\
███████║██████╦╝██║░░██║██║░░░██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║\n\
██╔══██║██╔══██╗██║░░██║██║░░░██║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║\n\
██║░░██║██████╦╝██████╔╝╚██████╔╝╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║\n\
╚═╝░░╚═╝╚═════╝░╚═════╝░░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝\n\
\n\
\033[1;30m\
\033[3m\
Written By\n\
Derrick Martinez\n\
\n")
print("\033[1;33m\
Select an option below:\n1: Continue Story\n2: Instructions\n")

def menu_select():
    valid = False
    while not valid:
        selection = str(input("Input: "))
        if selection == "1":
            valid = True
        elif selection == "2":
            print("You must respond to prompts with valid responses in order to reach the end of the hall.\n")
        else:
            print("Please enter either '1' or '2' to continue.\n")
menu_select()

print("-------------------------")
slowprint("\
Upon exiting the room, a long hallway stretches long before you.\n\
Within the fading darkness, you make out two doors.\n\
Each to your ~left~ and to your ~right~.\n")

def first_move():
    at_room2 = False
    while not at_room2:
        left_right = str(input("Input: ")).strip().lower()
        if "left" in left_right:
            slowprint("You notice that the the door is fastened by large, rusty chains held together by a padlock.\n\
Maybe try the door to the ~right~?\n")
        elif "right" in left_right:
            slowprint("The hinges barely hold on to the door, but you managed to carefully open it.\n\
The room's pungent must causes your breathing to become sluggish and burdensome.\n\
You scan the room and find a ~hairpin~ on top of a ~drawer~.\n")
            at_room2 = True
        else:
            print("Please enter a valid response.\n")
first_move()

def get_code():
    at_password = False
    while not at_password:
        drawer_pin = str(input("Input: ")).strip().lower()
        if "drawer" in drawer_pin:
            slowprint("You search the drawer thoroughly and find a note.\n\
Written on it is a message that instructs:\n\
'Starting from 0, go to 8, then 3, then 12, then 7, then back to 12.'\n\
This may be a sequence for unlocking a ~padlock~.\n")
            at_password = True
        elif "hairpin" in drawer_pin:
            slowprint("You pick up the hairpin and decide to try picking the padlock on the door to the left.\n\
Unfortunately, you don't know how to pick locks.\n\
Perhaps the ~drawer~ has something more useful for you.\n")
        else:
            print("Please enter a valid response.\n")
get_code()

def lock():
    at_lock = False
    while not at_lock:
        code_padlock = str(input("Input: ")).strip().lower()
        if "padlock" in code_padlock:
            slowprint("You kneel in front of the padlock that gatekeeps the door to the left.\n\
You must enter the combination chronologically using '<' and '>' in order to go from number to number.\n")
            at_lock = True
        else:
            print("Please enter a valid response.\n")
lock()

def unlock():
    at_unlock = False
    while not at_unlock:
        answer = str(input("Input: ")).strip()
        if ">>>>>>>><<<<<>>>>>>>>><<<<<>>>>>" == answer:
            slowprint("The padlock clicks open and drops dead to the ground as if hanging on the chain link was debilitating.\n\
You unwind the chains as the door creaks open.\n\
Peeping into the suprisingly lit and organized room, you see a ~toolbox~ awkwardly standing in the center.\n")
            at_unlock = True
        else:
            slowprint("The padlock resets.\n\
Take a look at the pattern once more.\n\
Then, make another attempt.\n")
unlock()

def flashlight():
    at_tool = False
    while not at_tool:
        open_toolbox = str(input("Input: ")).strip().lower()
        if "toolbox" in open_toolbox:
            slowprint("You lift the hood of the toolbox and find only a ~flashlight~.\n\
With some light, you could feasibly discover what remains of the barren ~hall~.\n")
            at_tool = True
        else:
            print("Please enter a valid response.\n")
flashlight()

def discovery():
    at_hall = False
    while not at_hall:
        walk_to = str(input("Input: ")).strip().lower()
        if "flashlight" in walk_to:
            slowprint("You take a look at the flashlight in your possession.\n\
It looks like it's built to be resilient.\n\
It is exactly what you need for the long, dark ~hall~ right outside.\n")
        elif "hall" in walk_to:
            slowprint("You step out of the cleanly room, back into the heavy, humid environment that resides within the rest of the facility.\n\
You turn on your newly obtained flashlight and see that there's a highly reflective ~thing~ hanging from the ceiling.\n")
            at_hall = True
        else:
            print("Please enter a valid response.\n")
discovery()

def end():
    at_end = False
    while not at_end:
        inspect_thing = str(input("Input: ")).strip().lower()
        if "thing" in inspect_thing:
            slowprint("You go to inspect the thing, it's a.aaa.a.a.aa...a")
            at_end = True
        else:
            print("Please enter a valid response.")
end()

time.sleep(5/2)

def jumpscare():
    message = "\033[0;31m\033[3mBEHIND YOU"
    amount = 0
    while amount < 24:
        print(message)
        amount += 1
        time.sleep(1/32)
jumpscare()

import smile_scare