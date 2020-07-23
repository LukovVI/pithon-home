def list_pull(L):
    m = []
    for i in L:
        if not type(i) == list:
            m.append(i)
        else:
            m.extend(list_pull(i))
    return m
