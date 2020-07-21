s = input()
def both_ends(s):
    if len(s) > 1:
        return str(s[0:2] + s[-2:])
    return str("")

print (both_ends(s))