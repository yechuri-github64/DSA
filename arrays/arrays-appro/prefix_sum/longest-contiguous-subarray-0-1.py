def longest_equal_0_1(arr):
    prefix_sum = 0
    max_len = 0
    mp = {0: -1}   # prefix_sum -> earliest index

    for i in range(len(arr)):
        # transform
        if arr[i] == 0:
            prefix_sum += -1
        else:
            prefix_sum += 1

        if prefix_sum in mp:
            max_len = max(max_len, i - mp[prefix_sum])
        else:
            mp[prefix_sum] = i

    return max_len


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(longest_equal_0_1(arr))

