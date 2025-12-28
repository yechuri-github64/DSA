def main_logic(arr, k):
    freq = {0: 1}
    prefix_sum = 0
    count = 0
    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum - k in freq:
            count += freq[prefix_sum - k]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    return count

if __name__ == "__main__":
     arr = list(map(int, input().split()))

     k = int(input())

     print(main_logic(arr, k))

