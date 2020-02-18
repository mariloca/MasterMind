
import loop as lp
import color as cl
player=input("----------Welcome to MasterMind Game-----------\nWhat's your name?")
#Create Main Menu for the Game, which allows the player to:
#start a new game, view game score, exit the game, go to help.
print("Hi,", player, "! Below is the Main Menu:")
instru='''-------------------Main Menu-------------------                                               
In this Mastermind game, you are playing against the computer. 
You must guess the right number combinations within 10 attempts to win the game.
Game default setting: 10 attempts to guess a four number combinations from 0~7.
You can always change the difficulty of the game by yourself!
------------------------------------------------
Here are the options you can do during the game:
1.Start a new game ---Enter: "s"
2.Change the game difficulty ---Enter:"c"
3.Reset the game to default setting ---Enter:"r"
3.View your game score ---Enter: "v"
4.Exit the game ---Enter: "e"
5.See the menu ---Enter: "m"
------------------------------------------------
	'''
cl.prBold(instru)
#Default setting
digit=4
lower=0
upper=7
attm=10
score_list=[]
while True:
	option=input("What would you like to do? Enter:")

	if option=='s': #start a new game
		#start guessloop here
		score=lp.guessloop(digit,lower,upper,attm)
		if score>0:
			cl.prGreen("Bingo! You got it!")
		elif score==0:
			cl.prRed("You have reached the guess limits.")
		score_list.append(score)
	elif option=="c": #change difficulty
		digit=int(input("Please enter the number digits: "))
		lower=int(input("Please enter the lower bound: "))
		upper=int(input("Please enter the upper bound: "))
		attm=int(input("Please enter guess times: "))
	elif option=='r':
		digit=4
		lower=0
		upper=7
		attm=10
	elif option=='v': #show scoreboard, keep the past scores
		s=player + ", your scores are:" + str(score_list)
		cl.prLightPurple(s)
	elif option=='e':	#Exit the game
		s="See you next time," + player + "!" 
		cl.prPurple(s)
		break
	elif option=='m':
		cl.prYellow(instru)
	else:
		cl.prPurple("Invalid input. Please enter again!")
		














