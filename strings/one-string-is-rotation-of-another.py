#If s2 is a rotation of s1,
#then s2 must be a substring of s1 + s1.
#example
#s1 = "abcd"
#s1+s1 = "abcdabcd"
#s2 = "cdab"  ← exists inside

def main_logic(s1, s2):
    if len(s1) != len(s2):
        return False

    return s2 in (s1 + s1)

if __name__ == "__main__":
    s1, s2 = input().split()

    print(main_logic(s1, s2))

