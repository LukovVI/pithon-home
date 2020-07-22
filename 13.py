def fi(L0, L1, n):
    L = [L0, L1]
    for i in range (1, n):
        L.append(L[0]+L[1])
        L = L[1:]# срез последних 2-х элементов для избежания ошибки памяти
    return Decimal(L[1])/L[0]