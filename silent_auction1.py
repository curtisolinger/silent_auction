from os import system
# import os
# system('clear')
from art import logo
import sys


def main():
	print(logo)
	# register = []
	register = {}


	# bid(register)
	
	continuing_running = False

	while not continuing_running:
		name = input("Please enter your name: ")
		bid = float(input("Please enter your bid for the amazing lamp: "))
		register[name] = bid
		

		
		continue_bidding = input("Are there other users who would like to bid? Type 'yes' or 'no'. ")
		if continue_bidding == 'yes':
			system('clear')
		else:
			print(f"The highest bidder is {highest(register)}")
			continuing_running = True

	sys.exit(0)
	

def highest(register):
	value = 0
	for entry in register:
		if register[entry] > value:
			value = register[entry]
			name = entry
	return(name)


main()