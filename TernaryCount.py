# Increment in ternary cycle
num = 3                        # число разрядов
trenary = []                    # список 0-2
startPoint = 0
for _ in range (num):
    trenary.append(startPoint)
n = 0
while n < 3**num-1:
    print(trenary)
    trenary[0] += 1             # инкремент
    # for i in range(num):        # проверка на перенос единицы в следующий разряд
    #     if trenary[i] > 1:
    #         trenary[i] = -1
    #         trenary[i+1] += 1
    i = 0
    while trenary[i] > 2 + startPoint:
        trenary[i] = startPoint
        trenary[i+1] += 1
        i += 1

    n+=1


