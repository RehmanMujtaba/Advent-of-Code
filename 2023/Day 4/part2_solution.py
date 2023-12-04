x = open(0).read().splitlines()

total = len(x)

tickets = [1]

def getScore(num):
    allNums = x[num - 1].split(":")[1].split("|")
    winningNums = [num for num in allNums[0].split(" ") if num]
    theNums = [num for num in allNums[1].split(" ") if num]
    score = 0
    for num in theNums:
        if num in winningNums:
            score += 1
    return score


for i in range(1, total + 1):
    score = getScore(i)
    for j in range(i, i + score + 1):
        if j < total:
            total += getScore(j)
    total += score
    print(total)

print(total)