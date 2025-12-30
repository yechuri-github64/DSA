def helper(s):
    freq = set('aeiou')
    cnt = 0
    for ch in s:
        if ch in freq:
            cnt += 1
    return cnt

def main_logic(s, k):
    st = ""
    maxx = 0
    for i in range(len(s) - k + 1):
        st = s[i:i+k]

        maxx = max(maxx, helper(st))
    return maxx


if __name__ == "__main__":
    s = input()
    k = int(input())
    print(main_logic(s, k))

