#http://informatics.mccme.ru/mod/statements/view3.php?id=3962&chapterid=3800#1
#Рекурсия! Должна быть рекурсия!

#yes it works


def power(a, n):
    if n == 0:
        return 1
    return(a * power(a, n - 1))
a = input()
try:
    a = int(a)
except:
    a = float(a)
    n = int(input())
    print(power(a, n))
else:
    n = int(input())
    print(power(a, n))
