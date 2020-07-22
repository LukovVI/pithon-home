def bruteforce(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    for i in range(len(alphabet) - 1, 0, -1):
        print(caesar(text, i, alphabet))


def caesar(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text.upper()
    L = ""
    for i in text:
        if i in alphabet:
            L += alphabet[(alphabet.index(i) + key) % len(alphabet)]
    return L