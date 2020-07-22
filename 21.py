def jarriquez_encryption(text, key, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", reverse=False):
    key = list(str(key))
    r = 1
    if reverse:
        r = -1
    key = list(map(lambda x: r*int(x), key))
    text = text.upper()
    L = ""
    tex = ""
    for i in text:
        if i in alphabet:
            tex += i
    for i in range(len(tex)):
        L += alphabet[(alphabet.index(tex[i]) + key[i%len(key)])%len(alphabet)]
    return L
