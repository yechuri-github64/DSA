arr = list(map(int, input().split()))

if len(arr) < 2:
    print("bdsk send me more than 2 elements")
else:
    maxii = second_maxii = float('-inf')
    mini = sec_mini = float('inf')

    for i in arr:
      if i > maxii:
        second_maxii = maxii
        maxii = i
      elif i > second_maxii and i != maxii:
        second_maxii = i

      if i < mini:
        sec_mini = mini
        mini = i
      elif i < sec_mini and i != mini:
        sec_mini = i
    if second_maxii == float('-inf') or sec_mini == float('inf'):
        print("Second largest or smallest does not exist")
    else:
        print(f"second largest element is {second_maxii} and second smallest ele is {sec_mini}")


