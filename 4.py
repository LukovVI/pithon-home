def maxId(L):
    l = list(map(int, L)) #превращение всех элементов в числа
    return l.index(max(l))
