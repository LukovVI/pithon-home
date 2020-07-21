n = int(input())
def donuts(n):
    if n <= 9:
        return str("Всего пончиков: " + str(n))
    return str("Всего пончиков: много")
print (donuts(n))