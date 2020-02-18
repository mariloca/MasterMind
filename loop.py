import rand as r
from dict import dictionary
import color as cl

#class dictionary(dict):
#    # __init__ function  
#    def __init__(self):
#  		self = dict()
#    # Function to add key:value  
#    def add(self, key, value):  
#    	self[key] = value

def guessloop(num,lower,upper,attempt):
	#Generate random number
	secret=r.rnumlistwithoutreplacement(num,lower,upper)
	#Check guess answer
	#print(secret)
	# joins elements of secret by '' 
	# and stores in an integer ans as a hint to guess 
	ans = int("".join(secret))
	print(ans)
	#Generate list, dicts, ready for use
	#Create Key-Value pair for the answer and input number
	i=0
	j=len(secret)
	#'sdict' stores key-value pairs of guess answer
	sdict = dictionary()  
	for number in secret:
		sdict.key=i
		i=i+1
		sdict.value=number
		sdict.add(sdict.key, sdict.value) 
	#print(sdict)
	#'repeat' stores keys as answer numbers, values as number repeat times
	#This is to check how many correct numbers have been guessed
	#and it allows duplicate number 
	repeat = dictionary()  
	n=0
	for number in secret:
		repeat.key=secret[n]
		repeat.value=secret.count(secret[n])
		repeat.add(repeat.key, repeat.value) 
		n=n+1
	#print(repeat)

	score=100
	dpoint=score/attempt
	print("*****************************************\nAre you ready? Let's get started!")
	#Start the guess loop
	while True:
		g=input("Please enter your guess: ")
		#Make sure each guess will have the same repeat dict to compare
		#Values that have been minus, add back
		local_repeat=dictionary()
		for key,value in repeat.items():
			#print(key, value)
			local_repeat.add(key,value)
		#print(local_repeat)
		#Try-except step is to catch input error.
		#But if the guess number starts with zero like '0762', int(g) will omit the first zero,
		#so, I create 'guess' as a copy.
		guess=g
		try:
			#Check if 'g' is a valid number
			g=int(g)
			#print("Your guess is ", guess,".")
			glist=[]
			for i in str(guess):
				glist.append(i)
			#print(glist)
		#'gdict' stores key-value pairs of player input number
			m=0
			gdict=dictionary()
			for numbers in glist:
				gdict.key=m
				m=m+1
				gdict.value=numbers
				gdict.add(gdict.key, gdict.value)
			#print(gdict)
	
	#Starts to compare sdict and gdict
	#1. To compare gdict(idx).value to sdict(idx).value, 
	#   to check if there is any correct number at the correct position.
	#2. To check if gdict(idx).value exists in sdict, to check if there is a correct number 
	#3. If both 1&2 have negative results, then start the while loop again,
	#   asking new input to start guess again.
			idx=0
			bingo=0
			almost=0
			wrong=0
			for idx in range(0,j):
				#Check if the guess number has any digits at the correct position
				if gdict[idx]==sdict[idx]:
					bingo=bingo+1
				#Check if the guess number has any correct digits
				if gdict[idx] in local_repeat.keys():
		            #print(gdict[idx])
					if local_repeat[gdict[idx]]>0:
						almost=almost+1
					#print(repeat[gdict[idx]])
						local_repeat[gdict[idx]]=local_repeat[gdict[idx]]-1
					#print(almost)
				#Check if the guess is totally wrong
				#elif gdict[idx] not in sdict.values():
				else:
					wrong=wrong+1
	
			#Hint
			if g>ans:
				print("Hint: Your guess is bigger than the answer.")
			elif g<ans:
				print("Hint: Your guess is smaller than the answer.")
			print("Guess number:", guess, "Correct number:", almost, "Correct position:", bingo)
			
			#Based on compare result, check if need next input guess
			#if the input is correct, then break, return score
			#if the input is incorrect, attempt-1, score-10, back to next guess
			#if attempt==0, then game over.
			if bingo==num:
				break
			attempt=attempt-1
			print("You have", attempt, "guesses left.\n===================================")
			score=int(score-dpoint)
				#print("s:", score)
			if attempt==0:
				break
			
		except:
			cl.prRed("Invalid input. Please enter a number.")

	return score

#ss=guessloop(4,0,7,10)
#print(ss)
