#You are given a string s that contains words separated by spaces.
#Return a new string where the order of words is reversed.


def main_logic(s):
    l = s.split()

    return " ".join(l[::-1])

if __name__ == "__main__":
    s = input()
    print(main_logic(s))





