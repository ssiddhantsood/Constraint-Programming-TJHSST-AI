import sys; args = sys.argv[1:]
import random


init = "".join(['.' for x in range(0,49)])
if args:
    init = str(args[1])



board_size = 49
chars  = [0,1,2,3,4,5,6]

Q2 = [{0,1,2,6,7,8}, {2,3,4,8,9,10}, {5,6,7,12,13,14}, {7,8,9,14,15,16}, {9,10,11,16,17,18}, {13,14,15,19,20,21}, {15,16,17,21,22,23}]

Q3 = [{0,1,2,3,4}, {5,6,7,8,9,10,11},{12,13,14,15,16,17,18}, {19,20,21,22,23}, {0,1,5,6,12}, 
     {2,3,7,8,13,14,19}, {4,9,10,15,16,20,21}, {11,17,18,22,23}, {5,12,13,19,20}, {0,6,7,14,15,21,22}, {1,2,8,9,16,17,23},{3,4,10,11,18},
     {0,1,2,6,7,8}, {2,3,4,8,9,10}, {5,6,7,12,13,14}, {7,8,9,14,15,16}, {9,10,11,16,17,18}, {13,14,15,19,20,21}, {15,16,17,21,22,23}]


def isInvalid(pzl):
    ls = []
    n=7
    
    ls.append([])
    ls.append([])

    for i in range(7):
    
        ls.append(pzl[i*7:n*i+n])
        ls.append(pzl[i::n])
        ls[0].append(pzl[n-1 *(i+1)])
        ls[1].append(pzl[(n+1)*i])
    




    for i in Q3:
        t = [k for k in i if k!= "."]
        if len(t) > len(set(t)):
            return True
    return False
    

def getChoices(pzl):
    for i, c in enumerate(pzl):
        if c == ".":
            poss = []
            for l in chars:
                temp = list(pzl[:])
                temp[i] = l
                poss.append(temp)
            return poss
    return []


def bruteForce(pzl):
    
    ff= isInvalid(pzl)
    
    if ff:
        return ""
    
    if not(ff) and not('.' in pzl):
        return str(pzl) 
    
    choice = getChoices(pzl)
    for possible in choice:
        subPzl = possible
        gg = bruteForce(subPzl)
        if gg: return gg

    return "" 
    

def random_state(state):
    for i in range(len(state)):
        state[i] = i
    random.shuffle(state)
    return state



w = bruteForce(init)

print(w)

