

#D:
n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(sum(map(int, input().split())))
print(l.count(max(l)))
#this code doesn't work right, and I don't know why
