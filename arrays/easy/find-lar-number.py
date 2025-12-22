arr = list(map(int, input().split()))
length = 0

for i in arr:
    length += 1

maxii = arr[0]
for i in arr:
    if maxii < i:
        maxii = i


print(f"maxi element is {maxii} and array length is {length}")

