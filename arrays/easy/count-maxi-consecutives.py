#Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array..

def main_logic(arr):
    maxxi = float('-inf')
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            cnt += 1
        else:
            maxxi = max(cnt, maxxi)
            cnt = 0
    maxxi = max(cnt, maxxi)

    return maxxi

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(f"consecutive 1’s in the array out of which maximum is {main_logic(arr)}.")
