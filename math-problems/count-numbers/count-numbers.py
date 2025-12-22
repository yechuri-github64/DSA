n = input().strip()


count = 0
for ch in n:
    if '0' <= ch <= '9':
        count += 1

print(count)
