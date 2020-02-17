
import loop as lp

#Create Main Menu for the Game, which allows the player to:
#start a new game, view game score, exit the game, go to help.
instru='''
----------Welcome to MasterMind Game-----------
-------------------Main Menu-------------------
In this Mastermind game, you are playing against the computer. 
You must guess the right number combinations within 10 attempts to win the game.
Game default setting: 10 attempts to guess a four number combinations from 0~7.
You can always change the difficulty of the game by yourself!
------------------------------------------------
Here are the options you can do during the game:
1.Start a new game ---Enter: "s"
2.Change the game difficulty ---Enter:"c"
3.View your game score ---Enter: "v"
4.Exit the game ---Enter: "e"
5.See the menu ---Enter: "m"
------------------------------------------------
	'''
print(instru)
#Default setting
digit=4
lower=0
upper=7
attm=10
while True:
	option=input("What would you like to do? Enter:")

	if option=='s': #start a new game
		#start guessloop here
		score=lp.guessloop(digit,lower,upper,attm)
		if score>0:
			print("Bingo! You got it!\nYour score is", score )
		elif score==0:
			print("You have reached the guess limits.")
	elif option=="c": #change difficulty
		digit=int(input("Please enter the number digits: "))
		lower=int(input("Please enter the lower bound: "))
		upper=int(input("Please enter the upper bound: "))
		attm=int(input("Please enter guess times: "))
	elif option=='v': #show scoreboard
		print(score)

	elif option=='e':	#Exit the game
		print("See you next time!")
		break
	elif option=='m':
		print(instru)
	else:
		print("Invalid input. Please enter again!")
		














