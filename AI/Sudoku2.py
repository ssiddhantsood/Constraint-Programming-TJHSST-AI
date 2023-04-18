import sys; args = sys.argv[1:]
from time import perf_counter
import math
import random



def main():

    with open(args[0]) as w1:
        puzzles=[str(line.strip()) for line in w1]

    ilb = perf_counter()
    for y,x in enumerate(puzzles):  
        makeGlobals(x)
 
        s = perf_counter()
        print("#"+str(y+1)+" "*((5-len(str(y+1)))) +x)    

        w = bruteForce(x, ds, None,ids)
        
        end = perf_counter()
   
        
        print(" "*(len(str(y+1)))+ " "*(6-len(str(y+1))) + w + " " + checkSum(w) + " " + str(round(end-s,4)))



    ilr = perf_counter()

    print(str(round(ilr-ilb,4)))

def getChoices(dotlook,idx,pzl,idl):

    update = {}
    if idx != None:
        for i in neigh[idx]:
            if pzl[i] == '.' and pzl[idx] in dotlook[i]:
                dotlook[i] = dotlook[i] - {pzl[idx]}

            if idx in dotlook:
                if idx in update:
                    update[idx] = update[idx] + dotlook[idx]
                else:
                    update[idx] = dotlook[idx]
                del dotlook[idx]

        
        for x in idl:
            if idx in idl[x]:
                idl[x].remove(idx)





    index = 0;best = 10;length = 0;ideal = 1000
    for i in dotlook:
        length = len(dotlook[i])
        if length < ideal:
            ideal = length
            best = dotlook[i]
            index = i


    for cs in neigh:
        for sym in idl:
            allp = idl[sym] & cs
            if len(allp) == 1:
                return [sym, [*allp][0]]


            

    return [best,index] #best is ideal symbol, index is the dot location

def checkSum(pzl):
    sum = 0

    smallestval = 1000
    for i in pzl:
        if ord(i)<smallestval:
            smallestval = ord(i)
    for i in range(len(pzl)):
        sum += ord(pzl[i])-smallestval
    return str(sum)


def bruteForce(pzl, dotlook, idx,idl):
    if not('.' in pzl): return pzl 
    choice = getChoices(dotlook,idx,pzl,idl)

    t = 0

    for possible in choice[0]:
        t = t+1

        subPzl = pzl[:choice[1]]+possible+pzl[choice[1]+1:]
        
        if not(t== len(choice[0])):
            cop = dotlook.copy()
            cop2 = idl.copy()
        else:
            cop = dotlook
            cop2 = idl


        gg = bruteForce(subPzl,cop, choice[1],idl)
        #for xx in choice[2]:
        #    dotlook[xx] = choice[2][xx]
        if gg: 

            print("hehe " + "".join(gg))
            return "".join(gg)


    #print(choice[2])
    #print(dotlook)
    
    

        
    
#________________________________________   





def makeGlobals(pzl):
    
    global chars
    global joint
    global neigh
    global ds
    global ids

    height = 9 
    pzlen = len(pzl)
    height = int(math.sqrt(pzlen))



    chars = {*pzl} - {'.'}
    otherc = [*"123456789abcdefhijk"]
    while len(chars) <  height:
        chars.add(otherc.pop(-1))






    r = [{y for y in range(x,x+height)}for x in range(0,pzlen,height)] 
    c = []
    for x in range(0,height):
        c.append({y+x for y in range(0,pzlen,height)})


    subheight = int(math.sqrt(height))
    subwidth = int(height/subheight)
    if subheight *subwidth != height: subwidth = subwidth +1

    
    sub=[{i for j in range(k,k+subheight*height,height) for i in range(j,j+subwidth)} for l in range(0,pzlen,height*subheight) for k in range(l,l+height,subwidth)]


    joint = sub + r +c 
    neigh = list()

    for x in range(0,pzlen):
        t = []
        for y in joint:
            
            if x in y:
                t = t + list(y-{x})
       
        neigh.append(set(t))
    ds = {i: chars - {pzl[i] for i in neigh[i]} for i in range(pzlen) if pzl[i] == '.'}
    
    ids = {i:set() for i in chars  }

    for x in ds:
        for y in ds[x]:
            ids[y].add(x)

    #print(ids)



    

if __name__=="__main__":
    main()
 
#Siddhant Sood Period 7 2024
