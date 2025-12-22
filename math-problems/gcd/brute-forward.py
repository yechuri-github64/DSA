def gcd(n1, n2):

    res = 1

    for i in range(1, min(n1, n2) + 1):
        if (n1 % i) == 0 and (n2 % i) == 0:
            res = i

    return res

if __name__ == "__main__":
    n1, n2 = map(int, input().split())

    print(gcd(n1, n2))
