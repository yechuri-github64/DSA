def bubble(arr):
    n = len(arr)

    for i in range(n-1):
        swap = 0
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1

        if swap == 0:
            break

    return arr

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(bubble(arr))


