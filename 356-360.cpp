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
#3 из 5 - это ведь несколько, да?
