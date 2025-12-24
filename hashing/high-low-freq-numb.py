def high_low_freq(l):
    high = float('-inf')
    key_1 = float('inf')
    key_2 = float('inf')
    low = float('inf')
    freq = {}
    for i in l:
        freq[i] = freq.get(i,0) + 1

    for k, v in freq.items():
        if v > high:
            high = v
            key_1 = k

        if v < low:
            low = v
            key_2 = k
    print(f"The frequency of {key_1} is {high}, i.e. the highest and the frequency of {key_2} is {low} i.e the lowest")

if __name__ == "__main__":
    l = list(map(int, input().split()))
    high_low_freq(l)
