def Palindrome(n):
    if n < 0 or ( n % 10 == 0 and n != 0):
        return False 
    rev = 0

    while n > rev:
        rev = rev * 10 + (n % 10)
        n = n // 10 

    return rev == n or n == rev // 10

if __name__ == "__main__":
    n = int(input( ))
    print(Palindrome(n))

