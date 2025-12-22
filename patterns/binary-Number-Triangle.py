n = int(input())

for i in range(1, n+1):
    r = ""
    for j in range(1, i+1):
        r += str(j%2)
    print(r)
