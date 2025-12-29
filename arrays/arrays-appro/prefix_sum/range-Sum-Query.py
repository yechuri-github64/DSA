#Given an integer array arr of size n and multiple queries, each query contains two integers l and r. For each query, return the sum of elements from index l to r (inclusive).

def main_logic(arr, l, r):
    prefix_sum = 0
    freq = { }
    for i in range(len(arr)):

        prefix_sum += arr[i]

        freq[i] = prefix_sum 

    if l == 0:
        return freq[r]
    else:
        return freq[r] - freq[l-1]

if __name__ == "__main__":

    arr = list(map(int, input().split()))

    l = int(input())
    r = int(input())

    print(main_logic(arr, l - 1, r))




