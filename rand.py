import urllib.request, urllib.error, urllib.parse


def rnumlistwithoutreplacement(num, min, max):
    """Returns a randomly ordered list of the integers between min and max"""
    if checkquota() < 1:
        raise Exception("Your www.random.org quota has already run out.")
    requestparam = build_request_parameterNR(num, min, max)
    request = urllib.request.Request(requestparam)
    request.add_header('User-Agent', 'randomwrapy/0.1 very alpha')
    opener = urllib.request.build_opener()
    numlist = opener.open(request).read()
    newlist=numlist.decode()
    return newlist.split()
    

#helper
def build_request_parameterNR(num, min, max):
    randomorg = 'https://www.random.org/integers/?num='
    vanilla = '&col=1&base=10&format=plain&rnd=new'
    params = str(num) + '&min=' + str(min) + '&max=' + str(max)
    return randomorg + params + vanilla


def checkquota():
    request = urllib.request.Request("https://www.random.org/quota/?format=plain")
    request.add_header('User-Agent', 'randomwrapy/0.1 very alpha')
    opener = urllib.request.build_opener()
    quota = opener.open(request).read()
    return int(quota)

def reportquota():
    request = urllib.request.Request("https://www.random.org/quota/?format=plain")
    request.add_header('User-Agent', 'randomwrapy/0.1 very alpha')
    opener = urllib.request.build_opener()
    quota = opener.open(request).read()
    print("This IP address has", quota, "bits left. Visit http://www.random.org/quota for more information.")    
    
    
#if __name__=="__main__":
    #numlists=rnumlistwithoutreplacement(4,0,7)
    #for i in numlists:
        #print(int(i))
    #print(numlists)