def longest_unique_substring(s):
    freq = {}          # stores last index of each character
    p = 0              # left pointer
    max_len = 0

    for q in range(len(s)):     # right pointer
        if s[q] in freq and freq[s[q]] >= p:
            p = freq[s[q]] + 1   # move left pointer after duplicate

        freq[s[q]] = q          # update last seen index
        max_len = max(max_len, q - p + 1)

    return max_len


if __name__ == "__main__":
    s = input()
    print(longest_unique_substring(s))

