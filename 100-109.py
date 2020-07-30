#100
n = int(input())
m = int(input())
dice = list([1] * n + [2]*m)
results = [1 for i in range(400000) if random.choice(dice) == 1]
print(str(round(sum(results)/4000, 1))+"%")

#101
a = input().split()
b = list(map(int, input().split()))
c = input().split()
dice = []
for i in range(len(a)):
    dice.extend([a[i]] * b[i])
results = [1 for i in range(400000) if random.choice(dice) in  c]
print(str(round(sum(results)/4000, 1))+"%")

#102
import random
n = int(input())
dice = list(range(n))
I = 0
for i in range(400000):
    random.shuffle(dice)
    for j in range(n):
        if dice[j] == j:
            I += 1
            break
print(str(round(I/4000, 1))+"%")

#103
a = list(map(int, sorted(input().split())))
m = {}
mr = {}
d = 0
for i in a:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1
for i in m:
    if m[i] in mr:
        mr[m[i]].append(i)
    else:
        mr[m[i]] = [i]
print(*mr[sorted(mr)[-1]])

#104
n = list(map(int,input().split()))
if len(n) < 2:
    print('Ошибка. Кучек слишком мало, чтобы можно было решить задачу.')
elif (len(n) == 2 and n[0]!=n[1]) or (not len(n)%2 and sum(n)%2):
    print('Кучки нельзя уравнять')
else:
    N1 = sum(n)
    while len(set(n)) != 1:
        n.sort()
        n[0],n[1] = n[0]+1, n[1]+1
    print(int((sum(n)-N1)/2), n[0])

# 105
def check_chess(num_1, num_2):
    num_1, num_2 = num_1 % 2, num_2 % 2
    if (num_1 + num_2) % 2:
        return True
    return False
a, b = list(map(int, input().split()))
print("Замостить можно" if check_chess(a,b) else "Замостить нельзя")

#106
num = int(input())
some_l = list()
while num > 9:
    some_l.append(9)
    num -= 9
some_l.append(num)
print(*reversed(some_l), sep="")

#107
a = list(map(int, input().split()))
p = 1
for i in range(len(a)-1):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            p *= -1
print(p)

#108
b = [1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12, 15, 14, 13]
a = []
for i in range(4):
    a.extend(list(map(int, input().split())))
def chet(a):
    p = 1
    for i in range(len(a)-1):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                p *= -1
    return p
if chet(a) == chet(b):
    print("Бинго!")
else:
    print("Не повезло...")

#109
class animal():
    def __init__(self, name):
        self.name = name
    def echo(self, name):
        print (str(name.upper()))
        print (name)
        print (str(name.lower()))