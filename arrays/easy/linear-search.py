def liner(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return True
    return False


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(liner(arr, k))
