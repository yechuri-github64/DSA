def main_logic(arr, k):

    prefix_sum = 0
    count = 0
    freq = {0: 1}

    for num in arr:
        prefix_sum += num


        if prefix_sum - k in freq:
            count = count + freq[prefix_sum - k]


        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(main_logic(arr, k))
