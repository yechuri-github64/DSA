def main_logic(arr, k):
    n = len(arr)
    if n == 0:
        return -1 

    prefix_sum = 0
    freq = {0: -1}
    cnt = 0
    ans = []

    for i in range(n):
        prefix_sum += arr[i]


        if prefix_sum - k in freq: #start_index = freq[prefix_sum - k] + 1 ans.append(arr[start_index:i + 1])  # Add the subarray ans.append((freq[prefix_sum - k] + 1, i))
            return True

        freq[prefix_sum] = i

    return False


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print(main_logic(arr, k))

