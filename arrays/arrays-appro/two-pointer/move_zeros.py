def main_logic(arr):
    slow = 0

    n = len(arr)

    for fast in range(n):

        if arr[fast] != 0:
            arr[slow],arr[fast] = arr[fast], arr[slow]
            slow += 1

    return arr

if __name__ == "__main__":

    arr = list(map(int, input().split()))
    print(main_logic(arr))



