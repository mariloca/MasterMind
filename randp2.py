import urllib2


def rnumlistwithoutreplacement(num, min, max):
    """Returns a randomly ordered list of the integers between min and max"""
    if checkquota() < 1:
        raise Exception ("Your www.random.org quota has already run out.")
    #requestparam = build_request_parameterNR(min, max)
    #requestparam="https://www.random.org/strings/?num=10&len=8&digits=on&upperalpha=on&loweralpha=on&unique=on&format=html&rnd=new"
    #requestparam="https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"
    requestparam=build_request_parameterNR(num, min, max)
    request = urllib2.Request(requestparam)
    request.add_header('User-Agent', 'randomwrapy/0.1 very alpha')
    opener = urllib2.build_opener()
    numlist = opener.open(request).read()
    #print(numlist)
    return numlist.split()

def build_request_parameterNR(num, min, max):
    #randomorg = 'https://www.random.org/sequences/?min='
    randomorg = 'https://www.random.org/integers/?num='
    #vanilla = '&format=plain&rnd=new'
    vanilla='&col=1&base=10&format=plain&rnd=new'
    params = str(num) + '&min=' + str(min) + '&max=' + str(max)
    return randomorg + params + vanilla

def checkquota():
    request = urllib2.Request("https://www.random.org/quota/?format=plain")
    request.add_header('User-Agent', 'randomwrapy/0.1 very alpha')
    opener = urllib2.build_opener()
    quota = opener.open(request).read()
    return int(quota)

def reportquota():
    request = urllib2.Request("https://www.random.org/quota/?format=plain")
    request.add_header('User-Agent', 'randomwrapy/0.1 very alpha')
    opener = urllib2.build_opener()
    quota = opener.open(request).read()
    print ("This IP address has", quota, "bits left. Visit https://www.random.org/quota for more information." )   

if __name__=="__main__":
	numlists=rnumlistwithoutreplacement(4,0,7)
	#for i in numlists:
		#print(i)
	print(numlists)



