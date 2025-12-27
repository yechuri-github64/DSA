def rotate(arr, k):

    for i in range(k):
        temp = arr[0]
        for j in range(1, len(arr)):
            arr[j-1] = arr[j]

        arr[-1] = temp

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    rotate(arr, k)

    print(arr)


