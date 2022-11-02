inn = 94
inweights = [34, 7, 4, 25, 30, 27, 39]      # тест

def weight(n, weights):
    if n > (sum(weights)):
        print("no")
        # return ('No')

    signs = []
    startPoint = -1                         # Легаси
    num = len(weights)
    res = []
    flags = [0] * n                         # флаги уникальности полученной суммы
    for _ in range(num):
        signs.append(startPoint)            # num-разрядное чисто в троичной СС

    ctr = 0                                 #счётчик для выхода из while
    while ctr < (3 ** num) - 1:
        summa = 0
        signs[0] += 1                       # первое значение [-1, -1 .. -1] можно выкинуть, т.к. сумма заведомо будет отрицательна
        i = 0
        while signs[i] > 2 + startPoint:    # inc but in ternary
            signs[i] = startPoint
            signs[i + 1] += 1
            i += 1
        ctr += 1
        for j in range(num):
            summa += weights[j] * signs[j]      # считаем сумму
            if (summa > 0) and (summa <= n):    # Нам не надо запоминать суммы <0 и >n т.к. они нас не интересуют
                if flags[summa-1] == 0:
                    res.append(summa)
                    flags[summa-1] = 1

    res = sorted(res)
    # print (res)

    try:
        if res[n - 1] == n:
            print("Yes")
            # return ('Yes')

        else:
            print("no")
            # return ('No')

    except IndexError:
        print("no")
        # return ('No')


weight(inn, inweights)