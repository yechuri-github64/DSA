def checking(s):
    if len(s) == 0:
        return -1

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return -1

if __name__ == "__main__":
    s = input()
    print(checking(s))
