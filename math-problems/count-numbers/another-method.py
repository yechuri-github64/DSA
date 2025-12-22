def countDig(n):
    cnt = 0

    while n > 0:
        cnt += 1

        n = n // 10

    return cnt

if __name__ == "__main__":
    n = int(input( ))
    digits = countDig(n)
    print(digits)
