def missing_ele(arr, k):

    for i in range(1, k+1):
        found = False
        for x in arr:
            if x == i:
                found = True
                break
        if not found:
            return i
    return -1 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print(missing_ele(arr, k))
