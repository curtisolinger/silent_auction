from os import system
# import os
# system('clear')
from art import logo
import sys


def main():
	print(logo)
	register = []
	bid(register)

	
	# print(register)
	run = True
	while run:
		answer = input("Are there other users who would like to bid? Type 'yes' or 'no'.")
		if answer == 'yes':
			system('clear')
			bid(register)
		else:
			print(f"The highest bidder is {highest(register)}")
			# print(register)

			run = False

	
def bid(register):
	name = input("Please enter your name: ")
	bid = float(input("Please enter your bid for the amazing lamp: "))
	entries(register, name, bid)

def entries(register, name, bid):
	register.append(
			{
				"Name" : name,
				"Bid" : bid
			}
		)


def highest(register):
	value = 0
	
	for entry in register:
		if entry["Bid"] > value:
			value = entry["Bid"]
	return(value)


main()