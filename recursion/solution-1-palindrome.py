def is_palindrome_half_method(s):
    s = s.strip()
    n = len(s)

    if n == 0:
        return True

    mid = n // 2

    if n % 2 == 0:
        left = s[:mid]
        right = s[mid:]
    else:
        left = s[:mid]
        right = s[mid+1:]

    return left == right[::-1]

if __name__ == "__main__":
    s = input()
    print(is_palindrome_half_method(s))
