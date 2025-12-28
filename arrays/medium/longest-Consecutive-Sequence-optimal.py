def main_logic(arr):
    n = len(arr)
    if n == 0:
        return 0


    long = 1
    st = set()


    for i in range(n):
        st.add(arr[i])

    for x in st:
        if x - 1 not in st:
            cnt = 1
            k = x

        while k + 1 in st:
            cnt += 1

            k += 1
        long = max(cnt, long)
    return long

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(main_logic(arr))
