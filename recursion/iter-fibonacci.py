def f(n):
    a, b = 0, 1
    for _ in range(n+1):
        print(a, end = " ")
        a, b = b, a+b

    return 

if __name__ == "__main__":
    n = int(input())
    f(n)

