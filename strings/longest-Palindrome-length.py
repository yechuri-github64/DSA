def main_logic(s):

    mapp = {}
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for ch in s:
        mapp[ch] = mapp.get(ch, 0) + 1

    for v in mapp.values():
        if v != 1 and v % 2 == 0:
            cnt1 += v
        elif v != 1 and v % 2 == 1:
            cnt2 = cnt2 + (v -1)
        elif v == 1:
            cnt3 += 1

    if cnt3 or cnt2:
        return cnt1 + cnt2 + 1
    else:
        return cnt1

if __name__ == "__main__":
    s = input()
    print(main_logic(s))

