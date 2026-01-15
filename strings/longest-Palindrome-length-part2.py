def main_logic(s):
    length = 0
    odd_found = False
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for v in freq.values():
        length += (v // 2) * 2
        if v % 2 == 1:
            odd_found = True

    if odd_found:
        length += 1

    return length 

if __name__ == "__main__":
    s = input()
    print(main_logic(s))


