#Решатель Квадратных Уравнений!!!
#         авторы: Матвеев и Орусов
q = input()
w = q.find('x^2')
a = q[:w]
if a == '':
    a = 1
else:
    a = int(a)
d=max(q.find("2+"), q.find('2-'))
z = max(q.find('x+'), q.find('x-'))
b = q[d+2:z]
if b == '':
    b = 1
else:
    b = int(b)
e = q.find('=')
c = int(q[z+2:e])
if d == q.find("2-"):
    b = -b
if z == q.find('x-'):
    c = -c
D = b**2 - 4 * a * c
if D < 0:
    x = (-b + 1j * D ** 0.5)/(2 * a)
    y = (-b - 1j * D ** 0.5)/(2 * a)
    print(x, ';', y)
elif D == 0:
    x = (-b)/(2 * a)
    print(x)
else:
    x = (-b + D ** 0.5)/(2 * a)
    y = (-b - D ** 0.5)/(2 * a)
    print(x, ';', y)
    # конец кода
