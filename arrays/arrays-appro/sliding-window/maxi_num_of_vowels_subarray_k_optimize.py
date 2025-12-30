def main_logic(s, k):
    vow = set('aeiou')
    cur_cnt = 0
    max_cnt = 0

    for i in range(k):
        if s[i] in vow:
            cur_cnt += 1
    max_cnt = cur_cnt 

    for i in range(k, len(s)):
        if s[i] in vow:
            cur_cnt += 1
        if s[i - k] in vow:
            cur_cnt -= 1

        max_cnt = max(max_cnt, cur_cnt)
    return max_cnt


if __name__ == "__main__":
    s = input()
    k = int(input())
    print(main_logic(s, k))
        
