def main_logic(arr):
    total_sum = sum(arr)
    left_sum = 0
    res = []

    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            res.append(i)

        left_sum += arr[i]

    if not res:
        return -1
    return res


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(main_logic(arr))

