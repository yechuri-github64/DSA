def main_logic(l):
    group = {}

    for w in l:

        count = [0] * 26 

        for ch in w:
            count[ord(ch) - 97 ] += 1

        key = tuple(count)


        if key not in group:
            group[key] = []
        group[key].append(w)

    return list(group.values())


if __name__ == "__main__":
    l = input().split()
    print(main_logic(l))
