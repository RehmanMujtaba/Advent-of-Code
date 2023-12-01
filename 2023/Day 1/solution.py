import sys
import fileinput


total = 0
for line in fileinput.input():
    for char in line:
        if char.isnumeric():
            num1 = char
            break
    for char in line[::-1]:
        if char.isnumeric():
            num2 = char
            break

    sum = num1 + num2
    total +=  int(sum)
print(total)    


fileinput.close()