def main_logic(arr):
    ans = []
    
    for i in range(len(arr)):
        is_leader = True
        for j in range(i+1, len(arr)):

            if arr[i] <= arr[j]:
                is_leader = False
                break
        if is_leader:
            ans.append(arr[i])

    return ans


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(main_logic(arr))
