#http://informatics.mccme.ru/mod/statements/view.php?id=15232#1
#решить несколько задач из 5
#A:
n, m = map(int, input().split())
mx, mn = 0, n
for i in range(n):
    x = sum(map(int, input().split()))
    if x > mx:
        mx = x
        mn = i
print(mx, mn)
#B:
n, m = map(int, input().split())
mr, mn, mm = 0, 0, 0
for i in range(n):
    s = list(map(int, input().split()))
    for x in range(m):
        if s[x] > mr:
            mr = s[x]
            mn = i
            mm = x
print(mr)
print(mn, mm)

#C:
n, m = map(int, input().split())
mr, mn, mm, ms = 0, 0, 0, 0
for i in range(n):
    s = list(map(int, input().split()))
    for x in range(m):
        if s[x] == mr:
            if sum(s) > ms:
                mr = s[x]
                mn = i
                mm = x
                ms = sum(s)
        if s[x] > mr:
            mr = s[x]
            mn = i
            mm = x
            ms = sum(s)
print(mn)

#D:
n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(sum(map(int, input().split())))
print(l.count(max(l)))
#this code doesn't work right, and I don't know why

#marytomilina #A
n, m = map(int, input().split())
A = [sum(map(int, input().split())) for z in range(n)]
print(max(A))
print(A.index(max(A)))

#marytomilina#B
n, m = map(int, input().split())
A = [list(map(int, input().split())) for z in range(n)]
maxi = 0
for i in range(n):
    for j in range(m):
        if int(A[i][j]) > maxi:
            maxi = A[i][j]
a = n - 1
nsto = 0
nstr = 0
kol = 0
while a >= 0:
    kol = A[a].count(maxi)
    if kol >= 1:
        nsto = a
        nstr = A[a].index(maxi)
    a = a - 1
print(maxi)
print(nsto, nstr)
