#Moore’s Voting Algorithm

def main_logic(arr):
    n = len(arr)
    
    cnt = 0

    ele = 0

    for i in range (n):
        if (cnt == 0):
            cnt = 1
            ele = arr[i]
        elif (arr[i] == ele):
            cnt += 1
        else:
            cnt -= 1
    cnt2 = arr.count(ele)

    if (cnt2 > n // 2):
        return ele
    else:
        return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(main_logic(arr))
