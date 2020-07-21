i = input()
if os.path.isfile(i):# проверка существования файла
    print("CONTENT:", open(i).read(), sep = "\n")
elif os.path.exists(i):# проверка существования пути
    print("ERROR:\nЭто каталог, а не файл")
else:
    print("ERROR:\nФайл не существует")