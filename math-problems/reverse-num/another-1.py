def reverDig(n):
    if n == 0:
        return "0"

    digits = []

    while n > 0:
        digits.append(str(n % 10))
        n //= 10

    return ''.join(digits)


if __name__ == "__main__":
    n = int(input( )) 
    print(reverDig(n))
