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
