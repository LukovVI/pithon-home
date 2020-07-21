n = 1
f = 0
if os.path.isfile(file_name):#проверка существования
    f = open(file_name).readlines()# построчное считывание
    # поиск первой непустой строки и проверка номера последнего события
    for i in f:
        i = i.split()
        if i:
            n = int(i[1]) + 1
            break
open(file_name, "w").write("event " + str(n) + " - '" + event + "'\n")# запись нового события
if f:
    open(file_name, "a").writelines(f)# запись старых событий