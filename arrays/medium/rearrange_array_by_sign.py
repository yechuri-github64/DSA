def main_logic(arr):

    pos = []
    neg = []

    for x in arr:
        if x > 0:
            pos.append(x)
        else:
            neg.append(x)

    for i in range(len(arr) //2 ):
        arr[2 * i] = pos[i]
        arr[2 * i + 1] = neg[i]

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    main_logic(arr)

    print(arr)


