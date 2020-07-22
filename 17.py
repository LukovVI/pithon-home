def multiplication_check_list(start = 10, stop = 99):
    t = 0
    f = 0
    for i in range(start, stop+1):
        for j in range(start, stop+1):
            if multiplication_check(i, j):
                t += 1
            else:
                f += 1
    print("Правильных результатов:", t)
    print("Неправильных результатов:", f)
    return

def simple_multiplication(x, y):
    return (100-(200-x-y))*100 + (100-x)*(100-y)


def multiplication_check(x, y):
    return simple_multiplication(x, y) == x*y
