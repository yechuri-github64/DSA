def numbers(n):
    if n == 0:
        return 
    print(n)
    numbers(n-1)

if __name__ == "__main__":
    n = int(input())
    numbers(n)
