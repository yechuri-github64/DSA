n = int(input( ))


for i in range(n):
    for j in range(n-i-1, n):
        print(chr(ord('A')+j), end="")
    print()

