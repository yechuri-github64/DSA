def main_logic(s):
    l = ['a', 'i', 'e', 'o', 'u']
    vow = 0
    con = 0

    for ch in s:
        if ch.lower() in l:
            vow += 1
        elif ch.isalpha():
            con += 1
    return con, vow

if __name__ == "__main__":
    s = input()
    print(main_logic(s))

