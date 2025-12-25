def permutations(s):
    if len(s) == 1:
        return [s]
    result = [  ]
    for i in range(len(s)):
        fix = s[i]
        rem = s[:i] + s[i+1:]

        for j in permutations(rem):
            result.append(fix + j)


    return sorted(result)


if __name__ == "__main__":
    s = input()
    print(permutations(s))

