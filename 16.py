def simple_multiplication(x, y):
    return (100-(200-x-y))*100 + (100-x)*(100-y)


def multiplication_check(x, y):
    return simple_multiplication(x, y) == x*y
