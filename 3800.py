#http://informatics.mccme.ru/mod/statements/view3.php?id=3962&chapterid=3800#1
#Рекурсия! Должна быть рекурсия!

#yes it works


def power(a, n):   #Функция возведения в степень
    if n == 0:     #Разбор случая, в ктором степень равна 0
        return 1
    return(a * power(a, n - 1)) #Рекурсия, возводим в n-1 (a^n = a * a^n-1)
a = input() #Входные данные
try: 
    a = int(a)    #Ну здесь все понятно
except:
    a = float(a)
    n = int(input())
    print(power(a, n))
else:
    n = int(input())
    print(power(a, n))
