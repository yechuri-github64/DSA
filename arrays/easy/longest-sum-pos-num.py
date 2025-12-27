def main_logic(arr, k):
    # Pointers to mark the start and end of window
    i = 0 #left
    j = 0  #right
    l = []
    # to store maxi length
    max_l = 0 

    # To store the sum of elements in the window
    summ = arr[0]

    n = len(arr)


    while j < n:

        while i <= j and summ > k:
            summ -= arr[i]
            i += 1

        if summ == k:
            cur_len = j - i + 1
            if cur_len > max_l:
                max_l = cur_len
                l = [arr[i:j+1]]
            elif cur_len == max_l:
                l.append(arr[i:j+1])


        j += 1
        if j < n:
            summ += arr[j]


    return max_l, l

if __name__ == "__main__":

    arr = list(map(int, input().split()))
    k = int(input())
    print(main_logic(arr, k))

