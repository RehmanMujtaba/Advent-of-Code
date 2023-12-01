import sys
import fileinput


number_mapping = {
        'one': "1",
        'two': "2",
        'three': "3",
        'four': "4",
        'five': "5",
        'six': "6",
        'seven': "7",
        'eight': "8",
        'nine': "9"
    }

total = 0
for line in fileinput.input():
    curr_slice = ""
    found = False
    for char in line:
        if found:
            break
        elif char.isnumeric():
            num1 = char
            break
        else:
            curr_slice += char
        for key in number_mapping:
            if key in curr_slice:
                num1 = number_mapping[key]
                found = True
                break

                
    curr_slice = ""
    found = False
    for char in line[::-1]:
        if found:
            break
        elif char.isnumeric():
            num2 = char
            break
        else:
            curr_slice += char
        for key in number_mapping:
            if key in curr_slice[::-1]:
                num2 = number_mapping[key]
                found = True
                break
            else:
                continue
            break
            

    
    sum1 = num1 + num2
    total +=  int(sum1)
print(total)    


fileinput.close()