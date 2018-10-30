# import the random packages so that we can generate random numbers
from random import randint

#choices is an array => a container that can hold multiple items 
# arrays are a 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]

# make the computer choose a weapon from the choices array at random 
computer_choice = choices [randint(0,2)]

# print the choice to the terminal window
print("Computer chooses: ", computer_choice)

#set up your logo
while player is False:
	# set plauer to True by making selection
	print("Choose your weapon!")
	player = input("Rock, Paper or Scissors?\n")

	print(player, "\n")
	# check for a tie = choices are the same
		if player == computer_choice:
		print("Tie! You live to shoot another day")
		# check to see if the computer choice beats our choice or not
	elif player == "Rock":
		if computer_choice == "Paper!":
		# computer won. Crap!
		print("You lose!" , computer_choice, "cut" , player)
	else:
		# we win! such winning
		print("You win!" , player, "smashes" computer_choice)

	elif player == "Paper":
		if computer_choice == "Scissors":
		# computer won. Crap!
		print("You lose!" , computer_choice, "cut" , player)
	else:
		# we win! such winning
		print("You win!" , player, "covers" computer_choice)

	elif player == "Scissors":
	if computer_choice == "Rock":
		# computer won. Crap!
		print("You lose!" computer_choice , "smashes" player)
	else:
		# we win! such winning
		print("You win!" , player, "cut" computer_choice)


	elif player == "quit"
	exit()

	else:
		print("Check your spelling...that's not a valid choice\n")
		# reset the game loop and start over
		player = False
		computer_choice = choices[randint(0, 2)]


		# Score variables

		player wins = 0
		computer_wins = 0

		user_wins += 1
		computer_wins += 1

		# check for 3 wins
	if player_wins == 3:
		print("You win the match!")
		exit()

	elif computer_choice == 3:
		print("The computer win the match!")
		exit()