s = input()
def fix_start(s):
    m = s[0]# начало создания нового слова
    for i in range(1, len(s)):
        if s[i] != s[0]:# проверка соответствия символов
            m = m + s[i]#дописать букву
        else:
            m = m + "*"# дописать символ
    return m
print (fix_start(s))