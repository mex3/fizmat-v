

#marytomilina #A
n, m = map(int, input().split())
A = [sum(map(int, input().split())) for z in range(n)]
print(max(A))
print(A.index(max(A)))
