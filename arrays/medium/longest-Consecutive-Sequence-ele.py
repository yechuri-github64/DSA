def main_logic(arr):


    n = len(arr)

    if n == 0:
        return 0

    st = set()
    cnt = 0

    long = 0
    
    ele = 0

    for i in arr:
        st.add(i)

    for x in st:
        if x - 1 not in st:
            cnt = 1

            k = x
            while k + 1 in st:
                k += 1
                cnt += 1

            if cnt > long:
                long = cnt
                ele = x
    result = []
    for i in range(long):
        result.append(ele + i)

    return result

if __name__ == "__main__":

    arr = list(map(int, input().split()))
    print(main_logic(arr))
