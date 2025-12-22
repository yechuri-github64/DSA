def count_digits(n):
    n = abs(n)
    cnt = 0
    while n > 0:
        cnt += 1
        n = n // 10
    return cnt
def Armstrong(n):

    if n == 0 or n == 1:
        return True

    cnt = count_digits(n)
    summ = 0
    temp = 0
    n1 = n
    while n1 > 0:
        temp = n1 % 10
        summ = summ + temp ** cnt
        n1 = n1 // 10 
    return n == summ

if __name__ == "__main__":
    n = int(input( ))

    print(Armstrong(n))
