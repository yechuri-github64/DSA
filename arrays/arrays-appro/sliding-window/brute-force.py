def main_logic(arr, k):

    n = len(arr) 
    maxx = float('-inf')


    for i in range(n -k + 1):
        summ = 0
        for j in range(k):
            summ += arr[i+j]

        maxx = max(summ, maxx)

    return maxx


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print(main_logic(arr, k))
