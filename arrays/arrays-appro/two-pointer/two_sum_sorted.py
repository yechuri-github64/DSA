def main_logic(arr, k):

    left = 0
    right = len(arr) - 1


    while left < right :
        curr_sum = arr[left] + arr[right]
        
        if curr_sum == k:
            return left, right
        elif curr_sum > k:
            right -= 1
        else:
            left += 1
    return -1


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print(main_logic(arr, k))
