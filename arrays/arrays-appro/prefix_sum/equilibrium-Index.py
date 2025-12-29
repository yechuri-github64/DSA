def main_logic(arr):
    l = []
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            l.append(i)

    if not l:
        return -1
    else:
        return l

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(main_logic(arr))
