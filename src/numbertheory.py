import math
#Check if a number is prime or not in O(n**0.5)
def chkPrime(n):
    flag = 1
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            flag = 0
            break

    return flag


#Returns set prime factors O(sqrt(n))
def primefactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(i)
            n = n // i

    if n > 2:
        l.append(n)

    return l

#Returns Divisors in O(sqrt(n))
def divisors(n):
    i = 1
    l = []
    while i <= int(n**0.5):
        if (n % i == 0):
            if (n // i == i):
                l.append(i)

            else:
                l.append(n // i)
                l.append(i)

        i = i + 1

    return l

#Fast modular exponentiation
def powerModulo(x,y,M):
    ans = 1
    while(y>0):
        if(y%2 == 1):
            ans = (ans*x)%M
        y = y //2
        x = (x*x)%M
    return ans%M