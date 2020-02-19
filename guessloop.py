import rand 
from dict import dictionary
import color 

def guessloop(num,lower,upper,attempt):
	#Generate random number in a list
	secret=rand.randomnumbergenerate(num,lower,upper)
	answerdict=convertlisttodict(secret)
	repeatdict=repeattimedict(secret)
	score=100
	#score of each attempt
	deductpoint=score/attempt

	print("*****************************************\nAre you ready? Let's get started!")
	hint=input("Do you want to see the Hint? Please enter Y or N: ")
	
	while True:
		guess=input("Please enter your guess: ")
		#Try-except step is to catch input error.
		#try:
		#Check if 'guess' is a valid number input
		guessint=int(guess)
		guesslist=[]
		for i in str(guess):
			guesslist.append(i)
		guessdict=convertlisttodict(guesslist)
		#Create copy of the 'repeat' dictionary
		repeatdictcopy=dictionary()
		for key,value in repeatdict.items():	
			repeatdictcopy.add(key,value)
		#Starts to compare sdict and gdict
		#1. To compare gdict(idx).value to sdict(idx).value, 
		# check if there is any correct number at the correct position.
		#2. To check if gdict(idx).value exists in sdict, to check if there is a correct number 
		#3. If both 1&2 have negative results, then start the while loop again,
		# asking new input to start guess again.
		idx=0
		bingo=0
		almost=0
		wrong=0
		#input 'num', three dicts, return match or not
		for idx in range(0,num):
			#Check if the guess number has any digits at the correct position
			if guessdict[idx]==answerdict[idx]:
				bingo=bingo+1
			#Check if the guess number has any correct digits
			if guessdict[idx] in repeatdictcopy.keys():
				if repeatdictcopy[guessdict[idx]]>0:
					almost=almost+1
					repeatdictcopy[guessdict[idx]]=repeatdictcopy[guessdict[idx]]-1
			#Check if the guess is totally wrong
			else:
				wrong=wrong+1
		if bingo==num: break
		print("Guess number:", guess, "Correct number:", almost, "Correct position:", bingo)
		
		# if loop return=1: break
		#if loop return=0, continue the following step

		#Hint
		if hint=="Y": showhint(secret, guessint)
		
		#Based on compared result, check if need next input guess
		
		attempt=attempt-1
		score=int(score-deductpoint)
		print("You have", attempt, "guesses left.\n===================================")
		if attempt==0: break #game over
		
		
			#color.prRed("Invalid input. Please enter a number.")

	return score


def showhint(answer, guessnumber):
	answer = int("".join(answer))
	if guessnumber>answer:
		print("Hint: Your guess is bigger than the answer.")
	elif guessnumber<answer:
		print("Hint: Your guess is smaller than the answer.")


def convertlisttodict(numlist):
	#Convert list into a dictionary
	i=0
	numdict = dictionary()  
	for number in numlist:
		numdict.key=i
		numdict.value=number
		numdict.add(numdict.key, numdict.value) 
		i=i+1
	return numdict

def repeattimedict(numlist):
	#Keys of 'repeatdict' are answers
	#Values are repeat times of each digit of the answer
	#Prepare for compare how many digits are correct
	i=0
	repeatdict = dictionary()  
	for number in numlist:
		repeatdict.key=numlist[i]
		repeatdict.value=numlist.count(numlist[i])
		repeatdict.add(repeatdict.key, repeatdict.value) 
		i=i+1
	return repeatdict

ss=guessloop(4,0,7,10)
print(ss)
