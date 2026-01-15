def main_logic(s):
    s1 = "".join(ch.lower() for ch in s if ch.isalnum())
    return s1 == s1[::-1]

if __name__ == "__main__":
    s = input()
    print(main_logic(s))
