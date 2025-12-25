def insertion(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]      # element to insert
        j = i - 1

        # shift larger elements to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # insert key at correct position
        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(insertion(arr))

