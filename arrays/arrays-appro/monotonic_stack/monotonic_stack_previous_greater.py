def main_logic(arr):

    n = len(arr)

    res = [-1] * n
    stack = []


    for i in range(n):


        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            res[i] = stack[-1]
        else:
            res[i] = -1 


        stack.append(arr[i])

    return res


if __name__ == "__main__":

    arr = list(map(int, input().split()))
    print(main_logic(arr))
