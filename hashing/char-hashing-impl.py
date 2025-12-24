def char_hashing(s):

    feq = {}

    for ch in s:
        feq[ch] = feq.get(ch, 0) + 1

    return feq


if __name__ == "__main__":
    s = input()
    print(char_hashing(s))
