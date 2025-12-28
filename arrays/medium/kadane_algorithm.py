def main_logic(arr):

    maxx = float('-inf')
    summ = 0

    for i in arr:
        summ += i

        if summ > maxx:
            maxx = summ

        if summ < 0:
            summ = 0
    return maxx


if __name__ == "__main__":

    arr = list(map(int, input().split()))

    print(main_logic(arr))
