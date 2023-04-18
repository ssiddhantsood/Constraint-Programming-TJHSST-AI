import sys; args = sys.argv[1:]
import time
import math
import random

startTime = time.time()
sts = time.process_time()
#initial = args[0]
initial ="87123456_"
goal = "83274165_"
#if len(args)>1: goal = args[1]

x = len(goal)
height = int(math.sqrt(x))
width = int(x/height)
if height *width != len(initial) : width = width +1





def main():
    if len(args)>1:

        if (initial ==goal):
            print (initial[0:3] )
            print (initial[3:6] )
            print (initial[6:9])
            print ("\nSteps: 0")
            print ("Time: " + str(round(time.time() - startTime,2)) + 's')


        elif (initial[:6] ==  goal[:6] and initial[7]==goal[8]  ):
            print (initial[0:3] +"   " + goal[0:3])
            print (initial[3:6] +"   " + goal[3:6])
            print (initial[6:9]+"   " + goal[6:9])
            print ("\nSteps: 1")
            print ("Time: " + str(round(time.time() - startTime,2)) + 's')
            exit()



        w = ShortestPath(initial,goal)
 
 
        if w ==-1:
            print (initial[0:3])
            print (initial[3:6])
            print (initial[6:9])
            print ("\nSteps: -1")
            print ("Time: " + str(round(time.time() - startTime,2)) + 's')

        else:
            pb(w)
            print ("\nSteps: " + str(len(w)-1))
            print ("Time: " + str(round(time.time() - startTime,2)) + 's')
    else:
        stats = [0,0]
        pznums = 500
        lpz = ['1','2','3','4','5','6','7','8','_']
        for i in range(500):
            random.shuffle(lpz)
            pz = ''.join(lpz)

            w = 0
            for x in range(8):
                if (pz[x] != "_"):
                    nono = getChildrenz(pz,x)

                    for v in nono:

                        if x==v:
                            w = w+1;

            if w==0:
                goal = "83274165_"
                w = ShortestPath(pz,goal)
                if w != -1: 
                    print(pz)

            
                #stats[0] = stats[0]+1
                #stats[1] = stats[1] + len(w)-1


        ste = time.process_time()
        #print("total time: " + str(ste-sts) )
        #print("total tested: " + str(pznums) )
        #print("solvable puzzles: " + str(stats[0]) )
        #print("average puzzle length: " + str(int(stats[1])/pznums))

    

    



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



def getChildren(init):
    pos= init.find("_")
    c = []
    if pos>=width:         c.append(swap(init,pos,pos-width))
    if pos+width<len(init):    c.append(swap(init,pos,pos+width))
    if pos%width != 0:       c.append(swap(init,pos,pos-1))
    if pos%width != width-1 :    c.append(swap(init,pos,pos+1))

    return c

def getChildrenz(init,pos):
    #pos= init.find("")
    c = []
    #up 
    if pos>=width:         c.append(pos-width)
    #down
    if pos+width<len(init):    c.append(pos+width)
    #left
    if pos%width != 0:       c.append(pos-1)
    #right
    if pos%width != width-1 :    c.append(pos+1)

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
    
    

def ShortestPath(pz, goal):
    if pz == goal: return [pz]
    if parity(pz,goal): return -1

    parseMe = [pz]
    
    seen = {pz: ""}

    for n in parseMe:
        for i in getChildren(n):
            if i not in seen: 
                seen[i] = n
                if i == goal:   return path(seen, pz, goal)
                parseMe.append(i)
    return -1


if __name__=="__main__":
    main()

    
#Siddhant Sood Period 7 2024