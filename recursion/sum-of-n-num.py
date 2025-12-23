def sum_of_n(summ, n):

    if n == 0:
        return summ

    summ += n
    return sum_of_n(summ, n-1)

if __name__ == "__main__":
    n = int(input())
    print(sum_of_n(0, n))

