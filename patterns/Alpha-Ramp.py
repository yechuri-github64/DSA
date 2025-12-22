n = int(input( ))
k = 0

for i in range(n):
    for j in range(i+1):
        print(chr(ord('A') + k ), end="")
    k += 1
    print()

