x = open(0).read().splitlines()
total = 0

for line in x:
    allNums = line.split(":")[1].split("|")
    winningNums = [num for num in allNums[0].split(" ") if num]
    theNums = [num for num in allNums[1].split(" ") if num]
    score = 0

    for num in theNums:
        if num in winningNums and score == 0:
            score = 1
        elif num in winningNums:
            score *= 2
    
    total += score

print(total)
            