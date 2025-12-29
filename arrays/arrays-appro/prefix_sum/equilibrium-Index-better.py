def main_logic(arr):
    freq = {-1: 0}
    prefix_sum = 0
    n = len(arr)
    l = []
    for i in range(n):
        prefix_sum += arr[i]
        freq[i] = prefix_sum

    for i in range(n):
        if freq[i-1] == (freq[n-1] - freq[i]):
            l.append(i)

    if not l:
        return -1
    else:
        return l





if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(main_logic(arr))
