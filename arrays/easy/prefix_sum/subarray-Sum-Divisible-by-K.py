def main_logic(arr, k):

    prefix_sum = 0 
    freq = {0: 1}
    cnt = 0

    for num in arr:
        prefix_sum += num


        if (prefix_sum % k) in freq:
            cnt += freq.get(prefix_sum, 0) + 1






