def missing(arr, k):
    summ = (k * (k + 1)) // 2
    actual = sum(arr)

    return summ - actual 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(missing(arr, k))
