	
	if score>0:
		print("Bingo! You got it!\nYour score is", score )
		onemore=input("Do you want to start again? Please enter Y or N:")
		#o=onemore
		if onemore=="Y":
			lp.guessloop()
		elif onemore=="N":
			print("See you next time!")
			break
		elif onemore==" " or onemore != "Y" or onemore != "N":
			print("Invalid input. Please enter Y or N.")
			
			#continue to onemore to enter Y or N
		
	elif score==0:
		again=input("You have reached the guess limits.\nDo you want to start again? Please enter Y or N:")
		#ag=again
		if again=="Y":
			lp.guessloop()
		elif again=="N":
			print("See you next time!")
			break
		elif again==" " or again != "Y" or again != "N":
			print("Invalid input. Please enter Y or N.")