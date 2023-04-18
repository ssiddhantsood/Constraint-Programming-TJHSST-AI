import sys
sys.setrecursionlimit(200000000)
CACHE = {}

def change(n, coinList):
	w  = 0 
	if n == 0:
		return 1
	if len(coinList) == 0 or n <0:
		return 0
	key = (n, *coinList)
	if key in CACHE: return CACHE[key]

	CACHE[key] = change(n,coinList[1:]) + change(n-coinList[0],coinList)

	return change(n,coinList[1:]) + change(n-coinList[0],coinList)

answer = str(change(10000, [100,50,25,10,5,1]))
print(answer)
