def main_logic(arr, k):

    n = len(arr)

    window_sum = sum(arr[:k])
    maxx = window_sum


    for i in range(k, n):
        window_sum += arr[i]

        window_sum -= arr[i - k]

        maxx = max(maxx, window_sum)

    return maxx


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(main_logic(arr, k))

