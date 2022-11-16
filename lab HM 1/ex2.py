import random

n = int(input("How many numbers in the arr: "))
arr = []
for i in range(0, n):
    arr.append(random.randint(0, 100))

n = 0
while n < len(arr) - 1:
    arr.insert(n + 1, int(arr[n]) + int(arr[n+1]))
    n += 2

print(arr)