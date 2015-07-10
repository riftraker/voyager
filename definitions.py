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
		print "The Pilot"
		print "Good with ships, but that's about it.  Aggressive, controlled,"
		print "and always pushing the limit."
		print "Doesn't really understand fear, this is sometimes a downfall."
		print "Can hold his/her own in a scrap."
		print "SPECIAL: Ignores any negative ship status effects."
		print "\nAre you sure you're a pilot?"

def chosen_profession(prof_choice):
	if prof_choice == "1":
		print "I thought you looked Pilot-ey."