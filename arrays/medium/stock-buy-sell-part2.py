def main_logic(arr):

    minn = float('inf')

    maxx = 0


    for i in range(len(arr)):

        if arr[i] < minn:
            minn = arr[i]
        else:
            maxx = max(maxx, arr[i] - minn)

    return maxx


if __name__ == "__main__":
    aee = list(map(int, input().split()))
    print(main_logic(aee))
