def Divisors(n):
    l = []
    if n == 0 or n == 1:
        return n 
    for i in range(1, n+1):
        if n % i == 0:
            l.append(i)

    return l

if __name__ == "__main__":
    n = int(input())
    print(Divisors(n))
