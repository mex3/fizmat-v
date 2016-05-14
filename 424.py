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
kalkal = []
need = []
first = 1
qwe = []
mess = ["January","February","March","April","May","June","July","August","September","October","November","December"]
while mes <= 12:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        days = 31
    elif mes == 2:
        if l == 0:
            days = 28
        else:
            days = 29
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
    for m in range(b):
        for i in range(c):
            if kal[m][i] == ' ':
                kal[m][i] = '  '
    print(mess[mes-1])
    if len(kal) < 6:
        kal.append(['  ','  ','  ','  ','  ','  ','  '])
    Transpose(kal)
    kalkal += [kal]
    ned = 1
    day = 1
    dayses = 1
    kal = []
    need = []
    first = 1
    mes += 1
for c in range (k):
    for m in range (12):
        qwe += [kalkal[m][c] + ["   "]]
n = 0
tyg = []
tyr = []
tygr = []
print(kalkal)
while n < 12:
    for j in range(7):
        for i in range(len(kalkal[n])):
            tyg += [kalkal[n][i][j]]
        tyr += [tyg]
        tyg = []
    tygr += [tyr]
    tyr = []
    n += 1
hj = ""
nd = ""
for i in range(7):
    for j in range(12):
        fusk = " ".join(tygr[j][i])
        if j % k == 0:
            1
            #nd = '\n'
        else:
            nd = ''
        print(fusk, end=nd)
    print("")
