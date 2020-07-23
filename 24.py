def derivative(f, x0=0):
    dx = 0.0000001
    return round((f(x0 + dx) - f(x0)) / dx, 3)

