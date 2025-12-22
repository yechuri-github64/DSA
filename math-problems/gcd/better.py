def gcd(n1, n2):

    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1 == n2:
        return n1

    if n1 > n2:
        return gcd(n1 - n2, n2)
    else:
        return gcd(n1, n2 - n1)

if __name__ == "__main__":

    n1 ,n2 = map(int, input().split())

    print(gcd(n1, n2))
