def main_logic(arr, k):
    n = len(arr)
    summ = sum(arr[:k])
    maxx = summ
    for i in range(k, n):
        summ += arr[i] - arr[i - k]
        maxx = max(maxx, summ)
    return maxx

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(main_logic(arr, k))





