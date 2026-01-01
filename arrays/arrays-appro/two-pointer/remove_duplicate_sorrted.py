def main_logic(arr):

    slow = 0
    n = len(arr)

    for fast in range(1, n):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    

    return arr[:slow+1]


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(main_logic(arr))
