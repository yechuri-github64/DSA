def main_logic(arr):


    left = 0
    right = len(arr) - 1
    maxx = 0

    while left < right:

        cur = min(arr[left], arr[right]) * (right - left)

        maxx = max(maxx, cur)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return maxx

if __name__ == "__main__":

    arr = list(map(int, input().split()))

    print(main_logic(arr))

