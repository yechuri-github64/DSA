def ls(arr, x):

    for i in range(len(arr)):
        if arr[i] == x:
            return True
    return False


def main_logic(arr):

    if not arr:
        return 0

    n = len(arr)

    long = 1

    for i in range(n):
        x = arr[i]

        cnt = 1

        while ls(arr, x + 1):
            x += 1
            cnt += 1

        long = max(long, cnt)
    return long 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(main_logic(arr))
