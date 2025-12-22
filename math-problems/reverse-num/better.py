def reverDig(n):

    rev = 0 

    while n > 0:
        rev = rev * 10 + (n % 10)

        n = n // 10

    return rev 

if __name__ == "__main__":
    n = int(input( ))
    print(reverDig(n))
