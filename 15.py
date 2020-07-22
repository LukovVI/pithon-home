def translate(n, c):#перевод из десятичной
    S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < c:
        return S[n]
    return str(translate(n//c, c)) + S[n%c]

def convert(num, to_base=10, from_base=10):
    S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    N = 0
    c = ""
    for i in range(len(str(num))):# перевод в десятичную
        N += S.index(num[-1-i])*from_base**i
    return str(translate(N, to_base))


