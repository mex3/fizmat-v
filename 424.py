#http://informatics.mccme.ru/mod/statements/view3.php?chapterid=424#1
d, l, k = map(int, input().split())
mes = 1
ned = 1
day = 1
dayses = 1
kal = []
need = []
first = 1
if l == 0:
    while mes <= 12:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            days = 31
        elif mes == 2:
            days = 28
        else:
            days = 30
        while ned <= 4:
            while dayses <= 7*ned:
                if day < days+1:
                    need += [day]
                    if first == 1 and day == 7-d+1:
                        dayses = 1
                        day += 1
                        break
                    day += 1
                dayses += 1
            if need != []:
                kal += [need]
            need = []
            if first != 1:
                ned += 1
            first = 0
        while days >= day > 28:
            need += [day]
            day += 1
            dayses += 1
        if need != []:
            kal += [need]
        ######################
        print(kal)          ##
        ######################
        ned = 1
        day = 1
        dayses = 1
        d = len(kal[len(kal)-1]) + 1
        kal = []
        need = []
        first = 1
        mes += 1
# короче сейчас эта прога делает списки из всех месяцев, причём построчно(т.е. горизонтально), как их перевернуть? -
# - типа транспонирования матрицы...
