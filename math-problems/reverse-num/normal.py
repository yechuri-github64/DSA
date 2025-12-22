def reverDig(n):

    s = ""

    if n == 0:
        return 0
    else:
        while n > 0:
            s += str(n % 10)

            n = n // 10

    return s

if __name__ == "__main__":
    n = int(input( ))

    print(reverDig(n))
