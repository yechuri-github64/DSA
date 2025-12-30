def main_logic(arr, k):

    n = len(arr)
    left = 0
    curr_sum = 0
    max_len = 0

    for r in range(n):
        curr_sum += arr[r]

        while curr_sum > k:
            curr_sum -= arr[left]
            left += 1

        max_len = max(max_len, r - left + 1)
    return max_len


if __name__ == "__main__":

    arr = list(map(int, input().split()))
    k = int(input())
    print(main_logic(arr, k))




