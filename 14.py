def super_L(n):
    if n % 6 == 0:
        return (super_L(n//6)**6 - 6 * (-1)**(n//6) * super_L(n//6)**4 + 9 * super_L(n//6)**2 - 2 * (-1)**(n//6))
    if n % 5 == 0:
        return (super_L(n//5)**5 - 5 * (-1)**(n//5) * super_L(n//5)**3 + 5 * super_L(n//5))
    if n % 4 == 0:
        return (super_L(n//4)**4 - 4 * (-1)**(n//4) * super_L(n//4)**2 + 2)
    if n % 3 == 0:
        return (super_L(n//3)**3 - 3 * (-1)**(n//3) * super_L(n//3))
    if n % 2 == 0:
        return (super_L(n//2)**2 - 2 * (-1)**(n//2))
    fib1 = 2
    fib2 = 1
    for _ in range(n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1

