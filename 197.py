#http://informatics.mccme.ru/mod/statements/view.php?id=197#1
z = x = input()
i = 1
w = 0
while w == 0:
    o = str(i)
    q = 0
    x = z
    while q < len(o) and w == 0:
        if x.find(o[q]) != -1:
            p = x.find(o[q]) + 1
            x = x[p:]
            q += 1
        else:
            w = 1
        i += 1
m = i - 1
print(m)
# вот программа, но только не очень верная
# всмысле - не очень верная? опиши как можно конкретнее, что она выводит?
