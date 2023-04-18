import sys; args = sys.argv[1:]
from time import perf_counter




def main():

    with open(args[0]) as w1:
        puzzles=[str(line.strip()) for line in w1]

    ilb = perf_counter()

    for y,x in enumerate(puzzles):  
        makeGlobals(x)
 
        s = perf_counter()
        print("#"+str(y+1)+" "*((5-len(str(y+1)))) +x)    
        w = bruteForce(x, ds, None)
        
        end = perf_counter()
   
        
        print(" "*(len(str(y+1)))+ " "*(6-len(str(y+1))) + w + " " + checkSum(w) + " " + str(round(end-s,4)))

    ilr = perf_counter()

    print(str(round(ilr-ilb,4)))

def getChoices(dotlook,idx,pzl):

    #update = []
    if idx != None:
        for i in neigh[idx]:
            if pzl[i] == '.' and pzl[idx] in dotlook[i]:
                dotlook[i] = dotlook[i] - {pzl[idx]}

        if idx in dotlook:
            #update = update + [*dotlook[idx]]
            del dotlook[idx]



    index = 0;best = 10;length = 0;ideal = 1000
    for i in dotlook:
        length = len(dotlook[i])
        if length < ideal:
            ideal = length
            best = dotlook[i]
            index = i
            
    return [best,index]

def checkSum(pzl):
    sum = 0
    for i in range(81):
        sum += ord(pzl[i])-ord('1')
    return str(sum)


def bruteForce(pzl, dotlook, idx):
    
    if not('.' in pzl): return pzl 
   
    choice = getChoices(dotlook,idx,pzl)

    
    mm = choice[0]
    for possible in choice[0]:

        subPzl = pzl[:choice[1]]+possible+pzl[choice[1]+1:]
        cop = dotlook.copy()


        gg = bruteForce(subPzl,cop, choice[1])
        if gg: return "".join(gg)

    
   
    

        
    
#________________________________________   





def makeGlobals(pzl):
    
    global chars
    global joint
    global neigh
    global ds
    

    chars = {*pzl} - {'.'}
    otherc = [*"123456789"]
    while len(chars) < 9:
        chars.add(otherc.pop(-1))

    r = [{y for y in range(x,x+9)}for x in range(0,81,9)] 
    c = []
    for x in range(0,9):
        c.append({y+x for y in range(0,81,9)})
    sub = [
    {1, 2, 3, 10, 11, 12, 19, 20, 21},
    {4, 5, 6, 13, 14, 15, 22, 23, 24},
    {7, 8, 9, 16, 17, 18, 25, 26, 27},
    {28, 29, 30, 37, 38, 39, 46, 47, 48},
    {31, 32, 33, 40, 41, 42, 49, 50, 51},
    {34, 35, 36, 43, 44, 45, 52, 53, 54},
    {55, 56, 57, 64, 65, 66, 73, 74, 75},
    {58, 59, 60, 67, 68, 69, 76, 77, 78},
    {61, 62, 63, 70, 71, 72, 79, 80, 81}
    ]

    sub = [{y-1 for y in x} for x in sub]

    joint = sub + r +c 
    neigh = list()

    for x in range(0,81):
        t = []
        for y in joint:
            
            if x in y:
                t = t + list(y-{x})
       
        neigh.append(set(t))
    ds = {i: chars - {pzl[i] for i in neigh[i]} for i in range(81) if pzl[i] == '.'}

    


if __name__=="__main__":
    main()
 
#Siddhant Sood Period 7 2024
