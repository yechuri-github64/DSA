def main_logic(l):
    dis = {}

    for w in l:

        s = ''.join(sorted(w))
        if s in dis:
            dis[s].append(w)
        else:
            dis[s] = [w]

    return list(dis.values())

if __name__ == "__main__":
    l = input().split()
    print(main_logic(l))



