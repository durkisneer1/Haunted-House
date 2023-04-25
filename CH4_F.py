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
░█████╗░██╗░░██╗░█████╗░██████╗░████████╗███████╗██████╗░  ░░██╗██╗██╗\n\
██╔══██╗██║░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ░██╔╝██║╚═╝\n\
██║░░╚═╝███████║███████║██████╔╝░░░██║░░░█████╗░░██████╔╝  ██╔╝░██║░░░\n\
██║░░██╗██╔══██║██╔══██║██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗  ███████║░░░\n\
╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░███████╗██║░░██║  ╚════██║██╗\n\
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░░░░░╚═╝╚═╝\n\
\n\
███████╗██████╗░░█████╗░░█████╗░████████╗██╗░░░██╗██████╗░███████╗\n\
██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██╔══██╗██╔════╝\n\
█████╗░░██████╔╝███████║██║░░╚═╝░░░██║░░░██║░░░██║██████╔╝█████╗░░\n\
██╔══╝░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░\n\
██║░░░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░╚██████╔╝██║░░██║███████╗\n\
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝\n\
\n\
\033[1;30m\
\033[3m\
Written By\n\
Derrick Martinez\n\
\n")
print("\033[1;33m\
Select an option below:\n1: Continue Story\n2: Instructions\n")

T = time.sleep(1)

def menu_select():
    valid = False
    while not valid:
        selection = str(input("Input: "))
        if selection == "1":
            valid = True
        elif selection == "2":
            print("You can't fix this.")
            T
            slowprint("\033[1;34mSo let me help you.\033[1;33m\n")
        else:
            print("Please enter either '1' or '2' to continue.\n")
menu_select()

print("-------------------------")

slowprint("You reach the bottom floor of wherever you are at.")
T
slowprint("The room before you is somehow darker and thicker than where you came from.")
T
slowprint("Barely visible, a lightswitch bleakily sits on the wall parellel to you.")
time.sleep(2)
slowprint("Walk.")
input()