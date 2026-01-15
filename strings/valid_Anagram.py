def main_logic(s1, s2):
    freq ={}
    if len(s1) != len(s2):
        return False

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq:
            return False

        freq[ch] = freq[ch] - 1
        if freq[ch] < 0:
            return False
    return True


if __name__ == "__main__":
    s1, s2 = input().split()

    print(main_logic(s1, s2))
