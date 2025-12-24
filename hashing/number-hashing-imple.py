def hashing(l):

    hashh = {}
    for i in l:
        if i in hashh:
            hashh [i] += 1
        else:
            hashh [i] = 1

    return hashh

if __name__ == "__main__":
    l = list(map(int, input().split()))
    print(hashing(l))
