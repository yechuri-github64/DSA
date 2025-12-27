def remove_dup(arr):
    if not arr:
        return 0

    i = 0 #index of lastr unique ele

    for j in range(1, len(arr) -1):
        if arr[i] != arr[j]:
            i += 1

            arr[i] = arr[j]
    return i + 1


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print("Array after removing duplicates:", arr[:remove_dup(arr)])
