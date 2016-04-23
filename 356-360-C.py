
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
