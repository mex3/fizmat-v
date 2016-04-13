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
