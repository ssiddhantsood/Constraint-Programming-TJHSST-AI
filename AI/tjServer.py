import sys; args = sys.argv[1:]
import re 
import random
import time

board ='.'*27 + "ox......xo" + '.'*27
firstTok = ""; premoves = []; moveF = "";HOLELIMIT = 13
topn = []; botn = []; leftn = []; rightn = [];
verbose = False
CACHEM = dict(); CACHEMM = dict(); CACHEA = dict(); CACHEAB = dict()


class Strategy:
  logging = True # turns on logging
  def best_strategy(self, board, player, best_move, running):
      time.sleep(1)
      if running.value:
        best_move.value = quickMove(board, player, False)



def makeGlobals(args):
  global board,firstTok,premoves,moveF, CACHEM, topn, botn,leftn,rightn, CACHEMM ,HOLELIMIT, CACHEA, verbose
  topn = [x for x in range (0,8)]; botn = [x for x in range (56,64)]; leftn = [x for x in range (0,57,8)]
  rightn = [x for x in range (7,64,8)]

  let = {"a": 0, "b": 1, "c":2, "d": 3, "e": 4, "f":5, "g": 6, "h": 7 }
  premoves = []; change = True
  for ele in args:
    if ele == "": continue
    elif "HL" in ele: HOLELIMIT = int(ele[2:])
    elif (ele)=='x' or (ele)=='X' or  (ele)=='o' or  (ele)=='O':
      firstTok=ele.lower()
      change = False
    elif ele.lower() == "v": verbose = True
    elif not '.' in ele:
      if ele[0].lower() in let: ele = int((int(ele[1]) - 1) * 8 + let[ele[0].lower()])
      premoves.append(ele)
      if len(premoves[-1])>3:
        pre = re.findall(r"..",premoves[-1])
        
        for x in range(len(pre)):
          if '_' in pre[x]:
            w = pre[x][1]
            pre[x] = w 
        premoves = premoves[:-1]
        premoves = premoves + pre
    
    else: board= ele.lower()
  if change:
    if (board.count('x') +  board.count('o'))% 2 ==0: firstTok = 'x'
    else: firstTok = 'o'

def main():

  makeGlobals(args)
  if '.' not in board: print("No moves possible")
  else:
    token = 33
    if len(findMoves(board, firstTok)) == 0: token = notT(firstTok)
    else: token = firstTok
    
    moves = findMoves(board, token)
    if len(moves) ==0:
      
      printBoard(board)
      print(board)
      print(str(board.count("x"))+"/"+str(board.count("o")))
      print("No moves possible")


    elif len(premoves) ==0:
      bb = showMoves(moves,(token),board)
      printSnap((token), bb, moves,None,85,board)
      print("Preferred Move is:" + str(quickMove(board,token,True)[0]))

    else:
      te = board
      bb = showMoves(moves,token,board)
      if verbose: printSnap(token, bb, moves,None,85,te)
      
      boar = te; bb = ""; move = ""; oldtok = ""
      
      for move in premoves:

        bb = bb.lower()
        move = int(move)
        if move<0: continue

        boar = makeMove (move, boar, token); oldtok = token
        token = notT(token);
        moves = findMoves(boar, token)
        if len(moves)==0:
          token = notT(token)
          moves = findMoves(boar, token)
        bb = showMoves(moves,token,boar)
        bb =list(bb)
        bb = "".join(bb[:move] + [bb[move].upper()] + bb[move+1:])
        if ("." not in boar or not(findMoves(boar, token) and findMoves(boar, notT(token)))) and verbose :
          
          printSnap(token,bb,moves,move,oldtok,boar)
          print(oldtok.upper()+ " moves to " + str(move))
          boar =list(boar); boar= "".join(boar[:move] + [boar[move].upper()] + boar[move+1:])
          printBoard(boar)
          boar = boar.lower()
          print(boar)
          print(str(boar.count("x")+boar.count("X"))+"/"+str(boar.count("O") +boar.count("o")))     #terminating condition

        elif verbose:
          printSnap(token,bb,moves,move,oldtok,boar)
          print("Preferred Move is: " + token + " to " + str(quickMove(boar,token,True)[0]))
      
      if not verbose:
        printSnap(token,bb,moves,move,oldtok,boar)
        print("Preferred Move is: " + token + " to " + str(quickMove(boar,token,True)[0]))
  
  
#-------------------------------------------
def alphabeta(brd, tkn, lowerBnd, upperBnd,level):
  global CACHEA
  key = (brd,tkn, lowerBnd, upperBnd)
  if key in CACHEA: return CACHEA[key]
  if not (findMoves(brd,tkn)):
    if not (findMoves(brd,notT(tkn))):
      return [brd.count(tkn)-brd.count(notT(tkn))]

    key = (brd,notT(tkn), -1*upperBnd, -1*lowerBnd)
    if key in CACHEA: return CACHEA[key]
    else:
      nmOTHER = alphabeta(brd,notT(tkn),-1*upperBnd,-1*lowerBnd,False)
      CACHEA[key] = [-nmOTHER[0]] + nmOTHER[1:] + [-1]
      return [-nmOTHER[0]] + nmOTHER[1:] + [-1]

  best = [lowerBnd-1]
  for mv in findMoves(brd,tkn):

    key = (makeMove(mv,brd,tkn),notT(tkn),-1*upperBnd,-1*lowerBnd)
    ab = 303
    if key in CACHEA: 
      ab = CACHEA[key]
    else: 
      ab = alphabeta(makeMove(mv,brd,tkn),notT(tkn),-1*upperBnd,-1*lowerBnd,False)
      CACHEA[key] = ab
   
    score = -1*ab[0]
    if score<=lowerBnd: continue
    if score>upperBnd: return[score]
    if score>best[0]: best = [score] + ab[1:] + [mv]
    lowerBnd = score + 1
    

  if level:
    #print(tkn + "  " + brd + "  " + str(lowerBnd) + " " + str(upperBnd))
    print("Min Score:" + str(best[0])+ " Move Sequence: " + str(best[1:]))
  CACHEA[key] = best
  return best 
#--------------------------------------------

def mab(brd, tkn, lowerBnd, upperBnd,deep):
  global CACHEAB
  if deep<=0: return [evalu(brd,tkn)]
  key = (brd,tkn, lowerBnd, upperBnd)
  if key in CACHEAB: return CACHEAB[key]
  
  ls = findMoves(brd,tkn)

  if not ls:
    if findMoves(brd,notT(tkn)):
      oth = mab(brd,notT(tkn),-upperBnd, -lowerBnd, deep-1)
      return [oth[0]] + oth[1:] + [-1]

  
  best = [lowerBnd-1]
  ls = quickMove(brd, tkn, False)
  for mv in ls:
    ab = mab(makeMove(mv,brd,tkn),notT(tkn),-1*upperBnd,-1*lowerBnd,deep-1)
   
    score = -1*ab[0]
    if score<=lowerBnd: continue
    if score>upperBnd: return[score]
    if score>best[0]: best = [score] + ab[1:] + [mv]
    lowerBnd = score + 1
    
  CACHEAB[key] = best
  return best 
#--------------------------------------------


def gameOver(brd,token): return brd.count('.') == 0 

def evalu(brd,tkn): return brd.count(tkn) - brd.count(notT(tkn))
  #return len(findMoves(brd,(tkn))) - len(findMoves(brd,notT(tkn)))
def quickMove(pzl, token,do):
  global HOLELIMIT
  if not pzl:
    HOLELIMIT = token
    return

  pos = findMoves(pzl, token)
  if len(pos)==0:
    pos = findMoves(pzl, notT(token))
  

  if do:
    if pzl.count('.') < HOLELIMIT:
      return [alphabeta(pzl,token,-65,65,True)[-1]]
    #if pzl.count('.')<30:
    # return [mab(pzl,token,-600, 600,5)[-1]]

  corners = [0,7,56,63]
  nextToCorners = [{1,8,9},{6,14,15},{57,49,48},{62,54,55}]
  
  ans = []
  for x in range(len(corners)):
    if corners[x] in pos:
      ans.append(corners[x])

  

  for x in pos:
    copypzl = makeMove(x,pzl,token)
    
    if x in topn:
      ws = {copypzl[i] for i in topn[0:x]}
      if (len(ws) ==1) and ws.pop() == token: ans.append(x)
      ws = {copypzl[i] for i in range(7,x,-1)}
      if (len(ws) ==1) and ws.pop() == token: ans.append(x)
    elif x in botn:
      ws = {copypzl[i] for i in range(56,x)}
      if (len(ws) ==1) and ws.pop() == token: ans.append(x)
      ws = {copypzl[i] for i in range(63,x,-1)}
      if (len(ws) ==1) and ws.pop() == token: ans.append(x)
    elif x in leftn:
      ws = {copypzl[i] for i in range(0,x,8)}
      if (len(ws) ==1) and ws.pop() == token: ans.append(x)
      ws = {copypzl[i] for i in range(56,x,-8)}
      if (len(ws) ==1) and ws.pop() == token: ans.append(x)
    elif x in rightn:
      ws = {copypzl[i] for i in range(7,x,8)}
      if (len(ws) ==1) and ws.pop() == token: ans.append(x)
      ws = {copypzl[i] for i in range(63,x,-8)}
      if (len(ws) ==1) and ws.pop() == token: ans.append(x)
      
    for y in range(len(corners)):
      if pzl[corners[y]] == "." or pzl[corners[y]] == notT(token):
        for z in nextToCorners[y]:
          if len(pos)>1: pos =  pos - {z}
  

  top = [pzl[x] for x in range (0,8)]
  bot = [pzl[x] for x in range (56,64)]
  left = [pzl[x] for x in range (0,57,8)]
  right = [pzl[x] for x in range (7,64,8)]


  for x in pos:
    if top.count('.') == 1 and x in top: ans.append(x)
    if bot.count('.') == 1 and x in bot: ans.append(x)
    if right.count('.') == 1 and x in right: ans.append(x)
    if left.count('.') == 1 and x in left: ans.append(x)

  

  if pzl.count(".")<30:
    ideal = 122222
    masterX = 44
    for x in pos:
      copyPzl = makeMove(x,pzl,token)
      length = len(findMoves(copyPzl,notT(token)))
      if length<ideal:
        ideal = length
        masterX = x
          
    ans.append(masterX)
    

  #for x in pos:
  # if x in [20,21,22,23,28,29,30,31,36,37,38,39,44,45,46,47]: return x
  ans = ans + [x for x in pos if x not in ans]
  return ans[0]

def printBoard(nn):
  length = len(nn)
  for i in range(8):
    for j in range(8):
      index = i * 8 + j
      if index < length: print(nn[index], end="")
    print()

def findMoves(board, token):
  global CACHEM
  key = (board,token)
  if key in CACHEM: return CACHEM[(board,token)]
  poss = []
  for i in [idx for idx,ele in enumerate(board) if ele==token]:
    neigh = [(i+1,1),(i+7,7),(i+8,8),(i+9,9),(i-1,-1),(i-7,-7),(i-8,-8),(i-9,-9)]
    
    for x in neigh:
      
      if x[0]<0 or x[0]>63: continue
      spot = board[x[0]]; move = x[1]
      
      if spot == '.' or spot == token: continue
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
  
  poss = set(poss)
  CACHEM[key] = poss
  return poss

def notT(token):
  if token == 'o': othertok = 'x'
  else: othertok = 'o'
  return othertok

def showMoves(moves,firstTok,board):
  bb = list(board)
  for x in moves: bb[x] = '*'
  return ("".join(bb))

def makeMove(position, board, token):
  global CACHEMM
  key = (board,token,position)
  if key in CACHEMM: return CACHEMM[key]

  bo = [list(board[i:i+8]) for i in range(0, 64, 8)]
  row = int(position/8)
  col = position%8
  bo[row][col] = token

  for drow, dcol in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
    bo = flip_tokens(bo, row, col, drow, dcol, token)
 
  x = "".join([''.join(row) for row in bo])
  CACHEMM[key] = x
  return x

def flip_tokens(bo, row, col, drow, dcol, token):
  toFlip = []
  johnathan = False
  trow = row; tcol = col
  if token == 'o': othertok = 'x'
  else: othertok = 'o'
  while True:
    trow = trow + drow;tcol = tcol + dcol
    if trow<0 or trow>=8 or tcol<0 or tcol>=8:  break
    if bo[trow][tcol] == token: johnathan = True
    elif bo[trow][tcol] != othertok: break
 
  while johnathan:
    row = row + drow; col = col + dcol
    if row<0 or row>=8 or col<0 or col>=8:  break
    if bo[row][col] == token or bo[row][col] =='.':  break
    toFlip.append((row, col))
  for row, col in toFlip: bo[row][col] = token
  return bo

def printSnap(first,boar,possible,move,oldtok,d1):
  possible = set(possible)
  if move:
    print(oldtok.upper() + " moves to " + str(move))
  printBoard(boar)
  print(d1 + " "+ (str(boar.count("x")+boar.count("X"))+"/"+str(boar.count("O") +boar.count("o"))))
  print()


  gg = "".join(str(x) + ", " for x in possible)[:-2]
  print("Possible moves for " + first + " :"  + gg )


if __name__=="__main__":
    main()
 
#Siddhant Sood Period 7 2024