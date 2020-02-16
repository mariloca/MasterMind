#Dict compare

sdict={0:"1", 1:"2", 2:"2", 3:"4"}
gdict={0:"2", 1:"2", 2:"2", 3:"2"}


#print(sdict[0])
#print(gdict[2])

#for idx in range(0,j):
#	print(gdict[idx])
#	print(sdict[idx])

j=4
idx=0
bingo=0
almost=0
wrong=0
for idx in range(0,j):
	if gdict[idx]==sdict[idx]:
		bingo=bingo+1
	elif gdict[idx] in sdict.values():
		almost=almost+1
	elif gdict[idx] not in sdict.values():
		wrong=wrong+1
if bingo==4:
	print("Bingo! You got it!")	
if wrong==4:
	print("Your guess is incorrect. Try again!")

print("Correct number:", almost, "Correct position:", bingo)
print(almost)
print(bingo)
print(wrong)
#print(idx)



