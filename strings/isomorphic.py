def main_logic(s1, s2):
    if len(s1) != len(s2):
        return False

    map_s1s2 = {}
    map_s2s1 = {}

    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]

        if c1 in map_s1s2:
            if map_s1s2[c1] != c2:
                return False
        else:
            map_s1s2[c1] = c2


        if c2 in map_s2s1:
            if map_s2s1[c2] != c1:
                return False
        else:
            map_s2s1[c2] = c1

    return True

if __name__ == "__main__":
    s1, s2 = input().split()

    print(main_logic(s1, s2))
