def main_logic(arr, k):
    mp = {}


    for i in range(len(arr)):
        if (k - arr[i]) in mp:
            return arr[i], arr[mp[k - arr[i]]]

        mp[arr[i]] = i

    return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print(main_logic(arr, k))

