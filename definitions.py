from sys import exit
import time
import random

def start_console(shipname):
	global ship_day
	global ship_month
	global ship_year
	ship_day = random.choice(range(0, 41))
	ship_month = random.choice(range(0, 13))
	ship_year = random.choice(range(3000, 9999))
	ship_date = [ship_day, ship_month, ship_year]
	time = range(0000, 9999)
	ship_time = (random.choice(time))
	print "\n"
	print "\tShip time    :%r" % ship_time
	print "\tDate code    :%r" % ship_date
	print "\tSolar System :Quelah"
	print "\tVessel       :%s" % shipname
	print "\tMission      :Undefined"
	print "\n"

def user_description(choice):
	if choice == "1":
		print "\n"
		print "Pilot"
		print "\n"
		print "Good with ships, but that's about it.  Aggressive, controlled,"
		print "and always pushing the limit."
		print "Doesn't really understand fear, this is sometimes a downfall."
		print "Can hold his/her own in a scrap."
		print "SPECIAL: Ignores any negative ship status effects."
		print "\nAre you sure you're a pilot?"
	elif choice == "2":
		print "\n"
		print "Bounty Hunter"
		print "\n"
		print "Lord of gadgets, gizmos, etc for hunting humans in space."
		print "Eye is always on the money and is quite selfish in most cases."
		print "Does not trust many. Is a boss at fighting."
		print "SPECIAL: Ignores any negative fight status effects."
	elif choice == "3":
		print "\n"
		print "Medic"
		print "\n"
		print "Heals like a boss, cares deeply for his/her friends."
		print "Trustworthy, honest, and calculated."
		print "The Medic is a nice guy, sometimes too nice."
		print "Scrawniest of the classes."
		print "SPECIAL: Heals at a TBD rate every TBD amount of rooms."
	elif choice == "4":
		print "\n"
		print "Scoundrel"
		print "\n"
		print "Lying, cheating, and sneaking are all traits of The Scoundrel."
		print "Is very good at convincing others to bend to his/her will."
		print "Forges alliances that benefit his/her power and influence."
		print "SPECIAL: Can sneak past many foes unnoticed."

def chosen_profession(prof_choice):
	if prof_choice == "1":
		print "\nI thought you looked Pilot-ey."

	elif prof_choice == "2":
		print "\nI thought you looked Bounty Hunter-ey."

	elif prof_choice == "3":
		print "\nI thought you looked Medic-ey."

	elif prof_choice == "4":
		print "\nI thought you looked Scoundrel-ey."


def console_home():
	print "\n"
	print "Loading system directory..."
	time.sleep(0.1)

	print ">Ship Status"
	time.sleep(0.1)

	print ">Transmission Logs"
	time.sleep(0.1)

	print ">Next Destination"
	time.sleep(0.1)

	print ">Exit"

	menu_selection = raw_input("\n> ").lower()

	if "ship" in menu_selection:
		ship_status()
	elif "transmission" in menu_selection:
		transmission_log()
	elif "next" in menu_selection:
		next_dest()
	elif "exit" in menu_selection:
		print "\nThank you for using the console.  Shutting down."

def ship_status():
	print "\nHull  : 10"
	print "Shield: 05"
	print "Radar:  10"
	print "Comms:  00"
	back = raw_input("Type 'x' to go back: ")
	if back == "x":
		console_home()

def transmission_log():
	print "\nTransmissions - "
	print "\nERR: NO LOGS FOUND, COMMS SYSTEM NOT IN OPERATION."
	back = raw_input("Type 'x' to go back: ")
	if back == "x":
		console_home()

def next_dest():
	print "\nNext destination:"
	back = raw_input("\nType 'x' to go back: ")
	if back == "x":
		console_home()