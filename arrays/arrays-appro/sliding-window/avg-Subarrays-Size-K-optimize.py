def main_logic(arr, k):
    n = len(arr)
    if n < k:
        return -1
    window_start = sum(arr[:k])
    l = []
    l.append(window_start/k)


    for i in range(k, n):
        window_start += arr[i]
        window_start -= arr[i - k]

        l.append(window_start/k)

    return l

if __name__ == "__main__":

    arr = list(map(int, input().split()))

    k = int(input())

    print(main_logic(arr, k))
