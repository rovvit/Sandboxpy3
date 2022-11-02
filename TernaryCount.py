# Increment in ternary cycle
num = 3                        # число разрядов
trenary = []                    # список 0-2
for _ in range (num):
    trenary.append(-1)
n = 0
while n < 3**num-1:
    print(trenary)
    trenary[0] += 1
    for i in range(num):
        if trenary[i] > 1:
            trenary[i] = -1
            trenary[i+1] += 1
    n+=1



print(trenary)