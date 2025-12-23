def f(n, a, b):
    if n == 0:
        return

    print(a, end=" ")
    f(n-1, b, b+a)

if __name__ == "__main__":
    n = int(input())
    f(n + 1, 0, 1)
