def main_logic(s):
    seen = {}
    max_len = 0
    left = 0

    for i in range(len(s)):
        if s[i] in seen and seen[s[i]] >= left:
            left = seen[s[i]] + 1
        seen[s[i]] = i
        max_len = max(max_len, i - left + 1)

    return max_len

if __name__ == "__main__":
    s = input()
    print(main_logic(s))
            
