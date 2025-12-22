import math
def Divisors(n):


    l = []

    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            l.append(i)
            if i != n //i:
                l.append(n//i)
    return l

if __name__ == "__main__":
    n = int(input())
    print(Divisors(n))
