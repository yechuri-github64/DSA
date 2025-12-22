import math 
def countdig(n):
    if n == 0:
        return 1
    else:
      cnt = int(math.log10(abs(n)) + 1)

    return cnt

if __name__ == "__main__":
    n = int(input( ))
    dig = countdig(n)
    print(dig)
