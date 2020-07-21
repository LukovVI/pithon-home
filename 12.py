check = []
def numerics(n):# перевод числа в список
    return list(map(int, str(n)))

def kaprekar_step(L):# преобразование списска в разность чисел составленных из него
    L = "".join(sorted(map(str, L)))
    return abs(int(L) - int(L[::-1]))

def kaprekar_check(n):# проверка на возможность проведения операции
    if n in [100, 1000, 100000]:
        return False
    if len(set(numerics(n))) == 1:# проверка разности цифр
        return False
    if not len(numerics(n)) in [3, 4, 6]:# проверка порядка
        return False
    return True

def kaprekar_loop(n):
    global check
    if n in check:# проверка на упоминание числа
        print("Следующее число - ", n,", кажется процесс зациклился...", sep = "")
    elif not kaprekar_check(n):
        print("Ошибка! На вход подано число ", n, ", не удовлетворяющее условиям процесса Капрекара", sep = "")
    elif n in [495, 6174, 549945, 631764]:
        print(n)
    else:
        print(n)
        check.append(n)# дополнение списка упоминаний
        kaprekar_loop(kaprekar_step(numerics(n)))# запуст рекурсии