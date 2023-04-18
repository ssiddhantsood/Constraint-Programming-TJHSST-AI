import sys; args = sys.argv[1:]
import time
import math
import random


def main():
    
    with open(args[0]) as w1:
        puzzles=[str(line.strip()) for line in w1]
    goal = puzzles[0]
    x = len(goal)

    height =4

    goaldic = {goal[0]: 0,goal[1]: 1,goal[2]: 2,goal[3]: 3,
                goal[4]: 4, goal[5]: 5, goal[6]: 6, goal[7]: 7,
                 goal[8]: 8,goal[9]: 9, goal[10]: 10, goal[11]: 11,
                  goal[12]: 12, goal[13]: 13, goal[14]: 14, goal[15]: 15}

    neigh = { 0:[1,4],1:[0,2,5],2:[1,3,6],3:[2,7],
              4:[8,0,5],5:[4,1,9,6],6:[2,5,7,10],7:[3,6,11],
              8:[9,4,12],9:[5,8.10,13],10:[9,11,14,6],11:[7,15,10],
              12:[8,13],13:[12,9,14],14:[13,10,15],15:[14,11],  
            }

    for y in puzzles:
        w = astar(y,goal,goaldic,neigh)
        if not w:
            print(y + ": X")
        elif w == "G" :
            print(y + ": G")
        else:
            print(y + ": " + w)
  
def h(initial,goal,goaldic,neigh):
    sum = 0
    f = 0
    for i in range(len(initial)):
        if(initial[i] == '_'):
            f = i
        p = goaldic[initial[i]]
        x1 = p // 4
        x2 = i // 4
        y1 = p % 4
        y2 =  i % 4
        sum += abs(x1 - x2) + abs(y1 - y2)
    return [sum,f]

def swap(init, x,y):
   init = list(init)
   init[y],init[x] = init[x],init[y]
   return "".join(init)

   #a,b = (x,y) if x<y else (y,x)
   #return init[:a] + init[b] + init[a+1:b] + init[a] + init[b+1:]

def pb(paa):

    path = [paa[i:i+8] for i in range(0, len(paa), 8)]

    for seet in path:
        for z in range(0,width):
            total = ""
            for y in range (0,len(seet)):
                total = total +"  "+(seet[y][width*z:width*(z+1)])

def getChildren(init,pos,neigh):
    wi = 4
    c = set()
    #up 
    if pos>=wi:   
        c.add((swap(init,pos,pos-wi), pos,pos-wi,"U"))
    #down
    if pos+wi<len(init):   
        c.add((swap(init,pos,pos+wi),pos,pos+wi,"D"))
    #left
    if pos%wi!= 0:     
        c.add((swap(init,pos,pos-1),pos,pos-1,"L"))
    #right
    if pos%wi != wi-1 : 
        c.add((swap(init,pos,pos+1),pos,pos+1,"R"))

    return c

def parity(init,goal):
    a = 0
    b = 0
    base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    q =len(init)
    tempa = init
    tempb = goal


    init = init.replace("_","")
    goal = goal.replace("_","")
    for i in range(q-1):
        for j in range (i+1,q-1):
            if ((init[i]) > (init[j])):
                a +=1
            if ((goal[i]) > (goal[j])):
                b +=1
    # i have my counts for both

    if q % 2 == 1:
        return (a%2==b%2)
    else:   
        return ((a + tempa.find("_")//4)%2 ==(b + tempb.find("_")//4)%2)

def astar(root, goal, goaldic,neigh):
    if not(parity(root, goal)): return []
    if root == goal: return "G"
    openSet = [[] for x in range (70)]
    

    pp = h(root,goal,goaldic,neigh)
    minv = pp[0]

    po = pp[1]
    openSet[minv].append((minv, [root],0,"","", po))


    closedSet = {}

    while True:
        if not openSet[minv]:
            minv = minv + 2
        
        deep = openSet[minv].pop()
        po =deep[5]
        
        if deep[1][-1] in closedSet: continue
        closedSet[deep[1][-1]] = deep[3]


        if str(deep[1][-1]) ==goal: return deep[4]
         



        for n in getChildren(deep[1][-1],po,neigh):

            if len(deep[1])>1 and n[0] == deep[1][-2]: continue     
            pp = goaldic[n[0][n[1]]] // 4     
            gg = goaldic[n[0][n[1]]] %  4   
            b = abs(n[1] // 4 - pp) + abs(n[1] % 4 - gg) - abs(n[2] // 4- pp ) - abs(n[2] % 4 - gg)
            if b>0:   
                openSet[minv+2].append((minv+2-deep[2]-1, deep[1] + [n[0]], deep[2]+1, deep[1][-1],deep[4] + n[3],n[2]))
            else:
                openSet[minv].append((minv-deep[2]-1, deep[1] + [n[0]], deep[2]+1, deep[1][-1],deep[4] + n[3],n[2]))

if __name__=="__main__":
    main()
 
#Siddhant Sood Period 7 2024