s = 'ABCD'
numRows = 2

str_array = [[] for _ in range(numRows)]
i = 0
direction = 0
for char in s:
    match direction:
        case 0:
            str_array[i].append(char)
            i = i + 1
        case 1:
            for k in range(numRows):
                if k == i:
                    str_array[k].append(char)
                else:
                    if i > 0:
                        str_array[k].append(' ')
            i = i - 1
    if i == numRows:
        i = numRows - 2
        direction = 1
    if i == 0:
        i = 1
        direction = 0





for item in str_array:
    print(item)

result = ''
for string in str_array:
            for char in string:
                if char != ' ':
                    result = result + char
print(result)