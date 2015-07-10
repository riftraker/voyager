from sys import exit
import time
import random

def galley():
	print "Upon entering the galley, you notice a pungent stench that fills"
	print "the room.  You start poring through cabinets, attempting to"
	print "locate the foul odor.  Eventually you locate it's source."
	print "You left the space bananas out before entering hibernation."
	print "Way to go..."
	print "\n"
	print 

	excuse = raw_input("> ")

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