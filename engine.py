from sys import exit
import random
import time
import definitions


print "\nYou awake from suspended hibernation to the cryo-chamber."
print "The other tubes are empty...turns out it wasn't a bad nightmare"
print "after all."
print "You are the lone survivor aboard---"
print "What was this vessel called again?"

global user_ship
user_ship = raw_input("> ")

print "\nAh, yes, %s." % user_ship.title()
print "A fine enough ship for interstellar exploration, not the best for"
print "fending off astro-raiders."
print "No use crying over spilled milk."
print "Have to motivate."
print "Have to survive."
print "Let's fire up the ship's console and make sure everything is still"
print "operating normally."

definitions.start_console(user_ship.title())

print "user: "

global user_name
user_name = raw_input("> ")

print "Welcome, %s." % user_name
print "This is your first time in the %s system console." % user_ship

chosen = False

while chosen == False:
	print "\nPlease identify class."
	print "1. Pilot"
	print "2. Bounty Hunter"
	print "3. Medic"
	print "4. Scoundrel"

	choice = raw_input("> ")

	if choice == "1" or choice == "2" or choice == "3" or choice == "4":
		definitions.user_description(choice)

		double_check = False
		while double_check == False:
			confirm = raw_input("\nY/N: ")
			if confirm == "y" or confirm == "Y":
				definitions.chosen_profession(choice)
				double_check = True
				chosen = True
			elif confirm == "N" or confirm == "n":
				double_check = True
				chosen = False
			else:
				print "\nPlease enter Y or N."
				double_check = False

	else:
		print "\nPlease enter a number between 1 and 4."