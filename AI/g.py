import sys; args = sys.argv[1:]
#siddhant sood, rohan kalahasty, jiwoo hwang
import random; import math

global bb
bb = []

width = 0
height = 0

board = args[0]
# board = board.replace("[", "")
# board = board.replace("]", "")
if len(args) == 2:
  width = int(args[1])
else:
  width = int (len(board)**(1/2))



height = int(len(board)/width)

if not(width * height) == len(board):
    width = width + 1




#print(board)
print(height)
print(width)
for x in range(width):
    s = ""
    for y in range(height):
        s + board[height*x + y]
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

    verticalFlip = getVerticalFlip(bb)
    pset.add("".join(verticalFlip))

    ccw90 = ["".join([x[i] for x in bb]) for i in range(len(bb[0]))][::-1]
    ccw180 = ["".join([x[i] for x in ccw90]) for i in range(len(ccw90[0]))][::-1]
    ccw270 = ["".join([x[i] for x in ccw180]) for i in range(len(ccw180[0]))][::-1]

    pset.add(("".join(ccw90)))
    pset.add(("".join(ccw180)))
    pset.add(("".join(ccw270)))
    
    # diagonalFlip = getDiagonalFlip(bb)
    # better = []
    # for i in diagonalFlip:
    #     better.append("".join(i))
    # pset.add(("".join(better))
   
    pset = list(pset)
    for x in pset:
        print(x)


def getDiagonalFlip(bb):
    split = []
    for i in bb: 
        split
    newDiagonal = bb.copy()
    for i in range(0, width):
        for j in range(i+1, width):
            newDiagonal[i][j],newDiagonal[j][i] = newDiagonal[j][i],newDiagonal[i][j]
    return newDiagonal


def getHorizontalFlip(m):
    horizontalFlip = []
    for i in m:
        horizontalFlip.append("".join(i[::-1]))

    return horizontalFlip
    
def getVerticalFlip(m):
    return m[::-1]
        
transformationPrint()


#Siddhant Sood, 7, 2024








