#http://informatics.mccme.ru/mod/statements/view3.php?chapterid=424#1
d, k, l = map(int, input().split())
#print(d,k,l)
j = []
h = 1 #счёт дней недели
z = 0 #счёт дней месяца
mes = 1 #счёт номера месяца
s = 0 #ограничение по неделям - снос столбцов
n = l
c = []
if k == 0:
    while mes <= 12:
        if mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            m = 31
        else:
            m = 30        
        while z <= m:
            s += 7
            if s > m:
                s = m
                k = 1
            while n <= s:
                c += [h]
                h += 1
                z += 1
                n += 1
            j += [[c]]
            c = []
            if k == 1:
                break
        mes += 1
        print(j)
        j = []
# короче сейчас эта прога делает вписок из первого месяца, причём построчно(т.е. горизонтально), как его перевернуть? -
# - типа транспонирования матрицы...
