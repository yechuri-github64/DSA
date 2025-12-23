def is_palindrome_recursive(s, left, right):
    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return is_palindrome_recursive(s, left + 1, right - 1)


def is_palindrome(s):
    s = s.strip()
    return is_palindrome_recursive(s, 0, len(s) - 1)

if __name__ == "__main__":
    s = input()
    print(is_palindrome(s))
