def main_logic(arr):

    maxx = float('-inf')
    val = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            p = arr[j] - arr[i] 
            maxx = max(p, maxx)

    return maxx

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print("Max Profit:", main_logic(arr))
