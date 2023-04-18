import sys; args = sys.argv[1:]
import re

def makeGlobals(args):
  global board,firstTok,premoves,moveF
  
  let = {"a": 0, "b": 1, "c":2, "d": 3, "e": 4, "f":5, "g": 6, "h": 7 }


  premoves = []
  board='.'*27 + "ox......xo" + '.'*27

  firstTok = 'x'

  for ele in args:
    if (ele)=='x' or (ele)=='X' or  (ele)=='o' or  (ele)=='O':
      firstTok=ele.lower()
    elif not '.' in ele:
      if ele[0].lower() in let.keys():
        ele = int( (int(ele[1]) - 1) * 8 + let[ele[0].lower()])
      premoves.append(ele)

    else:
      board=(ele.lower())


def printBoard(nn):
  length = len(nn)
  for i in range(8):
    for j in range(8):
      index = i * 8 + j
      if index < length: print(nn[index], end="")
    print()

def findMoves(board, token):

  poss = []
  for i in [idx for idx,ele in enumerate(board) if ele==token]:
    neigh = [(i+1,1),(i+7,7),(i+8,8),(i+9,9),(i-1,-1),(i-7,-7),(i-8,-8),(i-9,-9)]
    for x in neigh:
      
      if x[0]<0 or x[0]>63: continue
      
      spot = board[x[0]]; move = x[1]
      
      if spot == '.' or spot == token:
        continue
      if i%8 ==7 and move in [-7,1,9]: continue
      elif i%8 ==0 and move in [7,-1,-9]: continue
      
      idx = x[0]
      
      while idx>-1 and idx<64:
        
        if board[idx] ==token: break
        if board[idx] =='.':   poss.append(idx);break
        
        if idx%8==7:
          if move in [-7,1,9]: break
          else: idx = idx + move; continue
        
        elif idx%8 ==0:
          if move in [7,-1,-9]: break
          else: idx = idx+move
        
        else:
          idx = idx + move


  return poss
  




def putMoves(moves,firstTok,board):
  bb = list(board)
  for x in moves:
    bb[x] = '*'

  return ("".join(bb))
  
def nextMove(mo):
      bb = putMoves(moves,firstTok,board)
      printSnap()
      printBoard(bb)
      print(set(moves))

def printSnapShot(move, boar, )



def main():

  makeGlobals(args)
  if '.' not in board: print("No moves possible")
  else:
    moves = findMoves(board, firstTok)
    if len(moves) ==0:
      print("No moves possible")
    else:
      nextMove(premove)
     
    





if __name__=="__main__":
    main()
 
#Siddhant Sood Period 7 2024