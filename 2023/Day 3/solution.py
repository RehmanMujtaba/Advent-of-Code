x = open(0).readlines()

rowsize = len(x[0]) - 1
colomnsize = len(x)

total = 0

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
    print(num)
    return int(num)

for i, line in enumerate(x):
    for j, char in enumerate(line):
        if not char.isnumeric() and char != "." and char != "\n":
            top = False
            bottom = False
            # Check Horizontal
            if j != 0 and line[j - 1].isnumeric(): 
                total += addNum(i, j - 1)
            if j != rowsize - 1 and line[j + 1].isnumeric():
                total += addNum(i, j + 1)
            # Check Vertical
            if i != 0 and x[i - 1][j].isnumeric(): 
                total += addNum(i - 1, j)
                top = True
            if i != colomnsize - 1 and x[i + 1][j].isnumeric():
                total += addNum(i + 1, j)
                bottom = True
            # Check Diagonal
            if i != 0 and j != 0 and x[i - 1][j - 1].isnumeric() and not top: 
                total += addNum(i - 1, j - 1)
            if i != 0 and j != rowsize - 1 and x[i - 1][j + 1].isnumeric() and not top:
                total += addNum(i - 1, j + 1)
            if i != colomnsize - 1 and j != 0 and x[i + 1][j - 1].isnumeric() and not bottom:
                total += addNum(i + 1, j - 1)
            if i != colomnsize - 1 and j != rowsize - 1 and x[i + 1][j + 1].isnumeric() and not bottom:
                total += addNum(i + 1, j + 1)
print(total)           