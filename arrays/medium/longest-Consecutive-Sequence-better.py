def main_logic(arr):


    cnt = 0
    n = len(arr)

    if n == 0:
        return 0

    last = float('-inf')
    long = 1

    arr.sort()

    for i in range(n):


        if arr[i] - 1 == last:
            cnt += 1
            last = arr[i]
        elif arr[i] != last:
            cnt = 1
            last = arr[i]

        long = max(long, cnt)
    return long

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(main_logic(arr))




