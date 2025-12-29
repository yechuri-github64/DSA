from collections import deque

def main_logic(arr, k):
    n = len(arr)
    q = deque()   # store negative numbers
    ans = []

    for i in range(n):
        # add incoming element
        if arr[i] < 0:
            q.append(arr[i])

        # window size reached
        if i >= k - 1:
            # first negative for this window
            if q:
                ans.append(q[0])
            else:
                ans.append(0)

            # remove outgoing element
            if arr[i - k + 1] < 0:
                q.popleft()

    return ans


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(main_logic(arr, k))

