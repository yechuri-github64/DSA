def main_logic(arr):
    xorr = 0

    for x in arr:
        xorr ^= x
    return xorr


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(main_logic(arr))
