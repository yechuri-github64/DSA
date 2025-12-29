def main_logic(arr, k):
    n = len(arr) 

    l = []

    for i in range(n - k + 1):
        temp = []
        for j in range(k):
            temp.append(arr[i + j])


        l.append(sum(temp)/k)

    return l


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    k = int(input())

    print(main_logic(arr, k))


