def main_logic(arr, k):
    n = len(arr)
    max_len = 0

    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += arr[j]

            if summ > k:
                break

            max_len = max(max_len, j - i + 1)

    return max_len


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(main_logic(arr, k))

