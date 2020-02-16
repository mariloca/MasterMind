import rand as r

print("Welcome to MasterMind Game!\nIn this game, you will have 10 attempts to guess four numbers from 0~7.")
print("If you want to try a easier one or to challenge yourself, you can set the game by yourself!")
flag=True
digit=0
lower=0
upper=0
attm=0
while flag:
	chall=input("Do you want to change the default game? Please enter Y or N: ") 
	if chall=="Y":
		digit=int(input("Please enter the number digits: "))
		lower=int(input("Please enter the lower bound: "))
		upper=int(input("Please enter the upper bound: "))
		attm=int(input("Please enter guess times: "))
		flag=False
	elif chall=="N":
		digit=4
		lower=0
		upper=7
		attm=10
		flag=False
	#Input error check
	elif chall==" " or chall != "Y" or chall != "N":
		print("Invalid input. Please enter Y or N. ")
#Generate random number using function from imported Module rand
secret=r.rnumlistwithoutreplacement(digit,lower,upper)
#Check guess answer
#print(secret)

#Create Key-Value pair for the answer and input number
class dictionary(dict):  
  
    # __init__ function  
    def __init__(self):  
        self = dict()  
          
    # Function to add key:value  
    def add(self, key, value):  
        self[key] = value
i=0
j=len(secret)-1
#print(j)
 
#sdict stores key-value pairs of guess answer
sdict = dictionary()  
for number in secret:
	sdict.key=i
	i=i+1
	sdict.value=number
	j=j-1
	sdict.add(sdict.key, sdict.value) 
#print(sdict)

print("*****************************************\nAre you ready? Let's get started!")

guess=input("Please enter your guess: ")















