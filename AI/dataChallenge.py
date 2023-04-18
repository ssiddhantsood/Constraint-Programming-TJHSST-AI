import sys; args = sys.argv[1:]
from time import perf_counter
start = perf_counter()
# data structure challenge
# sort the array by using heapsort algorithm. 
# use swap and heapDown

def addh(ls,ob):
    ls.append(ob)
    ls = heapUp(ls, ls[-1])

    return ls

def main():
#read in files 
#solve the lab here
    if args:
        with open(args[0]) as w1:
            line1=[int(line.strip()) for line in w1]
        with open(args[1]) as w2:
            line2=[int(line.strip()) for line in w2]
        with open(args[2]) as w3:
            line3=[int(line.strip()) for line in w3]

        end = perf_counter()
        print('#0: Read in files ' + str(round(end-start,4)) + "s") 
        
        first(line1,line2)
        second(line1)
        third(line1,line2,line3)
        fourth(line1)
        fifth(line2)
        sixth(line1)

        end = perf_counter()
        print('Total time: ' +  str(round(end-start,4)) + "s") 
    
    else:  print('no input')


def first(o,t):
    s = perf_counter()
    oo = {*o}
    tt = {*t}
    nu = len(oo.intersection(tt))
    end = perf_counter()
    print('#1: ' + str(nu) + "; " + str(round(end-s,4)) + "s") 

def second(f):
    s = perf_counter()
    count = 1
    tot = []
    seen = set()
    
    for x in f:
        if x not in seen:
            seen.add(x)
            if count == 0:
                tot.append(x)
            count = (count+1)%100

    end = perf_counter()
    print('#2: ' + str(sum(tot)) + "; " + str(round(end-s,4)) + "s") 
    
def third(o,t,b):
    s = perf_counter()
    
    dic = {}
    for x in o:
        if x in dic:
            dic[x] = dic[x]+1
        else:
            dic[x] = 1
    for x in t:
        if x in dic:
            dic[x] = dic[x]+1
        else:
            dic[x] = 1
    a = sum(dic[ind] for ind in b if ind in dic)

    
    end = perf_counter()
    print('#3: ' + str(a) + "; " +str(round(end-s,4)) + "s") 

def fourth(o):
    s = perf_counter()
    nu = sorted(list(dict.fromkeys(o)))[:10]
    end = perf_counter()
    print('#4: ' + str(nu) + "; " + str(round(end-s,4)) + "s")
def fifth(f):
    s = perf_counter()
    w = set()
    dic = {}
    for x in f:
        if x in dic:
            dic[x] = dic[x]+1
        else:
            dic[x] = 1
    for x in f:
        if dic[x]>=2:
            w.add(x)



    end = perf_counter()
    print('#5: ' + str((sorted(w)[:-11:-1])) + "; " + str(round(end-s,4)) + "s")
def sixth(e):

    s = perf_counter()
   
     
    seen = []
    seq = set()
    for v in e:
        seen = addh(seen,v)
        if v % 53 ==0:
            nex = heappop(seen)
            while nex in seq:
                nex = heappop(seen)
            seq.add(nex)


        
    end = perf_counter()
    print('#6: ' + str(sum(seq)) + "; " + str(round(end-s,4)) + "s")

def heappop(ls):
    a, end = ls[0], ls.pop()
    if len(ls) == 0: return a
    ls[0], current = end, 0
    while False == False:
        one = 2*current+1
        if one >= len(ls): return a
        two = one + 1
        if two < len(ls) and ls[two] < ls[one]: child = two
        else: child = one
        if ls[current] <= ls[child]: return a
        ls[child], ls[current] = ls[current], ls[child]
        current = child
        pass
    return ls

def addh(ls, value):
    current = len(ls)
    ls.append(value)
    while current > 0:
        parent = (current - 1) // 2
        if ls[parent] <= ls[current]: break
        ls[current], ls[parent] = ls[parent], ls[current]
        current = parent
        pass
    return ls




    
    


if __name__ == "__main__" : main()



# Siddhant Sood, 2024, Period 7