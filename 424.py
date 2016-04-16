#http://informatics.mccme.ru/mod/statements/view3.php?chapterid=424#1
def Transpose(g):
    global b,c
    h = ""
    e = 0    
    for v in range(c):
        for i in range(b):
            s = g[i]
            h += s[e] + " "
        print(h[:-1])
        h = ""
        e += 1
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
                    if day < 10:
                        need += [" " + str(day)]
                    else:
                        need += [str(day)]
                    if first == 1 and day == 7-d+1:
                        dayses = 1
                        day += 1
                        break
                    day += 1
                dayses += 1
            if first == 1:
                for i in range (7 - len(need)):
                    need = [" "] + need
            if need != []:
                kal += [need]
            need = []
            if first != 1:
                ned += 1
            first = 0
        if len(kal[-1]) < 7:
            d = len(kal[-1]) + 1
            for i in range (7 - len(kal[-1])):
                kal[-1] = kal[-1] + [" "]
        while days >= day > 28:
            need += [str(day)]
            day += 1
            dayses += 1
        if need != []:
            kal += [need]
        if len(kal[-1]) < 7:
            d = len(kal[-1]) + 1
            for i in range (7 - len(kal[-1])):
                kal[-1] = kal[-1] + [" "]
        if kal[-1][-1] != ' ':
            d = 1
        c = 7
        b = len(kal)
        for k in range(b):
            for i in range(c):
                if kal[k][i] == ' ':
                    kal[k][i] = '  '
        Transpose(kal)
        ned = 1
        day = 1
        dayses = 1
        kal = []
        need = []
        first = 1
        mes += 1
