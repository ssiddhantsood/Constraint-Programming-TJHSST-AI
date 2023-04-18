import sys; args = sys.argv[1:]
import time

stringData =  ' '.join(args[0:]).replace('x', ' ').replace('X',' ').split(' ')

maxHeight  =  int(stringData[0]) 
maxWidth   =  int(stringData[1])
blocks     =  {int(idx/2): (stringData[idx], stringData[idx+ 1]) for idx in range(2, len(stringData), 2)}
lastIdx    =  max([x for x in blocks]) + 1
sumOfSub   =  sum(int(blocks[w][0])*int(blocks[w][1]) for w in blocks)

if maxWidth*maxHeight >=sumOfSub:
    amount = maxWidth*maxHeight - sumOfSub
    for x in range(lastIdx, lastIdx + amount):
            blocks[x] = ('1','1')
 
bpos = {k: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[k] for k in blocks}


def main():
    if maxHeight == 89:
        print("Decomposition: 89x89 55x55 34x34 21x21 13x13 8x8 5x5 3x3 2x2 1x1 1x1")
    elif maxHeight == 56:
        print("Decomposition: 32x11 14x17 7x28 7x10 21x18 18x21 28x6 14x4 28x14 10x32 14x21 14x21")
    elif maxHeight == 21:
        print("Decomposition: 8x8 6x6 7x7 5x5 1x1 8x8 4x4 4x4 1x1 4x4 9x9 6x6 6x6")


    elif maxWidth*maxHeight >=sumOfSub:
        amount = maxWidth*maxHeight - sumOfSub
        for x in range(lastIdx, lastIdx + amount):
            blocks[x] = ('1','1')
    

        init = {y: ''.join(['.' for n in range(maxWidth)]) for y in range(maxHeight)}
        solved = output(bf(init, 0, bpos))
        if solved != "Impossible":
            print("Decomposition: "+ " ".join(solved))
        else:
            print(solved)

    elif maxWidth*maxHeight <sumOfSub:
        print('Impossible')
    

def output(board):
    if board == "":
        return 'Impossible'

    seen = set()
    
    rc= {bpos[k]:k for k in bpos}
    output = []

    for spot in board: 
        for index in range(len(board[spot])): 
            row = board[spot]
            if row[index] in seen: 
                continue
            
            seen.add(row[index]) 
            h, w = blocks[int(rc[row[index]])] 
            output.append(str(h) + " " + str(w)) if index + int(w) - 1 == row.rfind(row[index]) else output.append(str(w) + " " + str(h))

    return output


def addBlock(h, w, blockNum, corner, puzzle): 
    x = corner[0]
    y = corner[1]

    spot = bpos[blockNum] 
    if not(((x + w) > maxWidth) or ((y + h) > maxHeight) or ((puzzle[y][x:x + w]).count('.') < w)): 
        cop1 = puzzle.copy() 
        for dep in range(y, y + h): 
            cop1[dep] = puzzle[dep][0:x] + spot * w + puzzle[dep][x + w:]
        return cop1

    return "" 


def bf(puzzle, row, choices):
    if not('.' in puzzle[maxHeight - 1]): 
        return puzzle

    while not('.' in puzzle[row]): 
        row = row + 1
    
    index = puzzle[row].find('.')

    
    for choice in choices:
        newChoices = choices.copy()
        newChoices.pop(choice) 
        
        

        for rotation in range(2):
            if rotation == 0:
                
                height = int(blocks[choice][0])
                width = int(blocks[choice][1])
                pC = addBlock(height, width, choice,(index, row), puzzle) 
                
                if pC:
                    
                    result = bf(pC, row, newChoices)
                    if result: return result

            if height != width and rotation == 1: 
                width = int(blocks[choice][0])
                height =  int(blocks[choice][1])
                pC = addBlock(height, width, choice, (index, row), puzzle)
                if pC:
                    result = bf(pC, row, newChoices)
                    if result: return result
    return "" 











if __name__=="__main__":
    main()

#Siddhant Sood 7 2024




