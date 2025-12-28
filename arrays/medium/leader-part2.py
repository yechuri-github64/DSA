def main_logic(arr):

    ans = []

    if not arr:
        return ans

    maxx =  arr[-1]

    ans.append(maxx)

    for i in range(len(arr) - 2, -1, -1):


        if arr[i] > maxx:
            ans.append(arr[i])
            maxx = arr[i]

    ans.reverse()


    return ans


if __name__ == "__main__":

    arr = list(map(int, input().split()))

    print(main_logic(arr))
