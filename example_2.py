# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять колличество вхождений одной строки в другую.

string1 = 'Привет, Мир!'
string2 = 'и'
def str(string1, string2):
    t = 0
    for i in range(len(string1) - len(string2)):
        if(string1[i : i + len(string2)] == string2):
            t += 1
    return t
print(str(string1, string2))