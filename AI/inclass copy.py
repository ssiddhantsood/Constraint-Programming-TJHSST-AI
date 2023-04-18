
theDict = 
        { 
        1: 0
        2: 0
        3: 0
        4: 0
        5: 0
        6: 0
        7: 0
        8: 0
        9: 0 
        }
def main():
    pz = "12345678_"

    bfs(pz):





def swap(init, x,y):
    init = list(init)
    init[y],init[x] = init[x],init[y]
    return "".join(init)

def path(seen, start, goal):
    x = []
    while (goal!= start):
        x.append(goal)
        goal = seen[goal]

    x.append(start)
    return x[::-1]

def pb(paa):
    path = [paa[i:i+8] for i in range(0, len(paa), 8)]

    for seet in path:
        for z in range(0,width):
            total = ""
            for y in range (0,len(seet)):
                total = total +"  "+(seet[y][width*z:width*(z+1)])
            print (total.lstrip())
        print()

def getChildren(init,wi):
    pos= init.find("_")
    c = []
    #up 
    if pos>=wi:         c.append(swap(init,pos,pos-wi))
    #down
    if pos+wi<len(init):    c.append(swap(init,pos,pos+wi))
    #left
    if pos%wi!= 0:       c.append(swap(init,pos,pos-1))
    #right
    if pos%wi != wi+1 :    c.append(swap(init,pos,pos+1))

    return c 

def parity(init,goal):
    count1 = 0
    count2 = 0
    q =len(init)
    tempa = init
    tempb = goal

    
    init = init.replace("_","")
    goal = goal.replace("_","")
    for ele in range(q-1):
        for i in range (ele+1,q-1):
            if (init[ele]>init[i]):
                count1 +=1
            if (goal[ele]>goal[i]):
                count2 +=1
    # i have my counts for both

    if q % 2 == 1:
        return not(count1%2==count2%2)
    else:   
        return not(count1 + tempa.find("_")//width)%2 ==(count2 + tempb.find("_")//width)%2
    


def bfs(pz):

    parseMe = [pz]
    
    seen = {pz: ""}

    for n in parseMe:
        for i in getChildren(n):
            w = getChildren(n)
            

            if i not in seen: 
                seen[i] = n
                if i == goal:   return path(seen, pz, goal)
                parseMe.append(i)
    return -1