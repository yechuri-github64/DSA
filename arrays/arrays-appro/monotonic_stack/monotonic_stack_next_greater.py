def main_logic(arr):
    n = len(arr)
    res = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            res[idx] = arr[i]

        stack.append(i)

    return res


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(main_logic(arr))


