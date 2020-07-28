#  70
def rotor(symbol, n, reverse=False):
    forward = ({'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I',
                'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R',
                'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'},
               {'A': 'E', 'E': 'L', 'L': 'T', 'T': 'P', 'P': 'H', 'H': 'Q', 'Q': 'X', 'X': 'R', 'R': 'U',
                'U': 'A', 'B': 'K', 'K': 'N', 'N': 'W', 'W': 'B', 'C': 'M', 'M': 'O', 'O': 'Y', 'Y': 'C',
                'D': 'F', 'F': 'G', 'G': 'D', 'I': 'V', 'V': 'I', 'J': 'Z', 'Z': 'J', 'S': 'S'},
               {'F': 'I', 'I': 'X', 'X': 'V', 'V': 'Y', 'Y': 'O', 'O': 'M', 'M': 'W', 'W': 'F', 'C': 'D',
                'D': 'K', 'K': 'L', 'L': 'H', 'H': 'U', 'U': 'P', 'P': 'C', 'E': 'S', 'S': 'Z', 'Z': 'E',
                'B': 'J', 'J': 'B', 'G': 'R', 'R': 'G', 'N': 'T', 'T': 'N', 'A': 'A', 'Q': 'Q'},
               {'A': 'B', 'B': 'D', 'D': 'H', 'H': 'P', 'P': 'E', 'E': 'J', 'J': 'T', 'T': 'A', 'N': 'N',
                'C': 'F', 'F': 'L', 'L': 'V', 'V': 'M', 'M': 'Z', 'Z': 'O', 'O': 'Y', 'Y': 'Q', 'Q': 'I',
                'I': 'R', 'R': 'W', 'W': 'U', 'U': 'K', 'K': 'X', 'X': 'S', 'S': 'G', 'G': 'C'}
               )
    back = ({'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I',
             'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R',
             'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'},
            {'A': 'U', 'U': 'R', 'R': 'X', 'X': 'Q', 'Q': 'H', 'H': 'P', 'P': 'T', 'T': 'L', 'L': 'E',
             'E': 'A', 'B': 'W', 'W': 'N', 'N': 'K', 'K': 'B', 'C': 'Y', 'Y': 'O', 'O': 'M', 'M': 'C',
             'D': 'G', 'G': 'F', 'F': 'D', 'I': 'V', 'V': 'I', 'J': 'Z', 'Z': 'J', 'S': 'S'},
            {'F': 'W', 'W': 'M', 'M': 'O', 'O': 'Y', 'Y': 'V', 'V': 'X', 'X': 'I', 'I': 'F', 'C': 'P',
             'P': 'U', 'U': 'H', 'H': 'L', 'L': 'K', 'K': 'D', 'D': 'C', 'E': 'Z', 'Z': 'S', 'S': 'E',
             'B': 'J', 'J': 'B', 'G': 'R', 'R': 'G', 'N': 'T', 'T': 'N', 'A': 'A', 'Q': 'Q'},
            {'C': 'G', 'G': 'S', 'S': 'X', 'X': 'K', 'K': 'U', 'U': 'W', 'W': 'R', 'R': 'I', 'I': 'Q',
             'Q': 'Y', 'Y': 'O', 'O': 'Z', 'Z': 'M', 'M': 'V', 'V': 'L', 'L': 'F', 'F': 'C', 'N': 'N',
             'A': 'T', 'T': 'J', 'J': 'E', 'E': 'P', 'P': 'H', 'H': 'D', 'D': 'B', 'B': 'A'}
            )
    if reverse:
        return back[n][symbol]
    else:
        return forward[n][symbol]

# 71
def reflector(symbol, n):
    REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
                  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
                  3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
                  4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'}
    return REFLECTORS[n][REFLECTORS[0].index(symbol)]

#72
def rotor(symbol, n, reverse=False):
    forward = ({'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I',
                'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R',
                'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'},
               {'A': 'E', 'E': 'L', 'L': 'T', 'T': 'P', 'P': 'H', 'H': 'Q', 'Q': 'X', 'X': 'R', 'R': 'U',
                'U': 'A', 'B': 'K', 'K': 'N', 'N': 'W', 'W': 'B', 'C': 'M', 'M': 'O', 'O': 'Y', 'Y': 'C',
                'D': 'F', 'F': 'G', 'G': 'D', 'I': 'V', 'V': 'I', 'J': 'Z', 'Z': 'J', 'S': 'S'},
               {'F': 'I', 'I': 'X', 'X': 'V', 'V': 'Y', 'Y': 'O', 'O': 'M', 'M': 'W', 'W': 'F', 'C': 'D',
                'D': 'K', 'K': 'L', 'L': 'H', 'H': 'U', 'U': 'P', 'P': 'C', 'E': 'S', 'S': 'Z', 'Z': 'E',
                'B': 'J', 'J': 'B', 'G': 'R', 'R': 'G', 'N': 'T', 'T': 'N', 'A': 'A', 'Q': 'Q'},
               {'A': 'B', 'B': 'D', 'D': 'H', 'H': 'P', 'P': 'E', 'E': 'J', 'J': 'T', 'T': 'A', 'N': 'N',
                'C': 'F', 'F': 'L', 'L': 'V', 'V': 'M', 'M': 'Z', 'Z': 'O', 'O': 'Y', 'Y': 'Q', 'Q': 'I',
                'I': 'R', 'R': 'W', 'W': 'U', 'U': 'K', 'K': 'X', 'X': 'S', 'S': 'G', 'G': 'C'}
               )
    back = ({'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I',
             'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R',
             'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'},
            {'A': 'U', 'U': 'R', 'R': 'X', 'X': 'Q', 'Q': 'H', 'H': 'P', 'P': 'T', 'T': 'L', 'L': 'E',
             'E': 'A', 'B': 'W', 'W': 'N', 'N': 'K', 'K': 'B', 'C': 'Y', 'Y': 'O', 'O': 'M', 'M': 'C',
             'D': 'G', 'G': 'F', 'F': 'D', 'I': 'V', 'V': 'I', 'J': 'Z', 'Z': 'J', 'S': 'S'},
            {'F': 'W', 'W': 'M', 'M': 'O', 'O': 'Y', 'Y': 'V', 'V': 'X', 'X': 'I', 'I': 'F', 'C': 'P',
             'P': 'U', 'U': 'H', 'H': 'L', 'L': 'K', 'K': 'D', 'D': 'C', 'E': 'Z', 'Z': 'S', 'S': 'E',
             'B': 'J', 'J': 'B', 'G': 'R', 'R': 'G', 'N': 'T', 'T': 'N', 'A': 'A', 'Q': 'Q'},
            {'C': 'G', 'G': 'S', 'S': 'X', 'X': 'K', 'K': 'U', 'U': 'W', 'W': 'R', 'R': 'I', 'I': 'Q',
             'Q': 'Y', 'Y': 'O', 'O': 'Z', 'Z': 'M', 'M': 'V', 'V': 'L', 'L': 'F', 'F': 'C', 'N': 'N',
             'A': 'T', 'T': 'J', 'J': 'E', 'E': 'P', 'P': 'H', 'H': 'D', 'D': 'B', 'B': 'A'}
            )
    if reverse:
        return back[n][symbol]
    else:
        return forward[n][symbol]


def reflector(symbol, n):
    mirrows = ({'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I',
                'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R',
                'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'},
               {'A': 'Y', 'Y': 'A', 'B': 'R', 'R': 'B', 'C': 'U', 'U': 'C', 'D': 'H', 'H': 'D', 'E': 'Q',
                'Q': 'E', 'F': 'S', 'S': 'F', 'G': 'L', 'L': 'G', 'I': 'P', 'P': 'I', 'J': 'X', 'X': 'J',
                'K': 'N', 'N': 'K', 'M': 'O', 'O': 'M', 'T': 'Z', 'Z': 'T', 'V': 'W', 'W': 'V'})
    return mirrows[n][symbol]


def enigma(text, ref, rot1, rot2, rot3):
    encripted = ''
    for symbol in text:
        if symbol.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            encripted += rotor(rotor(rotor(reflector(rotor(rotor(rotor(symbol.upper(), rot3), rot2),
                                                           rot1), ref), rot1, reverse=True), rot2, reverse=True), rot3, reverse=True)
    return encripted


#73
rotors = {1: ('AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'),
          2: ('FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'),
          3: ('ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N'),
          4: ('AEPLIYWCOXMRFZBSTGJQNH', 'DV', 'KU'),
          5: ('AVOLDRWFIUQ', 'BZKSMNHYC', 'EGTJPX'),
          6: ('AJQDVLEOZWIYTS', 'CGMNHFUX', 'BPRK'),
          7: ('ANOUPFRIMBZTLWKSVEGCJYDHXQ'),
          8: ('AFLSETWUNDHOZVICQ', 'BKJ', 'GXY', 'MPR'),
          'beta': ('ALBEVFCYODJWUGNMQTZSKPR', 'HIX'),
          'gamma': ('AFNIRLBSQWVXGUZDKMTPCOYJHE'),
          }

reflectors = {1: ('AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW'),
              2: ('AF', 'BV', 'CP', 'DJ', 'EI', 'GO', 'HY', 'KR', 'LZ', 'MX', 'NW', 'TQ', 'SU'),
              3: ('AE', 'BN', 'CK', 'DQ', 'FU', 'GY', 'HW', 'IJ', 'LO', 'MP', 'RX', 'SZ', 'TV'),
              4: ('AR', 'BD', 'CO', 'EJ', 'FN', 'GT', 'HK', 'IV', 'LM', 'PW', 'QZ', 'SX', 'UY')
              }

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def rotor(symbol, n, reverse=False):
    if not n:
        return symbol
    for chain in rotors[n]:
        if symbol in chain:
            return chain[(chain.index(symbol)+1 * (1, -1)[reverse]) % len(chain)]


def reflector(symbol, n):
    if not n:
        return symbol
    for chain in reflectors[n]:
        if symbol in chain:
            return chain[chain.index(symbol)-1]


def shift(symbol, n):
    if not n:
        return symbol
    return alphabet[(alphabet.index(symbol) + n) % len(alphabet)]


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    text = [i for i in text.upper() if i in alphabet]
    r_s = [(rot1, shift1), (rot2, shift2), (rot3, shift3)]
    for i in range(len(text)):
        for rot in r_s[::-1]:
            text[i] = shift(text[i], rot[1])
            text[i] = rotor(text[i], rot[0])
            text[i] = shift(text[i], -rot[1])
        text[i] = reflector(text[i], ref)
        for rot in r_s:
            text[i] = shift(text[i], rot[1])
            text[i] = rotor(text[i], rot[0], True)
            text[i] = shift(text[i], -rot[1])
    return ''.join(text)

#74
def rotor(symbol, n, sh, reverse=False):
    rotors = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
              2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
              3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
              }
    if reverse:
        return ''.join([rotors[0][(rotors[n].index(rotors[0]
                                                   [(rotors[0].index(i)+sh) % len(rotors[0])])-sh) % len(rotors[n])]
                        for i in symbol])
    else:
        return ''.join([rotors[0][(rotors[0].index(rotors[n]
                                                   [(rotors[0].index(i)+sh) % len(rotors[0])])-sh) % len(rotors[0])]
                        for i in symbol])


def reflector(symbol, n):
    reflectors = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
                  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
                  }
    return ''.join([reflectors[n][reflectors[0].index(i)] for i in symbol])


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, x=[]):
    a, b = [[rot3, rot2, rot1], [shift3, shift2, shift1]], {2: 5, 1: 17, 3: 22}

    for z in text.upper():
        if z in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            a[1][0] += 1
            if b[a[0][0]] == a[1][0]:
                a[1][1] += 1

            for i in range(len(a[0])):
                z = rotor(z, a[0][i], a[1][i])
            z = reflector(z, ref)
            for i in range(len(a[0])-1, -1, -1):
                z = rotor(z, a[0][i], a[1][i], reverse=True)
            x += z

            if b[a[0][1]] == a[1][1]+1:
                a[1][1] += 1
                a[1][2] += 1
            for i in range(len(a[1])):
                if a[1][i] == 26:
                    a[1][i] -= 26

    return ''.join(x)

#75
def caesar(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    return ''.join([alphabet[(alphabet.find(ch) + key) % len(alphabet)] for ch in text.upper() if ch in alphabet])


def rotor(symbol, n, reverse=False):
    rotors = {
        1: ['AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'],
        2: ['FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'],
        3: ['ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N'],
        4: ['AEPLIYWCOXMRFZBSTGJQNH', 'DV', 'KU'],
        5: ['AVOLDRWFIUQ)(BZKSMNHYC', 'EGTJPX'],
        6: ['AJQDVLEOZWIYTS', 'CGMNHFUX', 'BPRK'],
        7: ['ANOUPFRIMBZTLWKSVEGCJYDHXQ'],
        8: ['AFLSETWUNDHOZVICQ', 'BKJ', 'GXY', 'MPR'],
        'beta': ['ALBEVFCYODJWUGNMQTZSKPR', 'HIX'],
        'gamma': ['AFNIRLBSQWVXGUZDKMTPCOYJHE'],
    }
    if n == 0:
        return symbol
    sign = -1 if reverse else 1
    for i in rotors[n]:
        if symbol in i:
            return i[(i.index(symbol) + sign) % len(i)]


def reflector(symbol, n):
    reflectors = {
        1: ['AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW'],
        2: ['AF', 'BV', 'CP', 'DJ', 'EI', 'GO', 'HY', 'KR', 'LZ', 'MX', 'NW', 'TQ', 'SU'],
    }
    if n == 0:
        return symbol
    for i in reflectors[n]:
        if symbol in i:
            return i[(i.index(symbol) + 1) % 2]


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
    pairs = pairs.upper().split()
    check_pairs = ''.join([i for i in pairs])
    for i in check_pairs:
        if check_pairs.count(i) > 1:
            return "Извините, невозможно произвести коммутацию"
    shift_rotor = {
        1: 17,
        2: 5,
        3: 22,
        4: 10,
        5: 0,
        6: (0, 13),
        7: [0, 13],
        8: [0, 13],
    }
    rotors = [rot3, rot2, rot1]
    shifts = [shift3, shift2, shift1]
    encrypt = ''
    for char in text.upper():
        if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            continue
        for i in pairs:
            if char == i[0]:
                char = i[1]
                break
            elif char == i[1]:
                char = i[0]
                break
        shifts[0] = (shifts[0] + 1) % 26
        for i in range(len(shifts) - 1):
            if shifts[i + 1] == shift_rotor[rotors[i + 1]] - 1:
                if shifts[-1] == shift_rotor[rotors[i + 1]] - 1:
                    continue
                shifts[i + 1] = (shifts[i + 1] + 1) % 26
            if rotors[i] in [6, 7, 8]:
                if shifts[i] in shift_rotor[rotors[i]]:
                    shifts[i + 1] = (shifts[i + 1] + 1) % 26
            if shifts[i] == shift_rotor[rotors[i]]:
                shifts[i + 1] = (shifts[i + 1] + 1) % 26
        for i in range(len(rotors)):
            char = caesar(
                rotor(caesar(char, shifts[i]), rotors[i]), -shifts[i])
        char = reflector(char, ref)
        for j in range(len(rotors) - 1, -1, -1):
            char = caesar(
                rotor(caesar(char, shifts[j]), rotors[j], reverse=True), -shifts[j])
        for i in pairs:
            if char == i[0]:
                char = i[1]
                break
            elif char == i[1]:
                char = i[0]
                break
        encrypt += char
    return encrypt
