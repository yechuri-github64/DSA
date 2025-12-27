def combination(arr, k):

    l = []

    for i in range(len(arr)):
        fix = arr[i]

        for j in range(i + 1, len(arr)):
            if arr[j] + fix == k:
                l.append(fix, arr[j])
            if arr[j] + fix < k:
                fix 

