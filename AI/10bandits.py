import math; import random

numberArms = 10
def bandit(testNum, armIdx, pullVal):
    global numberArms, pullsNumber, avgReward, ucb
    if testNum == 0:
        numberArms = armIdx
        pullsNumber = [0] * numberArms
        avgReward = [3] * numberArms
        ucb = [0.0] * numberArms
        return 0

    pullsNumber[armIdx] += 1
    avgReward[armIdx] += (pullVal - avgReward[armIdx]) / pullsNumber[armIdx]

    for i in range(numberArms):
        if pullsNumber[i] > 0: ucb[i] = avgReward[i] + 0.8 * math.sqrt(2 * math.log(testNum) / pullsNumber[i])
        else: ucb[i] = float('inf')  

    return ucb.index(max(ucb))
# Siddhant Sood Period 7 2024
