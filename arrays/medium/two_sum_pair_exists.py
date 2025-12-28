def merge(arr, left, mid, right):
    temp = []
    i, j  = left, mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[left + k] = temp[k]

def merge_sort(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)

    merge(arr, left, mid, right)

def main_logic(arr, k):
    merge_sort(arr, 0, len(arr) - 1)

    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == k:
            return arr[left], arr[right]

        if arr[left] + arr[right] > k:
            right -= 1

        if arr[left] + arr[right] < k:
            left += 1

    return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(main_logic(arr, k))




