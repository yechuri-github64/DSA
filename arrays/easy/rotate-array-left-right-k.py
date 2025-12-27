def reverse(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

def main_logic_right(arr, k):
    if not arr:
        return 
    n = len(arr)
    k = k % n

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)

def main_logic_left(arr, k):
    if not arr:
        return
    n = len(arr)
    k = k % n

    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    user = input()
    user = user.lower()

    if user == "right":
        main_logic_right(arr, k)
    else:
        main_logic_left(arr, k)

    print(arr)

