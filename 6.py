s = open(sheet).readlines()
lict = []
for i in s:
    i.strip()#удаление знака переноса строки
    i = i.split()# разделение на слова
    if i[-1] == "(автомат)" or i[-1] == "(экзамен)":# проверка вида оценивания
        lict.append(int(i[-2]))# запись оценки в список

if sum(lict) / len(lict) == float(open(mean).read()):#cравнение средней оценки с заданным числом
    print("OK")
else:
    print("ERROR")