def union(arr1, arr2):
    feq = {}
    l = []
    for i in arr1:
        feq[i] = feq.get(i, 0) + 1

    for j in arr2:
        feq[j] = feq.get(j, 0) + 1

    for k in feq.keys():
        l .append(k)
    return l

if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(union(arr1, arr2))



