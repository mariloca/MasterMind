import random

flag=True
while flag:

	num=input("Please enter the upper limit: ")
	if num.isdigit():
		print("Let's play!")
		num=int(num)
		flag=False
	else:
		print("Invalid Input. Please enter an integer number!")

answer=random.randint(0,num)

guess=None
count=10

while guess!=answer:
	guess = input("Please enter your guess: ")
	if guess.isdigit():
		guess=int(guess)
	else: print("Invalid Input. Try again. Please enter a valid integer number!")
	if guess == answer:
		print ("Bingo! You got it!")
	else:
		print ("Your guess is wrong. Try again!")
		count = count - 1
		print ("You have ", count, " times left.")





 