def reverse_list(first ,last, l):

    if first >= last:
        return l

    l[first], l[last] = l[last], l[first]

    return reverse_list(first+1, last-1, l)

if __name__ == "__main__":

    l = list(map(int, input().split()))

    last = len(l) - 1

    print(reverse_list(0, last, l))


