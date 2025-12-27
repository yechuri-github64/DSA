def delete_ele(arr, k):
    for i in range(k, len(arr) - 1):
        arr[i] = arr[i+1]

    arr.pop()
def remove_dup(arr):
     i = 0
     j = len(arr) - 1
     while i < j:
         if arr[i] == arr[j]:
             delete_ele(arr, j)
             i = 0 
             j = len(arr) - 1
         else:
             i += 1
             j -= 1



if __name__ == "__main__":
    arr = list(map(int, input().split()))
    remove_dup(arr)
    print(arr)


