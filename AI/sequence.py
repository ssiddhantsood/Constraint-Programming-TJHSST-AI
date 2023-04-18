import sys; args = sys.argv[1:]
import random

def makeGlobals(args):
   global row, column, board, blockLimit, foo, rawWords 
   row = 0; column = 0; board = "0x0"; blockLimit = 0; foo = []; rawWords = ""
   if not args:
      pass
   for arg in args:
      #print(arg)
      if '.txt' in arg: rawWords = arg                             #txt pass
      elif 'x' in arg and board == "0x0": board = arg       #board set
      elif 'x' in arg: 
         for pos,character in enumerate(arg[::-1]):
            if character.isdigit(): 
               direction = arg[0].upper()
               dimensions = arg[1:len(arg)-pos].split('x')
               string = arg[len(arg)-pos:].strip()
               if not(string ==""):
                  foo.append([direction,int(dimensions[0]),int(dimensions[1]),string])
               break            #wordsappend
      else: blockLimit = int(arg)                      #amount of blocks set
   row = int(board.split('x')[0]); column = int(board.split('x')[1])
   board = "".join(['-' for e in range(row*column)])


def putInitialValues():
   global row, column, board, blockLimit, foo
   for blocker in foo:
      position = blocker[1]*column+blocker[2]
      if blocker[0] == 'H':
         board = board[:position] + blocker[3] + board[(position+len(blocker[3])): ]
      elif blocker[0] == 'V':
         for char in blocker[3]:
            board = board[:position] + char + board[position+1:]
            position = position + column


def print2D(board,row ,column):
   #board = board.replace("~","-")
   for layer in range(row): print(str(board[layer*column:layer*column + column]))

def fillBlocks(pzl,blocks,pos):
   while not(pzl.count('#') == blockLimit):
      pzl[pos] = '#'
      pzl[len(pzl[pos])-pos] = '#'
   return "".join(pzl)

def initialMakeLegal(board):
   board = list(board)
   for pos,character in enumerate(board):
      if character == '#':
         ill = illegalPositions(pos, board,[])
         for change in ill:
            board[change] = '#'
   return "".join(board)

def reflect(board):
   board = list(board); reverseBoard = board[::-1]

   for x in range(int(len(board)/2)):
      if board[x] == '#': board[len(board)-1-x] ='#'
      if board[x] == '~': board[len(board)-1-x] ='~'
   for x in range(int(int(len(board)/2)),int(len(board))):
      if board[x] == '#': board[len(board)-1-x] ='#'
      if board[x] == '~': board[len(board)-1-x] ='~'

   board = "".join(board)
   return board

def makeValid(board):
   global row, column, blockLimit, foo
   for x in foo:
      if x[3] == '#':
         illegal = illegalPositions(board)
         for position in illegal:
            board = board[:position] + '#' + board[position+1:]

def illegalPositions(pos, second, seen):
   global row, column, blockLimit, foo
   bottom = [pos-column*2, pos-column*3]
   top = [pos+column*2, pos+column*3]
   right = [pos+2, pos+3]
   left = [pos-2, pos-3]

   illegal = []
   if bottom[0] < 0:
      if pos-column > 0:
         illegal.append(pos-column)
   else:
      if second[bottom[0]] == '#':
         illegal.append(pos-column)
      if bottom[1] < 0:
         illegal.append(pos-column)
         illegal.append(pos-column*2)
      else:
         if second[bottom[1]] == '#':
            illegal.append(pos-column)
            illegal.append(pos-column*2)

   if top[0] > column*row-1:
      if pos+column<column*row:
         illegal.append(pos+column)
   else:
      if second[top[0]] == '#':
         illegal.append(pos+column)
      if top[1] > column*row-1:
         illegal.append(pos+column)
         illegal.append(pos+column*2)
      else:
         if second[top[1]] == '#':
            illegal.append(pos+column)
            illegal.append(pos+column*2)

   if left[0]//column < pos//column:
      if (pos-1)//column == pos//column:
         illegal.append(pos-1)
   else:
      if second[left[0]] == '#':
         illegal.append(pos-1)

      if left[1]//column < pos//column:
         illegal.append(pos-1)
         illegal.append(pos-2)
      else:
         if second[left[1]] == '#':
            illegal.append(pos-1)
            illegal.append(pos-2)

   rando = [second[x] for x in illegal]
   if '~' in rando:
      return False


   if right[0]//column > pos//column:
      if (pos+1)//column == pos//column:
         illegal.append(pos+1)
   else:
      if second[right[0]] == '#':
         illegal.append(pos+1)

      if right[1]//column > pos//column:
         illegal.append(pos+1)
         illegal.append(pos+2)
      else:
         if second[right[1]] == '#':
            illegal.append(pos+1)
            illegal.append(pos+2)
   return illegal

def getChoices(pzl):
   global row, column, board, blockLimit, foo
   pos = pzl.find('-')
   ret = []
   first = pzl[:pos] + '~' + pzl[(pos+1):]
   second = pzl[:pos] + '#' + pzl[(pos+1):]
   second = reflect(second)
   queue = illegalPositions(pos, second, [])
   if queue == False: return [first]
   seen = [] 
   if len(queue) == 0: r = 100
   else:
      while queue:
         pp = queue.pop(0)
         seen.append(pp)
         second = second[:pp] + '#' +second[pp+1:]
         if not(connected(second)):
            return [first]
         second = reflect(second)
         tempQ = illegalPositions(pp, second, seen)
         if queue == False: return [first]
         tempQ = tempQ + illegalPositions(pp, second, seen)
         if queue == False: return [first]
         if isinstance(tempQ, int):
            tempQ = [tempQ]
         queue = tempQ + queue
         queue = [x for x in queue if x not in seen]
   
   return [second, first]

def makeUntouchable(board):
   board = list(board)
   for pos,val in enumerate(board):
      if not(val == '#') and not(val =='-'):
         board[pos] = '~'
   return "".join(board)

def bruteForce(pzl):
   global blockLimit
   if pzl.count("#") > blockLimit : return ""
   if pzl.count("#") == blockLimit : 
      return pzl
   for choice in getChoices(pzl):
      brute = bruteForce(choice)
      if brute: return brute
   return 

def connectFill(pzl, pos, ro, col):
   global column, row
   if ro< 0 or ro > row + 1 or col < 0 or col > column + 1:
      return pzl
   pzl[pos] = '^'
   if ro-1>=0 and pzl[pos -column] != '^' and pzl[pos - column] != '#':
      pzl = connectFill(pzl,col + (ro-1)*column ,ro-1, col)
   if ro+1<row and pzl[pos +column] != '^' and pzl[pos + column] != '#':
      pzl = connectFill(pzl,col + (ro+1)*column ,ro+1, col)
   if col-1>=0 and not(pzl[pos -1] == '^')and pzl[pos - 1] != '#':
      pzl = connectFill(pzl,(col-1) + (ro)*column ,ro, col-1)
   if col+1< column and not(pzl[pos +1] == '^') and pzl[pos +1] != '#':
      pzl = connectFill(pzl,(col+1) + (ro)*column ,ro, col+1)
   return pzl

def connected(pz):
   global column
   pz = pz.replace('~','-')
   r = pz.find('-')
   pz = list(pz)
   check = connectFill(pz, r, r//column, r%column)
   if '-' in check:
      return False
   return True

def totalInitializations():
   global board
   makeGlobals(args)
   putInitialValues()
   board = makeUntouchable(board)
   board = reflect(board)
   board = initialMakeLegal(board)

def makeStructure():
   global row, column, board, blockLimit, foo
   totalInitializations()
   board = bruteForce(board)
   if len(board) > row*column and not(board[:row*column].count('#') == blockLimit):
      board = "".join(['-' for e in range(row*column)])
      putInitialValues()
      board = makeUntouchable(board)
      board = reflect(board)
      board = initialMakeLegal(board)
      x = board[1:].index('#') + 2
      board = list(board)
      board[x] = '#'
      board = "".join(board)
      board = makeUntouchable(board)
      board = reflect(board)
      board = initialMakeLegal(board)
   putInitialValues()
   board = board.replace('~','-')

def dictInput(rawWords):
   with open(args[0]) as w1:
      rawWords = [[] for x in range(70)]
      for line in w1:
         wrd = line.strip()
         rawWords[len(wrd)].append(wrd)
   return rawWords

def rot90(board, width, height):
   newBoard = ''
   for col in range(width):
      ts = ""
      for nextVal in range(height):
         nextVal = col + height*nextVal
         ts = ts + board[nextVal]
      newBoard = newBoard + ts 
   return newBoard


def cond1(element):
   return element[2].count('-')

def findWordPositions(board):
   global row, column
   needToAdd = []
   hBoard = rot90(board, column, row)
   
   print2D(board, column, row)
   print('--')
   print2D(hBoard, row, column)
   for pos, val in enumerate(board):
      if val == '-'  or val.lower() in "abcdefghijklmnopqrstuvwxyz":
         if (pos-1)//column < pos//column:
            t = board[pos:(pos//column+1)* column]
            if '#' in t:
               needToAdd.append([pos, t.index('#'), board[pos:pos+ t.index('#')] ])
            else:
               needToAdd.append([pos, len(t),board[pos:pos+ len(t)]])
         elif board[pos-1] == '#':
            t = board[pos+1:(pos//column+1)* column]
            if '#' in t:
               needToAdd.append([pos, 1+t.index('#'),board[pos:pos+ t.index('#')]])
            else:
               needToAdd.append([pos, 1+len(t),board[pos:pos+ len(t)]])

   for pos, val in enumerate(board):
      if val == '-'  or val.lower() in "abcdefghijklmnopqrstuvwxyz":
         if (pos-1)//column < pos//column:
            t = board[pos:(pos//column+1)* column]
            if '#' in t:
               needToAdd.append([pos, t.index('#'), board[pos:pos+ t.index('#')] ])
            else:
               needToAdd.append([pos, len(t),board[pos:pos+ len(t)]])
         elif board[pos-1] == '#':
            t = board[pos+1:(pos//column+1)* column]
            if '#' in t:
               needToAdd.append([pos, 1+t.index('#'),board[pos:pos+ t.index('#')]])
            else:
               needToAdd.append([pos, 1+len(t),board[pos:pos+ len(t)]])
   
   
   board = rot90(board, column, row)


   '''
   for pos, val in enumerate(board):
      if val == '-'  or val.lower() in "abcdefghijklmnopqrstuvwxyz":
         if (pos-1)//column < pos//column:
            l = pos//row
            p = pos%row
            rPos = l
            t = board[pos:(pos//column+1)* column]
            if '#' in t:
               needToAdd.append([pos, t.index('#'), board[pos:pos+ t.index('#')]])
            else:
               needToAdd.append([pos, len(t),board[pos:pos+ len(t)]])
         elif board[pos-1] == '#':
            t = board[pos+1:(pos//column+1)* column]
            if '#' in t:
               needToAdd.append([pos, 1+t.index('#'),board[pos:pos+ t.index('#')]])

   print(needToAdd)
   '''
   needToAdd.sort(key=cond1)
   return (needToAdd)


def easyH(board,needToAdd, rawWords):
   for val in needToAdd:
      word = random.choice(rawWords[val[1]])
      check = board[val[0]:val[1] + val[0]]
      
      if not(check == len(check) * check[0]):
         can = False
         while not(can):
            can = True
            for x in range(len(word)):
               if check[x] =='-':
                  r = 100
               else:
                  if check[x].lower() != word[x].lower():
                     can = False
                     word = random.choice(rawWords[val[1]])
      board = board = board[:val[0]] + word + board[(val[0]+val[1]): ]

   return board


def transpose(board):
   global column
   return "".join([board[val::column] for val in range(column)]) 

def main():
   global row, column, board, blockLimit, foo, rawWords
   makeStructure()
   rawWords = dictInput(rawWords)
   needToAdd =findWordPositions(board)
   board = easyH(board, needToAdd, rawWords)





   print2D(board, row, column)


if __name__=="__main__":
    main()
#Siddhant Sood, 7, 2024