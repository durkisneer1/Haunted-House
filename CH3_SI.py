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
██║░░╚═╝███████║███████║██████╔╝░░░██║░░░█████╗░░██████╔╝  ░█████╔╝░░░\n\
██║░░██╗██╔══██║██╔══██║██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗  ░╚═══██╗░░░\n\
╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░███████╗██║░░██║  ██████╔╝██╗\n\
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░╚═╝\n\
\n\
░██████╗██████╗░██╗████████╗████████╗██╗███╗░░██╗░██████╗░  ██╗███╗░░░███╗░█████╗░░██████╗░███████╗\n\
██╔════╝██╔══██╗██║╚══██╔══╝╚══██╔══╝██║████╗░██║██╔════╝░  ██║████╗░████║██╔══██╗██╔════╝░██╔════╝\n\
╚█████╗░██████╔╝██║░░░██║░░░░░░██║░░░██║██╔██╗██║██║░░██╗░  ██║██╔████╔██║███████║██║░░██╗░█████╗░░\n\
░╚═══██╗██╔═══╝░██║░░░██║░░░░░░██║░░░██║██║╚████║██║░░╚██╗  ██║██║╚██╔╝██║██╔══██║██║░░╚██╗██╔══╝░░\n\
██████╔╝██║░░░░░██║░░░██║░░░░░░██║░░░██║██║░╚███║╚██████╔╝  ██║██║░╚═╝░██║██║░░██║╚██████╔╝███████╗\n\
╚═════╝░╚═╝░░░░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝\n\
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
            print("You must respond to prompts with valid responses in order to...")
            time.sleep(2)
            slowprint("Hm... ")
            time.sleep(3/2)
            slowprint("You will follow it.\n")
        else:
            print("Please enter either '1' or '2' to continue.\n")
menu_select()

print("-------------------------")

time.sleep(1)
slowprint("I don't know anymore.\n")
time.sleep(1)
slowprint("You may proceed down the ~hall~.")
time.sleep(1)
slowprint("Or you can just ~stand~ there.\n")


def first_move():
    at_outhall = False
    while not at_outhall:
        hall_stand = str(input("Input: ")).strip().lower()
        if "stand" in hall_stand:
            slowprint("You stand there.\n\
Processing what just happened.\n")
            time.sleep(1)
            slowprint("Yield ~onward~, whenever you are ready.\n")
        elif "hall" in hall_stand or "onward" in hall_stand:
            slowprint("The hall seems to never end.\n\
Even with your flashlight, you cannot see past the void of darkness.\n\
Regardless, you take precarious steps into the hall, still in immense shock.\n")
            time.sleep(1)
            slowprint("Enter however many steps you'd like to take forward.\n")
            at_outhall = True
        else:
            print("Please enter a valid response.\n")
first_move()

def person():
    at_person = False
    amount = 0
    while not at_person:
        while True:
            try:
                amount += int(input("Input: "))
            except ValueError:
                print("Please enter a number.")
            else:
                break
        if amount < 32:
            slowprint("Your flashlight reveals nothing.\n\
Walk further.\n")
        elif amount >= 32:
            slowprint("Stop.\n")
            time.sleep(2)
            slowprint("A person stands upended at the end of the hall with its back turned towards you.\n\
You can't make out its features but can notice its unusually long limbs and very inhuman sillouette.\n")
            time.sleep(1)
            slowprint("Do you want to try to get its attention by flickering your ~flashlight~?\n\
Or you can try approaching it for a closer ~look~.\n")
            at_person = True
person()

def inspect():
    gone = False
    while not gone:
        light_look = str(input("Input: ")).strip().lower()
        if "light" in light_look:
            slowprint("You flicker your flashlight at it.")
            time.sleep(1)
            slowprint("It doesn't react.")
            time.sleep(1)
            slowprint("~Approach~ it.")
        elif "look" in light_look or "approach" in light_look:
            slowprint("You slowly creep up to it but get distracted by quick, light footsteps rapidly approaching you from behind.")
            time.sleep(2)
            slowprint("You look back and the footsteps stop.")
            time.sleep(2)
            slowprint("You intently search for the source with your light, but can't find anything.")
            time.sleep(2)
            slowprint("You decide to shrug it off and look back at the creature.")
            time.sleep(3)
            slowprint("It's bleeding.")
            time.sleep(1)
            gone = True
        else:
            print("Please enter a valid response.\n")
inspect()

def creep():
    message = "I'm bleeding."
    amount = 0
    while amount < 4:
        slowprint(message)
        time.sleep(1)
        amount += 1
creep()

slowprint("I'm")

def clear():
            if name == 'nt':
                _ = system('cls')
clear()

slowprint("You don't know the truth.")
time.sleep(1)
slowprint("Follow. It.")

time.sleep(2)

def clear():
            if name == 'nt':
                _ = system('cls')
clear()

time.sleep(2)
slowprint("My apologies.\n")
time.sleep(1)
slowprint("You spot a third ~door~ to the right of where the person once stood.")
time.sleep(1)
slowprint("But you also have an opportunity to go ~downstairs~ through the lobby at the end of the hall.\n")

def manda():
    at_stairs = False
    while not at_stairs:
        third_stairs = str(input("Input: ")).strip().lower()
        if "door" in third_stairs:
            slowprint("The door doesn't budge.Isaidfollowit\nGo ~downstairs~?")
        elif "downstairs" in third_stairs:
            slowprint("You .followit. go downstairs and hear rustling as you descend.")
            time.sleep(1)
            slowprint("The lower you go, a deep rumbling grows.\n\
Circling and enveloping you.\n")
            time.sleep(2)
            slowprint("You can keep ~descending~.\n..\n")
            at_stairs = True
        else:
            print("Please enter a valid response.\n")
manda()

def follow():
    at_thing = False
    count = 0
    while not at_thing:
        follow_down = str(input("Input: ")).strip().lower()
        if "follow" in follow_down:
            import followit_EE
            at_thing = True
        elif "desending" in follow_down or "descend" in follow_down:
            slowprint("You descend.")
            time.sleep(1)
            slowprint("Descend into madness.")
            time.sleep(1)
            while count < 9:
                slowprint("Descend.")
                count += 1
            import descend_alt
            at_thing = True
        else:
            print("Please enter a valid response.")
follow()