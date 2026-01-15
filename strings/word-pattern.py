def main_logic(s1, s2):

    l1 = s2.split()
    if len(s1) != len(l1):
        return False

    map_s1 = {}

    map_s2 = {}

    for i in range(len(s1)):
        c1 = s1[i]
        w1 = l1[i]

        if c1 in map_s1:
            if map_s1[c1] != w1:
                return False
        else:
            map_s1[c1] = w1

        if w1 in map_s2:
            if map_s2[w1] != c1:
                return False
        else:
            map_s2[w1] = c1
    return True

if __name__ == "__main__":
    s1 = input()
    s2 = input()

    print(main_logic(s1, s2))
