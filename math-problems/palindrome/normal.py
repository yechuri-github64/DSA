def Palindrome(n):
    if n < 0:
        return False
    else:
        rev = 0 
        l = n
        while n > 0:
            rev = rev * 10 + (n % 10)
            n = n // 10

    if rev == l:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input( ))
    print(Palindrome(n))
