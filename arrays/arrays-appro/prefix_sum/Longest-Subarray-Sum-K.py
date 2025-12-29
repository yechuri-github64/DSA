def main_logic(arr, k):
     freq = {0: -1}
     prefix_sum = 0
     maxx = 0


     for i in range(len(arr)):
         prefix_sum += arr[i]

         if prefix_sum - k in freq:
             maxx = max(i - freq[prefix_sum - k], maxx)
         if prefix_sum - k not in freq:
             freq[prefix_sum] = i

     return maxx


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(main_logic(arr, k))
