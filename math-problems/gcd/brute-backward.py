def gcd(n1, n2):

    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i


    return 1


if __name__ == "__main__":

    n1, n2 = map(int, input().split())

    print(gcd(n1, n2))
