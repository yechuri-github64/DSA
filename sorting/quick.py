def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for k in range(low, high):
        if arr[k] < pivot:
            i += 1
            arr[i], arr[k] = arr[k], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick(arr, low, p - 1)
        quick(arr, p + 1, high)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    quick(arr, 0, len(arr) - 1 )
    print(arr)



