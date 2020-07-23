import random 
random.seed(42)

def print_mimic(mimic_dict, word):
    S = [word]
    while len(S) < 200:
        if S[-1] in mimic_dict:
            S.append(random.choice(mimic_dict[S[-1]]))
        else:
            S.append(random.choice(mimic_dict[""]))
    return " ".join(S)