def main_logic(arr):
    n = len(arr)
    ans = [0] * n

    pos = 0
    neg = 1

    for i in range(n):
        if arr[i] < 0:
            ans[neg] = arr[i]
            neg += 2
        else:
            ans[pos] = arr[i]
            pos += 2
    return ans


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(main_logic(arr))
