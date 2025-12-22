def count_digits(n):
    if n == 0:
        return 1

    n = abs(n)
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt

def Armstrong(n):

    if n < 0:
        return False

    cnt = count_digits(n)
    powers = [ i ** cnt for i in range(10)]
    temp = n
    summ = 0

    while temp > 0:
        summ += powers[temp % 10]
        temp = temp // 10
    return summ == n

if __name__ == "__main__":
    n = int(input()) 
    print(Armstrong(n))
