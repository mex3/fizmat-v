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
