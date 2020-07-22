def multiplication_check_list(start=10, stop=99, length_check = True):
    t = 0
    f = 0
    for i in range(start, stop+1):
        for j in range(start, stop+1):
            if wisdom_multiplication(i, j, length_check) == i*j:
                t += 1
            else:
                f += 1
    print("Правильных результатов:", t)
    print("Неправильных результатов:", f)
    return

def wisdom_multiplication(x, y, length_check = True):
    a, b = 100-x, 100-y
    c = 100-a-b
    d = str(a*b)
    if length_check and len(d) < 2:
        d = "0" + d
    return int(str(c) + d)
