def main_logic(arr, k):

    n = len(arr)

    ans = [ ]
    cnt = 0


    for i in range(n - k + 1):
        for j in range(k):
            if arr[i+j] < 0:
                ans.append(arr[i+j])
                break

        if len(ans) == cnt:
            ans.append(0)
        else:
            cnt += 1

    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print(main_logic(arr, k))

