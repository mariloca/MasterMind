slist=["1","2","2","4"]
sdict={0:"1", 1:"2", 2:"2", 3:"4"}
gdict={0:"2", 1:"2", 2:"2", 3:"2"}
#gdict={"0":"2", "1":"2", "2":"2", "3":"2"}
class dictionary(dict):  
  
    # __init__ function  
    def __init__(self):  
        self = dict()  
          
    # Function to add key:value  
    def add(self, key, value):  
        self[key] = value

# Main Function  
corr = dictionary()  
i=0
for number in slist:
	corr.key=slist[i]
	corr.value=slist.count(slist[i])
	corr.add(corr.key, corr.value) 
	i=i+1


#print(corr) 
j=4
almost=0
idx=0
for idx in range(0,j):
	#print(gdict[idx])
	if gdict[idx] in corr.keys():
		#print(corr[gdict[idx]])
		if corr[gdict[idx]]>0:
			almost=almost+1
			#print(corr[gdict[idx]])
			corr[gdict[idx]]=corr[gdict[idx]]-1
print(almost)
		
#print(gdict[0])
#print(corr.keys())