import sys; args = sys.argv[1:]
#siddhant sood, rohan kalahasty, jiwoo hwang
import random; import math

global bb
bb = []

width = 0
height = 0
print(args)
board = args[0]
if len(args) == 2:
  width = int(args[1])
else:
  width = int(len(board)**(1/2))

height = int(len(board)/width)



#print(board)
#print(height)
#print(width)
for x in range(width):
    s = ""
    for y in range(height):
        s += board[height*x + y]
    bb.append(s)

#print(bb)

# threeDboard = ""  'abcdefghijkl'] 
# for x in range(height):
#     s = ""
#     for y in range(width):
#         s += board[height*x + y]
#     threeDboard += s + "\n"
# print(threeDboard)
       

def transformationPrint():
    pset = set()
    ident = str("".join(bb))
    pset.add(ident)
    
    horizontalFlip = getHorizontalFlip(bb)
    pset.add(("".join(horizontalFlip)))

    ccw90 = ["".join([x[i] for x in bb]) for i in range(len(bb))][::-1]
    ccw180 = ["".join([x[i] for x in ccw90]) for i in range(len(ccw90))][::-1]
    ccw270 = ["".join([x[i] for x in ccw180]) for i in range(len(ccw180))][::-1]

    pset.add(("".join(ccw90)))
    pset.add(("".join(ccw180)))
    pset.add(("".join(ccw270)))

    vert = flipVertical()
    pset.add(("".join(bb)))
   
    pset = list(pset)
    for x in pset:
        print(x)



def flipVertical():
  global bb
  bb = bb[::-1]
  return bb


def getHorizontalFlip(m):
    horizontalFlip = []
    for i in m:
        horizontalFlip.append("".join(i[::-1]))

    return horizontalFlip
    

transformationPrint()


#Siddhant Sood, 7, 2024








