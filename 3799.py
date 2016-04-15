#http://informatics.mccme.ru/mod/statements/view3.php?id=3962&chapterid=3799#1
#РЕКУРСИЯ!
#РЕКУРСИЯ!

#this code works
#and I don't know why we have to use recursion

def IsPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if IsPrime(int(input())):
    print('YES')
else:
    print('NO')
    
Вот мой код. Он непроходит несколько тестов из-за превышения максимального времени (marytomilina).
def IsPrime(n):
    i = 2
    while n % i != 0:
        i = i + 1
    if i == n:
        return 'YES'
    else:
        return 'NO'
 
print(IsPrime(int(input())))
