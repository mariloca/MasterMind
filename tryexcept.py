
#Error handling while player inputs guess number
while True:
	g=input("Please enter your guess: ")
	#Try-except step is to catch input error.
	#But if the guess number starts with zero, like '0983',
	#int(g) will omit the first zero,
	#so, I create 'guess' as a copy of 'g'.
	guess=g
	try:
		g=int(g)
		glist=[]
		for i in str(guess):
			glist.append(i)
		print(glist)
		#print("Your guess is ", guess,".")	
	except:
		print("Invalid input. Please enter a number.")
		


