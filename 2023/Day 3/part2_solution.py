x = open(0).readlines()

rowsize = len(x[0]) - 1
colomnsize = len(x)
total = 0
currCount = 0

def addNum(i, j):
    num = ""
    if j != 0 and x[i][j-1].isnumeric():
        if j -1 != 0 and x[i][j-2].isnumeric():
            num += x[i][j-2]
        num += x[i][j-1]
    # print(num)
    num += x[i][j]
    # print(num)
    if j != colomnsize - 1 and x[i][j+1].isnumeric():
        num += x[i][j+1]
        if j + 1 != colomnsize - 1 and x[i][j+2].isnumeric():
            num += x[i][j+2]
    # print(num)
    global currCount
    currCount += 1
    return int(num)

for i, line in enumerate(x):
    for j, char in enumerate(line):
        currCount = 0
        if char == "*":
            top = False
            bottom = False
            product = 1

            # Check Horizontal
            if j != 0 and line[j - 1].isnumeric(): 
                product *= addNum(i, j - 1)
            if j != rowsize - 1 and line[j + 1].isnumeric():
                product *= addNum(i, j + 1)
            # Check Vertical
            if i != 0 and x[i - 1][j].isnumeric(): 
                product *= addNum(i - 1, j)
                top = True
            if i != colomnsize - 1 and x[i + 1][j].isnumeric():
                product *= addNum(i + 1, j)
                bottom = True
            # Check Diagonal
            if i != 0 and j != 0 and x[i - 1][j - 1].isnumeric() and not top: 
                product *= addNum(i - 1, j - 1)
            if i != 0 and j != rowsize - 1 and x[i - 1][j + 1].isnumeric() and not top:
                product *= addNum(i - 1, j + 1)
            if i != colomnsize - 1 and j != 0 and x[i + 1][j - 1].isnumeric() and not bottom:
                product *= addNum(i + 1, j - 1)
            if i != colomnsize - 1 and j != rowsize - 1 and x[i + 1][j + 1].isnumeric() and not bottom:
                product *= addNum(i + 1, j + 1)
            if currCount == 2:
                total += product
                # print(product)
           
print(total)           