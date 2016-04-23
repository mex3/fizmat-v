

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
