def main_logic(s):
    freq = {}
    l = []
    for ch in s:
        if ch != ' ':
            freq[ch] = freq.get(ch, 0) + 1
    for k,v in freq.items():
        if v > 1:
            l.append(k)

    return l


if __name__ == "__main__":
    s = input()
    print(main_logic(s))


