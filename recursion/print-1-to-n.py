def numb(n):
    if n < 1:
        return 
    numb(n-1)
    print(n)

if __name__ == "__main__":
    n = int(input())
    numb(n)
