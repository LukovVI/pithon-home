def wisdom_multiplication(x, y, length_check = True):
    a, b = 100-x, 100-y
    c = 100-a-b
    d = str(a*b)
    if length_check and len(d) < 2:
        d = "0" + d
    return int(str(c) + d)