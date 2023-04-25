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
░█████╗░██╗░░██╗░█████╗░██████╗░████████╗███████╗██████╗░  ░░███╗░░██╗\n\
██╔══██╗██║░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ░████║░░╚═╝\n\
██║░░╚═╝███████║███████║██████╔╝░░░██║░░░█████╗░░██████╔╝  ██╔██║░░░░░\n\
██║░░██╗██╔══██║██╔══██║██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗  ╚═╝██║░░░░░\n\
╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░███████╗██║░░██║  ███████╗██╗\n\
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚══════╝╚═╝\n\
\n\
███████╗░██████╗░█████╗░░█████╗░██████╗░███████╗  ██████╗░░█████╗░░█████╗░███╗░░░███╗\n\
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔══██╗████╗░████║\n\
█████╗░░╚█████╗░██║░░╚═╝███████║██████╔╝█████╗░░  ██████╔╝██║░░██║██║░░██║██╔████╔██║\n\
██╔══╝░░░╚═══██╗██║░░██╗██╔══██║██╔═══╝░██╔══╝░░  ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║\n\
███████╗██████╔╝╚█████╔╝██║░░██║██║░░░░░███████╗  ██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║\n\
╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝  ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝\n\
\n\
\033[1;30m\
\033[3m\
Written By\n\
Derrick Martinez\n\
\n")
print("\033[1;33m\
Select an option below:\n1: Begin Story\n2: Instructions\n")

def menu_select():
    valid = False
    while not valid:
        selection = str(input("Input: "))
        if selection == "1":
            valid = True
        elif selection == "2":
            print("You must respond to prompts with valid responses in order to escape the room.\n")
        else:
            print("Please enter either '1' or '2' to continue.\n")
menu_select()

print("-------------------------")
slowprint("You wake up in a ~room~, crowded with desolation.\nThe first thing you notice is a chipped, wooden ~door~ looking down on you.\n")

def first_move():
    at_paper = False
    while not at_paper:
        door_room = str(input("Input: ")).strip().lower()
        if "door" in door_room:
            slowprint("You inspect the door and notice it's locked. It requires a key.\nMaybe take a look around the ~room~?\n")
        elif "room" in door_room:
            slowprint("You look around the room and see a soggy, torn up piece of ~paper~ on the floor.\nYou also spot a ~safe~ cowering in the corner of the room.\n")
            at_paper = True
        else:
            print("Please enter a valid response.\n")
first_move()

def decryption():
    at_trans = False
    while not at_trans:
        safe_paper = str(input("Input: ")).strip().lower()
        if "safe" in safe_paper:
            slowprint("You inspect the safe and see a keypad with an etching above it, marking 'Ψ Ω Σ Ξ Π Φ Δ Θ'.\nYou may need to find something that has writing on it. Perhaps a piece of ~paper~.\n")
        elif "paper" in safe_paper:
            slowprint("You take a look at the paper and see symbol decryptions.\nΔ = 3\nΣ = 1\nΠ = 9\nΨ = 6\nΦ = 5\nΘ = 7\nΩ = 2\nΞ = 8\nThis may be useful to unlocking something. Perhaps a ~safe~.\n")
            at_trans = True
        else:
            print("Please enter a valid response.\n")
decryption()

def unlock():
    at_key = False
    while not at_key:
        safe_code = str(input("Input: ")).strip().lower()
        if "safe" in safe_code:
            slowprint("You inspect the safe and see a keypad with an etching above it, marking 'Ψ Ω Σ Ξ Π Φ Δ Θ'.\nEnter the code.\n")
            while True:
                answer = str(input("Input: ")).strip()
                if answer == "62189537":
                    slowprint("You have unlocked the safe.\nInside you find a key.\nThis may be useful for opening a ~door~.\n")
                    break
                else:
                    slowprint("The safe beeps in denial.\nTry again.\n")
            at_key = True
        else:
            print("Please enter a valid response.\n")
unlock()

def escape():
    at_exit = False
    while not at_exit:
        door = str(input("Input: ")).strip().lower()
        if "door" in door:
            slowprint("You walk up to the door as it stands over you.\nIt looks like you need a ~key~ to unlock it.\n")
            use_key = str(input("Input: ")).strip().lower()
            if "key" in use_key:
                slowprint("You have escaped the room!\n")
                at_exit = True
        else:
            print("Please enter a valid response.\n")
escape()

time.sleep(1)
slowprint("Would you like to continue to 'Chapter 2: Abduction'?\n")

def cont():
    at_ch2 = False
    while not at_ch2:
        pick = str(input("Input: ")).strip().lower()
        if "y" in pick:
            at_ch2 = True
        elif "n" in pick:
            print("\nThanks for playing!")
            input("Press ENTER to exit.\n")
            exit()
        else:
            print("Please enter either 'yes/y' or 'no/n'.\n")
cont()

print("-------------------------")

import CH2_A