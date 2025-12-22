n = int(input())
k=0
for i in range(n):
    for j in range(i+1):
        k += 1
        print(k, end=" ")
    print()
