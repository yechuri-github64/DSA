def main_logic(s, t):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        freq[ch] = freq.get(ch, 0) - 1

    for k, v in freq.items():
        if v == -1:
            return k

if __name__ == "__main__":
  s, t = input().split()
  print(main_logic(s, t))
